import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # GeoAI with scikit-learn: Supervised Land Cover Classification

    ## 1. Introduction

    Geospatial Artificial Intelligence (GeoAI) refers to the integration of
    machine learning techniques with spatial data. In practice, this means
    using algorithms to discover patterns, make predictions, or classify
    geographic phenomena from remotely sensed imagery and other spatial datasets.

    In this notebook, we will build a complete supervised land cover classification
    workflow using a Sentinel-2 composite image and labeled training polygons.
    Rather than relying on specialized GeoAI libraries, we will use
    **scikit-learn**, a general-purpose machine learning library.

    This approach is intentional. It allows us to clearly understand what happens
    under the hood when we apply machine learning to raster data.

    ---

    ## 2. Why Use scikit-learn for GeoAI?

    scikit-learn is one of the most widely used machine learning libraries in Python.
    Although it is not inherently spatial, it becomes extremely powerful once we
    transform raster data into tabular form.

    In other words:

    - A raster image becomes a matrix of features (spectral bands).
    - Training polygons provide class labels.
    - Machine learning models learn the relationship between spectral signatures and land cover types.

    This transformation—from spatial raster to feature matrix—is the core idea
    behind many GeoAI workflows.

    By using scikit-learn, we emphasize:

    - Conceptual clarity
    - Reproducibility
    - Model transparency
    - Strong evaluation practices

    ---

    ## 3. Dataset Overview

    We will use two datasets:

    **1. Sentinel-2 Composite Image**
    `data/S2_JFM_2025.tif`
    A multispectral composite covering January–March 2025.

    Each pixel contains multiple spectral bands. These bands will serve as
    our predictive features.

    **2. Training Polygons**
    `data/training_polygons.shp`
    A set of labeled polygons representing different land cover classes.

    These polygons define the ground truth used to train our model.

    ---

    ## 4. Learning Objective

    By the end of this notebook, you will be able to:

    - Convert raster data into a machine-learning-ready format
    - Extract training samples from labeled polygons
    - Train a supervised classification model
    - Evaluate model performance
    - Generate a classified land cover map

    This notebook demonstrates the complete GeoAI pipeline:

    Raster → Feature Matrix → Model Training → Evaluation → Full Image Prediction

    Understanding this workflow is fundamental to applying machine learning
    in remote sensing and geospatial analysis.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. From Raster Data to Machine Learning Features

    Machine learning models in scikit-learn expect data in tabular form:

    - Rows represent samples
    - Columns represent features

    However, raster data is not tabular. It is spatial.

    A multispectral raster image can be thought of as a 3D array:

    (height × width × bands)

    Each pixel contains multiple spectral values, one for each band.
    For example, a Sentinel-2 image may contain:

    - Blue
    - Green
    - Red
    - Near Infrared (NIR)
    - Other spectral bands

    From a machine learning perspective, each pixel can be treated as
    one observation (one sample), and each band becomes a feature.

    This means we must transform the raster into a 2D feature matrix:

    (number_of_pixels × number_of_bands)

    In other words:

    Every pixel → one row
    Every spectral band → one column

    This transformation removes spatial structure temporarily so that
    a machine learning model can process the data.

    ---

    ### What About Labels?

    Supervised learning requires labels.

    In our case, labels come from the training polygons. These polygons
    define known land cover types.

    For pixels that fall inside a labeled polygon:

    - We extract their spectral values (features)
    - We assign the polygon's land cover class (label)

    This produces:

    X → Feature matrix (spectral values)
    y → Label vector (land cover class)

    The model then learns the relationship between spectral signatures
    and land cover categories.

    ---

    ### Important Note on Spatial Context

    At this stage, we are treating pixels independently.
    The model does not “know” where pixels are located in space.

    This has important implications:

    - Spatial autocorrelation can inflate accuracy
    - Neighboring pixels often share similar spectral values
    - Random train-test splits may not reflect real-world performance

    We will revisit these limitations later.

    For now, the goal is to understand how spatial raster data becomes
    machine learning input.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Loading and Inspecting the Data

    Before building a machine learning model, we must first understand
    the structure of our datasets.

    We will:

    - Load the Sentinel-2 raster composite
    - Load the training polygons
    - Verify coordinate reference systems (CRS)
    - Inspect raster dimensions and band information

    Understanding your data is a critical step in any GeoAI workflow.
    """)
    return


@app.cell
def _():
    # ============================================================
    # Import Required Libraries
    # ============================================================

    # rasterio is used to read and work with raster datasets
    import rasterio

    # geopandas is used to read and work with vector datasets (e.g., shapefiles)
    import geopandas as gpd

    # numpy is used for numerical operations and array handling
    import numpy as np

    # matplotlib is used for quick visualization
    import matplotlib.pyplot as plt

    # Optional: improves plot display
    plt.rcParams["figure.figsize"] = (6, 6)

    print("Libraries successfully imported.")
    return gpd, np, plt, rasterio


@app.cell
def _(gpd, rasterio):
    # ============================================================
    # Define File Paths
    # ============================================================

    # Path to Sentinel-2 composite image
    raster_path = "data/S2_JFM_2025.tif"

    # Path to training polygons shapefile
    polygons_path = "data/training_polygons.shp"


    # ============================================================
    # Load Raster Dataset
    # ============================================================

    # rasterio.open() does NOT load the entire raster into memory.
    # It creates a dataset object that allows us to read metadata
    # and access bands when needed.
    src = rasterio.open(raster_path)


    # ============================================================
    # Load Vector Dataset (Training Polygons)
    # ============================================================

    # geopandas reads the shapefile into a GeoDataFrame.
    # This behaves like a pandas DataFrame but includes geometry.
    gdf = gpd.read_file(polygons_path)


    print("Raster and training polygons successfully loaded.")
    return gdf, src


@app.cell
def _(gdf, src):
    # ============================================================
    # Check Coordinate Reference Systems (CRS)
    # ============================================================

    # The CRS defines how spatial coordinates are represented.
    # Both raster and polygons MUST share the same CRS
    # for spatial operations (like sampling) to work correctly.

    print("Raster CRS:")
    print(src.crs)

    print("\nPolygon CRS:")
    print(gdf.crs)


    # If CRS do not match, we must reproject the polygons.
    # (We are NOT reprojecting yet — just checking.)
    return


@app.cell
def _():
    # # Reproject polygons if CRS do not match
    # if gdf.crs != src.crs:
    #     print("\nCRS mismatch detected. Reprojecting polygons to raster CRS...")
    #     gdf = gdf.to_crs(src.crs)
    #     print("Reprojection complete.")
    # else:
    #     print("\nCRS already match.")
    return


@app.cell
def _(src):
    # ============================================================
    # Inspect Raster Metadata
    # ============================================================

    # Raster width (number of columns)
    print("Raster width (columns):", src.width)

    # Raster height (number of rows)
    print("Raster height (rows):", src.height)

    # Number of spectral bands
    print("Number of bands:", src.count)

    # Raster resolution (pixel size in map units)
    print("Pixel resolution:", src.res)

    # Raster bounds (spatial extent of the image)
    print("Raster bounds:", src.bounds)

    # Data type of raster values
    print("Raster data type:", src.dtypes)
    return


@app.cell
def _(src):
    # ============================================================
    # Extract Band Descriptions (Marimo-safe variables)
    # ============================================================

    band_desc_list = [
        band_name.lower() if band_name else ""
        for band_name in src.descriptions
    ]

    print("Band descriptions:", band_desc_list)
    return (band_desc_list,)


@app.cell
def _(band_desc_list):
    # ============================================================
    # Detect RGB Band Indices (Unique variable names)
    # ============================================================

    detected_red_band = None
    detected_green_band = None
    detected_blue_band = None

    for band_position, band_text in enumerate(band_desc_list):

        if "b4" in band_text or "red" in band_text:
            detected_red_band = band_position + 1

        if "b3" in band_text or "green" in band_text:
            detected_green_band = band_position + 1

        if "b2" in band_text or "blue" in band_text:
            detected_blue_band = band_position + 1

    print("Detected bands:")
    print("Red band index:", detected_red_band)
    print("Green band index:", detected_green_band)
    print("Blue band index:", detected_blue_band)
    return


@app.cell
def _(np, src):
    # Check statistics band-by-band
    for band_number in range(1, src.count + 1):
        band_data_check = src.read(band_number)

        print(f"\nBand {band_number}")
        print("Min:", np.nanmin(band_data_check))
        print("Max:", np.nanmax(band_data_check))
    return


@app.cell
def _(np, plt, src):
    # ============================================================
    # RGB Visualization
    # Assuming band order: 1=B2, 2=B3, 3=B4, 4=B8
    # ============================================================

    rgb_red_band_index = 3
    rgb_green_band_index = 2
    rgb_blue_band_index = 1

    rgb_band_stack_final = src.read([
        rgb_red_band_index,
        rgb_green_band_index,
        rgb_blue_band_index
    ]).astype("float32")

    # Replace zeros with NaN (common nodata in composites)
    rgb_band_stack_final[rgb_band_stack_final == 0] = np.nan

    rgb_transposed_final = np.transpose(rgb_band_stack_final, (1, 2, 0))

    # Compute per-channel stretch (better than global stretch)
    rgb_stretched_final = np.zeros_like(rgb_transposed_final)

    for channel_index in range(3):
        channel_data = rgb_transposed_final[:, :, channel_index]

        lower = np.nanpercentile(channel_data, 2)
        upper = np.nanpercentile(channel_data, 98)

        rgb_stretched_final[:, :, channel_index] = np.clip(
            (channel_data - lower) / (upper - lower),
            0,
            1
        )

    plt.figure(figsize=(8, 8))
    plt.imshow(rgb_stretched_final)
    plt.title("Sentinel-2 RGB Composite (Bands 3-2-1)")
    plt.axis("off")
    plt.show()
    return (rgb_stretched_final,)


@app.cell
def _(gdf):
    # ============================================================
    # Inspect Training Polygon Attributes
    # ============================================================

    # Display first few rows
    print(gdf.head(20))

    # Show available columns
    print("\nAvailable columns:")
    print(gdf.columns)

    # Count number of polygons
    print("\nNumber of training polygons:", len(gdf))
    return


@app.cell
def _(gdf, plt, rgb_stretched_final, src):
    # ============================================================
    # RGB + Training Polygons Overlay Colored by Class
    # ============================================================

    import matplotlib.cm as cm

    # Raster bounds
    raster_bounds = src.bounds

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8))

    # Show RGB image with geographic extent
    ax.imshow(
        rgb_stretched_final,
        extent=[raster_bounds.left, raster_bounds.right,
                raster_bounds.bottom, raster_bounds.top],
        origin='upper'
    )

    # Updated colormap (Matplotlib 3.7+ safe)
    num_classes = gdf['class'].nunique()
    cmap = plt.get_cmap('Set1', num_classes)  # new recommended syntax

    # Plot polygons with color by class
    for idx in range(len(gdf)):
        poly_geom = gdf.iloc[idx].geometry
        class_id = gdf.iloc[idx]['class']

        # Map class ID to 0-based index for colormap
        color = cmap(class_id - 1)

        if poly_geom.geom_type == 'Polygon':
            x, y = poly_geom.exterior.xy
            ax.plot(x, y, color=color, linewidth=1.5)

        elif poly_geom.geom_type == 'MultiPolygon':
            for part in poly_geom.geoms:
                x, y = part.exterior.xy
                ax.plot(x, y, color=color, linewidth=1.5)

    ax.set_title("Training Polygons Overlay on Sentinel-2 RGB (Colored by Class)")
    ax.axis("off")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Extracting Training Samples

    We now convert the raster + training polygons into a tabular dataset for ML.

    For each polygon:
    - Mask the raster to extract pixels inside the polygon
    - Remove zero or nodata pixels
    - Flatten pixel values into feature vectors
    - Assign the polygon's class label

    Output:
    - X → Feature matrix (n_samples × n_bands)
    - y → Label vector (n_samples)
    """)
    return


@app.cell
def _(gdf, np, src):
    # ============================================================
    # Extract training samples from polygons (features and labels)
    # ============================================================

    from rasterio.mask import mask

    # Lists to collect features and labels
    features_collection = []
    labels_collection = []

    # Number of bands in the raster
    num_bands = src.count

    # Loop through each polygon (use a unique variable name)
    poly_counter = 0

    for poly_counter in range(len(gdf)):

        # Single polygon GeoDataFrame
        single_poly_df = gdf.iloc[[poly_counter]]

        # Numeric class label
        poly_class_value = single_poly_df["class"].values[0]

        # Mask raster inside polygon
        masked_raster_data, _ = mask(
            dataset=src,
            shapes=single_poly_df.geometry,
            crop=True
        )

        # Reshape to (pixels, bands)
        pixels_array = masked_raster_data.reshape(num_bands, -1).T  # (n_pixels, n_bands)

        # Remove pixels where all bands are zero
        valid_pixels_mask = ~(pixels_array == 0).all(axis=1)
        valid_pixels = pixels_array[valid_pixels_mask]

        # Skip polygon if no valid pixels
        if valid_pixels.shape[0] == 0:
            continue

        # Append to lists
        features_collection.append(valid_pixels)

        # Create labels array
        pixel_labels = np.full(valid_pixels.shape[0], poly_class_value)
        labels_collection.append(pixel_labels)

    print("Finished extracting training samples.")
    return features_collection, labels_collection


@app.cell
def _(features_collection, labels_collection, np):
    # ============================================================
    # Stack all features and labels into final feature and label arrays
    # ============================================================

    X_train_samples = np.vstack(features_collection)
    y_train_labels = np.concatenate(labels_collection)

    print("Feature matrix shape:", X_train_samples.shape)
    print("Label vector shape:", y_train_labels.shape)
    return X_train_samples, y_train_labels


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. Train-Test Split and RandomForest Classifier

    We now split our dataset into training and testing subsets,
    fit a RandomForestClassifier, and evaluate its accuracy.

    - `X_train_samples` → features (spectral bands)
    - `y_train_labels` → labels (land cover classes)
    """)
    return


@app.cell
def _(X_train_samples, y_train_labels):
    # ============================================================
    # Train-test split
    # ============================================================

    from sklearn.model_selection import train_test_split

    # Split data: 70% train, 30% test
    X_features_train, X_features_test, y_labels_train, y_labels_test = train_test_split(
        X_train_samples,
        y_train_labels,
        test_size=0.3,
        random_state=42,
        stratify=y_train_labels  # ensures class distribution is preserved
    )

    print("Training samples:", X_features_train.shape[0])
    print("Testing samples:", X_features_test.shape[0])
    return X_features_test, X_features_train, y_labels_test, y_labels_train


@app.cell
def _(X_features_test, X_features_train, y_labels_test, y_labels_train):
    # ============================================================
    # RandomForest Classifier Training
    # ============================================================

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    # Create RandomForest model (marimo-safe variable name)
    rf_model = RandomForestClassifier(
        n_estimators=100,      # number of trees
        random_state=42
    )

    # Fit the model
    rf_model.fit(X_features_train, y_labels_train)

    # Predict on test set
    y_pred_labels = rf_model.predict(X_features_test)

    # Evaluate accuracy
    accuracy = accuracy_score(y_labels_test, y_pred_labels)
    print("Test set accuracy:", accuracy)

    # Detailed classification report
    print("\nClassification Report:\n", classification_report(y_labels_test, y_pred_labels))
    return RandomForestClassifier, rf_model


@app.cell
def _(plt, rf_model):
    # Feature importance plot (marimo-safe)
    feature_importances = rf_model.feature_importances_

    plt.figure(figsize=(6, 4))
    plt.bar(range(len(feature_importances)), feature_importances, color='skyblue')
    plt.xticks(range(len(feature_importances)), [f'Band {i+1}' for i in range(len(feature_importances))])
    plt.ylabel('Importance')
    plt.title('RandomForest Feature Importance per Band')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Feature Importance Interpretation

    From the RandomForest feature importance graph, the bands are ranked as follows:

    Band 4 > Band 3 > Band 1 > Band 2

    Band 4 is significantly higher than the others.

    **1. Band 4 (NIR) — Most Important**
    - Near-infrared (NIR) is highly reflective for vegetation.
    - The model relies on it most to separate forest from built-up and water areas.
    - This is expected for Sentinel-2 imagery, as vegetation stands out strongly in NIR.

    **2. Band 3 (Red) — Second Most Important**
    - Sensitive to chlorophyll absorption in vegetation.
    - Helps distinguish vegetation from soil or built-up areas.

    **3. Bands 1 (Blue) and 2 (Green) — Less Important**
    - Blue helps with water detection.
    - Green contributes slightly to vegetation differentiation.
    - Both are less discriminative for land cover types in this study area.

    **Practical Takeaways**
    - The model correctly leverages NIR to identify forested areas.
    - Bands 3 and 4 are critical; bands 1 and 2 are secondary.
    - For dimensionality reduction, focusing on bands 3 and 4 may retain most of the classification power.
    - This explains why the RandomForest performs well: it uses the bands with the strongest spectral signals for the target classes.

    **Notebook narrative example**
    The feature importance plot shows Band 4 (NIR) is the most influential, followed by Red (Band 3), then Blue (Band 1) and Green (Band 2). NIR strongly separates vegetation (forest) from water and built-up areas, Red contributes to vegetation detection, and Bands 1 and 2 play smaller supporting roles.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. Full-Raster Classification and Visualization

    In this step, we apply the trained RandomForest model to the entire Sentinel-2 composite image to produce a classified land cover map.

    **Steps:**

    1. Reshape the full raster from (bands, rows, cols) to a 2D array of shape (pixels, bands) so it can be used as input for the model.
    2. Use the trained RandomForest model (`rf_model`) to predict the class for each pixel.
    3. Reshape the predicted labels back to the raster's original dimensions.
    4. Visualize the resulting land cover classification map, assigning a distinct color to each class.

    This allows us to see how the model generalizes from the training polygons to the entire image, producing a spatially continuous land cover map.

    ## 11. Fast Full-Raster Classification

    For large rasters, predicting all pixels at once can be slow.
    Here, we implement a faster approach by:

    1. Optionally downsampling the raster for quick visualization.
    2. Splitting the raster into smaller chunks for prediction.
    3. Using the trained RandomForest model (`rf_model`) to classify pixels efficiently.

    This allows us to generate a land cover map without overwhelming memory or CPU.
    """)
    return


@app.cell
def _(np, plt, rf_model, src):

    import matplotlib.colors as mcolors
    from rasterio.windows import Window

    # ------------------------------
    # Get raster dimensions
    # ------------------------------
    rows_count = src.height
    cols_count = src.width
    bands_count = src.count

    # ------------------------------
    # Downsampling factor for preview
    # ------------------------------
    downsample_factor = 4  # e.g., 1/4 resolution

    rows_ds = rows_count // downsample_factor
    cols_ds = cols_count // downsample_factor

    # ------------------------------
    # Read downsampled raster
    # ------------------------------
    raster_downsampled = src.read(
        out_shape=(bands_count, rows_ds, cols_ds)
    )

    # Initialize classified raster
    classified_raster_ds = np.zeros((rows_ds, cols_ds), dtype=np.uint8)

    # ------------------------------
    # Tile parameters
    # ------------------------------
    tile_size_ds = 200  # tile size in pixels

    # ------------------------------
    # Tiled prediction
    # ------------------------------
    for row_start in range(0, rows_ds, tile_size_ds):
        row_end = min(row_start + tile_size_ds, rows_ds)
        for col_start in range(0, cols_ds, tile_size_ds):
            col_end = min(col_start + tile_size_ds, cols_ds)

            # Extract tile
            tile_array = raster_downsampled[:, row_start:row_end, col_start:col_end]

            # Reshape for sklearn
            tile_pixels = tile_array.reshape(bands_count, -1).T

            # Mask pixels where all bands are zero
            mask_tile = ~(tile_pixels == 0).all(axis=1)
            pixels_for_tile = tile_pixels[mask_tile]

            # Predict
            predicted_tile = np.zeros(tile_pixels.shape[0], dtype=np.uint8)
            if pixels_for_tile.shape[0] > 0:
                predicted_tile[mask_tile] = rf_model.predict(pixels_for_tile)

            # Reshape back to 2D and insert into full downsampled raster
            predicted_tile_2d = predicted_tile.reshape(row_end - row_start, col_end - col_start)
            classified_raster_ds[row_start:row_end, col_start:col_end] = predicted_tile_2d

    print("Fast preview tiled classification complete!")

    # ------------------------------
    # Visualization
    # ------------------------------
    classified_plot_ds = classified_raster_ds - 1  # shift to 0-based for colormap

    colors_for_7_classes = [
        'blue',       # 1: water
        'red',        # 2: built up
        'green',      # 3: forest
        'lightgray',  # 4: clouds
        'sandybrown', # 5: bare soil
        'cyan',       # 6: pond
        'yellow'      # 7: crops
    ]

    cmap_7_classes = mcolors.ListedColormap(colors_for_7_classes)

    plt.figure(figsize=(12, 12))
    plt.imshow(classified_plot_ds, cmap=cmap_7_classes)
    plt.title("RandomForest Land Cover Classification (Fast Preview)")
    plt.axis('off')
    plt.show()
    return bands_count, mcolors, raster_downsampled


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise: Improve Land Cover Classification with NDVI

    **Goal:** Improve the RandomForest land cover classification by adding **NDVI** as an additional feature. NDVI helps distinguish vegetation (forest, crops) from non-vegetated classes (water, bare soil).

    ---

    ## Instructions

    1. **Compute NDVI from the raster bands**
       - Use **Band 4 (NIR)** and **Band 3 (Red)**.
       - Formula:
         ```
         NDVI = (NIR − Red) / (NIR + Red)
         ```

    2. **Add NDVI as a feature**
       - Flatten NDVI to match the shape of your raster pixels.
       - Combine NDVI with the original bands to create a new feature array.

    3. **Compute NDVI for training samples**
       - Use the same formula for pixels inside your training polygons.
       - Combine with the original training bands to create a training feature array.

    4. **Retrain your RandomForest**
       - Use the new feature array (original bands + NDVI) and the training labels.

    5. **Predict the raster**
       - Use **tiling and chunked prediction** as before.
       - Include NDVI as a feature for each tile.

    6. **Visualize the results**
       - Use the same 7-class colormap as before.
       - Compare with the previous classification without NDVI.

    7. **Reflect and Experiment**
       - Which classes improved after adding NDVI?
       - Which land cover types are most affected by NDVI?
       - Optional: try adding other indices like NDWI (water) or NDBI (built-up) to further improve classification.

    ---

    **Tips:**

    - Start with a **downsampled raster** to speed up the first run.
    - Check `np.unique()` of predicted classes to ensure the model predicts multiple classes.
    """)
    return


@app.cell
def _(
    RandomForestClassifier,
    X_train_samples,
    bands_count,
    mcolors,
    np,
    plt,
    raster_downsampled,
    y_train_labels,
):
    # ============================================================
    # NDVI-Enhanced RandomForest Classification — Marimo-Safe
    # ============================================================

    # ------------------------------
    # Step 1: Compute NDVI for raster
    # ------------------------------

    ndvi_nir_band = raster_downsampled[3, :, :]  # Band 4 (NIR)
    ndvi_red_band = raster_downsampled[2, :, :]  # Band 3 (Red)

    ndvi_array_raster = np.divide(
        (ndvi_nir_band - ndvi_red_band),
        (ndvi_nir_band + ndvi_red_band),
        out=np.zeros_like(ndvi_nir_band),
        where=(ndvi_nir_band + ndvi_red_band) != 0
    )

    print("NDVI calculated. Range:", ndvi_array_raster.min(), "to", ndvi_array_raster.max())

    # ------------------------------
    # Step 2: Add NDVI to raster features
    # ------------------------------
    raster_pixels_original = raster_downsampled.reshape(bands_count, -1).T
    ndvi_flat_column = ndvi_array_raster.reshape(-1, 1)
    raster_features_with_ndvi = np.hstack([raster_pixels_original, ndvi_flat_column])

    print("Raster features with NDVI shape:", raster_features_with_ndvi.shape)

    # ------------------------------
    # Step 3: Compute NDVI for training samples
    # ------------------------------
    ndvi_train_nir = X_train_samples[:, 3]
    ndvi_train_red = X_train_samples[:, 2]
    ndvi_train_values = (ndvi_train_nir - ndvi_train_red) / (ndvi_train_nir + ndvi_train_red + 1e-10)
    X_train_with_ndvi = np.hstack([X_train_samples, ndvi_train_values.reshape(-1, 1)])

    # ------------------------------
    # Step 4: Retrain RandomForest with NDVI
    # ------------------------------
    rf_model_ndvi_unique = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model_ndvi_unique.fit(X_train_with_ndvi, y_train_labels)
    print("RandomForest retrained with NDVI feature.")

    # ------------------------------
    # Step 5: Tiled Prediction with NDVI
    # ------------------------------
    tile_size_ndvi_unique = 200
    rows_ds_unique, cols_ds_unique = raster_downsampled.shape[1], raster_downsampled.shape[2]
    classified_raster_ndvi_unique = np.zeros((rows_ds_unique, cols_ds_unique), dtype=np.uint8)

    for tile_row_start in range(0, rows_ds_unique, tile_size_ndvi_unique):
        tile_row_end = min(tile_row_start + tile_size_ndvi_unique, rows_ds_unique)
        for tile_col_start in range(0, cols_ds_unique, tile_size_ndvi_unique):
            tile_col_end = min(tile_col_start + tile_size_ndvi_unique, cols_ds_unique)

            # Extract tile
            tile_array_unique = raster_downsampled[:, tile_row_start:tile_row_end, tile_col_start:tile_col_end]
            tile_pixels_unique = tile_array_unique.reshape(bands_count, -1).T

            # NDVI for tile
            tile_nir_unique = tile_pixels_unique[:, 3]
            tile_red_unique = tile_pixels_unique[:, 2]
            tile_ndvi_unique = (tile_nir_unique - tile_red_unique) / (tile_nir_unique + tile_red_unique + 1e-10)
            tile_features_unique = np.hstack([tile_pixels_unique, tile_ndvi_unique.reshape(-1, 1)])

            # Mask
            mask_tile_unique = ~(tile_pixels_unique == 0).all(axis=1)
            pixels_to_predict_unique = tile_features_unique[mask_tile_unique]

            # Predict
            predicted_tile_unique = np.zeros(tile_pixels_unique.shape[0], dtype=np.uint8)
            if pixels_to_predict_unique.shape[0] > 0:
                predicted_tile_unique[mask_tile_unique] = rf_model_ndvi_unique.predict(pixels_to_predict_unique)

            # Reshape and insert
            predicted_tile_2d_unique = predicted_tile_unique.reshape(tile_row_end - tile_row_start, tile_col_end - tile_col_start)
            classified_raster_ndvi_unique[tile_row_start:tile_row_end, tile_col_start:tile_col_end] = predicted_tile_2d_unique

    print("NDVI-enhanced classification complete!")

    # ------------------------------
    # Step 6: Visualization
    # ------------------------------
    classified_plot_ndvi_unique = classified_raster_ndvi_unique - 1

    colors_7_classes_unique = [
        'blue',       # 1: water
        'red',        # 2: built up
        'green',      # 3: forest
        'lightgray',  # 4: clouds
        'sandybrown', # 5: bare soil
        'cyan',       # 6: pond
        'yellow'      # 7: crops
    ]

    cmap_7_classes_unique = mcolors.ListedColormap(colors_7_classes_unique)

    plt.figure(figsize=(12, 12))
    plt.imshow(classified_plot_ndvi_unique, cmap=cmap_7_classes_unique)
    plt.title("RandomForest Classification with NDVI")
    plt.axis('off')
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exercise 2: Improve Classification with NDVI and SVM

    **Goal:** Explore how adding the **NDVI index** as a feature and switching the classifier to **SVM** affects land cover classification.

    ---

    ## Instructions

    1. **Compute NDVI from the raster bands**
       - Use **Band 4 (NIR)** and **Band 3 (Red)**.
       - Formula:
         ```
         NDVI = (NIR − Red) / (NIR + Red)
         ```

    2. **Add NDVI as a feature**
       - Flatten the NDVI array to match the shape of your raster pixels.
       - Combine with the original 4 bands to create a new feature array for classification.

    3. **Compute NDVI for training samples**
       - Use the same formula on pixels inside training polygons.
       - Combine with the original training bands to create the training feature array.

    4. **Train an SVM classifier**
       - Use `sklearn.svm.SVC`.
       - Use the new feature array (4 bands + NDVI) and the training labels.
       - Optional: experiment with `kernel='linear'` or `kernel='rbf'`.

    5. **Predict the raster**
       - Use the **tiling + chunked prediction approach** you implemented before.
       - Make sure NDVI is included as a feature for each tile.

    6. **Visualize the results**
       - Use the same 7-class colormap as before.
       - Compare with your previous RandomForest classification (NDVI only).

    7. **Reflect and Experiment**
       - Which classes improved after adding NDVI?
       - How does the SVM classifier perform compared to RandomForest?
       - Optional: try different kernels and note the differences in predicted maps.
    """)
    return


@app.cell
def _(
    X_train_samples,
    mcolors,
    np,
    plt,
    raster_downsampled,
    src,
    y_train_labels,
):
    ### NOTE: NOT OPTIMIZED YET. TAKES TOO LONG TO RUN >20 mins

    # ============================================================
    # Exercise 2 Solution: NDVI + SVM Classification
    # ============================================================

    from sklearn.svm import SVC

    # ------------------------------
    # Step 0: Optional Downsample Raster for Faster Execution
    # ------------------------------
    downsample_factor_svm = 8  # 1 = full res, 2 = half resolution, etc.
    bands_count_svm = raster_downsampled.shape[0]
    rows_svm = raster_downsampled.shape[1] // downsample_factor_svm
    cols_svm = raster_downsampled.shape[2] // downsample_factor_svm

    raster_svm_preview = src.read(
        out_shape=(bands_count_svm, rows_svm, cols_svm)
    )

    # ------------------------------
    # Step 1: Compute NDVI
    # ------------------------------
    nir_svm = raster_svm_preview[3, :, :]   # Band 4 (NIR)
    red_svm = raster_svm_preview[2, :, :]   # Band 3 (Red)

    ndvi_svm = np.divide(
        (nir_svm - red_svm),
        (nir_svm + red_svm),
        out=np.zeros_like(nir_svm),
        where=(nir_svm + red_svm) != 0
    )

    print("NDVI calculated.")

    # ------------------------------
    # Step 2: Prepare Raster Features
    # ------------------------------
    raster_pixels_svm = raster_svm_preview.reshape(bands_count_svm, -1).T
    ndvi_flat_svm = ndvi_svm.reshape(-1, 1)
    raster_features_svm = np.hstack([raster_pixels_svm, ndvi_flat_svm])
    print("Raster features shape:", raster_features_svm.shape)

    # ------------------------------
    # Step 3: Prepare Training Features
    # ------------------------------
    ndvi_train_svm = (X_train_samples[:, 3] - X_train_samples[:, 2]) / (X_train_samples[:, 3] + X_train_samples[:, 2] + 1e-10)
    X_train_svm = np.hstack([X_train_samples, ndvi_train_svm.reshape(-1, 1)])

    # ------------------------------
    # Step 4: Train SVM Classifier
    # ------------------------------
    svm_model_svm = SVC(kernel='rbf', probability=False, random_state=42)
    svm_model_svm.fit(X_train_svm, y_train_labels)
    print("SVM classifier trained with NDVI.")

    # ------------------------------
    # Step 5: Tiled Prediction for Raster
    # ------------------------------
    tile_size_svm = 100  # pixels per tile
    classified_raster_svm = np.zeros((rows_svm, cols_svm), dtype=np.uint8)

    for row_start_svm in range(0, rows_svm, tile_size_svm):
        row_end_svm = min(row_start_svm + tile_size_svm, rows_svm)
        for col_start_svm in range(0, cols_svm, tile_size_svm):
            col_end_svm = min(col_start_svm + tile_size_svm, cols_svm)

            # Extract tile
            tile_array_svm = raster_svm_preview[:, row_start_svm:row_end_svm, col_start_svm:col_end_svm]
            tile_pixels_svm = tile_array_svm.reshape(bands_count_svm, -1).T

            # NDVI for tile
            tile_ndvi_svm = (tile_pixels_svm[:, 3] - tile_pixels_svm[:, 2]) / (tile_pixels_svm[:, 3] + tile_pixels_svm[:, 2] + 1e-10)
            tile_features_svm = np.hstack([tile_pixels_svm, tile_ndvi_svm.reshape(-1, 1)])

            # Mask zero pixels
            mask_tile_svm = ~(tile_pixels_svm == 0).all(axis=1)
            pixels_to_predict_tile_svm = tile_features_svm[mask_tile_svm]

            # Predict
            predicted_tile_svm = np.zeros(tile_pixels_svm.shape[0], dtype=np.uint8)
            if pixels_to_predict_tile_svm.shape[0] > 0:
                predicted_tile_svm[mask_tile_svm] = svm_model_svm.predict(pixels_to_predict_tile_svm)

            # Reshape and insert into full raster
            predicted_tile_2d_svm = predicted_tile_svm.reshape(row_end_svm - row_start_svm, col_end_svm - col_start_svm)
            classified_raster_svm[row_start_svm:row_end_svm, col_start_svm:col_end_svm] = predicted_tile_2d_svm

    print("SVM classification with NDVI complete.")

    # ------------------------------
    # Step 6: Visualization
    # ------------------------------
    classified_plot_svm = classified_raster_svm - 1  # zero-based for colormap

    colors_7_classes_svm = [
        'blue',       # 1: water
        'red',        # 2: built up
        'green',      # 3: forest
        'lightgray',  # 4: clouds
        'sandybrown', # 5: bare soil
        'cyan',       # 6: pond
        'yellow'      # 7: crops
    ]

    cmap_7_classes_svm = mcolors.ListedColormap(colors_7_classes_svm)

    plt.figure(figsize=(12, 12))
    plt.imshow(classified_plot_svm, cmap=cmap_7_classes_svm)
    plt.title("SVM Classification with NDVI (Tiled + Downsampled)")
    plt.axis('off')
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
