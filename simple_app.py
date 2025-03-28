import streamlit as st
import os
import subprocess
import shutil
import zipfile

def run_city4cfd_command(config_file):
    # Show current working directory and contents for debugging
    st.info(f"Current working directory: {os.getcwd()}")
    st.info(f"Directory contents: {os.listdir('.')}")
    
    # Create results directory if it doesn't exist
    os.makedirs("TUDCampus/results", exist_ok=True)
    
    # Run the city4cfd command
    try:
        process = subprocess.Popen(
            ["../build/city4cfd", config_file, "--output_dir", "results"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            cwd="TUDCampus"
        )
        
        # Create an expander for the full output
        with st.expander("Full Command Output", expanded=False):
            output_container = st.empty()
            full_output = ""
            
            # Stream the output in real-time
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    full_output += output
                    output_container.code(full_output, language="text", height = 500)
        
        # Check for errors
        return_code = process.poll()
        if return_code != 0:
            error = process.stderr.read()
            st.error(f"Command failed with error: {error}")
            return None
        
        # Zip the results folder
        shutil.make_archive("results", 'zip', "results")
        st.success("Command executed successfully!")
        return "results.zip"
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        return None

# Create the Streamlit interface
st.title("City4CFD Command Runner")

# File upload widget
uploaded_file = st.file_uploader("Upload config JSON file", type=["json"])
config_file = uploaded_file.name if uploaded_file else "config_bpg.json"

if st.button("Run City4CFD Command"):
    zip_path = run_city4cfd_command(config_file)
    if zip_path and os.path.exists(zip_path):
        with open(zip_path, "rb") as f:
            st.download_button(
                label="Download Results",
                data=f,
                file_name="results.zip",
                mime="application/zip"
            )
