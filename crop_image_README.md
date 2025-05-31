# flyer.jpg
## 1. 30-second overview
- Step 0  ➜  deskew & trim    (make the page upright, erase outer white border)
- Step 1  ➜  vertical slice   (cut tall “columns” wherever you see a long white stripe)
- Step 2  ➜  horizontal slice (inside every column, cut “rows” wherever you see a blank bar)

- Step 3  ➜  slice-or-keep    (very skinny rows get chopped in half vertically)
- Step 4  ➜  item crop        (inside every row/half, crop around each product block)

## 2. Class skeleton you will create
```python
class FlierSegmentor:
    def __init__(self, 
        flier_path: Path, 
        temp_root: Path, 
        final_output_dir: Path,
        *, 
        aspect_threshold_step3=0.55, aspect_threshold_step4=0.64,
        trim_margin=5):
        # remember where everything lives
        # calculate helper paths like tmp/step1/, tmp/step2/, tmp/step3/
        # store user-tunable thresholds
```
### Attribute (Why it matters)
- flier_path: 
  - original flyer image file
- base_name: 
  - same name without extension (handy for naming slices)
- temp_step1/2/3: 
  - scratch folders that keep intermediate slices
- final_output_dir:
  - where the finished item images are saved
- Thresholds: 
  - control when the algorithm decides “this is too skinny ⇒ split again”

## Utility helpers (build these first)
- _clear_directory(path)	
  - start each run with a clean directory	
  - shutil.rmtree if exists → mkdir
- _trim_white_border_adaptive(img, margin)	
  - crop away useless outer whitespace	
  - convert to gray → Otsu threshold → boundingRect of non-white pixels → expand by margin
- _is_white(pixel, thr=250)	
  - treat near-white pixels as background	
  - return all(channel ≥ thr)
- correct_image_rotation(img)	
  - deskew pages that were scanned a bit tilted	  
  - Canny edges → Hough lines → pick longest diagonal → rotate back     

`You can implement deskew later; the rest of the pipeline works fine with a perfectly upright flyer.`

