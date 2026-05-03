# CITY4CFD Configuration Generator

A [Streamlit](https://streamlit.io/) web app for generating JSON configuration files for [CITY4CFD](https://github.com/tudelft3d/city4cfd) — a tool for automatic reconstruction of 3D city models for CFD simulations.

---

## What It Does

Instead of writing JSON configs by hand, this app provides a guided UI with tabs for every configuration section:

- Point Clouds
- Polygons (Buildings, Surface Layers)
- Reconstruction Regions
- Import Geometries
- Domain Dimensions
- BPG Settings
- Reconstruction Settings
- Output Settings

Fill in the fields, preview the resulting JSON, and download it — ready to pass directly to `city4cfd`.

---

## Prerequisites

### Python

Python 3.11+ is recommended. Install dependencies with:

```bash
pip install streamlit
```

### CGAL (Required for building city4cfd)

CITY4CFD depends on **CGAL 6.0.1** (the version used for testing and included in this repo as `CGAL-6.0.1-library.tar.xz`).

**Download CGAL:**  
👉 https://github.com/CGAL/cgal/releases/tag/v6.0.1

CGAL is a header-only library for this use case, so no compilation is required — just extract it and point CMake at it.

**Other system dependencies** (for building city4cfd on Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y \
  libboost-all-dev \
  libgmp-dev \
  libmpfr-dev \
  libeigen3-dev \
  libomp-dev \
  libgdal-dev
```

---

## Running the App

### Locally

```bash
streamlit run app.py
```

The app will open at [http://localhost:8501](http://localhost:8501).

### With Dev Container (VS Code / GitHub Codespaces)

This repo includes a `.devcontainer` configuration. Open the folder in VS Code with the **Dev Containers** extension installed, or launch it directly on GitHub Codespaces — the environment will be set up automatically and the app will start on port 8501.

---

## Building city4cfd

A pre-built binary (`build/city4cfd`) is included for Linux (Debian Bullseye). To rebuild from source:

1. Extract CGAL:
   ```bash
   tar -xf CGAL-6.0.1-library.tar.xz
   ```

2. Clone the city4cfd source and follow its CMake build instructions, pointing `CGAL_DIR` at the extracted folder.

> **Note:** The `TUDCampus/` folder contains a sample dataset that can be used to test a full config run.

---

## Repository Structure

```
.
├── app.py                    # Main Streamlit app
├── simple_app.py             # Minimal example app
├── packages.txt              # apt packages for the dev container
├── example.config.json       # Example CITY4CFD config (with comments)
├── config_bpg.json           # BPG-specific example config
├── config_bpg_comments.json  # Annotated BPG config
├── CGAL-6.0.1-library.tar.xz # CGAL 6.0.1 source (header-only)
├── build/                    # Pre-built city4cfd binary (Linux)
├── TUDCampus/                # Sample dataset for testing
└── .devcontainer/            # Dev container configuration
```

---

## Related

- [CITY4CFD on GitHub](https://github.com/tudelft3d/city4cfd)
- [CGAL 6.0.1 Release](https://github.com/CGAL/cgal/releases/tag/v6.0.1)
- [Streamlit Documentation](https://docs.streamlit.io/)
