import requests
import os
import cv2
import pytesseract

def DownloadImageExtractText(index, url):
    
    save_path = "images/"+str(index)+".jpg"

    if os.path.exists(save_path):
        # Your code to process the existing file goes here
        print("Already Exists")
        return save_path
    else:        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses

            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"Image downloaded successfully and saved at {save_path}")
            return save_path
        except requests.exceptions.RequestException as e:
            print(f"Error downloading the image: {e}")