# CS2 Object Detection
This is a very simple object detection that detects CT's and T's in the game of Counter Strike 2. I know this doesn't look like a lot... and that is because it isnt right now. 
This project was done in the span of a couple hours -- with most of that being annotating. This is something that I want to come back to.

# Steps
1. Collect data
2. Annotate
3. Train via transfer learning and Yolo
4. Test

## Data collection
To start data collection, I wrote a script (screenshot.py) which would take a screenshot roughly every N seconds.

## Annotate
To annotate I used Roboflow's labeling tool and drew a box around T's and CT's for roughly 100 images. I know what you are thinking! Only 100? Yeah... I was lazy.

![Example annotation](https://github.com/SamSkinner01/cs2-od/raw/main/image.png)

## Train
Performed transfer learning on a YoloV9 model with these 100 images for 25 epochs. 

## Test
Here is an example of the output gif. You can tell that it struggles, but for only 100 images and very little of my time it is very impressive. Lots of room for improvement.


![Output gif](https://github.com/SamSkinner01/cs2-od/raw/main/image.png)
