### Important
I built a model for Face Detection using YOLOv8. I exported the YOLOv8 model to ONNX format. As a result, when i predicted the video through the ONNX model, the FPS went up to 23. I used the Google Cloud Free Program and created a VM and deployed using streamlit via ngrok.

- ONNX model: <a href= "https://github.com/makhmudjumanazarov/Google-Cloud-CPU-ONNX-Deploy-via-ngrok-with-streamlit-face-detecion/blob/main/best.onnx"> face.onnx </a>
 - Code to convert YOLOv8 model to ONNX format:  <a href= "https://github.com/makhmudjumanazarov/TensorRT-Deploy-via-ngrok-with-streamlit-for-face-detecion/blob/main/pytorch_convert_onnx.py"> pytorch_convert_onnx.py </a>
 
### Result
 * **Video inference**: <a href= "https://www.youtube.com/shorts/NgkfgO7wyV0"> Result Video </a>
 
### Steps to Use
<pre>
 You get the Google Cloud Free Program and create a Virtual Machine.The Virtual Machine Properties:
</pre> 
![Alt Text](/images/1.png)
![Alt Text](/images/2.png)
![Alt Text](/images/3.png)
![Alt Text](/images/4.png)
<pre>
If you have problems installing Python, use the following <a href= "https://www.linuxcapable.com/how-to-install-python-3-9-on-debian-linux/#Section-1-Install-Python-39-via-source-on-Debian-12-11-or-10">link</a>.
</pre> 
<br />
Cloning 
<pre>
git clone https://github.com/makhmudjumanazarov/Google-Cloud-CPU-ONNX-Deploy-via-ngrok-with-streamlit-face-detecion
</pre> 
Create a new virtual environment 
<pre>
python -m venv onnx_cpu
</pre> 
<br/>
Activate your virtual environment
<pre>
source onnx_cpu/bin/activate # Linux/Debian
</pre>
<br/>
Install dependencies and add virtual environment to the Python Kernel
<pre>
python -m pip install --upgrade pip
pip install -r requirements.txt 
pip install ipykernel
python -m ipykernel install --user --name=onnx_cpu
</pre>
<br/>
Run streamlit on localhost by running the stream.py file via terminal command (You can select an optional port)
<pre>
streamlit run stream.py --server.port 8520
</pre>

<br/>
Open another page in the terminal (it should be the same as the path above). 
<pre>
  - Sign up: https://ngrok.com/
  - Connect your account: 
                        1. ngrok config add-authtoken your token
                        2. ngrok http 8520     
                        
</pre>
<br/>

If you facing this error, may be you haven’t downloaded/installed ngrok setup or may be there was an issue in going through this.
- Download the <a href= "https://dashboard.ngrok.com/get-started/setup">zip file for Linux</a>
- Unzip it.
- Open The terminal in the current location (inside unzip folder) where you unzip the file.
- Execute the following command into the terminal :
<pre>
sudo cp ngrok /usr/local/bin
</pre>
- Now Run ngrok http 8520
