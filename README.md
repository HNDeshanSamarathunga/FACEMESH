
# 🧠 Real-Time Face Mesh Detection using MediaPipe and OpenCV

This project captures video from your webcam and detects facial landmarks using [MediaPipe Face Mesh](https://google.github.io/mediapipe/solutions/face_mesh.html). The landmarks are drawn in real time using OpenCV.

---

## ✅ 1. Import Required Libraries

```python
import mediapipe as mp
import numpy as np
import cv2
```

- **mediapipe**: Used for detecting and drawing the face mesh (468 facial landmarks).
- **numpy**: Imported here but not used heavily in this script.
- **cv2**: OpenCV, used for capturing video from the webcam and displaying the output.

---

## ✅ 2. Initialize MediaPipe Modules

```python
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
```

- `mp_face_mesh`: Contains the model for detecting facial landmarks.
- `mp_drawing`: Contains functions to draw landmarks and connections on an image.
- `mp_drawing_styles`: Optional styles for drawing (not directly used here).

---

## ✅ 3. Start Webcam

```python
cap = cv2.VideoCapture(0)
```

- Opens the default webcam (index 0). Use `1`, `2`, etc., if you have multiple cameras.

---

## ✅ 4. Initialize the Face Mesh Detector

```python
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=True,
    min_tracking_confidence=0.6,
    min_detection_confidence=0.6
)
```

- `static_image_mode=True`: Treats each frame as a static image (better for single-frame input).
- `min_tracking_confidence=0.6`: Minimum confidence to continue tracking a detected face.
- `min_detection_confidence=0.6`: Minimum confidence to initially detect a face.

> 🔁 **Tip:** For real-time performance, use `static_image_mode=False`.

---

## ✅ 5. Main Loop to Read Webcam Frames

```python
while True:
    ret, frm = cap.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break
```

- `cap.read()`: Captures a single frame from the webcam.
- `ret`: A boolean flag to check if capture was successful.
- If frame capture fails, exit the loop.

---

## ✅ 6. Convert BGR to RGB

```python
rgb = cv2.cvtColor(frm, cv2.COLOR_BGR2RGB)
```

- MediaPipe requires RGB format, but OpenCV uses BGR by default.
- Converts the captured frame to RGB before processing.

---

## ✅ 7. Process Frame to Detect Face Mesh

```python
results = face_mesh.process(rgb)
```

- Passes the frame into the face mesh model.
- `results.multi_face_landmarks`: Contains facial landmarks for each detected face.

---

## ✅ 8. Draw Landmarks on Detected Faces

```python
if results.multi_face_landmarks:
    for face_landmarks in results.multi_face_landmarks:
        mp_drawing.draw_landmarks(
            image=frm,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=1)
        )
```

- Loops through all detected faces and draws:
  - **Landmarks**: small green dots.
  - **Connections**: red lines connecting landmarks.

---

## ✅ 9. Show the Output Frame

```python
cv2.imshow("window", frm)
```

- Displays the frame in a window titled `"window"`.

---

## ✅ 10. Break Loop on ESC Key

```python
if cv2.waitKey(1) & 0xFF == 27:
    break
```

- Waits 1 millisecond for a key press.
- If **Esc (ASCII 27)** is pressed, the loop ends.

---

## ✅ 11. Release Resources

```python
cap.release()
cv2.destroyAllWindows()
```

- Releases the webcam.
- Closes all OpenCV windows.

---

## 🔍 Summary

- **Goal**: Detect faces and draw face mesh in real time using a webcam.
- **Technologies Used**:
  - MediaPipe for face landmark detection.
  - OpenCV for webcam access and drawing.
- **Performance Tip**: Set `static_image_mode=False` for optimized real-time performance.

---

## 📷 Preview

> Include a screenshot or GIF of your app running here (optional).

---

## 🔧 Requirements

- Python 3.x
- `mediapipe`
- `opencv-python`
- `numpy`

Install with:

```bash
pip install mediapipe opencv-python numpy
```

---

## 💡 Inspired by

- [MediaPipe Face Mesh Docs](https://google.github.io/mediapipe/solutions/face_mesh.html)

---

## 📄 License

MIT License
