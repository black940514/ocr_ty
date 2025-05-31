from doctr.io import DocumentFile # !pip install "python-doctr[torch]"
from doctr.models import ocr_predictor
from pathlib import Path
from utils_ty import track_time

@track_time
def doctr_vision_ai(image_path:Path):
    
    doc = DocumentFile.from_images(image_path)

    model = ocr_predictor(
        det_arch="db_resnet50",  ## 텍스트가 있는 영역을 detection
        reco_arch="crnn_vgg16_bn", 
        pretrained=True)

    result = model(doc)

    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                texts = [word.value for word in line.words]
                print(texts)

if __name__ == "__main__":
    image_path = Path("src/emart_flier4.jpg")
    # pass
    doctr_vision_ai(image_path)