import cv2

videoCapture = cv2.VideoCapture('in/megamind.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('out/my_output_vid.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)

success, frame = videoCapture.read()

while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()