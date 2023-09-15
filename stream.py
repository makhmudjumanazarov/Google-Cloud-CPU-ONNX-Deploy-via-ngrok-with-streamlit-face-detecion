import streamlit as st
import cv2
import tempfile
from yolov8 import YOLOv8
import time

st.write("""
### Face Detection with ONNX
""")

# Upload a video file
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

# Initialize YOLOv8 model
model_path = "/home/mahmud/Google-Cloud-CPU-ONNX-Deploy-/best.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)


if video_file is not None:
    # Create a temporary file to store the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tfile:
        tfile.write(video_file.read())
    
    # Open the video file for reading
    cap = cv2.VideoCapture(tfile.name)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # or use 'XVID'
    out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (width, height))

    if cap.isOpened():
        st.write("Video Playback:")
        fps = 0
        fpss = []
        prev_time = 0
        curr_time = 0
        fps_out = st.empty()
        image_out = st.empty()
        # Read and display frames from the video
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (width, height))

            # Update object localizer
            prev_time = time.time()
            boxes, scores, class_ids = yolov8_detector(frame)
            curr_time = time.time()
            combined_img = yolov8_detector.draw_detections(frame)

            
            fps = 1.0 / (curr_time - prev_time)
            fps_out.write(f"FPS:{fps}")

            # Write the frame into the file 'output.mp4'
            out.write(combined_img)
        
            # Display the frame in Streamlit
            image_out.image(combined_img, channels="BGR", use_column_width=True)
        
        # Release everything after the job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    else:
        st.write("Error: Unable to open the video file.")
else:
    st.write("Please upload a video file to display.")