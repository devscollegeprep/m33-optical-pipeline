# m33-optical-pipeline

This is an automated astronomical image processing and data analysis pipeline optimized to calibrate, register, stack, align, normalize, and identify star formation regions relative to the core in the Triangulum Galaxy (Messier 33

## scientific objectives

- **Sensor Noise Mitigation: isolate weak galactic signals by mathematically subtracting planes containing dark current disturbances and flat-field optical disturbances from viable images of the galaxy
  
- **Geometric Registration: correct subtle spatial field drift by caused by atmospheric refraction and galactic drift by realigning images with similar micro-errors over long exposure imaging
  
- **Signal-To-Noise Ratio (SNR) Optimization: Co-add and mediate raw multi-gigabyte .fits image data sets to create a viable, data-extractable image with supressed stellar background noise
  
- **Aperture Photometry: Calculate precise photon flux-per-pixel values relative to the core for key star formation regions in the Triangulum galaxy, specificallly targeting NGC-604

## repository architecture
```text
|--data/
|   |--raw/              # ignored - local raw telescope .fits data frames
|   |__processed/        # ignored - calibrated master output .fits data matrice
|--notebooks/
|   |__foundations.ipynb # active - weekly python notebooks showing learning progress
|--scripts/
|   |__pipeline.py.      # active - master python automated pipeline
|--.gitignore            # tracking shield for large local memory/data files
|__README.md             # structural blueprint and research logs
```

## 7-Week Development Roadmap 
- (due to limited access to information regarding hyperspecific learning requirements, a specialized AI tutor was used to complete a 7 week curriculum to effectively learn line-by-line what the python code typed was doing (during the creation of this repository, I am completely new to Python))

Week 1: Environmental Architecture & Git Integration
* Configured localized mac hardware to run on Python 3.13.14
* Established workspace using secure cryptographic Ed25519 cloud handshakes
* Deployed 'gitignore' protection rules to preserve folder architecture and repository integrity

Week 2: Python Basics & Foundational Engineering
* Construct mathematical logic engines in Jupyter Notebooks using variables, loops, and functions (basics of python)
* Learn useage of variable types Integers, Floats, Strings, Booleans) Boolean evaluation gates (if, elif, else) loops (for, while) and functional syntax arguments (def, return)

Week 3: FITS Architecture & Metadata Extraction
* Begin using astrophysics-specific libraries
* Utilize astropy.io.fits to unpack multi-extension space data cards and parse code coordinate systems aswell as metadata matrices

Week 4: Sensor Calibration (Dark and Flat Frame Processing)
* Begin to access multidimensional computational physics
* Utilize NumPy array operations to systemically subtract dark and flat disturbance frames from light viable data image
* flattening across digital imaging sensor pixel grids

Week 5: Coordinate Registration (Star Pattern Matching)
* Employ coordinate transformation matrices
* Implement astroalign to compute micropixel rotation, translation, and alignment to eliminate vectors and drift smears across long imaging sessins

Week 6: Matrix Stacking (Signal-to-Noise Optimization)
* Heavy statistical data reduction
* Executing high-volume median array stacking using system memory optimization (memmap=True) to maximize signal-to-noise ratios

Week 7: Non-Linear Asinh stretching & nebular Extraction 
* Enhancing faint light signals without oversaturating the core, and assigning mathematical photon values to extract exact photon flux matrices of star formation regions (especially NGC-604)
* Instead of deploying standard linear logarithmic stretching, 'astropy.visualization.AsinhStretch' and 'ImageNormalize' will be used to enhance faint arms while not blowing out m33's core
* Use 'Photoutils' to isolate precise pixel coordinates and apply an exact photon flux value to star forming regions

## Deliverable Target
> **Ending Product: A publication-quality, non-linearly stretched scientific image plotting of the Triangulum Galaxy pinned to the repository landing page

## **Core Academic Framework & Tech Libraries: 
- Language & Runtime: Python 3.13.14
- Astrophysics Engines: AstroPy (`AsinhStretch`, `ImageNormalize`) | Astroalign | Photoutils |
- Computational Core: | NumPy | Matplotlib |
