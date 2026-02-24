import marimo

__generated_with = "0.20.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **GEOSPATIAL PYTHON**

    _Sources: Parts of this session are based on AutoGIS: Python for geospatial analysis (2024) and CoPhil EO AI/ML Training (2025)_

    <br>

    # **Which GIS packages are available in Python?**

    In **Session 1 Python Programming Fundamentals**, you have already worked with several Python libraries for specific tasks — for example, <strong><a href="https://numpy.org/" target="_blank">NumPy</a></strong> for numerical computations and <strong><a href="https://matplotlib.org/" target="_blank">Matplotlib</a></strong> for visualization. In this section, we will expand that toolkit by introducing additional Python packages commonly used for GIS, spatial analysis, and geospatial data processing.

    Below is an overview of widely used Python libraries for GIS and spatial data analysis. This list serves as a starting point when tackling geospatial or data analysis problems. However, since the Python ecosystem evolves rapidly, it is always good practice to search for newer or more suitable alternatives when needed.

    Even if you learnt about a package from a blog post, or from this course, always check the package’s own documentation page for its recommended use.

    ## <strong>Core Geometry Library:</strong>


    <div style="display:flex; gap:12px; align-items:center;">
      <img src="https://autogis-site.readthedocs.io/en/latest/_images/simple-features_595x500px.svg" style="height:180px; width:auto;">
      <img src="https://shapely.readthedocs.io/en/2.1.1/_images/linestring.png" style="height:180px; width:auto;">
      <img src="https://i.sstatic.net/2l2Ir.png" style="height:180px; width:auto;">
    </div>

    - <strong><a href="https://shapely.readthedocs.io/" target="_blank">**Shapely**</a></strong>:
      Python package for manipulation and analysis of planar geometric objects (based on widely deployed GEOS).

    ## <strong>Vector Data Handling:</strong>

    <div style="display:flex; gap:12px; align-items:center;">
      <img src="https://geopandas.org/en/stable/_images/boro_centers_over_bounds.png" style="height:180px; width:auto;">
      <img src="https://geopandas.org/en/stable/_images/chicago_choro.png" style="height:180px; width:auto;">
      <img src="https://i.sstatic.net/p2NN4.png" style="height:180px; width:auto;">
    </div>

    - <strong><a href="https://geopandas.org/" target="_blank">**GeoPandas**</a></strong>:
      Working with geospatial data in Python made easier, combines the capabilities of pandas and shapely.

    ## <strong>Raster Data Processing:</strong>

    <div style="display:flex; gap:12px; align-items:center;">
      <img src="https://images.squarespace-cdn.com/content/v1/58c95854c534a56689231265/1606500759670-7D5DYJZCVFUW9XZ9HS03/imagen_2020-11-27_131150.jpg?format=2500w" style="height:180px; width:auto;">
      <img src="http://farm6.staticflickr.com/5032/13938576006_b99b23271b_o_d.png" style="height:180px; width:auto;">
      <img src="https://rasterio.readthedocs.io/en/stable/_images/subplots.jpg" style="height:180px; width:auto;">
    </div>

    - <strong><a href="https://rasterio.readthedocs.io/" target="_blank">**Rasterio**</a></strong>:
      Clean, fast geospatial raster I/O for Python.

    ## <strong>Coordinate Reference Systems:</strong>

    <div style="display:flex; gap:12px; align-items:center;">
      <img src="https://earthdatascience.org/images/courses/earth-analytics/spatial-data/compare-mercator-utm-wgs-projections.jpg" style="height:180px; width:auto;">
      <img src="https://pygis.io/_images/d_crs_assigned.png" style="height:180px; width:auto;">
      <img src="https://docs.qgis.org/3.40/en/_images/plate_carree_projection.png" style="height:180px; width:auto;">
    </div>

    - <strong><a href="https://pyproj4.github.io/pyproj/" target="_blank">**PyProj**</a></strong>:
      Performs cartographic transformations and geodetic computations (based on PROJ).


    ## <strong>Spatial Indexing and Advanced Tools:</strong>

    - <strong><a href="https://fiona.readthedocs.io/" target="_blank">**Fiona**</a></strong>:
      Reading and writing spatial data (alternative backend used by geopandas).

    - <strong><a href="https://gdal.org/" target="_blank">**GDAL**</a></strong>:
      Fundamental package for processing vector and raster data formats (many modules below depend on this). Used for raster processing.

    - <strong><a href="https://rtree.readthedocs.io/" target="_blank">**Rtree**</a></strong>:
      Spatial indexing for Python for quick spatial lookups.

    ## <strong>Visualization and Intereactive Mapping:</strong>

    - <strong><a href="https://matplotlib.org/" target="_blank">**Matplotlib**</a></strong>:
      Basic plotting library for Python

    - <strong><a href="https://plotly.com/python/" target="_blank">**Plotly**</a></strong>:
      Interactive visualizations (also maps) for the web (commercial - free for educational purposes)

    - <strong><a href="https://contextily.readthedocs.io/" target="_blank">**Contextily**</a></strong>:
      Add background basemaps for your static map visualizations.

    <div style="display:flex; gap:12px; align-items:center;">
      <img src="https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/folium-custom-binning.90ad36ea82de.png" style="height:180px; width:auto;">
      <img src="https://miro.medium.com/1%2AxhvBwedtB1-Ub7HfVcYstQ.png" style="height:180px; width:auto;">
      <img src="https://crimede-coder.com/images/FoliumMapDurham.png" style="height:180px; width:auto;">
    </div>

    - <strong><a href="https://python-visualization.github.io/folium/latest/" target="_blank">**Folium**</a></strong>:
      Interactive visualizations using Leaflet.js, allowing users to visualize data as markers, choropleths, or overlays, and supports various tilesets and vector/raster/HTML layers.


    ## <strong>Other data analysis & visualization libraries:</strong>

    - <strong><a href="https://numpy.org/" target="_blank">**NumPy**</a></strong>:
      Fundamental package for scientific computing with Python

    - <strong><a href="https://pandas.pydata.org/" target="_blank">**Pandas**</a></strong>:
      High-performance, easy-to-use data structures and data analysis tools

    - <strong><a href="https://scipy.org/" target="_blank">**SciPy**</a></strong>:
      A collection of numerical algorithms and domain-specific toolboxes, including signal processing, optimization and statistics

    - <strong><a href="https://bokeh.org/" target="_blank">**Bokeh**</a></strong>:
      Interactive visualizations for the web (also maps)


    ## <strong>Other GIS libraries:</strong>

    - <strong><a href="https://pysal.org/" target="_blank">**PySAL**</a></strong>:
      Library of spatial analysis functions written in Python.

    - <strong><a href="https://geopy.readthedocs.io/" target="_blank">**Geopy**</a></strong>:
      Geocoding library: coordinates ↔ address conversion.

    - <strong><a href="https://geoviews.org/" target="_blank">**GeoViews**</a></strong>:
      Interactive maps for the web.

    - <strong><a href="https://residentmario.github.io/geoplot/" target="_blank">**Geoplot**</a></strong>:
      High-level geospatial data visualization library for Python.

    - <strong><a href="https://dash.plotly.com/" target="_blank">**Dash**</a></strong>:
      Python framework for building analytical web applications.

    - <strong><a href="https://osmnx.readthedocs.io/" target="_blank">**OSMnx**</a></strong>:
      Retrieve, construct, analyze, and visualize street networks from OpenStreetMap.

    - <strong><a href="https://networkx.org/" target="_blank">**NetworkX**</a></strong>:
      Network analysis and routing in Python (e.g., Dijkstra and A* algorithms).

    - <strong><a href="https://scitools.org.uk/cartopy/" target="_blank">**Cartopy**</a></strong>:
      Drawing maps for data analysis and visualization.

    - <strong><a href="https://docs.scipy.org/doc/scipy/reference/spatial.html" target="_blank">**scipy.spatial**</a></strong>:
      Spatial algorithms and data structures.

    - <strong><a href="https://www.rsgislib.org/" target="_blank">**RSGISLib**</a></strong>:
      Remote Sensing and GIS Software Library for Python.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="
        background-color: white;
        border: 2px solid black;
        border-left: 21px solid black;
        padding: 16px;
        border-radius: 8px;
        color: black;
    ">

    <strong style="font-size:18px;">💡 TIP:</strong>

    <br><br>

    If you look through the list of links above, you will notice that many projects host their documentation on
    <a href="https://readthedocs.io" target="_blank" style="color:#4cc9f0;">
    readthedocs.io
    </a> (RTD), more specifically at the URL:

    <br><br>

    <code> https://{PROJECT_NAME}.readthedocs.io/</code>

    <br><br>

    RTD has become the de-facto standard service for hosting documentation for Python packages; if you are looking for documentation for a Python package, quickly trying its (assumed) readthedocs address often works.

    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Definition of Terms:**

    This section outlines key terms you may encounter when exploring geospatial Python and AI, organized alphabetically by category for easy reference.

    <strong style="font-size:18px;">Geospatial Data Terms:</strong>

    <ul>

    <li>
    <strong>Affine Transformation</strong><br>
    Mathematical operation describing the relationship between pixel coordinates and geographic coordinates in raster data.
    </li>

    <li>
    <strong>Bounding Box</strong><br>
    Rectangular area defined by minimum and maximum coordinates [minX, minY, maxX, maxY], used to specify geographic extents.
    </li>

    <li>
    <strong>Coordinate Reference System (CRS)</strong><br>
    System defining how coordinates relate to real-world locations, including datum and projection (e.g., WGS84, UTM).
    </li>

    <li>
    <strong>Digital Elevation Model (DEM)</strong><br>
    Raster representation of terrain elevation, with each pixel value representing height above a reference level.
    </li>

    <li>
    <strong>Feature</strong><br>
    In geospatial terms, a vector object (point, line, or polygon) with associated attributes.
    </li>

    <li>
    <strong>GeoJSON</strong><br>
    Open standard JSON format for encoding geographic data structures, widely used for web mapping.
    </li>

    <li>
    <strong>GeoPackage</strong><br>
    Open format for geospatial data storage in SQLite database, supporting both vector and raster data.
    </li>

    <li>
    <strong>Geometry</strong><br>
    The spatial component of a geographic feature, defining its shape and location (point, line, polygon).
    </li>

    <li>
    <strong>GeoTIFF</strong><br>
    Raster image format with embedded geographic metadata (CRS, extent, resolution), standard for geospatial raster data.
    </li>

    <li>
    <strong>NoData Value</strong><br>
    Special value in raster data indicating missing or invalid data (e.g., -9999, NaN).
    </li>

    <li>
    <strong>Pixel Resolution (Spatial Resolution)</strong><br>
    Ground area represented by one pixel (e.g., 10m means each pixel covers 10m × 10m on the ground).
    </li>

    <li>
    <strong>Projection</strong><br>
    Mathematical transformation converting 3D Earth coordinates to 2D map coordinates (e.g., Mercator, UTM).
    </li>

    <li>
    <strong>Raster Data</strong><br>
    Grid-based spatial data where each cell (pixel) contains a value, used for continuous phenomena (elevation, temperature, imagery).
    </li>

    <li>
    <strong>Reproject</strong><br>
    Converting geospatial data from one coordinate reference system to another.
    </li>

    <li>
    <strong>Shapefile</strong><br>
    Popular vector data format for GIS, consisting of multiple files (.shp, .shx, .dbf, .prj).
    </li>

    <li>
    <strong>Spatial Join</strong><br>
    Combining attributes from two geospatial datasets based on their spatial relationship (intersection, within, etc.).
    </li>

    <li>
    <strong>Vector Data</strong><br>
    Spatial data representing discrete features as points, lines, or polygons with associated attributes.
    </li>

    <li>
    <strong>Well-Known Text (WKT)</strong><br>
    Text markup language for representing vector geometry and spatial reference systems.
    </li>

    </ul>

    <strong style="font-size:18px;">Earth Observation Terms:</strong>

    <ul>

    <li>
    <strong>Absorption Band</strong><br>
    Wavelength region where atmospheric gases (water vapor, oxygen, CO2) absorb electromagnetic radiation, limiting remote sensing capabilities.
    </li>

    <li>
    <strong>Backscatter</strong><br>
    The portion of radar energy reflected back to the sensor from a target. Used in SAR imaging to detect surface properties and moisture.
    </li>

    <li>
    <strong>Cloud Masking</strong><br>
    The process of identifying and removing cloud-contaminated pixels from optical satellite imagery to improve data quality.
    </li>

    <li>
    <strong>Composite Image</strong><br>
    A single image created by combining multiple images from different dates, often using statistical methods (median, mean) to reduce noise and clouds.
    </li>

    <li>
    <strong>Earth Observation (EO)</strong><br>
    The gathering of information about Earth’s physical, chemical, and biological systems through remote sensing technologies, primarily satellites.
    </li>

    <li>
    <strong>False Color Composite</strong><br>
    An image display where spectral bands are assigned to RGB colors differently than natural vision (e.g., NIR-Red-Green), revealing features invisible to the human eye.
    </li>

    <li>
    <strong>Ground Truth</strong><br>
    Field-collected reference data used to validate remote sensing classifications and train machine learning models.
    </li>

    <li>
    <strong>Image Collection</strong><br>
    A set of satellite images covering the same geographic area at different times, used for time series analysis.
    </li>

    <li>
    <strong>Pixel</strong><br>
    The smallest unit in a raster image, representing a specific ground area (spatial resolution) and spectral value.
    </li>

    <li>
    <strong>Preprocessing</strong><br>
    Steps taken to correct raw satellite data before analysis, including atmospheric correction, geometric correction, and radiometric calibration.
    </li>

    <li>
    <strong>Remote Sensing</strong><br>
    The science of obtaining information about objects or areas from a distance, typically using sensors on satellites or aircraft.
    </li>

    <li>
    <strong>Revisit Time</strong><br>
    The frequency with which a satellite can observe the same location on Earth (e.g., Sentinel-2 has 5-day revisit with 3 satellites).
    </li>

    <li>
    <strong>Spectral Signature</strong><br>
    The unique reflectance pattern of an object across different wavelengths, used to identify materials and land cover types.
    </li>

    <li>
    <strong>True Color Composite</strong><br>
    An image display using red, green, and blue bands to create a natural-looking image similar to human vision.
    </li>

    </ul>

    <strong style="font-size:18px;">Satellite & Sensor Terms:</strong>

    <ul>

    <li>
    <strong>Active Sensor</strong><br>
    Sensor that emits its own energy and measures the reflected signal (e.g., SAR, LiDAR).
    </li>

    <li>
    <strong>Atmospheric Correction</strong><br>
    Processing step removing atmospheric effects (scattering, absorption) to retrieve surface reflectance.
    </li>

    <li>
    <strong>C-band</strong><br>
    Radar frequency band (4–8 GHz, wavelength 3.75–7.5 cm) used by Sentinel-1, good for vegetation and soil moisture.
    </li>

    <li>
    <strong>Electromagnetic Spectrum</strong><br>
    Range of all electromagnetic radiation wavelengths, from radio waves to gamma rays, including visible light.
    </li>

    <li>
    <strong>Geometric Correction</strong><br>
    Correcting image distortions caused by sensor viewing angle, terrain, and Earth’s curvature.
    </li>

    <li>
    <strong>Level 1C (L1C)</strong><br>
    Sentinel-2 product with Top-of-Atmosphere (TOA) reflectance, geometrically corrected.
    </li>

    <li>
    <strong>Level 2A (L2A)</strong><br>
    Sentinel-2 product with Bottom-of-Atmosphere (BOA) surface reflectance, atmospherically corrected.
    </li>

    <li>
    <strong>LiDAR</strong><br>
    Light Detection and Ranging – active sensor using laser pulses to measure distance, creating high-resolution 3D point clouds.
    </li>

    <li>
    <strong>Multispectral</strong><br>
    Imaging system capturing data in multiple (typically 3–15) wavelength bands across visible and infrared spectrum.
    </li>

    <li>
    <strong>Near Infrared (NIR)</strong><br>
    Electromagnetic radiation with wavelengths 0.7–1.4 μm, strongly reflected by healthy vegetation.
    </li>

    <li>
    <strong>Optical Sensor</strong><br>
    Passive sensor detecting reflected sunlight in visible and infrared wavelengths (e.g., Sentinel-2, Landsat).
    </li>

    <li>
    <strong>Orbit</strong><br>
    Path of a satellite around Earth, characterized by altitude, inclination, and period.
    </li>

    <li>
    <strong>Panchromatic</strong><br>
    Single-band imagery capturing all visible wavelengths, typically at higher spatial resolution than multispectral bands.
    </li>

    <li>
    <strong>Passive Sensor</strong><br>
    Sensor detecting naturally available energy, typically reflected sunlight (e.g., optical cameras).
    </li>

    <li>
    <strong>Polarization</strong><br>
    Orientation of radar waves (HH, VV, HV, VH), providing information about surface structure and moisture.
    </li>

    <li>
    <strong>Radiometric Calibration</strong><br>
    Converting raw sensor digital numbers to physical units (radiance or reflectance).
    </li>

    <li>
    <strong>SAR (Synthetic Aperture Radar)</strong><br>
    Active microwave imaging system creating high-resolution images independent of sunlight and clouds.
    </li>

    <li>
    <strong>Short-Wave Infrared (SWIR)</strong><br>
    Electromagnetic radiation with wavelengths 1.4–3.0 μm, useful for detecting moisture and minerals.
    </li>

    <li>
    <strong>Spectral Resolution</strong><br>
    Ability to distinguish between different wavelengths, determined by number and width of spectral bands.
    </li>

    <li>
    <strong>Sun-Synchronous Orbit</strong><br>
    Satellite orbit maintaining constant local solar time, ensuring consistent illumination conditions.
    </li>

    <li>
    <strong>Temporal Resolution</strong><br>
    Frequency of repeat observations over the same location (synonymous with revisit time).
    </li>

    </ul>

    <strong style="font-size:18px;">AI/ML Terms:</strong>

    <ul>

    <li>
    <strong>Activation Function</strong><br>
    Mathematical function in neural networks that introduces non-linearity (e.g., ReLU, Sigmoid, Tanh), enabling learning of complex patterns.
    </li>

    <li>
    <strong>Artificial Intelligence (AI)</strong><br>
    Computer systems capable of performing tasks that typically require human intelligence, including perception, reasoning, and decision-making.
    </li>

    <li>
    <strong>Backpropagation</strong><br>
    Algorithm for training neural networks by calculating gradients of loss and adjusting weights to minimize error.
    </li>

    <li>
    <strong>Batch Size</strong><br>
    Number of training samples processed before updating model weights. Smaller batches = more updates but noisier; larger batches = smoother but fewer updates.
    </li>

    <li>
    <strong>Classification</strong><br>
    Supervised learning task of assigning input data to predefined categories (e.g., forest, water, urban).
    </li>

    <li>
    <strong>Clustering</strong><br>
    Unsupervised learning technique that groups similar data points together without predefined labels (e.g., K-means, DBSCAN).
    </li>

    <li>
    <strong>Confusion Matrix</strong><br>
    Table showing predicted vs. actual classifications, used to calculate accuracy, precision, recall, and F1-score.
    </li>

    <li>
    <strong>Convolutional Neural Network (CNN)</strong><br>
    Deep learning architecture specialized for image analysis, using convolutional layers to detect spatial patterns.
    </li>

    <li>
    <strong>Data Augmentation</strong><br>
    Technique to artificially increase training data by applying transformations (rotation, flipping, scaling) to existing samples.
    </li>

    <li>
    <strong>Deep Learning</strong><br>
    Subset of machine learning using multi-layer neural networks to learn hierarchical representations of data.
    </li>

    <li>
    <strong>Epoch</strong><br>
    One complete pass through the entire training dataset during model training.
    </li>

    <li>
    <strong>Feature Engineering</strong><br>
    The process of creating new input variables from raw data to improve model performance.
    </li>

    <li>
    <strong>Feature Extraction</strong><br>
    Identifying and extracting relevant patterns or characteristics from raw data for use in machine learning models.
    </li>

    <li>
    <strong>Ground Truth Labels</strong><br>
    Verified, accurate labels for training data, typically from field surveys or expert interpretation.
    </li>

    <li>
    <strong>Hyperparameter</strong><br>
    Model configuration setting chosen before training (e.g., learning rate, number of layers) that affects model performance.
    </li>

    <li>
    <strong>Loss Function</strong><br>
    Mathematical function measuring the difference between predicted and actual values, used to guide model training.
    </li>

    <li>
    <strong>Machine Learning (ML)</strong><br>
    Subset of AI enabling systems to learn and improve from experience without explicit programming.
    </li>

    <li>
    <strong>Neural Network</strong><br>
    Computing system inspired by biological brains, consisting of interconnected nodes (neurons) organized in layers.
    </li>

    <li>
    <strong>Overfitting</strong><br>
    When a model learns training data too well, including noise, resulting in poor performance on new data.
    </li>

    <li>
    <strong>Precision</strong><br>
    Proportion of positive predictions that are actually correct. Precision = TP / (TP + FP).
    </li>

    <li>
    <strong>Random Forest</strong><br>
    Ensemble learning method using multiple decision trees to improve prediction accuracy and reduce overfitting.
    </li>

    <li>
    <strong>Recall (Sensitivity)</strong><br>
    Proportion of actual positives correctly identified. Recall = TP / (TP + FN).
    </li>

    <li>
    <strong>Regression</strong><br>
    Supervised learning task of predicting continuous numerical values (e.g., crop yield, temperature).
    </li>

    <li>
    <strong>Supervised Learning</strong><br>
    Machine learning where models learn from labeled training data (input-output pairs).
    </li>

    <li>
    <strong>Support Vector Machine (SVM)</strong><br>
    Classification algorithm that finds the optimal hyperplane separating different classes in feature space.
    </li>

    <li>
    <strong>Training Set</strong><br>
    Portion of data used to train a machine learning model (typically 70–80% of total data).
    </li>

    <li>
    <strong>Transfer Learning</strong><br>
    Reusing a pre-trained model on a new but related task, reducing training time and data requirements.
    </li>

    <li>
    <strong>Underfitting</strong><br>
    When a model is too simple to capture the underlying patterns in data, resulting in poor performance.
    </li>

    <li>
    <strong>Unsupervised Learning</strong><br>
    Machine learning where models find patterns in unlabeled data without predefined categories.
    </li>

    <li>
    <strong>Validation Set</strong><br>
    Data used to evaluate model performance during training and tune hyperparameters (typically 10–15% of data).
    </li>

    </ul>

    <strong style="font-size:18px;">Technical Acronyms:</strong>

    <ul>

    <li>
    <strong>AI</strong><br>
    Artificial Intelligence – computer systems performing tasks requiring human intelligence.
    </li>

    <li>
    <strong>API</strong><br>
    Application Programming Interface – set of functions allowing software to interact with services (e.g., Earth Engine Python API).
    </li>

    <li>
    <strong>BOA</strong><br>
    Bottom of Atmosphere – surface reflectance after atmospheric correction (Level 2A products).
    </li>

    <li>
    <strong>CNN</strong><br>
    Convolutional Neural Network – deep learning architecture for image analysis.
    </li>

    <li>
    <strong>CRS</strong><br>
    Coordinate Reference System – defines how coordinates relate to Earth’s surface.
    </li>

    <li>
    <strong>DEM</strong><br>
    Digital Elevation Model – raster representation of terrain elevation.
    </li>

    <li>
    <strong>DL</strong><br>
    Deep Learning – subset of ML using multi-layer neural networks.
    </li>

    <li>
    <strong>DRR</strong><br>
    Disaster Risk Reduction – strategies to minimize disaster impacts.
    </li>

    <li>
    <strong>EO</strong><br>
    Earth Observation – gathering information about Earth through remote sensing.
    </li>

    <li>
    <strong>EPSG</strong><br>
    European Petroleum Survey Group – whic originally published a database for spatial reference systems. EPSG codes refer to specific reference systems.
    </li>

    <li>
    <strong>ESA</strong><br>
    European Space Agency – operates Copernicus Sentinel missions.
    </li>

    <li>
    <strong>EVI</strong><br>
    Enhanced Vegetation Index – vegetation index less sensitive to atmospheric effects than NDVI.
    </li>

    <li>
    <strong>GEE</strong><br>
    Google Earth Engine – cloud platform for planetary-scale geospatial analysis.
    </li>

    <li>
    <strong>GIS</strong><br>
    Geographic Information System – software for capturing, managing, and analyzing spatial data.
    </li>

    <li>
    <strong>GPU</strong><br>
    Graphics Processing Unit – hardware accelerating deep learning computations.
    </li>

    <li>
    <strong>GNSS</strong><br>
    Global Navigation Satellite System – satellite-based positioning (GPS, Galileo, GLONASS).
    </li>

    <li>
    <strong>HDF</strong><br>
    Hierarchical Data Format – file format for storing large scientific datasets.
    </li>

    <li>
    <strong>IW</strong><br>
    Interferometric Wide Swath – Sentinel-1 acquisition mode with 250 km swath.
    </li>

    <li>
    <strong>LiDAR</strong><br>
    Light Detection and Ranging – laser-based remote sensing for elevation mapping.
    </li>

    <li>
    <strong>LULC</strong><br>
    Land Use Land Cover – classification of Earth’s surface into categories (forest, urban, agriculture, etc.).
    </li>

    <li>
    <strong>ML</strong><br>
    Machine Learning – algorithms enabling systems to learn from data.
    </li>

    <li>
    <strong>MODIS</strong><br>
    Moderate Resolution Imaging Spectroradiometer – NASA sensor providing daily global coverage.
    </li>

    <li>
    <strong>NASA</strong><br>
    National Aeronautics and Space Administration – operates Landsat and other EO missions.
    </li>

    <li>
    <strong>NDBI</strong><br>
    Normalized Difference Built-up Index – spectral index for detecting built-up areas.
    </li>

    <li>
    <strong>NDVI</strong><br>
    Normalized Difference Vegetation Index – spectral index measuring vegetation health/density.
    </li>

    <li>
    <strong>NDWI</strong><br>
    Normalized Difference Water Index – spectral index for detecting water bodies.
    </li>

    <li>
    <strong>NIR</strong><br>
    Near Infrared – electromagnetic radiation beyond visible red (0.7–1.4 μm).
    </li>

    <li>
    <strong>RGB</strong><br>
    Red-Green-Blue – color model using three primary colors, or the corresponding image bands.
    </li>

    <li>
    <strong>RF</strong><br>
    Random Forest – ensemble machine learning algorithm using multiple decision trees.
    </li>

    <li>
    <strong>SAR</strong><br>
    Synthetic Aperture Radar – active microwave imaging system.
    </li>

    <li>
    <strong>SCL</strong><br>
    Scene Classification Layer – Sentinel-2 cloud and land cover classification mask.
    </li>

    <li>
    <strong>SNAP</strong><br>
    Sentinel Application Platform – ESA’s free software for processing Sentinel data.
    </li>

    <li>
    <strong>SWIR</strong><br>
    Short-Wave Infrared – electromagnetic radiation with wavelengths 1.4–3.0 μm.
    </li>

    <li>
    <strong>SVM</strong><br>
    Support Vector Machine – classification algorithm finding optimal separating hyperplane.
    </li>

    <li>
    <strong>TOA</strong><br>
    Top of Atmosphere – apparent reflectance before atmospheric correction (Level 1C products).
    </li>

    <li>
    <strong>UTM</strong><br>
    Universal Transverse Mercator – widely-used projected coordinate system dividing Earth into zones.
    </li>

    <li>
    <strong>WGS84</strong><br>
    World Geodetic System 1984 – global geographic coordinate system (EPSG:4326).
    </li>

    </ul>

    <strong style="font-size:18px;">Spectral Indices:</strong>

    <ul>

    <li>
    <strong>NDVI (Normalized Difference Vegetation Index)</strong>
    <div style="margin-left:20px;">
        <strong>Formula:</strong> (NIR - Red) / (NIR + Red)<br>
        <strong>Range:</strong> -1 to +1<br>
        <strong>Interpretation:</strong><br>
        &nbsp;&nbsp;High values (0.6–0.9): Dense vegetation<br>
        &nbsp;&nbsp;Moderate (0.2–0.5): Sparse vegetation<br>
        &nbsp;&nbsp;Near zero: Bare soil, rock<br>
        &nbsp;&nbsp;Negative: Water, clouds<br>
        <strong>Sentinel-2 Bands:</strong> (B8 - B4) / (B8 + B4)
    </div>
    </li>

    <li>
    <strong>NDWI (Normalized Difference Water Index)</strong>
    <div style="margin-left:20px;">
        <strong>McFeeters Formula:</strong> (Green - NIR) / (Green + NIR)<br>
        <strong>Gao Formula:</strong> (NIR - SWIR) / (NIR + SWIR)<br>
        <strong>Range:</strong> -1 to +1<br>
        <strong>Interpretation:</strong><br>
        &nbsp;&nbsp;Positive values: Water bodies<br>
        &nbsp;&nbsp;Negative values: Land surfaces<br>
        <strong>Sentinel-2 (McFeeters):</strong> (B3 - B8) / (B3 + B8)<br>
        <strong>Sentinel-2 (Gao):</strong> (B8 - B11) / (B8 + B11)
    </div>
    </li>

    <li>
    <strong>NDBI (Normalized Difference Built-up Index)</strong>
    <div style="margin-left:20px;">
        <strong>Formula:</strong> (SWIR - NIR) / (SWIR + NIR)<br>
        <strong>Range:</strong> -1 to +1<br>
        <strong>Interpretation:</strong><br>
        &nbsp;&nbsp;Positive values: Built-up areas<br>
        &nbsp;&nbsp;Negative values: Vegetation, water<br>
        <strong>Sentinel-2:</strong> (B11 - B8) / (B11 + B8)
    </div>
    </li>

    <li>
    <strong>EVI (Enhanced Vegetation Index)</strong>
    <div style="margin-left:20px;">
        <strong>Formula:</strong> 2.5 × ((NIR - Red) / (NIR + 6×Red - 7.5×Blue + 1))<br>
        <strong>Range:</strong> -1 to +1<br>
        <strong>Advantages:</strong> Less sensitive to atmospheric effects and soil background than NDVI<br>
        <strong>Sentinel-2:</strong> 2.5 × ((B8 - B4) / (B8 + 6×B4 - 7.5×B2 + 1))
    </div>
    </li>

    </ul>

    <strong style="font-size:18px;">Sentinel-2 Band Summary:</strong>

    <table style="border-collapse: collapse; width: 100%;">
        <tr>
            <th style="border: 1px solid black; background-color: white;">Band</th>
            <th style="border: 1px solid black; background-color: white;">Name</th>
            <th style="border: 1px solid black; background-color: white;">Wavelength (nm)</th>
            <th style="border: 1px solid black; background-color: white;">Resolution (m)</th>
            <th style="border: 1px solid black; background-color: white;">Typical Use</th>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B1</td>
            <td style="border: 1px solid black; background-color: white;">Coastal aerosol</td>
            <td style="border: 1px solid black; background-color: white;">443</td>
            <td style="border: 1px solid black; background-color: white;">60</td>
            <td style="border: 1px solid black; background-color: white;">Atmospheric correction</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B2</td>
            <td style="border: 1px solid black; background-color: white;">Blue</td>
            <td style="border: 1px solid black; background-color: white;">490</td>
            <td style="border: 1px solid black; background-color: white;">10</td>
            <td style="border: 1px solid black; background-color: white;">Bathymetry, soil/vegetation</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B3</td>
            <td style="border: 1px solid black; background-color: white;">Green</td>
            <td style="border: 1px solid black; background-color: white;">560</td>
            <td style="border: 1px solid black; background-color: white;">10</td>
            <td style="border: 1px solid black; background-color: white;">Peak vegetation sensitivity</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B4</td>
            <td style="border: 1px solid black; background-color: white;">Red</td>
            <td style="border: 1px solid black; background-color: white;">665</td>
            <td style="border: 1px solid black; background-color: white;">10</td>
            <td style="border: 1px solid black; background-color: white;">Vegetation discrimination</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B5</td>
            <td style="border: 1px solid black; background-color: white;">Red Edge 1</td>
            <td style="border: 1px solid black; background-color: white;">705</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Vegetation health</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B6</td>
            <td style="border: 1px solid black; background-color: white;">Red Edge 2</td>
            <td style="border: 1px solid black; background-color: white;">740</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Vegetation stress</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B7</td>
            <td style="border: 1px solid black; background-color: white;">Red Edge 3</td>
            <td style="border: 1px solid black; background-color: white;">783</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Vegetation stress</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B8</td>
            <td style="border: 1px solid black; background-color: white;">NIR</td>
            <td style="border: 1px solid black; background-color: white;">842</td>
            <td style="border: 1px solid black; background-color: white;">10</td>
            <td style="border: 1px solid black; background-color: white;">Biomass, water bodies</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B8A</td>
            <td style="border: 1px solid black; background-color: white;">Narrow NIR</td>
            <td style="border: 1px solid black; background-color: white;">865</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Atmospheric correction</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B9</td>
            <td style="border: 1px solid black; background-color: white;">Water vapor</td>
            <td style="border: 1px solid black; background-color: white;">945</td>
            <td style="border: 1px solid black; background-color: white;">60</td>
            <td style="border: 1px solid black; background-color: white;">Atmospheric correction</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B11</td>
            <td style="border: 1px solid black; background-color: white;">SWIR 1</td>
            <td style="border: 1px solid black; background-color: white;">1610</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Moisture, soil/vegetation</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">B12</td>
            <td style="border: 1px solid black; background-color: white;">SWIR 2</td>
            <td style="border: 1px solid black; background-color: white;">2190</td>
            <td style="border: 1px solid black; background-color: white;">20</td>
            <td style="border: 1px solid black; background-color: white;">Moisture, burned areas</td>
        </tr>
    </table>


    <strong style="font-size:18px;">Common CRS for Philippines:</strong>

    <table style="border-collapse: collapse; width: 100%;">
        <tr>
            <th style="border: 1px solid black; background-color: white;">Name</th>
            <th style="border: 1px solid black; background-color: white;">EPSG Code</th>
            <th style="border: 1px solid black; background-color: white;">Type</th>
            <th style="border: 1px solid black; background-color: white;">Use Case</th>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">WGS84</td>
            <td style="border: 1px solid black; background-color: white;">4326</td>
            <td style="border: 1px solid black; background-color: white;">Geographic</td>
            <td style="border: 1px solid black; background-color: white;">Global datasets, web maps</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">UTM Zone 50N</td>
            <td style="border: 1px solid black; background-color: white;">32650</td>
            <td style="border: 1px solid black; background-color: white;">Projected</td>
            <td style="border: 1px solid black; background-color: white;">Western Mindanao</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">UTM Zone 51N</td>
            <td style="border: 1px solid black; background-color: white;">32651</td>
            <td style="border: 1px solid black; background-color: white;">Projected</td>
            <td style="border: 1px solid black; background-color: white;">Luzon, Visayas, most of Philippines</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">UTM Zone 52N</td>
            <td style="border: 1px solid black; background-color: white;">32652</td>
            <td style="border: 1px solid black; background-color: white;">Projected</td>
            <td style="border: 1px solid black; background-color: white;">Eastern Mindanao</td>
        </tr>
        <tr>
            <td style="border: 1px solid black; background-color: white;">PRS92</td>
            <td style="border: 1px solid black; background-color: white;">4683</td>
            <td style="border: 1px solid black; background-color: white;">Geographic</td>
            <td style="border: 1px solid black; background-color: white;">Philippine Reference System</td>
        </tr>
    </table>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Managing file paths (_pathlib_)**

    Managing file paths reliably is essential when working with data across computers, virtual environments, or version‑controlled projects like GitHub repositories. Hard‑coded strings and manual string manipulation for paths are fragile and prone to errors, especially when operating systems differ (e.g., / vs \).

    Python’s built‑in pathlib module (introduced in Python 3.4) provides an easy, cross‑platform, object‑oriented way to work with filesystem paths.

    ### **Key points:**

    **Path objects:**
    - Create path objects using pathlib.Path().
    - Without arguments, it refers to the current script/notebook directory.
    - Calling .resolve() converts it to an absolute, system‑aware path.

    **Useful methods and properties:**
    - .exists(), .is_dir(), etc., let you check path status on the filesystem.
    - path.parent gets the parent directory.
    - Path objects automatically convert to strings when needed.

    **Path manipulation with /:**
    - Join path components using the / operator (instead of string concatenation) for cleaner, OS‑independent code:

    **Good practice in projects:**
    - Define constants like **DATA_DIRECTORY = NOTEBOOK_PATH / "data"** at the start of notebooks to centralize where data files are stored and used.
    """)
    return


@app.cell
def _():
    from pathlib import Path

    # Create a Path object for the current directory
    current_dir = Path()
    print("Current directory:", current_dir.resolve())

    # Define a data folder and a file inside it
    data_dir = current_dir / "data"
    palay_dir = data_dir / "Non-Target Features (Palay, Fishponds)" / "PH_Palay2022S1S2_Post-GT_Updated" / "PH_Palay2022S1S2_Post-GT_Updated.shp"

    # Check if the data folder exists, create if not
    if not data_dir.exists():
        data_dir.mkdir()
        print("Created data directory:", data_dir)

    # Check if the file exists
    if palay_dir.exists():
        print("File exists:", palay_dir)
    else:
        print("File does not exist yet:", palay_dir)

    # Access parent directory and file name
    print("Parent directory of the file:", palay_dir.parent)
    print("File name:", palay_dir.name)
    print("File suffix/extension:", palay_dir.suffix)
    return data_dir, palay_dir


@app.cell
def _(palay_dir):
    import geopandas as gpd
    psa_survey_palay = gpd.read_file(palay_dir)
    psa_survey_palay.plot()
    return gpd, psa_survey_palay


@app.cell
def _(psa_survey_palay):
    psa_survey_palay.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Map projections**

    A **coordinate reference system (CRS)** is fundamental metadata for any geospatial dataset. Without a CRS, coordinates are just numbers with no connection to real-world locations. The CRS enables GIS software—including Python libraries—to accurately place these points on Earth or other roughly spherical bodies.

    ![img](https://pygis.io/_images/d_crs_assigned.png)


    CRS is closely related to map projections, though the two are not the same:
    - Map projections (or projected coordinate systems) are mathematical methods for converting locations from the three-dimensional surface of the Earth to a two-dimensional plane, like a flat map.
    - Geographic coordinate systems use latitude and longitude directly as x and y coordinates, representing degrees along the Earth’s surface.
    - Both projected and geographic coordinate systems can use ellipsoids to better approximate the Earth’s irregular form.
    - A full CRS includes both the coordinate system type (projected or geographic) and the ellipsoid.

    Different datasets often use different CRSs because no single system can perfectly preserve angles, distances, and areas across the globe. Therefore, reprojecting data between CRSs is a common GIS task, especially when combining layers. Failing to align CRSs can lead to incorrect results—for instance, checking whether points lie within a polygon will fail if the points use degrees (geographic CRS) and the polygon is measured in meters (projected CRS).

    Choosing an appropriate map projection requires considering your data and map purpose:
    - The “best” projection depends on the scale, resolution, and spatial extent of your data.
    - Every projection has trade-offs; no projection perfectly preserves angles, distances, and areas simultaneously.
    - The projection you choose can even reflect the priorities or perspective of the mapmaker.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Handling coordinate reference systems in Geopandas (_pyproj_)**

    Once you’ve determined the appropriate map projection, working with coordinate reference systems in GeoPandas is relatively straightforward. The **pyproj** library can provide detailed information about a CRS and help with more complex tasks, such as identifying the CRS of a dataset when it’s unknown.

    In this section, we will cover how to access the CRS information of a dataset and how to reproject the data into a different coordinate reference system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="
        background-color: white;
        border: 2px solid black;
        border-left: 21px solid black;
        padding: 16px;
        border-radius: 8px;
        color: black;
    ">

    <strong style="font-size:18px;"> ⚠️ Caution: Careful with Shapefiles</strong>

    <br>

    You might have noticed that geospatial data sets in ESRI Shapefile format consist of multiple files with different file extensions. The .prj file contains information about the coordinate reference system. Be careful not to lose it!

    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Displaying the CRS of a data set**
    """)
    return


@app.cell
def _(psa_survey_palay):
    psa_survey_palay.crs
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What we are looking at here is a **_pyproj.CRS_** object.

    The EPSG code (from the European Petroleum Survey Group) is a global standard used to identify coordinate reference systems. Each number corresponds to an entry in the EPSG Geodetic Parameter Dataset, which contains definitions for coordinate systems and transformations at global, regional, national, and local levels.

    n our GeoDataFrame, the EPSG code is 32651. This is a projected CRS corresponding to UTM Zone 51N, which covers part of the Philippines. Unlike geographic coordinates in degrees, this CRS uses meters, making it ideal for accurately measuring distances, areas, and performing local spatial analysis. Using a projected system like EPSG:32651 is particularly important in the Philippine context, where precise mapping of cities, provinces, or infrastructure is needed for planning, disaster management, and environmental monitoring. It ensures that spatial calculations are consistent and reliable within the region.
    """)
    return


@app.cell
def _(psa_survey_palay):
    psa_survey_palay.geometry.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Reprojecting a GeoDataFrame**

    Converting data between different coordinate reference systems in GeoPandas is straightforward. You simply call the _**to_crs()**_ method on a GeoDataFrame and provide the desired CRS. The method accepts various formats, with the simplest being an EPSG code.
    """)
    return


@app.cell
def _(psa_survey_palay):
    psa_survey_palay_wgs84 = psa_survey_palay.to_crs("EPSG:4326")

    psa_survey_palay_wgs84.crs
    return (psa_survey_palay_wgs84,)


@app.cell
def _(psa_survey_palay_wgs84):
    psa_survey_palay_wgs84.geometry.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Handling different CRS formats**

    - Common CRS formats: PROJ strings, EPSG codes, WKT, JSON
    - Spatial datasets may have different CRS formats
    - Conversion between CRS formats is often needed
    - GeoPandas + pyproj can parse, manage, and convert CRS information
    """)
    return


@app.cell
def _(psa_survey_palay):
    import pyproj

    crs = pyproj.CRS(psa_survey_palay.crs)

    print(f"CRS as a proj4 string: {crs.to_proj4()}\n")

    print(f"CRS in WKT format: {crs.to_wkt()}\n")

    print(f"EPSG code of the CRS: {crs.to_epsg()}\n")
    return (pyproj,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    <div style="
        background-color: white;
        border: 2px solid black;
        border-left: 21px solid black;
        padding: 16px;
        border-radius: 8px;
        color: black;
    ">

    <strong style="font-size:18px;"> 📒 NOTE </strong>

    <br>

    Not all coordinate reference systems have an assigned EPSG code. Therefore, PyProj attempts to find the closest matching EPSG code by default. If no suitable match is found, the <strong>to_epsg() </strong> method returns None.

    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **Use pyproj to find detailed information about a CRS**

    A pyproj.CRS object provides comprehensive details about a reference system, including its name, area of use (with bounds), datum, and ellipsoid.
    """)
    return


@app.cell
def _(pyproj):
    crs_info = pyproj.CRS("EPSG:4326")
    crs_info
    return (crs_info,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You can also access each piece of information individually, for example:
    """)
    return


@app.cell
def _(crs_info):
    # Access individual pieces of information
    print("Name:", crs_info.name)
    print("Area of Use:", crs_info.area_of_use)
    print("Datum:", crs_info.datum)
    print("Ellipsoid:", crs_info.ellipsoid)
    print("Coordinate System:", crs_info.coordinate_system)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Exploring vector and raster data in Python**

    In GIS workflows, understanding and exploring spatial data is as important as reading or writing it. Python provides a rich ecosystem of libraries for vector and raster data exploration, analysis, and visualization.

    ## **Vector Data**
    Vector data represents discrete features such as points, lines, and polygons. Common formats include ESRI Shapefiles, GeoPackage (GPKG), and GeoJSON.

    **GeoPandas**: High-level interface for reading, writing, and manipulating vector datasets.
    - Inspect attributes: gdf.head(), gdf.info(), gdf.describe()
    - Visualize geometries: gdf.plot()
    - Query/filter data by attribute or spatial conditions

    **Fiona**: Low-level file access when reading/writing vector files.

    ## **Raster Data**

    Raster data represents the world as a grid of cells (pixels), with each cell holding a value such as temperature, elevation, or land cover.

    - Single-band raster: Each pixel has a single value (e.g., elevation).
    - Multiband raster: Each pixel contains multiple values (e.g., Red, Green, Blue bands in satellite imagery).

    A key property of raster data is resolution, which defines the ground area each cell represents. Higher resolution provides more detail but increases file size.

    ### **Common raster formats:**
    - GeoTIFF: Flexible format supporting multiple bands, metadata, and compression.
    - JPEG, GIF, BMP, PNG: Suitable for presentations or online applications, but limited metadata support.
    - ASCII Grid: Simple text format often used for elevation data, with spatial info in the header.

    ### **Python libraries:**

    **Rasterio**: provides low-level access to raster files, built on GDAL, supporting reading/writing, pixel access, CRS management, and format conversion.

    **xarray**: handles labeled, multi-dimensional arrays, making it ideal for scientific and spatial data.

    **rioxarray**: extends xarray for geospatial raster operations, leveraging rasterio under the hood. It allows reading/writing raster formats like GeoTIFF, working with CRS, and performing GIS-specific tasks such as reprojection.

    By combining these tools, Python makes it possible to fully explore GIS data: inspect attributes, visualize spatial patterns, analyze relationships, and manipulate datasets for further analysis, for both vector and raster data.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **File formats -- Vector I/O**

    Fiona can read (almost) all geospatial file formats and write to many of them. The exact supported formats may vary depending on the local installation and version. To see which formats are available, you can print the list of Fiona’s file format drivers:
    """)
    return


@app.cell
def _():
    import fiona

    fiona.supported_drivers
    return (fiona,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Fiona uses drivers to handle different geospatial file formats. Each format in the list indicates the capabilities of the driver:

        r → file can be read
        w → file can be written
        a → data can be appended to an existing file

    Note: Each “format” actually refers to the driver implementation, and a single driver may support multiple related file formats.
    """)
    return


@app.cell
def _(data_dir, fiona):
    # Reading a Vector File

    training_data = data_dir / "Training Data (Geotagged target features with ODK Collect Tool)" / "ODk_geoshape" / "geoshape_odk_020426.shp"

    psa_crops_data = fiona.open(training_data / "", "r")

    for crops in psa_crops_data:
        if crops["properties"].get("crop_type") == "tobacco":
            print(crops)
    return (psa_crops_data,)


@app.cell
def _(psa_crops_data):
    # Checking metadata

    print("CRS:", psa_crops_data.crs)
    print("Schema:", psa_crops_data.schema)
    print("Driver:", psa_crops_data.driver)

    return


@app.cell
def _(psa_crops_data):
    for crops_info in psa_crops_data:
        geometry = crops_info["geometry"]
        crop = crops_info["properties"]["crop_type"]
        info = crops_info["properties"]["other_info"]
        print("Geometry:", geometry, "| Crop Type:", crop, "| Other Info:", info)
    return


@app.cell
def _(gpd, psa_crops_data):
    # Create GeoDataFrame with tobacco crops
    tobacco_gpf = gpd.GeoDataFrame(
        [
            {
                "geometry": tobacco_crop["geometry"],
                "crop_type": tobacco_crop["properties"]["crop_type"],
                "other_info": tobacco_crop["properties"]["other_info"]
            }
            for tobacco_crop in psa_crops_data
            if tobacco_crop["properties"].get("crop_type") == "tobacco"
        ],
        crs=psa_crops_data.crs
    )

    tobacco_gpf.head()
    return


if __name__ == "__main__":
    app.run()
