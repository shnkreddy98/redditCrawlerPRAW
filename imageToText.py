import requests
import os
import cv2
import pytesseract

def extractImage(path):

    try:
        img = cv2.imread(path)

        if img not in None:
            text = str(pytesseract.image_to_string(img))

        else:
            print(f"Skipped processing image at index {ix} due to wrong link.")

        return text

    except Exception as e:
        print(f"Error processing image at index {ix}: {e}")


def DownloadImageExtractText(index, url):
    
    save_path = "images/"+str(index)+".jpg"

    if os.path.exists(save_path):
        # Your code to process the existing file goes here
        print("Already Exists")
        return extractImage(save_path)

    else:        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses

            with open(save_path, 'wb') as file:
                file.write(response.content)

            print(f"Image downloaded successfully and saved at {save_path}")
            return extractImage(save_path)
            

        except requests.exceptions.RequestException as e:
            print(f"Error downloading the image: {e}")

if __name__ == "__main__":

    # Read csv file
    df = pd.read_csv("data/merged_data.csv")

    for ix, row in df.iterrows():
        df.loc[ix, 'image_text'] = str(pytesseract.image_to_string(img))
        
    # Output file name
    output_csv_file = 'data/merged_data_with_image_data.csv'

    df.to_csv(output_csv_file)

