### Important
I built a model for Face Detection using YOLOv8. I exported the YOLOv8 model to ONNX format. As a result, when i predicted the video through the ONNX model, the FPS went up to 23. I got Google Cloud as a free credit with $300 and created a VM and deployed using streamlit via ngrok.

- ONNX model: <a href= "https://github.com/makhmudjumanazarov/Google-Cloud-CPU-ONNX-Deploy-via-ngrok-with-streamlit-face-detecion/blob/main/best.onnx"> face.onnx </a>
 - Code to convert YOLOv8 model to ONNX format:  <a href= "https://github.com/makhmudjumanazarov/TensorRT-Deploy-via-ngrok-with-streamlit-for-face-detecion/blob/main/pytorch_convert_onnx.py"> pytorch_convert_onnx.py </a>
 
### Result
 * **Video inference**: <a href= "https://www.youtube.com/shorts/NgkfgO7wyV0"> Result Video </a>

 ### Steps to Use
<br />
<b>Step 1.</b> Clone <a href= "https://github.com/makhmudjumanazarov/TensorRT-Deploy-via-ngrok-with-streamlit-for-face-detecion.git">this repository </a>
via Terminal
<br/><br/>
<b>Step 2.</b> Create a new virtual environment 
<pre>
python -m venv TensorRT
</pre> 
<br/>
<b>Step 3.</b> Activate your virtual environment
<pre>
source TensorRT/bin/activate # Linux
</pre>
<br/>
<b>Step 4.</b> Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install -r requirements.txt 
pip install ipykernel
python -m ipykernel install --user --name=TensorRT
</pre>
<br/>
<b>Step 5.</b> Run streamlit on localhost by running the stream.py file via terminal command (You can select an optional port)
<pre>
streamlit run stream.py --server.port 8520
</pre>

<br/>
<b>Step 6.</b> Open another page in the terminal (it should be the same as the path above). 
<pre>
  - Sign up: https://ngrok.com/
  - Connect your account: 
                        1. ngrok config add-authtoken your token
                        2. ngrok http 8520     
                        
</pre>
<br/>

