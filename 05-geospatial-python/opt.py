import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Optimizing Python for AI/ML/RS**

    ##**Objectives**

    - Understand strategies to optimize Python code for AI/ML/RS tasks.
    - Learn data preparation techniques for faster modeling.
    - Explore multi-threading and multiprocessing in Python.
    - Learn how to leverage GPU processing for deep learning.
    - Hands-on exercises to apply optimization strategies.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1. Why Optimization Matters**

    Optimizing data is one of the most important steps in AI/ML/RS workflows. Well-prepared data reduces computation, prevents errors, and improves model performance. Key strategies include:
    - Cleaning and preprocessing,
    - Selecting efficient data structures,
    - Reducing feature dimensions,
    - Selecting relevant indices (for pixel-wise applications), and
    - Batching or caching data for faster access.

    Even the fastest algorithm is useless if the data is poorly prepared.

    For example, in remote sensing, a dataset may have millions of pixels with dozens of spectral bands. Processing all features without selection is slow and may produce overfitted models. Optimizing data reduces unnecessary computations and ensures the model focuses on relevant, high-value information. Here are other reasons whhy optimization matters:

    - AI/ML and RS datasets are huge (10GB+)
    - Slow I/O and CPU-bound computations
    - Python’s Global Interpreter Lock (GIL) limits multi-threading for CPU tasks
    - Memory inefficiency and model bottlenecks
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1.1. Data Cleaning & Preprocessing**

    Properly cleaning and preprocessing data ensures models run efficiently and accurately. Tasks include:
    - Handling missing values to prevent errors during computations.
    - Removing duplicates and outliers that can skew results.
    - Converting data types to reduce memory usage.

    Filling missing values ensures smooth execution during analysis. Converting string columns to categorical types reduces memory usage, which matters when processing large datasets. Even small savings per row add up to significant improvements when working with millions of pixels or samples.

    For example, numerical values can be converted to float32 instead of float64, and repetitive string columns can be converted to categorical types.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        'A': [1, 2, None, 4],
        'B': ['x', 'y', 'z', 'x']
    })
    df['A'] = df['A'].fillna(df['A'].mean())
    df['B'] = df['B'].astype('category')

    print(df.dtypes)
    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1.2. Feature Selection & Dimensionality Reduction**

    - Identify significant features to reduce computation and avoid overfitting.
    - Use PCA (Principal Component Analysis) or feature importance-based selection.

    Reducing dimensionality improves model efficiency, especially for datasets with many correlated variables or indices.
    """)
    return


@app.cell
def _(np):
    from sklearn.decomposition import PCA

    data_2 = np.random.rand(100, 10)
    pca = PCA(n_components=5)
    reduced_data = pca.fit_transform(data_2)

    print(reduced_data.shape)  
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1.3. Pixel-wise Applications**

    For pixel-wise machine learning, optimization focuses on selecting only the most relevant indices or features for modeling. Each pixel can have multiple features, and using only significant indices reduces computation and allows models to learn more efficiently. Examples include NDVI or SAVI in remote sensing applications, where irrelevant bands are discarded before modeling.

    - In pixel-wise ML, each pixel is a sample with multiple indices (features).
    - Optimization focuses on selecting only significant indices that matter for modeling.
    - Reduces unnecessary computation and improves convergence speed.

    In remote sensing, you may have 100+ spectral indices per pixel. Not all indices contribute equally. Selecting the most relevant indices reduces computation and makes models more interpretable. This principle is especially important for large-area analyses.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **1.4. Deep Learning Data Optimization**

    - Deep learning requires careful data preparation and hyperparameter tuning.
    - Data Augmentation: Introduce variations in color, brightness, rotation to improve generalization.
    - Hyperparameter Tuning: Patch size, batch size, learning rate, optimizer, and layer freezing.

    Unlike classical ML, deep learning relies heavily on training strategy. Augmentation ensures the model sees diverse examples, preventing overfitting. Hyperparameter tuning controls the learning dynamics, affecting both accuracy and speed. Combining these techniques is crucial for semantic segmentation, object detection, and image classification.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **2. Doing Multi-threading in Python**

    - Python is single-threaded (Global Interpreter lock - GIL) → executes one instruction at a time.
    - Multi-threading improves I/O-bound tasks.
    - Multiprocessing is better for CPU-bound iterative tasks.

    Iterative CPU tasks like calculating features for millions of pixels can be slow. Multi-threading allows tasks like file reading or API calls to run concurrently. For heavy computations, multiprocessing is preferable because it bypasses GIL and truly parallelizes computation across CPU cores.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **2.1. Using _threading_**
    """)
    return


@app.cell
def _():
    import threading
    import time

    def crawl(link, delay=3):
        print(f"crawl started for {link}")
        time.sleep(delay)  # Blocking I/O (simulating a network request)
        print(f"crawl ended for {link}")

    links = [
        "https://python.org",
        "https://docs.python.org",
        "https://peps.python.org",
    ]

    # Start threads for each link
    threads = []
    for link in links:
        # Using `args` to pass positional arguments and `kwargs` for keyword arguments
        t = threading.Thread(target=crawl, args=(link,), kwargs={"delay": 2})
        threads.append(t)

    # Start each thread
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Each thread executes the same function independently.

    Useful for I/O-heavy tasks, like loading multiple files simultaneously.

    Threads share memory, so data can be accessed by multiple threads without duplication.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **2.2. Using _concurrent.futures_**
    """)
    return


@app.cell
def _():
    import concurrent.futures
    import urllib.request

    URLS = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'http://nonexistent-subdomain.python.org/']

    # Retrieve a single page and report the URL and contents
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data))) 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **_concurrent.futures _**provides a higher-level interface for creating thread or process pools.

    It simplifies parallel execution and is ideal for batch processing tasks, such as calculating features for thousands of pixels or data points.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **3. GPU Processing with Python**

    GPUs are designed for high-throughput parallel computation and are essential for deep learning, large matrix operations, and other heavy computational tasks. Unlike CPU multi-threading, GPUs can perform thousands of small operations simultaneously. Libraries that enable GPU acceleration for Python workflows includes:

    - PyTorch,
    - TensorFlow, and
    - CuPy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **3.1. Using _PyTorch_ with GPU**
    """)
    return


@app.cell
def _():
    # Ensure that PyTorch was installed correctly 

    import torch
    x = torch.rand(5, 3)
    print(x)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Moving tensors to the GPU allows all subsequent computations to be executed on the GPU instead of the CPU.

    This improves computation speed significantly for large datasets and deep learning models.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## **3.2. GPU Optimization Tips**

    - Minimize data transfer between CPU and GPU to reduce latency.
    - Use mixed precision (float16) to reduce memory usage and increase training speed.
    - Profile GPU usage to identify bottlenecks and optimize performance.
    - Combine data augmentation and hyperparameter tuning to fully utilize GPU resources and enhance model efficiency.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Key Takeways**

    - Optimization in Python AI/ML/RS workflows involves data preparation, CPU parallelization, and GPU utilization.
    - Data cleaning, feature selection, and batching reduce computation and improve model efficiency.
    - Multi-threading and multiprocessing accelerate iterative CPU-bound tasks.
    - GPUs are essential for matrix-heavy and deep learning tasks.
    - Pixel-wise machine learning and deep learning models benefit from feature selection, data augmentation, and hyperparameter tuning to achieve faster and more accurate results.
    """)
    return


if __name__ == "__main__":
    app.run()
