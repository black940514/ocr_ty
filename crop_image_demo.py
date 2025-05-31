import numpy as np
import cv2
from pathlib import Path


def split_by_white_lines(img:np.ndarray, min_line_height:int = 10):
    if img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # RGB -> GRAY
    height, width = img.shape
    print(f"height: {height}, width: {width}")
    white_rows = np.where(np.all(img == 255, axis=1))[0]

    print(white_rows[:30])
    print("\n\n")
    lines = np.split(white_rows, np.where(np.diff(white_rows) > 1)[0] + 1) 
    print(lines)
    print("\n\n")
    # print(np.diff(white_rows)>1)
    start = 0
    segments = []
    for line in lines :
        end = line[0]
        if end - start >= min_line_height:
            segment = img[start:end, :]
            segments.append(segment)
        start = line[-1] + 1

    print(segments)


    for idx, segment in enumerate(segments):
        file_name = Path('output') / f"seg_{idx+1}.png"
        cv2.imwrite(str(file_name), segment)


if __name__ == "__main__":

    img_path = Path("src/sample.png")
    img:np.ndarray = cv2.imread(img_path)
    split_by_white_lines(img)
    # pass  
