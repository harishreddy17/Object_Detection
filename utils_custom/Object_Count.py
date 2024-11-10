import cv2
from collections import defaultdict

object_classes = ['person', 'chair', 'bottle', 'laptop', 'car']
frame_object_counts = defaultdict(int)

def update_object_counts(results):
    
    global frame_object_counts
    frame_object_counts.clear()  
    for _, row in results.iterrows():
        if row['name'] in object_classes:
            frame_object_counts[row['name']] += 1

def display_counts(frame):
    global frame_object_counts
    y_offset = 50  

    for obj_class, count in frame_object_counts.items():
        cv2.putText(frame, f"{obj_class}: {count}", (10, y_offset), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        y_offset += 30 