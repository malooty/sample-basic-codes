#This code is used to get the cordinates ,where the mouse pointer has been clicked.
# click on 2 points and press c ,the normalised form will be shown in the terminal

import argparse
import cv2

refPt = []

def click_and_capture(event, x, y, flags, param):
    global refPt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        print(f"Point {len(refPt)} - Coordinates: {refPt[-1]}")  # Print coordinates to console

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to the video file")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["video"])

fixed_width = 1920/2
fixed_height = 1080/2

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", click_and_capture)

with open("coordinates.txt", "w") as file:
    while True:
        ret, frame = cap.read()
        frame= cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)

        if not ret:
            break

        clone = frame.copy()
        refPt = []
        print()
        cv2.imshow("frame", frame)
        key = cv2.waitKey(0) & 0xFF

        if len(refPt) == 2:
            # Normalize coordinates using fixed width and height
            x1_norm = refPt[0][0] / fixed_width
            y1_norm = refPt[0][1] / fixed_height
            x2_norm = refPt[1][0] / fixed_width
            y2_norm = refPt[1][1] / fixed_height

            # Save normalized coordinates in the specified format [ (x1, y1, x2, y2, 0)]
            coordinates = [x1_norm, y1_norm, x2_norm, y2_norm, 0]
            print(coordinates)
            file.write(f"Frame {int(cap.get(cv2.CAP_PROP_POS_FRAMES))} - Normalized Coordinates: {coordinates}\n")

        if key == ord("c"):
            break

        if key == 27:  # 27 is the ASCII code for the 'Esc' key
            break

cap.release()
cv2.destroyAllWindows()
