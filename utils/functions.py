import cv2
import numpy as np
from database.info_database import InfoData
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Important functions for code operation
def draw_popup(frame, frame_width, popup_height, detected_objects, cursor_over_link01, cursor_over_link02, cursor_over_link03):

    font_size = 15
    font_path = BASE_DIR / 'font/arial.ttf'

    # Convert OpenCV frame to RGB and create a PIL image
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame_rgb)

    # Drawing popup window
    popup_x, popup_y = 30, 60
    popup_width = frame_width / 2
    draw = ImageDraw.Draw(pil_image)
    draw.rectangle([popup_x, popup_y, popup_x + popup_width, popup_y + popup_height], fill=(255, 255, 255))

    # Saving the entire popup area
    popup_area = (
        popup_x, popup_y, popup_x + popup_width, popup_y + popup_height
    )

    font = ImageFont.truetype(font_path, font_size)

    # Load info from database
    data_list = InfoData().get_info()

    last_text_y = 0
    link_positions = []
    link_dict = {}

    # Matching detected classes (objects) with database info
    # And displaying information on the screen
    for obj_name in detected_objects:

        for entry in data_list:

            if obj_name in entry:
                object_label, description, link = entry
        
                link_dict[obj_name] = link

                info_texts = [
                    f"Objeto Detectado: {object_label}",
                    f"Descrição: {description}",
                    "Link: Clique aqui para saber mais"
                ]

                # Check if any text exceeds the popup width
                formatted_texts = wrap_text_to_fit(
                    info_texts, 
                    popup_width,
                    font,
                    draw
                )

                for i, line in enumerate(formatted_texts):

                    draw.text(
                        (popup_x + 10, popup_y + 20 + i * 30),
                        line, 
                        font=font, 
                        fill=(0, 0, 0)
                    )
                    last_text_y = popup_y + 20 + i * 30

                popup_y = last_text_y + 10
                link_positions.append(last_text_y)

                # Divider line
                draw.line(
                    [
                        (popup_x + 10, popup_y + 30),
                        (popup_x + popup_width - 10, popup_y + 30)
                    ], 
                    fill=(0,0,0),
                    width=3
                )
                popup_y += 40


    # Convert image back to OpenCV BGR format
    frame_bgr = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    # # Draw underline for link on hover
    for i, pos_y in enumerate(link_positions):

        hover = [cursor_over_link01, cursor_over_link02, cursor_over_link03][i] if i < 3 else False
        thickness = 2 if hover else 1

        # Line position
        cv2.line(
            frame_bgr,
            (popup_x + 90, pos_y + 16),
            (popup_x + 116, pos_y + 16),
            (0, 0, 0),
            thickness
        )

    # Define clickable area for each link
    click_areas = []
    for pos_y in link_positions:
        x1 = popup_x + 95
        y1 = pos_y + 5
        x2 = popup_x + 120
        y2 = pos_y + 25
        click_areas.append((x1, y1, x2, y2))

    return frame_bgr, click_areas, link_dict, popup_area



def wrap_text_to_fit(text_list, max_width, font, draw):
    # Breaks lines to ensure text fits inside the popup width.

    wrapped_lines = []
    for block in text_list:

        words = block.split()
        current_line = ""

        for word in words:
            
            line_width = draw.textbbox(
                (0, 0), 
                current_line + word + ' ', 
                font=font)[2]

            if line_width > max_width - 60:
                wrapped_lines.append(current_line.strip())
                current_line = word + ' '
            else:
                current_line += word + ' '

        wrapped_lines.append(current_line.strip())

    return wrapped_lines
