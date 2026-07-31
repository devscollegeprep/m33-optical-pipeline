import os
from astropy.io import fits

def run_metadata_sweep(target_directory):
    """
    Scans a variable data folder path, builds absolute system address matrices, 
    and checks FITS metadata header badges to catalog imaging file configurations.
    """
    print(f"🚀 Initializing automated metadata scan on target: {target_directory}")
    

    if not os.path.exists(target_directory):
        print(f"CRITICAL ERROR: target path '{target_directory}' not found on disk.")
        return None
        
   
    raw_files = os.listdir(target_directory)
    
    
    full_paths = []
    for file_name in raw_files:
      
        full_path = os.path.join(target_directory, file_name)
        full_paths.append(full_path)
        
    print(f"absolute address path assembly complete. Bounded vector size: {len(full_paths)} files.")
    

    for path in full_paths:
        with fits.open(path) as hdul:
            file_header = hdul[0].header
            frame_type = file_header.get("IMAGETYP", "UNKNOWN")
            bit_depth = file_header.get("BITPIX", "UNKNOWN")
            
        print(f"file verified -> address: {path} | class: {frame_type} | bit-depth: {bit_depth}")
        
    print("AUTOMATED METADATA PIPELINE SWEEP MATRIX COMPLETE")
    return full_paths


active_data_path = "data/raw"


run_metadata_sweep(active_data_path)
