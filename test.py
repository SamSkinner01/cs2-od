from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

cap = cv2.VideoCapture('video.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=.25)

    boxes = results[0].boxes.xyxy.tolist()
    classes = results[0].boxes.cls.tolist()
    names = results[0].names
    confidences = results[0].boxes.conf.tolist()

    for box, cls, conf in zip(boxes, classes, confidences):
        x1, y1, x2, y2 = box
        
        if names[cls] == 't':
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'{names[cls]}: {conf:.2f}', (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        elif names[cls] == "ct": 
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            cv2.putText(frame, f'{names[cls]}: {conf:.2f}', (int(x1), int(y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    out.write(frame)


cap.release()
out.release()







