# Hair Extraction API
## Description:
This Python API allows users to upload images, from which it extracts hair using advanced computer vision techniques. The extracted hair region is then displayed to the user. It's a powerful tool for image-processing applications, especially in the beauty and fashion industries.

## Features:

**User-Friendly:** Easy-to-use API with straightforward image upload functionality.

**Hair Extraction:** Utilizes [FaceParsing-BiSeNet model](https://github.com/GithubRealFan/HairColorChange/commits?author=GithubRealFan) to accurately extract hair from the provided images.

**Real-time Display:** Instantly displays the extracted hair region to the user, providing quick feedback.

**Versatile Integration:** Can be integrated into various applications, including beauty apps, virtual try-on platforms, and more.

**Scalable:** Built using scalable and efficient Python libraries, ensuring smooth operation even with large volumes of requests.

## Usage:

**Upload Image:** Send a POST request with the user's image data.

**Hair Extraction:** The API processes the image and extracts the hair region.

**Display Result:** Receive the extracted hair region and display it to the user.

## API Endpoints:

**POST /HairExtraction/upload:** Uploads the user's image for hair extraction.

**GET /HairExtraction/download:** Retrieves the extracted hair region for display purposes.

## Requirements:
```
pip install torch
pip install numpy
pip install Pillow
pip install opencv-python
pip install torchvision
pip install fastapi uvicorn[standard]
```
