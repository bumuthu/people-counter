import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0")  # 'my_video.mp4' for file

# while True:
#     img = camera.Capture()
#     detections = net.Detect(img)

#     for detection in detections:
#         print(detection)

#     display.Render(img)
# 	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
