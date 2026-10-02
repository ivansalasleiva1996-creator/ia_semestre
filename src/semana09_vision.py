import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Configura el backend no interactivo antes de importar pyplot
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color, feature, filters, measure

def run_vision_pipeline():
    # 1. Paths configuration
    input_path = os.path.join("data", "imagen_proyecto.png")
    output_path = os.path.join("artifacts", "semana09_vision.png")
    os.makedirs("artifacts", exist_ok=True)

    # 2. Load Image
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Image not found at {input_path}. Please place 'imagen_proyecto.png' in data/")
    
    img_color = io.imread(input_path)
    
    # Convert to grayscale if image is RGB/RGBA
    if img_color.ndim == 3:
        if img_color.shape[2] == 4:
            img_color = img_color[:, :, :3]
        img_gray = color.rgb2gray(img_color)
    else:
        img_gray = img_color.copy()

    # 3. Contour / Edge Detection using Canny
    sigma_val = 1.0
    edges = feature.canny(img_gray, sigma=sigma_val)

    # 4. Thresholding using Otsu
    otsu_thresh = filters.threshold_otsu(img_gray)
    binary_mask = img_gray > otsu_thresh

    # 5. Connected Components / Region Analysis
    labeled_regions, num_features = measure.label(binary_mask, return_num=True)

    print(f"--- Processing Results ---")
    print(f"Otsu Threshold Value: {otsu_thresh:.4f}")
    print(f"Connected Regions Found: {num_features}")

    # 6. Generate and Save Visual Artifacts
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    ax = axes.ravel()

    ax[0].imshow(img_color if img_color.ndim == 3 else img_gray, cmap='gray' if img_color.ndim == 2 else None)
    ax[0].set_title("1. Original Image")
    ax[0].axis('off')

    ax[1].imshow(edges, cmap='gray')
    ax[1].set_title(f"2. Canny Edges (sigma={sigma_val})")
    ax[1].axis('off')

    ax[2].imshow(binary_mask, cmap='binary')
    ax[2].set_title(f"3. Otsu Thresholding (T={otsu_thresh:.3f})")
    ax[2].axis('off')

    ax[3].imshow(labeled_regions, cmap='nipy_spectral')
    ax[3].set_title(f"4. Connected Regions (N={num_features})")
    ax[3].axis('off')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Artifact successfully saved to: {output_path}")

if __name__ == "__main__":
    run_vision_pipeline()