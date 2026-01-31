import cv2
import math
from ultralytics import YOLO
from utils.functions import draw_popup
from utils.mouse_events import mouse_event
from yolo_detector.database.operations import InfoData
from yolo_detector.database.connection import DataGet
from add_object_info import COCO_CLASSES_PT

# Init database
get_data = DataGet()
info_data = InfoData()
detectable_objects = info_data.get_detectable_objects()


# UI ui_state management
ui_state = {
    'circle_clicked': False,
    'pause_stream': False,
    'popup_opening': False,
    'cursor_over_link01': False,
    'cursor_over_link02': False,
    'cursor_over_link03': False
}
# Select webcam (0 = built-in, 2 = OBS virtual camera)
VIDEO_SOURCE = 0

cap = cv2.VideoCapture(VIDEO_SOURCE)
frame_width = 640
frame_height = 480
cap.set(3, frame_width)
cap.set(4, frame_height)
# For mobile streaming (e.g., IP Webcam):
# ip = "https://192.168.1.66:8080/video"
# cap.open(ip)

# Popup settings
popup_height = 0
popup_max_height = frame_height - 100
popup_min_height = 0
popup_animation_speed = 50

# Model
model = YOLO("YOLOWeights/yolov8n.pt")

# COCO dataset class names (in Portuguese)
class_names = COCO_CLASSES_PT

# UI colors
COLOR_TEXT = (255, 255, 255)
COLOR_TEXT_LINE = (255, 255, 255)
COLOR_CIRCLE = (34, 34, 174)
COLOR_LINK = (255, 255, 255)

# Frame, link and popup_area storage
last_frame = None
link_dict = None
popup_area = None

# Flip mode
FLIP_MODE = True if VIDEO_SOURCE == 0 else False


while True:
    if not ui_state['pause_stream']:
        sucess, frame = cap.read()
        if not sucess:
            print("Não foi possivel abrir video")
            break
        last_frame = frame.copy()
    else:
        frame = last_frame.copy()

    if FLIP_MODE:
        # activate mirror mode only for Webcam
        frame = cv2.flip(frame, 1)

    results = model(frame)

    # Definições do ponto detector
    circle_x = 35
    circle_y = 25
    circle_radius = 10
    circle_thickness = -1
    circle_info = []

    detected_objects = []
    clickable_areas = []

    for result in results:
        boxes = result.boxes

        for box in boxes:

            confidence = math.ceil((box.conf[0] * 100)) / 100
            class_id = int(box.cls[0])

            # Only detect specific objects with confidence > 0.5
            if confidence > 0.5 and (
                    class_names[class_id] in detectable_objects):

                # Draw clickable circle
                cv2.circle(
                    frame, (circle_x, circle_y),
                    circle_radius, COLOR_CIRCLE,
                    circle_thickness
                )
                circle_info = [circle_x, circle_y, circle_radius]

                # Store detected object name
                object_name = class_names[class_id]
                detected_objects.append(object_name)

                # Animate popup height
                if ui_state['popup_opening'] and (
                        popup_height < popup_max_height):

                    popup_height += popup_animation_speed
                    if popup_height >= popup_max_height:
                        popup_height = popup_max_height

                if not ui_state['popup_opening'] and (
                        popup_height > popup_min_height):

                    popup_height -= popup_animation_speed
                    if popup_height <= popup_min_height:
                        popup_height = popup_min_height

                # Show popup if circle is clicked
                if ui_state['circle_clicked']:
                    frame, clickable_areas, link_dict, popup_area = draw_popup(
                        frame,
                        frame_width,
                        popup_height,
                        detected_objects,
                        ui_state['cursor_over_link01'],
                        ui_state['cursor_over_link02'],
                        ui_state['cursor_over_link03']
                    )

                # salvando dados a base de dados
                get_data.save_in_database(object_name)

    cv2.imshow("Video Test", frame)
    cv2.setMouseCallback(
        "Video Test",
        mouse_event,
        param=(
            ui_state,
            circle_info,
            clickable_areas,
            detected_objects,
            link_dict,
            popup_area,
        )
    )

    if cv2.waitKey(5) & 0xFF == ord('q'):

        break

print("\n\n\n")
# Show data that has benn collected
show_results_today = get_data.show_data_today()

print("Object detections from today:")
for obj, dt in show_results_today:
    print(f"- {obj} at {dt}")

# Closing All Connections
info_data.close_connection()
get_data.close_connection()
print("\n\nProgram finished.\n\n")
