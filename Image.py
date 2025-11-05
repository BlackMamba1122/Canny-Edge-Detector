from PIL import Image
import os
import numpy as np

class ImageOperations:
    def __init__(self, image_path: str):
        """Initialize with the image path."""
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")
        self.image_path = image_path

    def load_image(self) -> Image.Image:
        """
        Load and return the image object.
        
        Returns:
            PIL.Image.Image: The loaded image.
        """
        img = Image.open(self.image_path).convert('L')
        np_img = np.array(img)
        return np_img

    def save_image(self, image: Image.Image, output_path: str, format: str = 'PNG'):
        """
        Save the provided image in a desired format.

        Args:
            image (PIL.Image.Image): The image object to save.
            output_path (str): Path where the image should be saved.
            format (str, optional): Format like 'JPEG', 'PNG', 'BMP'.
                                    If None, inferred from output_path.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        arr = np.array(image, dtype=float)
        arr = arr - arr.min()
        if arr.max() > 0:
            arr = arr * (255.0 / arr.max())
        # arr = np.clip(arr, 0, 255).astype(np.uint8)

        img_out = Image.fromarray(image).convert('L')
        img_out.save(output_path, format=format)
        print(f"Image saved as {output_path} in {format} format.")