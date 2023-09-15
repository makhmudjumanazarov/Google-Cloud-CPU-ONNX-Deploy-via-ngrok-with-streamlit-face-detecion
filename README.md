### Important
- I built a model for Face Detection using YOLOv8. I exported the YOLOv8 model to ONNX format. As a result, when i predicted the video through the ONNX model, the FPS went up to 23 and deployed via ngrok using streamlit.

### Requirements

 * Check the **requirements.txt** file.
 * For ONNX, if you have a NVIDIA GPU, then install the **onnxruntime-gpu**, otherwise use the **onnxruntime** library.

### Installation
```shell
git clone https://github.com/ibaiGorordo/ONNX-YOLOv8-Object-Detection.git
cd ONNX-YOLOv8-Object-Detection
pip install -r requirements.txt
```
### ONNX Runtime
For Nvidia GPU computers:
`pip install onnxruntime-gpu`

Otherwise:
`pip install onnxruntime`

### Examples

 * **Video inference**: https://www.youtube.com/shorts/NgkfgO7wyV0
