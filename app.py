import streamlit as st
import json
import os
from typing import Dict, List, Any, Optional, Union

# Set page config
st.set_page_config(page_title="CITY4CFD Configuration Generator", layout="wide")

# Initialize session state for configuration
if 'config' not in st.session_state:
    st.session_state['config'] = {
        "point_clouds": {
            "ground": "",
            "buildings": ""
        },
        "polygons": [],
        "reconstruction_regions": [],
        "point_of_interest": [0, 0],
        "domain_bnd": None,
        "top_height": 300,
        "bnd_type_bpg": "Rectangle",
        "bpg_blockage_ratio": False,
        "flow_direction": [1, 1],
        "output_file_name": "Mesh",
        "output_format": "obj",
        "output_separately": True
    }

# Helper functions
def update_config():
    """Update the configuration based on the current session state"""
    # This function will be called when any widget changes
    # It will update the session state with the current values
    pass

def add_polygon():
    """Add a new polygon to the configuration"""
    new_polygon = {
        "type": "Building",
        "path": "",
        "unique_id": ""
    }
    st.session_state['config']['polygons'].append(new_polygon)

def remove_polygon(index):
    """Remove a polygon from the configuration"""
    st.session_state['config']['polygons'].pop(index)

def add_reconstruction_region():
    """Add a new reconstruction region to the configuration"""
    new_region = {
        "influence_region": 300,
        "lod": "1.2",
        "complexity_factor": 0.6
    }
    st.session_state['config']['reconstruction_regions'].append(new_region)

def remove_reconstruction_region(index):
    """Remove a reconstruction region from the configuration"""
    st.session_state['config']['reconstruction_regions'].pop(index)

def clean_config(config: Dict) -> Dict:
    """Remove empty fields from the configuration"""
    cleaned = {}
    
    for key, value in config.items():
        if isinstance(value, dict):
            cleaned_dict = clean_config(value)
            if cleaned_dict:  # Only add non-empty dictionaries
                cleaned[key] = cleaned_dict
        elif isinstance(value, list):
            if value and all(isinstance(item, dict) for item in value):
                # For lists of dictionaries (like polygons)
                cleaned_list = [clean_config(item) for item in value]
                cleaned_list = [item for item in cleaned_list if item]  # Remove empty dicts
                if cleaned_list:
                    cleaned[key] = cleaned_list
            elif value:  # For non-empty lists that aren't dicts
                cleaned[key] = value
        elif value not in ["", None, []]:
            cleaned[key] = value
    
    return cleaned

# Main app
st.title("CITY4CFD Configuration Generator")

# Create tabs for different sections
tabs = st.tabs([
    "Point Clouds", 
    "Polygons", 
    "Reconstruction Regions", 
    "Import Geometries",
    "Domain Dimensions", 
    "BPG Settings", 
    "Reconstruction Settings", 
    "Output Settings"
])

# Point Clouds tab
with tabs[0]:
    st.header("Point Clouds")
    
    col1, col2 = st.columns(2)
    with col1:
        ground_path = st.text_input(
            "Path to ground point cloud", 
            value=st.session_state['config']['point_clouds']['ground'],
            key="ground_path"
        )
        st.session_state['config']['point_clouds']['ground'] = ground_path
    
    with col2:
        buildings_path = st.text_input(
            "Path to buildings point cloud", 
            value=st.session_state['config']['point_clouds']['buildings'],
            key="buildings_path"
        )
        st.session_state['config']['point_clouds']['buildings'] = buildings_path

# Polygons tab
with tabs[1]:
    st.header("Polygons")
    
    # Button to add a new polygon
    st.button("Add Polygon", on_click=add_polygon)
    
    # Display existing polygons
    for i, polygon in enumerate(st.session_state['config']['polygons']):
        with st.expander(f"Polygon {i+1}", expanded=True):
            # Common fields for all polygon types
            polygon_type = st.selectbox(
                "Type", 
                options=["Building", "SurfaceLayer"],
                index=0 if polygon.get("type") == "Building" else 1,
                key=f"polygon_type_{i}"
            )
            st.session_state['config']['polygons'][i]["type"] = polygon_type
            
            polygon_path = st.text_input(
                "Path", 
                value=polygon.get("path", ""),
                key=f"polygon_path_{i}"
            )
            st.session_state['config']['polygons'][i]["path"] = polygon_path
            
            # Conditional fields based on polygon type
            if polygon_type == "Building":
                unique_id = st.text_input(
                    "Unique ID", 
                    value=polygon.get("unique_id", ""),
                    key=f"polygon_unique_id_{i}",
                    help="Optional - use building ID from the polygon file"
                )
                if unique_id:
                    st.session_state['config']['polygons'][i]["unique_id"] = unique_id
                
                height_attr = st.text_input(
                    "Height Attribute", 
                    value=polygon.get("height_attribute", ""),
                    key=f"polygon_height_attr_{i}",
                    help="Optional - use height from the polygon file for reconstruction"
                )
                if height_attr:
                    st.session_state['config']['polygons'][i]["height_attribute"] = height_attr
                
                floor_attr = st.text_input(
                    "Floor Attribute", 
                    value=polygon.get("floor_attribute", ""),
                    key=f"polygon_floor_attr_{i}",
                    help="Optional - use number of floors for reconstruction"
                )
                if floor_attr:
                    st.session_state['config']['polygons'][i]["floor_attribute"] = floor_attr
                    
                    # Floor height is required if floor_attribute is defined
                    floor_height = st.number_input(
                        "Floor Height", 
                        value=polygon.get("floor_height", 3.0),
                        key=f"polygon_floor_height_{i}",
                        help="Floor height, required if 'floor_attribute' is defined"
                    )
                    st.session_state['config']['polygons'][i]["floor_height"] = floor_height
                
                height_advantage = st.checkbox(
                    "Height Attribute Advantage", 
                    value=polygon.get("height_attribute_advantage", False),
                    key=f"polygon_height_advantage_{i}",
                    help="In case height attribute takes precedence over other reconstruction from point cloud"
                )
                st.session_state['config']['polygons'][i]["height_attribute_advantage"] = height_advantage
                
                avoid_bad_polys = st.checkbox(
                    "Avoid Bad Polygons", 
                    value=polygon.get("avoid_bad_polys", False),
                    key=f"polygon_avoid_bad_{i}",
                    help="Optional - ignore or try to reconstruct problematic (non-simple) polygons"
                )
                st.session_state['config']['polygons'][i]["avoid_bad_polys"] = avoid_bad_polys
                
                refine = st.checkbox(
                    "Refine", 
                    value=polygon.get("refine", False),
                    key=f"polygon_refine_{i}",
                    help="Optional - refine surface"
                )
                st.session_state['config']['polygons'][i]["refine"] = refine
                
            elif polygon_type == "SurfaceLayer":
                layer_name = st.text_input(
                    "Layer Name", 
                    value=polygon.get("layer_name", ""),
                    key=f"polygon_layer_name_{i}",
                    help="Optional - choose a layer name"
                )
                if layer_name:
                    st.session_state['config']['polygons'][i]["layer_name"] = layer_name
                
                flatten_surface = st.checkbox(
                    "Flatten Surface", 
                    value=polygon.get("flatten_surface", False),
                    key=f"polygon_flatten_surface_{i}",
                    help="Optional - set all points of the surface layer to the same height"
                )
                st.session_state['config']['polygons'][i]["flatten_surface"] = flatten_surface
                
                if flatten_surface:
                    surface_percentile = st.number_input(
                        "Surface Percentile", 
                        value=polygon.get("surface_percentile", 30),
                        key=f"polygon_surface_percentile_{i}",
                        help="Percentile of all points of the surface layer to set the height to"
                    )
                    st.session_state['config']['polygons'][i]["surface_percentile"] = surface_percentile
                
                flatten_vertical_border = st.checkbox(
                    "Flatten Vertical Border", 
                    value=polygon.get("flatten_vertical_border", False),
                    key=f"polygon_flatten_vertical_border_{i}",
                    help="Optional - enforce vertical walls between terrain and flattened surface"
                )
                st.session_state['config']['polygons'][i]["flatten_vertical_border"] = flatten_vertical_border
            
            # Button to remove this polygon
            st.button("Remove Polygon", key=f"remove_polygon_{i}", on_click=remove_polygon, args=(i,))

# Reconstruction Regions tab
with tabs[2]:
    st.header("Reconstruction Regions")
    
    # Button to add a new reconstruction region
    st.button("Add Reconstruction Region", on_click=add_reconstruction_region)
    
    # Display existing reconstruction regions
    for i, region in enumerate(st.session_state['config']['reconstruction_regions']):
        with st.expander(f"Reconstruction Region {i+1}", expanded=True):
            # Influence region type
            influence_type = st.selectbox(
                "Influence Region Type",
                options=["Radius", "Polygon Points", "Imported Polygon", "BPG"],
                index=0,  # Default to Radius
                key=f"region_influence_type_{i}"
            )
            
            # Fields based on influence region type
            if influence_type == "Radius":
                radius = st.number_input(
                    "Radius",
                    value=float(region.get("influence_region", 300)),
                    key=f"region_radius_{i}"
                )
                st.session_state['config']['reconstruction_regions'][i]["influence_region"] = radius
            elif influence_type == "Polygon Points":
                points_str = st.text_area(
                    "Polygon Points (format: [[x1, y1], [x2, y2], ...])",
                    value="" if not isinstance(region.get("influence_region"), list) else str(region.get("influence_region")),
                    key=f"region_points_{i}"
                )
                try:
                    # Try to parse the points string as a list of [x, y] pairs
                    points = eval(points_str)
                    st.session_state['config']['reconstruction_regions'][i]["influence_region"] = points
                except:
                    st.error("Invalid polygon points format. Use format: [[x1, y1], [x2, y2], ...]")
            elif influence_type == "Imported Polygon":
                polygon_path = st.text_input(
                    "Path to Polygon File",
                    value="" if not isinstance(region.get("influence_region"), str) else region.get("influence_region"),
                    key=f"region_polygon_path_{i}"
                )
                st.session_state['config']['reconstruction_regions'][i]["influence_region"] = polygon_path
            elif influence_type == "BPG":
                st.session_state['config']['reconstruction_regions'][i]["influence_region"] = None
            
            # LoD selection
            lod = st.selectbox(
                "Level of Detail (LoD)",
                options=["1.2", "1.3", "2.2"],
                index=0 if region.get("lod") == "1.2" else 1 if region.get("lod") == "1.3" else 2,
                key=f"region_lod_{i}"
            )
            st.session_state['config']['reconstruction_regions'][i]["lod"] = lod
            
            # Complexity factor (required for LoD 1.3 and 2.2)
            if lod in ["1.3", "2.2"]:
                complexity = st.number_input(
                    "Complexity Factor",
                    value=region.get("complexity_factor", 0.6),
                    min_value=0.0,
                    max_value=1.0,
                    key=f"region_complexity_{i}",
                    help="Graph cut optimisation bias for LoD1.3 and LoD2.2"
                )
                st.session_state['config']['reconstruction_regions'][i]["complexity_factor"] = complexity
                
                # LoD 1.3 step height
                lod13_step_height = st.number_input(
                    "LoD 1.3 Step Height",
                    value=region.get("lod13_step_height", 2.0),
                    key=f"region_lod13_step_height_{i}",
                    help="Optional - choose LoD1.3 minimum step height between roof faces in m"
                )
                st.session_state['config']['reconstruction_regions'][i]["lod13_step_height"] = lod13_step_height
            
            # Optional fields
            validate = st.checkbox(
                "Validate",
                value=region.get("validate", False),
                key=f"region_validate_{i}",
                help="Optional - do the geometric validity check and report on invalid buildings"
            )
            st.session_state['config']['reconstruction_regions'][i]["validate"] = validate
            
            enforce_validity = st.selectbox(
                "Enforce Validity",
                options=["None", "lod1.2", "surface_wrap"],
                index=0 if not region.get("enforce_validity") else 
                      1 if region.get("enforce_validity") == "lod1.2" else 2,
                key=f"region_enforce_validity_{i}",
                help="Optional - fall back to LoD1.2 reconstruction or surface wrap in case the geometric validity check fails"
            )
            if enforce_validity != "None":
                st.session_state['config']['reconstruction_regions'][i]["enforce_validity"] = enforce_validity
                
                if enforce_validity == "surface_wrap":
                    relative_alpha = st.number_input(
                        "Relative Alpha",
                        value=region.get("relative_alpha", 500),
                        key=f"region_relative_alpha_{i}",
                        help="Required when enforce_validity is surface_wrap"
                    )
                    st.session_state['config']['reconstruction_regions'][i]["relative_alpha"] = relative_alpha
                    
                    relative_offset = st.number_input(
                        "Relative Offset",
                        value=region.get("relative_offset", 1200),
                        key=f"region_relative_offset_{i}",
                        help="Required when enforce_validity is surface_wrap"
                    )
                    st.session_state['config']['reconstruction_regions'][i]["relative_offset"] = relative_offset
            
            skip_gap_closing = st.checkbox(
                "Skip Gap Closing",
                value=region.get("skip_gap_closing", False),
                key=f"region_skip_gap_closing_{i}",
                help="Optional - skip open border check and simple gap closing in LoD1.3 and LoD2.2 reconstruction"
            )
            st.session_state['config']['reconstruction_regions'][i]["skip_gap_closing"] = skip_gap_closing
            
            import_advantage = st.checkbox(
                "Import Advantage",
                value=region.get("import_advantage", False),
                key=f"region_import_advantage_{i}",
                help="Optional - whether imported or reconstructed take advantage in the region"
            )
            st.session_state['config']['reconstruction_regions'][i]["import_advantage"] = import_advantage
            
            # Button to remove this region
            st.button("Remove Region", key=f"remove_region_{i}", on_click=remove_reconstruction_region, args=(i,))

# Import Geometries tab
with tabs[3]:
    st.header("Import Geometries")
    
    include_import = st.checkbox(
        "Include Import Geometries",
        value="import_geometries" in st.session_state['config'],
        key="include_import_geometries"
    )
    
    if include_import:
        if "import_geometries" not in st.session_state['config']:
            st.session_state['config']["import_geometries"] = {
                "path": "",
                "true_height": True,
                "lod": "1.3",
                "refine": False
            }
        
        import_path = st.text_input(
            "Path",
            value=st.session_state['config']["import_geometries"].get("path", ""),
            key="import_path"
        )
        st.session_state['config']["import_geometries"]["path"] = import_path
        
        true_height = st.checkbox(
            "True Height",
            value=st.session_state['config']["import_geometries"].get("true_height", True),
            key="import_true_height"
        )
        st.session_state['config']["import_geometries"]["true_height"] = true_height
        
        import_lod = st.selectbox(
            "Level of Detail (LoD)",
            options=["1.2", "1.3", "2.2"],
            index=0 if st.session_state['config']["import_geometries"].get("lod") == "1.2" else 
                  1 if st.session_state['config']["import_geometries"].get("lod") == "1.3" else 2,
            key="import_lod"
        )
        st.session_state['config']["import_geometries"]["lod"] = import_lod
        
        import_refine = st.checkbox(
            "Refine",
            value=st.session_state['config']["import_geometries"].get("refine", False),
            key="import_refine",
            help="Optional - refine surface"
        )
        st.session_state['config']["import_geometries"]["refine"] = import_refine
    else:
        if "import_geometries" in st.session_state['config']:
            del st.session_state['config']["import_geometries"]

# Domain Dimensions tab
with tabs[4]:
    st.header("Domain Dimensions")
    
    col1, col2 = st.columns(2)
    with col1:
        poi_x = st.number_input(
            "Point of Interest X",
            value=st.session_state['config']['point_of_interest'][0],
            key="poi_x"
        )
    with col2:
        poi_y = st.number_input(
            "Point of Interest Y",
            value=st.session_state['config']['point_of_interest'][1],
            key="poi_y"
        )
    st.session_state['config']['point_of_interest'] = [poi_x, poi_y]
    
    include_domain_bnd = st.checkbox(
        "Include Domain Boundary",
        value=st.session_state['config']['domain_bnd'] is not None,
        key="include_domain_bnd"
    )
    if include_domain_bnd:
        domain_bnd = st.text_area(
            "Domain Boundary (format: [[x1, y1], [x2, y2], ...])",
            value="" if st.session_state['config']['domain_bnd'] is None else str(st.session_state['config']['domain_bnd']),
            key="domain_bnd"
        )
        try:
            # Try to parse the domain boundary string as a list of [x, y] pairs
            st.session_state['config']['domain_bnd'] = eval(domain_bnd)
        except:
            st.error("Invalid domain boundary format. Use format: [[x1, y1], [x2, y2], ...]")
    else:
        st.session_state['config']['domain_bnd'] = None
    
    top_height = st.number_input(
        "Top Height",
        value=st.session_state['config']['top_height'],
        key="top_height"
    )
    st.session_state['config']['top_height'] = top_height
    
    # Optional fields
    buffer_region = st.number_input(
        "Buffer Region",
        value=st.session_state['config'].get('buffer_region', -20),
        key="buffer_region",
        help="Optional - buffer region size in percentage of distance to bndpoly centroid"
    )
    st.session_state['config']['buffer_region'] = buffer_region
    
    reconstruct_boundaries = st.checkbox(
        "Reconstruct Boundaries",
        value=st.session_state['config'].get('reconstruct_boundaries', False),
        key="reconstruct_boundaries",
        help="Optional - reconstruct sides and top of the domain"
    )
    st.session_state['config']['reconstruct_boundaries'] = reconstruct_boundaries

# BPG Settings tab
with tabs[5]:
    st.header("BPG Settings")
    
    bnd_type_bpg = st.selectbox(
        "Boundary Type",
        options=["Rectangle", "Oval", "Round"],
        index=0 if st.session_state['config'].get('bnd_type_bpg') == "Rectangle" else 
              1 if st.session_state['config'].get('bnd_type_bpg') == "Oval" else 2,
        key="bnd_type_bpg",
        help="Round, Rectangle, Oval. Matters only if using BPG"
    )
    st.session_state['config']['bnd_type_bpg'] = bnd_type_bpg
    
    blockage_ratio_type = st.selectbox(
        "Blockage Ratio",
        options=["False", "True", "Custom"],
        index=0 if st.session_state['config'].get('bpg_blockage_ratio') is False else 
              1 if st.session_state['config'].get('bpg_blockage_ratio') is True else 2,
        key="blockage_ratio_type",
        help="Optional - blockage ratio BPG. Can be set as 'true' for default, or as a number defining max allowed blockage ratio"
    )
    
    if blockage_ratio_type == "False":
        st.session_state['config']['bpg_blockage_ratio'] = False
    elif blockage_ratio_type == "True":
        st.session_state['config']['bpg_blockage_ratio'] = True
    else:  # Custom
        custom_ratio = st.number_input(
            "Custom Blockage Ratio",
            value=0.5 if not isinstance(st.session_state['config'].get('bpg_blockage_ratio'), (int, float)) else 
                  st.session_state['config'].get('bpg_blockage_ratio'),
            min_value=0.0,
            max_value=1.0,
            key="custom_blockage_ratio"
        )
        st.session_state['config']['bpg_blockage_ratio'] = custom_ratio
    
    col1, col2 = st.columns(2)
    with col1:
        flow_dir_x = st.number_input(
            "Flow Direction X",
            value=st.session_state['config'].get('flow_direction', [1, 1])[0],
            key="flow_dir_x"
        )
    with col2:
        flow_dir_y = st.number_input(
            "Flow Direction Y",
            value=st.session_state['config'].get('flow_direction', [1, 1])[1],
            key="flow_dir_y"
        )
    st.session_state['config']['flow_direction'] = [flow_dir_x, flow_dir_y]
    
    # Domain size based on boundary type
    include_domain_size = st.checkbox(
        "Include Domain Size",
        value="bpg_domain_size" in st.session_state['config'],
        key="include_domain_size"
    )
    
    if include_domain_size:
        if bnd_type_bpg in ["Rectangle", "Oval"]:
            col1, col2 = st.columns(2)
            with col1:
                front = st.number_input(
                    "Front",
                    value=st.session_state['config'].get('bpg_domain_size', [5, 5, 15, 6])[0],
                    key="domain_front"
                )
                sides = st.number_input(
                    "Sides",
                    value=st.session_state['config'].get('bpg_domain_size', [5, 5, 15, 6])[1],
                    key="domain_sides"
                )
            with col2:
                back = st.number_input(
                    "Back",
                    value=st.session_state['config'].get('bpg_domain_size', [5, 5, 15, 6])[2],
                    key="domain_back"
                )
                top = st.number_input(
                    "Top",
                    value=st.session_state['config'].get('bpg_domain_size', [5, 5, 15, 6])[3],
                    key="domain_top"
                )
            st.session_state['config']['bpg_domain_size'] = [front, sides, back, top]
        else:  # Round
            col1, col2 = st.columns(2)
            with col1:
                sides = st.number_input(
                    "Sides",
                    value=st.session_state['config'].get('bpg_domain_size', [100, 5])[0],
                    key="domain_round_sides"
                )
            with col2:
                top = st.number_input(
                    "Top",
                    value=st.session_state['config'].get('bpg_domain_size', [100, 5])[1],
                    key="domain_round_top"
                )
            st.session_state['config']['bpg_domain_size'] = [sides, top]
    else:
        if "bpg_domain_size" in st.session_state['config']:
            del st.session_state['config']["bpg_domain_size"]

# Reconstruction Settings tab
with tabs[6]:
    st.header("Reconstruction Settings")
    
    # Terrain settings
    st.subheader("Terrain")
    
    terrain_thinning = st.number_input(
        "Terrain Thinning",
        value=st.session_state['config'].get('terrain_thinning', 80),
        min_value=0,
        max_value=100,
        key="terrain_thinning",
        help="Optional - percentage of randomly removed terrain points"
    )
    st.session_state['config']['terrain_thinning'] = terrain_thinning
    
    smooth_terrain = st.checkbox(
        "Smooth Terrain",
        value="smooth_terrain" in st.session_state['config'],
        key="smooth_terrain_checkbox",
        help="Optional - smoothing flag"
    )
    
    if smooth_terrain:
        if "smooth_terrain" not in st.session_state['config']:
            st.session_state['config']["smooth_terrain"] = {
                "iterations": 1,
                "max_pts": 100000
            }
        
        col1, col2 = st.columns(2)
        with col1:
            iterations = st.number_input(
                "Iterations",
                value=st.session_state['config']["smooth_terrain"].get("iterations", 1),
                min_value=1,
                key="smooth_terrain_iterations"
            )
            st.session_state['config']["smooth_terrain"]["iterations"] = iterations
        
        with col2:
            max_pts = st.number_input(
                "Max Points",
                value=st.session_state['config']["smooth_terrain"].get("max_pts", 100000),
                min_value=1000,
                key="smooth_terrain_max_pts",
                help="Number of points after optimized thinning for smoothing"
            )
            st.session_state['config']["smooth_terrain"]["max_pts"] = max_pts
    else:
        if "smooth_terrain" in st.session_state['config']:
            del st.session_state['config']["smooth_terrain"]
    
    flat_terrain = st.checkbox(
        "Flat Terrain",
        value=st.session_state['config'].get('flat_terrain', False),
        key="flat_terrain",
        help="Optional - make terrain flat"
    )
    st.session_state['config']['flat_terrain'] = flat_terrain
    
    # Buildings settings
    st.subheader("Buildings")
    
    building_percentile = st.number_input(
        "Building Percentile",
        value=st.session_state['config'].get('building_percentile', 90),
        min_value=0,
        max_value=100,
        key="building_percentile"
    )
    st.session_state['config']['building_percentile'] = building_percentile
    
    min_height = st.number_input(
        "Minimum Height",
        value=st.session_state['config'].get('min_height', 2.0),
        key="min_height",
        help="Optional - define the minimum allowed height for building reconstruction"
    )
    st.session_state['config']['min_height'] = min_height
    
    min_area = st.number_input(
        "Minimum Area",
        value=st.session_state['config'].get('min_area', 50.0),
        key="min_area",
        help="Optional - define the minimum allowed floorplan area for building reconstruction"
    )
    st.session_state['config']['min_area'] = min_area
    
    reconstruct_failed = st.checkbox(
        "Reconstruct Failed",
        value=st.session_state['config'].get('reconstruct_failed', False),
        key="reconstruct_failed",
        help="Optional - reconstruct buildings at minimum height if the reconstruction fails"
    )
    st.session_state['config']['reconstruct_failed'] = reconstruct_failed
    
    intersect_buildings_terrain = st.checkbox(
        "Intersect Buildings Terrain",
        value=st.session_state['config'].get('intersect_buildings_terrain', False),
        key="intersect_buildings_terrain",
        help="Optional - make buildings protrude through terrain"
    )
    st.session_state['config']['intersect_buildings_terrain'] = intersect_buildings_terrain
    
    # General settings
    st.subheader("General")
    
    edge_max_len = st.number_input(
        "Edge Max Length",
        value=st.session_state['config'].get('edge_max_len', 5.0),
        key="edge_max_len"
    )
    st.session_state['config']['edge_max_len'] = edge_max_len

# Output Settings tab
with tabs[7]:
    st.header("Output Settings")
    
    output_file_name = st.text_input(
        "Output File Name",
        value=st.session_state['config'].get('output_file_name', "Mesh"),
        key="output_file_name"
    )
    st.session_state['config']['output_file_name'] = output_file_name
    
    output_format = st.selectbox(
        "Output Format",
        options=["obj", "json", "geojson"],
        index=0 if st.session_state['config'].get('output_format') == "obj" else 
              1 if st.session_state['config'].get('output_format') == "json" else 2,
        key="output_format"
    )
    st.session_state['config']['output_format'] = output_format
    
    output_separately = st.checkbox(
        "Output Separately",
        value=st.session_state['config'].get('output_separately', True),
        key="output_separately"
    )
    st.session_state['config']['output_separately'] = output_separately
    
    output_log = st.checkbox(
        "Output Log",
        value=st.session_state['config'].get('output_log', True),
        key="output_log",
        help="Optional - also outputs GeoJSON file of building polygons that couldn't be reconstructed"
    )
    st.session_state['config']['output_log'] = output_log
    
    if output_log:
        log_file = st.text_input(
            "Log File",
            value=st.session_state['config'].get('log_file', "logFile.log"),
            key="log_file",
            help="Optional - defaults to 'log'"
        )
        st.session_state['config']['log_file'] = log_file

# JSON Preview and Download
st.header("Configuration Preview and Download")

# Clean the configuration to remove empty fields
clean_button = st.button("Clean Configuration")
if clean_button:
    st.session_state['config'] = clean_config(st.session_state['config'])

# Display the current configuration
st.subheader("Configuration Preview")
st.json(st.session_state['config'])

# Download button
config_str = json.dumps(st.session_state['config'], indent=2)
st.download_button(
    label="Download JSON Configuration",
    data=config_str,
    file_name="config.json",
    mime="application/json"
)

# Load example configurations
st.subheader("Load Example Configuration")
col1, col2 = st.columns(2)

with col1:
    if st.button("Load Example 1"):
        try:
            with open("example.config.json", "r") as f:
                # Remove comments from the JSON file
                lines = f.readlines()
                cleaned_lines = [line for line in lines if not line.strip().startswith('//') and '//' not in line]
                example_json = json.loads(''.join(cleaned_lines))
                st.session_state['config'] = example_json
                st.success("Example 1 loaded successfully!")
        except Exception as e:
            st.error(f"Error loading example: {str(e)}")

with col2:
    if st.button("Load Example 2"):
        try:
            with open("config_bpg_comments.json", "r") as f:
                # Remove comments from the JSON file
                lines = f.readlines()
                cleaned_lines = [line for line in lines if not line.strip().startswith('//') and '//' not in line]
                example_json = json.loads(''.join(cleaned_lines))
                st.session_state['config'] = example_json
                st.success("Example 2 loaded successfully!")
        except Exception as e:
            st.error(f"Error loading example: {str(e)}")