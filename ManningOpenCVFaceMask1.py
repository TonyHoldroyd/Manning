import numpy as np
import cv2

cam = cv2.VideoCapture(0)  # initialise webcam

while(True):
    # Preserve alpha channel
    face_mask = cv2.imread('mask.png', flags=cv2.IMREAD_UNCHANGED)
    # Channels 0..2, colour channels
    bgr_face_mask = face_mask[:, :, :3]
    # Channels 3, aplpha channel
    alpha_face_mask = face_mask[:, :, 3]
    # Display colour mask
    cv2.imshow('bgr_face_mask', bgr_face_mask)
    # Display background mask
    cv2.imshow('alpha_face_mask', alpha_face_mask)

    # Capture webcam
    on, picture = cam.read()
    # so we get single frame
    # cap.release()
    # Display the  webcam
    cv2.imshow('face', picture)
    # Wait for ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.imshow('face', picture)
cv2.waitKey(0) & 0xFF

# When done, release the capture
cam.release()
# And destroy windows
cv2.destroyAllWindows()
