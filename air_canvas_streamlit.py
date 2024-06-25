import cv2
import numpy as np
import mediapipe as mp
from collections import deque
import streamlit as st

# --- Camera Access Check ---
def get_available_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Add CAP_DSHOW for some systems
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

available_cameras = get_available_cameras()
if not available_cameras:
    st.error("No camera found. Please check your camera connections and permissions.")

# --- Page Configuration ---
st.set_page_config(page_title="Air Canvas", page_icon="🎨", layout="wide")

# --- Header and Description ---
st.title("Air Canvas 🎨")
st.write("Unleash your creativity and draw on the virtual canvas using just your hand gestures!")
st.write("**Instructions:**")
st.write("- Use your index finger as the drawing tool.")
st.write("- Raise your thumb to activate the drawing mode.")
st.write("- Select colors and clear the canvas from the sidebar.")

# --- Developer and Project Information (Sidebar) ---
with st.sidebar.expander("About the Developers ✨"):
    for dev in [
        ("Susanta Baidya", "https://www.linkedin.com/in/susanta-baidya-03436628a/"),
        ("Divyanshu Mittal", "https://www.linkedin.com/in/divyanshu-mittal-4b652228a/"),
        ("Manaswini Gupta", "https://www.linkedin.com/in/manaswini-gupta-1a698827b/"),
        ("Subhi Arjaria", "https://www.linkedin.com/in/subhi-arjaria-279336237/"),
    ]:
        st.write(f"- [{dev[0]}]({dev[1]})")

with st.sidebar.expander("About Air Canvas 🖌️"):
    st.write(
        """
        Air Canvas leverages the power of Mediapipe for hand tracking to create a fun and interactive drawing experience. 
        Let your imagination flow and explore the world of digital art with this innovative tool!
        """
    )

# --- Initialization ---
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Drawing Settings
bpoints, gpoints, rpoints, ypoints = [deque(maxlen=1024) for _ in range(4)]
color_index = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
color_names = ["Blue", "Green", "Red", "Yellow"]

# --- Sidebar Controls ---
st.sidebar.title("Control Panel 🕹️")
selected_camera = st.sidebar.selectbox(
    "Select Camera",
    available_cameras,
    index=0 if available_cameras else None
)
color_index = st.sidebar.selectbox("Color", range(len(colors)), format_func=lambda x: color_names[x])
if st.sidebar.button("Clear Canvas"):
    paintWindow[67:, :, :] = 255
    bpoints, gpoints, rpoints, ypoints = [deque(maxlen=1024) for _ in range(4)]

# --- Canvas Setup ---
paintWindow = np.zeros((471, 636, 3), dtype=np.uint8) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
paintWindow = cv2.rectangle(paintWindow, (160, 1), (255, 65), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (275, 1), (370, 65), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (390, 1), (485, 65), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (505, 1), (600, 65), colors[3], -1)
cv2.putText(paintWindow, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)

# --- Main Streamlit Loop ---
# Check if a camera is selected
if selected_camera is not None:
    cap = cv2.VideoCapture(selected_camera)  # Use selected_camera index
    frame_placeholder = st.empty()
    paint_placeholder = st.empty()

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            st.error("Ignoring empty camera frame.")
            continue
        # ... (rest of your drawing code remains the same)


    image = cv2.flip(image, 1)
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                mp_draw.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
            )
            
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv2.circle(image, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
                    if cy <= 65:
                        if 40 <= cx <= 140:  # Clear Button
                            bpoints = [deque(maxlen=512)]
                            gpoints = [deque(maxlen=512)]
                            rpoints = [deque(maxlen=512)]
                            ypoints = [deque(maxlen=512)]
                            paintWindow[67:, :, :] = 255
                        elif 160 <= cx <= 255:
                            color_index = 0
                        elif 275 <= cx <= 370:
                            color_index = 1
                        elif 390 <= cx <= 485:
                            color_index = 2
                        elif 505 <= cx <= 600:
                            color_index = 3
                    else :
                        bpoints[blue_index].appendleft((cx, cy))
                elif id == 4:
                    cv2.circle(image, (cx, cy), 5, (0, 255, 255), cv2.FILLED)

    for i in range(len(bpoints)):
        for j in range(1, len(bpoints[i])):
            if bpoints[i][j - 1] is None or bpoints[i][j] is None:
                continue
            cv2.line(paintWindow, bpoints[i][j - 1], bpoints[i][j], colors[0], 8)
            cv2.line(image, bpoints[i][j - 1], bpoints[i][j], colors[0], 8)

    for i in range(len(gpoints)):
        for j in range(1, len(gpoints[i])):
            if gpoints[i][j - 1] is None or gpoints[i][j] is None:
                continue
            cv2.line(paintWindow, gpoints[i][j - 1], gpoints[i][j], colors[1], 8)
            cv2.line(image, gpoints[i][j - 1], gpoints[i][j], colors[1], 8)

    for i in range(len(rpoints)):
        for j in range(1, len(rpoints[i])):
            if rpoints[i][j - 1] is None or rpoints[i][j] is None:
                continue
            cv2.line(paintWindow, rpoints[i][j - 1], rpoints[i][j], colors[2], 8)
            cv2.line(image, rpoints[i][j - 1], rpoints[i][j], colors[2], 8)

    for i in range(len(ypoints)):
        for j in range(1, len(ypoints[i])):
            if ypoints[i][j - 1] is None or ypoints[i][j] is None:
                continue
            cv2.line(paintWindow, ypoints[i][j - 1], ypoints[i][j], colors[3], 8)
            cv2.line(image, ypoints[i][j - 1], ypoints[i][j], colors[3], 8)


    # Display the frame and paint window
    frame_placeholder.image(image, channels="BGR")
    paint_placeholder.image(paintWindow, channels="BGR")
    


cap.release()

