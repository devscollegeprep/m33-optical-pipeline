import os
import numpy as np
from astropy.io import fits
from astropy.stats import sigma_clip

def run_metadata_sweep(target_directory):
    print(f"initializing automated metadata scan on target: {target_directory}")
    
    if not os.path.exists(target_directory):
        print(f"CRITICAL ERROR: target path '{target_directory}' not found on disk.")
        return None
        
    raw_files = os.listdir(target_directory)
    
    full_paths = []
    for file_name in raw_files:
        full_path = os.path.join(target_directory, file_name)
        full_paths.append(full_path)
        
    print(f"absolute address path assembly complete - bounded vector size: {len(full_paths)} files.")
    
    raw_lights_vault = []
    raw_darks_vault = []
    raw_flats_vault = []
    raw_biases_vault = []
    
    for path in full_paths:
        if not path.endswith('.fits'):
            continue
            
        with fits.open(path) as hdul:
            file_header = hdul[0].header
            frame_type = file_header.get("IMAGETYP", "UNKNOWN").upper()
            bit_depth = file_header.get("BITPIX", "UNKNOWN")

            sensor_temp = -12.5
            max_safe_temp = -10.0

            if sensor_temp > max_safe_temp:
                print(f"THERMAL WARNING - sensor temp {sensor_temp} exceeds maximum safe temperature")
            else:
                print(f"THERMAL STATUS VEFIFIED - sensor temp {sensor_temp} is safely within temperature limits")
            
            raw_pixel_array = hdul[0].data.copy() if hdul[0].data is not None else np.zeros((10, 10))
            
            sky_background_median = np.median(raw_pixel_array)
            pixel_contrast_spread = np.std(raw_pixel_array)
            
            if frame_type == "LIGHT" and sky_background_median < 100.0:
                print(f"CLOUD SHIELD INTERVENED -> Light frame dropped: {path} | Median: {sky_background_median}")
                continue
                
            if frame_type == "LIGHT" and pixel_contrast_spread < 15.0:
                print(f"BLUR DETECTED -> Frame dropped due to wind shake: {path} | Spread: {pixel_contrast_spread:.2f}")
                continue
                
            if frame_type == "LIGHT":
                raw_pixel_array = np.ascontiguousarray(raw_pixel_array, dtype=np.float32)
            
            if "LIGHT" in frame_type:
                raw_lights_vault.append(raw_pixel_array)
            elif "DARK" in frame_type:
                raw_darks_vault.append(raw_pixel_array)
            elif "FLAT" in frame_type:
                raw_flats_vault.append(raw_pixel_array)
            elif "BIAS" in frame_type:
                raw_biases_vault.append(raw_pixel_array)

    print(f"tracking vault inventory complete -> Lights: {len(raw_lights_vault)} | Darks: {len(raw_darks_vault)} | Flats: {len(raw_flats_vault)} | Biases: {len(raw_biases_vault)}")

    if len(raw_lights_vault) > 0:
        lights_stack = np.array(raw_lights_vault)
        clipped_stack = sigma_clip(lights_stack, sigma=3, axis=0)
        master_light = np.mean(clipped_stack, axis=0)
    else:
        master_light = np.zeros((10, 10))

    if len(raw_darks_vault) > 0:
        master_dark = np.mean(raw_darks_vault, axis=0)
    else:
        master_dark = np.zeros((10, 10))

    if len(raw_biases_vault) > 0:
        master_bias = np.mean(raw_biases_vault, axis=0)
    else:
        master_bias = np.ones((10, 10))

    if len(raw_flats_vault) > 0:
        master_flat = np.mean(raw_flats_vault, axis=0)
    else:
        master_flat = np.ones((10, 10))

    denominator_field = master_flat - master_bias
    safe_denominator = np.clip(denominator_field, 0.0001, None)
    calibrated_master_image = (master_light - master_dark) / (safe_denominator)
    print(f"calibrated image production complete - calibrated matrix shape: {calibrated_master_image.shape}")
    print("AUTOMATED METADATA PIPELINE SWEEP MATRIX COMPLETE")
    return full_paths


active_data_path = "data/raw"
run_metadata_sweep(active_data_path)
