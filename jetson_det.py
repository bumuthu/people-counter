import jetson.inference
import jetson.utils

net = jetson.inference.detectnet("ssd-mobilenet-v2", threshold=0.5)