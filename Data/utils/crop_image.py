import cv2
import numpy as np
import os
import secrets

cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0

path = './fish/Croaker'
image_list = os.listdir(path)
image_list = [list for list in image_list if not list.endswith(".csv")]

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping, roi

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)

for img in image_list:
    
    image = cv2.imread(os.path.join(path, img))
    oriImage = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)

    while True:

        i = image.copy()

        if not cropping:
            cv2.imshow("image", image)

        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)
        
        if cv2.waitKey(1) & 0xFF == ord('z'):
            cv2.imwrite(os.path.join(path,secrets.token_hex(30)+'.jpg'), roi)   

        if cv2.waitKey(1) & 0xFF == ord('x'):
            cv2.destroyAllWindows()
            break
