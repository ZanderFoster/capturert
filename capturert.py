import time
import mss
import cv2
import numpy as np

# Get information of monitor 2
monitor_number = 1
capture_width = 320
capture_height = 320

# Initialize the FPS counter
fps_start_time = time.time()
fps_frame_count = 0

# Create an MSS instance
with mss.mss() as sct:
    monitor = sct.monitors[monitor_number]
    capture_area = {
        "top": ((monitor["height"] - capture_height) // 2) + monitor["top"],  # 100px from the top
        "left": ((monitor["width"] - capture_width ) // 2) + monitor["left"],  # 100px from the left
        "width": capture_width,
        "height": capture_height
    }
    print(monitor["top"])
    print(capture_area["top"])
    while True:
        # Capture the screen region
        screenshot = sct.grab(capture_area)

        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)

        # Display the frame
        cv2.imshow("Screen Capture", frame)

        # Calculate and display the FPS
        fps_frame_count += 1
        fps_current_time = time.time()
        if fps_current_time - fps_start_time >= 1.0:
            fps = fps_frame_count / (fps_current_time - fps_start_time)
            print("FPS:", round(fps, 2))
            fps_start_time = fps_current_time
            fps_frame_count = 0
        time.sleep(0.013)
        # Exit if 'q' is pressed
        if cv2.waitKey(1) == ord("q"):
            break

# Clean up
cv2.destroyAllWindows()
