
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Detect objects in image
results = model.predict("image.jpg", save=True)

# Print detected objects
for result in results:
    for box in result.boxes:
        name = model.names[int(box.cls[0])]
        print("Detected object:", name)

print("Object detection completed!")
