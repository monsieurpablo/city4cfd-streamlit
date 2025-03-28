# Project Plan: Streamlit App for CITY4CFD JSON Configuration

This project plan outlines the development of a Python Streamlit application designed to generate JSON configuration files for CITY4CFD, a computational fluid dynamics tool for urban simulations. The app will feature a user-friendly front end, allowing users to input parameters interactively and produce a JSON file that mirrors the structure of the provided examples. The resulting JSON does not need to include all features unless explicitly specified by the user, offering flexibility in configuration generation.

## Objective
Create a web-based Streamlit application that enables users to:
- Input parameters for CITY4CFD simulations through an intuitive interface.
- Dynamically manage complex structures like polygons and reconstruction regions.
- Generate and download a JSON configuration file based on user inputs.

## Key Features
- **Interactive Input Forms**: Utilize Streamlit widgets to collect user inputs for various configuration sections.
- **Dynamic Inputs**: Support adding, removing, and editing items in arrays (e.g., polygons, reconstruction regions).
- **Conditional Logic**: Display relevant input fields based on user selections (e.g., polygon type-specific attributes).
- **Preview and Download**: Provide a configuration preview and a downloadable JSON file.

## Project Structure

### 1. Setup and Initialization
- **Session State Initialization**: Use `st.session_state` to store the configuration as a dictionary, initialized with default values from the example JSONs (e.g., `"height_attribute_advantage": false`).
- **Default Configuration**: Pre-populate fields with sensible defaults where applicable, ensuring the app is functional out of the box.

### 2. User Interface Layout
- **Tabbed Interface**: Organize the app using `st.tabs` for the following sections:
  - Point Clouds
  - Polygons
  - Reconstruction Regions
  - Import Geometries
  - Domain Dimensions
  - BPG Settings
  - Reconstruction Settings
  - Output Settings
- **Main Layout**: Include a sidebar for navigation or instructions and a main area for tabs and a JSON preview/download section.

### 3. Input Widgets and Logic
Below is a breakdown of input widgets for each configuration section:

#### Point Clouds
- **Fields**: Ground and buildings file paths.
- **Widgets**: `st.text_input` for each path (e.g., "Path to ground point cloud").

#### Polygons
- **Dynamic List**: Maintain a list in `st.session_state['config']['polygons']`.
- **Controls**: Button to "Add Polygon" and "Remove" buttons for each entry.
- **Fields per Polygon**:
  - **Type**: `st.selectbox` with options ["Building", "SurfaceLayer"].
  - **Path**: `st.text_input`.
  - **Conditional Fields**:
    - *Building*: `st.text_input` for `unique_id`, `height_attribute`, `floor_attribute`; `st.number_input` for `floor_height`; `st.checkbox` for `height_attribute_advantage`, `avoid_bad_polys`, `refine`.
    - *SurfaceLayer*: `st.text_input` for `layer_name`; `st.checkbox` for `flatten_surface`, `flatten_vertical_border`; `st.number_input` for `surface_percentile` (shown if `flatten_surface` is true).

#### Reconstruction Regions
- **Dynamic List**: Store in `st.session_state['config']['reconstruction_regions']`.
- **Controls**: Buttons to "Add Region" and "Remove" each entry.
- **Fields per Region**:
  - **Influence Region**: `st.selectbox` with options ["Radius", "Polygon Points", "Imported Polygon", "BPG"], followed by:
    - *Radius*: `st.number_input`.
    - *Polygon Points*: `st.text_area` for a list of [x, y] pairs.
    - *Imported Polygon*: `st.text_input` for path.
    - *BPG*: Set to `None`.
  - **LoD**: `st.selectbox` with options ["1.2", "1.3", "2.2"].
  - **Complexity Factor**: `st.number_input` (required for LoD 1.3/2.2).
  - **Optional Fields**: `st.number_input` for `lod13_step_height`, `relative_alpha`, `relative_offset`; `st.checkbox` for `validate`, `skip_gap_closing`, `import_advantage`; `st.selectbox` for `enforce_validity` ["lod1.2", "surface_wrap"].

#### Import Geometries
- **Optional Section**: `st.checkbox` to "Include Import Geometries".
- **Fields**: `st.text_input` for `path`; `st.checkbox` for `true_height`; `st.selectbox` for `lod` ["1.2", "1.3", "2.2"]; `st.checkbox` for `refine`.

#### Domain Dimensions
- **Fields**:
  - **Point of Interest**: Two `st.number_input` fields for X and Y coordinates.
  - **Domain Boundary**: `st.checkbox` to include (default `null` unless specified).
  - **Top Height**: `st.number_input`.
  - **Optional**: `st.number_input` for `buffer_region`; `st.checkbox` for `reconstruct_boundaries`.

#### BPG Settings
- **Fields**:
  - **Boundary Type**: `st.selectbox` with ["Rectangle", "Oval", "Round"].
  - **Blockage Ratio**: `st.selectbox` with ["False", "True", "Custom"] (custom shows `st.number_input`).
  - **Flow Direction**: Two `st.number_input` fields for X and Y.
  - **Domain Size**: Conditional inputs based on `bnd_type_bpg`:
    - *Rectangle/Oval*: Four `st.number_input` fields (front, sides, back, top).
    - *Round*: Two `st.number_input` fields (sides, top).

#### Reconstruction Settings
- **Terrain**:
  - `st.number_input` for `terrain_thinning`.
  - `st.checkbox` for `smooth_terrain`, showing `st.number_input` for `iterations` and `max_pts` if checked.
  - `st.checkbox` for `flat_terrain`.
- **Buildings**:
  - `st.number_input` for `building_percentile`, `min_height`, `min_area`.
  - `st.checkbox` for `reconstruct_failed`, `intersect_buildings_terrain`.
- **General**: `st.number_input` for `edge_max_len`.

#### Output Settings
- **Fields**:
  - `st.text_input` for `output_file_name`.
  - `st.selectbox` for `output_format` (e.g., ["obj", "json"]).
  - `st.checkbox` for `output_separately`, `output_log`.
  - `st.text_input` for `log_file`.

### 4. Dynamic Management of Arrays
- **Polygons and Reconstruction Regions**:
  - Use `st.button` to append new dictionaries to the respective session state lists with default values.
  - Display each item in an expander or column with a "Remove" button.
  - Assign unique keys to widgets (e.g., `f"polygon_type_{i}"` where `i` is the index).

### 5. Conditional Inputs
- **Logic**: Use Python `if` statements to show/hide fields based on selections (e.g., polygon type, influence region type).
- **Optional Fields**: Allow blank inputs or use checkboxes; omit from JSON if not specified (though defaults may be included for simplicity).

### 6. Preview and Generate JSON
- **Preview**: Display `st.session_state['config']` using `st.json` at the bottom of the app.
- **Download**: Use `st.download_button` to serialize the configuration dictionary to JSON and offer it as a file (e.g., `config.json`).

### 7. Validation (Optional)
- **Basic Checks**: Warn users if required fields (e.g., `floor_height` when `floor_attribute` is set) are missing.
- **Implementation**: Add conditional checks before JSON generation, displaying messages via `st.warning`.

## New Streamlit Features (Post-January 2024)
Streamlit updates after January 2024 offer enhancements that could improve the app:
- **Improved `st.data_editor`**: Consider using it for editing simpler array structures (e.g., reconstruction regions) in a table format, though nested fields may require custom widgets.
- **Pathlib Support**: Use `pathlib.Path` for robust file path handling if integrating file uploads (optional enhancement).
- **Enhanced Forms**: Leverage `st.form` to group related inputs, though tabs may suffice for this app’s complexity.
- **Timezone Context**: Access via `st.context` (not directly relevant but noted for completeness).

These features are optional but could enhance usability or robustness depending on implementation priorities.

## Implementation Steps
1. **Initialize App**:
   - Set up `st.session_state['config']` with a default dictionary.
2. **Build Tabs**:
   - Use `st.tabs` to create sections.
3. **Add Input Widgets**:
   - Implement widgets as outlined, ensuring unique keys.
4. **Manage Arrays**:
   - Use loops and buttons to handle dynamic lists.
5. **Implement Conditional Logic**:
   - Dynamically show fields based on user choices.
6. **Update Session State**:
   - Sync inputs with `st.session_state` in real-time.
7. **Add Preview and Download**:
   - Display configuration and provide a download option.

## Testing and Validation
- **Test Cases**: Generate JSONs with minimal inputs, full inputs, and edge cases (e.g., empty arrays).
- **Verification**: Compare outputs to example JSONs for structural accuracy.
- **Assumption**: If the format matches, it should be compatible with CITY4CFD (untestable without the tool).

## User Experience Enhancements
- **Labels and Placeholders**: Clearly label each input and provide default placeholders.
- **Tooltips**: Use `st.markdown` or `st.caption` for brief explanations of complex fields.
- **Layout**: Use `st.columns` and expanders for a clean, organized interface.

## Notes
- **Flexibility**: The JSON will include only user-specified fields, with optional fields included if provided (defaults may be retained for simplicity).
- **Scalability**: The plan supports future additions (e.g., new polygon types) via modular design.

This plan provides a comprehensive roadmap for building a functional, user-friendly Streamlit app tailored to CITY4CFD configuration needs, leveraging Streamlit’s capabilities and recent enhancements where applicable.