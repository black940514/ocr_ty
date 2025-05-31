import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from pathlib import Path
from utils_ty import track_time

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
load_dotenv()

try:
    endpoint = os.environ["VISION_ENDPOINT"]
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

@track_time
def azure_vision(image_path:Path): 


    with open(image_path, "rb") as f:
        image_data = f.read()

    # You need to create an Azure Computer Vision AI services 
    # https://portal.azure.com/
    region = "eastus"

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        region=region,
    )

    result = client.analyze(
        image_data,
        visual_features=[VisualFeatures.READ],
    )

    if result.read is not None:
        cnt = 0
        for line in result.read.blocks[0].lines:
            print(line.text)
            # for word in line.words:
            #     print(word.text, word.confidence)
            # cnt += 1
            # if cnt > 4:
            #     break

    # Print text (OCR) analysis results to the console
    print(" Read:")
    # if result.read is not None:
    #     for line in result.read.blocks[0].lines:
    #         print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
    #         for word in line.words:
    #             print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")


if __name__ == "__main__":
    image_path = Path("src/emart_flier4.jpg")
    # pass
    azure_vision(image_path)
