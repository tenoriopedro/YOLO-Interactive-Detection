import cv2
import webbrowser

def mouse_event(event, x, y, flags, params):
    (
        ui_state, 
        circle_info, 
        clickable_areas, 
        detected_classes, 
        link_dict, 
        popup_area,    
    ) = params

    try:
        circle_x1, circle_y1, radius = circle_info

        # Organizing clickable text areas
        areas_by_index = {}
        if clickable_areas:
            for i, area in enumerate(clickable_areas):
                areas_by_index[f"area_{i+1}"] = area

        # Handle click on circle (toggle popup and pause)
        if event == cv2.EVENT_LBUTTONDOWN:
            
            # Check if user clicked inside the circle 
            clicked_circle = (x - circle_x1) ** 2 + (y - circle_y1) ** 2 <= radius ** 2

            # Check if user clicked inside any clickable popup area
            if popup_area:
                px1, py1, px2, py2 = popup_area
                clicked_inside_popup = px1 <= x <= px2 and py1 <= y <= py2
            else:
                clicked_inside_popup = False
            
            # If popup is open and user clicks OUTSIDE 
            # Of both circle and popup links, close popup
            if ui_state['circle_clicked'] and not clicked_circle and not clicked_inside_popup:
                    ui_state['pause_stream'] = False
                    ui_state['circle_clicked'] = False
                    ui_state['popup_opening'] = False

                    return # early return to avoid further checks

            # If user clicks on the circle (toggle popup)
            if clicked_circle:
                if not ui_state['circle_clicked']:
                    ui_state['circle_clicked'] = True
                    ui_state['popup_opening'] = True
                    ui_state['pause_stream'] = True

                else:
                    ui_state['pause_stream'] = False
                    ui_state['circle_clicked'] = False
                    ui_state['popup_opening'] = False


        # Handle clicks and hover on individual object links
        if ui_state['circle_clicked']:

            if 'area_1' in areas_by_index:
                x1, y1, x2, y2 = areas_by_index['area_1']
                
                ui_state['cursor_over_link01'] = x1 <= x <= x2 and y1 <= y <= y2
                if ui_state['cursor_over_link01'] and len(detected_classes) >= 1:
                    if event == cv2.EVENT_LBUTTONDOWN:
                        webbrowser.open(link_dict[detected_classes[0]])


            # Check hover and click for second link
            if 'area_2' in areas_by_index:
                x3, y3, x4, y4 = areas_by_index['area_2']
                ui_state['cursor_over_link02'] = x3 <= x <= x4 and y3 <= y <= y4
                if ui_state['cursor_over_link02'] and len(detected_classes) >= 2:
                    if event == cv2.EVENT_LBUTTONDOWN:
                        webbrowser.open(link_dict[detected_classes[1]])

            # Check hover and click for third link
            if 'area_3' in areas_by_index:
                x5, y5, x6, y6 = areas_by_index['area_3']
                ui_state['cursor_over_link03'] = x5 <= x <= x6 and y5 <= y <= y6
                if ui_state['cursor_over_link03'] and len(detected_classes) >= 3:
                    if event == cv2.EVENT_LBUTTONDOWN:
                        webbrowser.open(link_dict[detected_classes[2]])

    except:
        pass