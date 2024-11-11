from picamera2 import Picamera2
from libcamera import controls
import time

# Initialize the camera
picam2 = Picamera2()

# Set autofocus mode to continuous
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})

# Start the camera preview for a live video stream
picam2.start(show_preview=True)

try:
    # Keep the stream open indefinitely
    while True:
        time.sleep(1)  # Add a delay to prevent high CPU usage
except KeyboardInterrupt:
    # Stop the stream when you press Ctrl+C
    pass
finally:
    # Clean up resources
    picam2.stop_preview()
    picam2.close()
