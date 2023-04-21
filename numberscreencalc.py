import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
import pyautogui
import keyboard


def capture_screenshot(region):
    screenshot = ImageGrab.grab(bbox=region)
    return screenshot

def extract_numbers(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    numbers = pytesseract.image_to_string(thresh, config='--psm 6 outputbase digits')
    return [int(num) for num in numbers.split() if num.isdigit()]

def calculate_sum(numbers):
    return sum(numbers)

def calculate_difference(region1, region2):
    # Capture screenshots of the specified regions
    img1 = capture_screenshot(region1)
    img2 = capture_screenshot(region2)

    # Convert PIL images to OpenCV images
    img1 = np.array(img1)
    img2 = np.array(img2)

    # Extract numbers from the images
    numbers1 = extract_numbers(img1)
    numbers2 = extract_numbers(img2)

    # Calculate the sums
    sum1 = calculate_sum(numbers1)
    sum2 = calculate_sum(numbers2)

    # Calculate the difference
    difference = sum1 - sum2
    return difference

if __name__ == "__main__":
    # Define the regions to capture
    region1 = (100, 100, 300, 300) # (left, top, right, bottom)
    region2 = (400, 100, 600, 300) # (left, top, right, bottom)

    while True:
        if keyboard.is_pressed('1'):
            difference = calculate_difference(region1, region2)
            print("Difference:", difference)
            break
