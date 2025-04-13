import mediapipe as mp  # Import MediaPipe for face mesh and drawing utilities
import numpy as np  # Import NumPy for numerical operations (not heavily used here)
import cv2  # Import OpenCV for video capture, image processing, and display

# Initialize MediaPipe modules
mp_face_mesh = mp.solutions.face_mesh  # Load the face mesh solution for detecting facial landmarks
mp_drawing = mp.solutions.drawing_utils  # Load drawing utilities to draw landmarks and connections
mp_drawing_styles = mp.solutions.drawing_styles  # Load predefined drawing styles (not used directly here)

# Start webcam to capture video
cap = cv2.VideoCapture(0)  # Open the default webcam (0). Use 1, 2, etc., for other cameras if needed.

# Create face mesh detector with specific configurations
face_mesh = mp_face_mesh.FaceMesh(  # Initialize the face mesh detector
    static_image_mode=True,  # Treat each frame as a static image (not tracking over time)
    min_tracking_confidence=0.6,  # Minimum confidence for tracking (0.0 to 1.0)
    min_detection_confidence=0.6  # Minimum confidence for initial face detection (0.0 to 1.0)
)

while True:  # Start an infinite loop to continuously capture and process video frames
    ret, frm = cap.read()  # Capture a frame from the webcam; 'ret' is True if successful, 'frm' is the frame
    if not ret:  # Check if frame capture failed
        print("Failed to capture frame. Exiting...")  # Print error message
        break  # Exit the loop if no frame is captured (e.g., webcam disconnected)

    # Convert the frame from BGR (OpenCV default) to RGB (MediaPipe requirement)
    rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)  # Convert color space for processing

    # Process the frame to detect faces and their landmarks
    results = face_mesh.process(rgb)  # Use the face mesh model to detect faces in the RGB frame

    # Check if any faces were detected
    if results.multi_face_landmarks:  # If there are any detected face landmarks
        for face_landmarks in results.multi_face_landmarks:  # Loop through each detected face
            # Draw the face mesh on the frame
            mp_drawing.draw_landmarks(  # Draw landmarks and connections on the frame
                image=frm,  # The frame where landmarks will be drawn
                landmark_list=face_landmarks,  # The landmarks of the current face
                connections=mp_face_mesh.FACEMESH_TESSELATION,  # Use FACEMESH_TESSELATION to draw the face outline and structure
                landmark_drawing_spec=mp_drawing.DrawingSpec(  # Style for drawing landmarks (points)
                    color=(0, 255, 0),  # Green color for landmarks (BGR: 0, 255, 0)
                    thickness=1,  # Thickness of the landmark points
                    circle_radius=1  # Radius of the circles marking landmarks
                ),
                connection_drawing_spec=mp_drawing.DrawingSpec(  # Style for drawing connections (lines)
                    color=(255, 0, 0),  # Red color for connections (BGR: 255, 0, 0)
                    thickness=1  # Thickness of the connection lines
                )
            )

    # Display the frame with any drawn landmarks
    cv2.imshow("window", frm)  # Show the frame in a window titled "window"

    # Check for key press to exit the loop
    if cv2.waitKey(1) & 0xFF == 27:  # Wait for 1ms; if Esc key (ASCII 27) is pressed, exit
        break  # Exit the loop when Esc is pressed

# Release resources and close windows
cap.release()  # Release the webcam to free up the camera
cv2.destroyAllWindows()  # Close all OpenCV windows