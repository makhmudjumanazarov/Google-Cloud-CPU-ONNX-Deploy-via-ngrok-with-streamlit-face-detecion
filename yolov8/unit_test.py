import time
import cv2
import onnxruntime
import numpy as np


path = "/home/jumanazarovalaylo2013/Google-Cloud-CPU-ONNX-Deploy-/best.onnx"
session = onnxruntime.InferenceSession(path,providers=onnxruntime.get_available_providers())
