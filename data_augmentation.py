import imgaug.augmenters as iaa
import imageio
import numpy as np
import cv2
import random

# Function to apply data augmentation to a TIFF image
def augment_tiff_image(image_path, output_path):
    # Read the TIFF image using cv2
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        raise ValueError("Error: Unable to load the image from the provided path.")

    # Resize the image to a smaller resolution for faster processing
    target_size = (int(image.shape[1] * 0.5), int(image.shape[0] * 0.5))
    image = cv2.resize(image, target_size)

    # Define the augmentation pipeline
    augmentation = iaa.Sequential([
        iaa.Fliplr(0.5),  # Flip the image horizontally with a probability of 0.5
        iaa.Affine(
            scale=(0.8, 1.2),  # Randomly scale the image by a factor between 0.8 and 1.2
            translate_percent=(-0.1, 0.1),  # Randomly translate the image by -10% to 10% of its size
            rotate=(-45, 45)  # Randomly rotate the image by -45 to 45 degrees
        ),
        iaa.GaussianBlur(sigma=(0, 1.0)),  # Apply random Gaussian blur with sigma between 0 and 1.0
        iaa.AdditiveGaussianNoise(scale=(0, 0.1 * 255))  # Add random Gaussian noise
    ])

    # Apply augmentation
    augmented_image = augmentation.augment_image(image)

    # Save the augmented image to TIFF format
    cv2.imwrite(output_path, augmented_image)

# Example usage:
# Load an example TIFF image
image_path = "C:/Users/Weyrd/Documents/Github/Cells_characteristics_Mems_ai/data_/Snail/Snail_sample_13/before comp 14.82μm.tif"
output_path = r"augmented_image.tif"

try:
    # Apply augmentation and save the augmented image
    augment_tiff_image(image_path, output_path)

    # Display the original and augmented images side by side (optional)
    original_image = cv2.imread(image_path)
    augmented_image = cv2.imread(output_path)

    combined_image = np.hstack((original_image, augmented_image))
    cv2.imshow("Original vs. Augmented", combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ValueError as e:
    print(str(e))


# nex class
class Data:
    def __init__(self):
        self.UseDataset = 0.04
        self.validation = 4000
        self.rotate = (1475, 1824)
        self.flip = (1405, 1574)
        self.Approve = 3299
        self.randomSeed = random.randint(0, 1)
        self.npR = np.random.randint
        self.r = self.rotate
        self.f = self.flip


    def _SuperIn__(self, Diff_, randomSeed):
        return self.npR(Diff_, randomSeed)
    
   
    def current_val(self):
        return self._reprx_(self.Approve)

    def _reprc_(self, Booleaan : int = 0):
        if Booleaan == 0:
            return self._SuperIn__(self.rotate[0], self.rotate[1])
        else:
            return np.random.randint(self.flip[0], self.flip[1])
    
    def _reprx_(self, Approve):
        return self.validation
    
    def check(self):
        X_, Y_ = 0, 0
        for val in self.r: X_ +=  val
        for val in self.f:  Y_ += val
        return int((X_+Y_ + (self.Approve * self.UseDataset)) % self.current_val())
    
    def _get_random_data(self, val):
        return self.randomSeed
    
    def maxVal(self, mt, val):
        return range(int(mt * val), mt)
