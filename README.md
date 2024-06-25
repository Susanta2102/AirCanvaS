# Air Canvas with Mediapipe

![Air Canvas Demo](demo.gif)

## Overview
Air Canvas is an interactive application that allows users to draw on a digital canvas using hand gestures captured by a webcam. It leverages Mediapipe for hand detection and tracking, enabling real-time drawing based on the movement of the user's hand. This project is built using Python, OpenCV, Mediapipe, and Streamlit.

## Features
- **Hand Detection:** Tracks the user's hand movements using the webcam.
- **Color Selection:** Users can choose from different colors (Blue, Green, Red, Yellow) to draw on the canvas.
- **Clear Canvas:** Provides a button to clear the entire canvas.
- **Save Artwork:** Allows users to save their drawings as images.
- **Dynamic Brush Size:** Adjusts the brush size based on the distance between the thumb and index finger.
- **Developer Information:** Links to the LinkedIn profiles of the developers are provided in the sidebar.

## How to Use
1. **Setup:**
   - Ensure your webcam is connected and positioned correctly.
   - Adjust lighting conditions for optimal hand detection.

2. **Interaction:**
   - Move your hand in front of the webcam to draw on the canvas.
   - Use your index finger to draw lines.
   - Raise your thumb to switch colors.

3. **Controls:**
   - **Color Selection:** Use the sidebar color picker to choose a color.
   - **Clear Canvas:** Click the 'Clear Canvas' button on the sidebar to erase all drawings.
   - **Save Artwork:** Click 'Save Artwork' to save your current drawing as an image.

4. **Advanced Features:**
   - Experiment with different hand movements and colors to create artwork.
   - Adjust brush size dynamically by varying the distance between your thumb and index finger.

5. **Developer Information:**
   - Connect with the developers through their LinkedIn profiles provided in the sidebar.

## Installation
To run the Air Canvas application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
streamlit run air_canvas.py
Requirements
Ensure you have the following libraries installed:

OpenCV (cv2)
Numpy (numpy)
Mediapipe (mediapipe)
Streamlit (streamlit)
Contributors
Susanta Baidya
Divyanshu Mittal
Manaswini Gupta
Subhi Arjaria
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Notes:
- Replace `<repository_url>` and `<repository_name>` with your actual repository URL and name.
- If your project does not have a `demo.gif`, you can remove the `![Air Canvas Demo](demo.gif)` line.
- Ensure you have a `requirements.txt` file listing the required Python packages.
- Adjust the sections as per your project details and structure.
- Include the `LICENSE` file in your project directory if not already present.

This README file provides comprehensive information about the Air Canvas project, including its purpose, features, usage instructions, installation guide, contributor details, and licensing information. Adjust the content as necessary to fit your specific project requirements and preferences.
