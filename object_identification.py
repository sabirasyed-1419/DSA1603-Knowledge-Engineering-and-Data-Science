
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Load AI model
model = YOLO("yolov8n.pt")

# Knowledge base
knowledge = {
    "laptop": {
        "category": "Electronic Device",
        "properties": "Portable, screen and keyboard",
        "function": "Used for learning and computing"
    },
    "book": {
        "category": "Educational Object",
        "properties": "Printed pages and cover",
        "function": "Used for reading"
    },
    "chair": {
        "category": "Furniture",
        "properties": "Seat with backrest",
        "function": "Used for sitting"
    },
    "bottle": {
        "category": "Container",
        "properties": "Holds liquids",
        "function": "Used for storing water"
    },
    "cell phone": {
        "category": "Electronic Device",
        "properties": "Portable touchscreen",
        "function": "Used for communication"
    },
    "dining table": {
        "category": "Furniture",
        "properties": "Flat surface with legs",
        "function": "Used for placing objects"
    }
}

# Read image
image = cv2.imread("laptop.jpg")

if image is None:
    print("Image not found! Keep laptop.jpg in the same folder.")
else:
    results = model(image)
    found = False

    for result in results:
        for box in result.boxes:
            name = model.names[int(box.cls[0])].lower()
            confidence = float(box.conf[0])

            if name in knowledge and confidence >= 0.40:
                found = True
                info = knowledge[name]

                print("\nObject:", name)
                print("Category:", info["category"])
                print("Properties:", info["properties"])
                print("Function:", info["function"])
                print("Confidence:", round(confidence * 100, 2), "%")

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(image, (x1, y1), (x2, y2),
                              (0, 255, 0), 2)
                cv2.putText(image, name, (x1, max(y1 - 10, 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                            (0, 255, 0), 2)

    if not found:
        print("Object could not be identified confidently.")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    plt.axis("off")
    plt.show()
