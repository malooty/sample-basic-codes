import cv2

# RTSP stream URL
rtsp_url = 'rtsp://192.168.99.70:8557/screen'

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Check if the stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

# Get the frame width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Print the resolution
print(f"Resolution: {width}x{height}")

# Release the video capture object
cap.release()
