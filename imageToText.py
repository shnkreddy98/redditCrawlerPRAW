import pandas as pd
import numpy as np
import requests
import os
import cv2
import pytesseract
import time

def extractText(path):

    try:
        img = cv2.imread(path)

        if img is not None:
            text = str(pytesseract.image_to_string(img))

        else:
            print(f"Skipped processing image at index {ix} due to wrong link.")

        return text

    except Exception as e:
        print(f"Error processing image at index {ix}: {e}")


def DownloadImage(index, url):

    # Create the 'images' directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")
    
    save_path = "images/"+str(index)+".jpg"

    if os.path.exists(save_path):
        # Your code to process the existing file goes here
        print("Already Exists")
        pass

    else:        
        try:
            response = requests.get(url, timeout = 10)
            response.raise_for_status()  # Raise an exception for bad responses

            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"Image downloaded successfully and saved at {save_path}")
            return extractText(save_path)
            

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the image: {e}")

if __name__ == "__main__":

    # Read csv file
    df = pd.read_csv("data/merged_data.csv")
    print(df.head())

    count = 0

    for ix, row in df.iterrows():
        if count == 10:
            time.sleep(5)
            count = 0
        df.loc[ix, 'image_text'] = DownloadImage(ix, row['url'])
        count += 1
        
    # Output file name
    output_csv_file = 'data/merged_data_with_image_data.csv'

    df.to_csv(output_csv_file)

