#  fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')#VideoWriter_fourcc为视频编解码器
#编码参数：
#  cv2.VideoWriter_fourcc('M', 'P', '4', 'V') MPEG-4编码 .mp4  要限制结果视频的大小，这是一个很好的选择。
#  cv2.VideoWriter_fourcc('X','2','6','4')   MPEG-4编码  .mp4  想限制结果视频的大小，这可能是最好的选择。
#  cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi   广泛兼容，但会产生大文件
#  cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi
#  cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi  要限制结果视频的大小，这是一个很好的选择。
#  cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv
#  cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv

#  函数原型 cv2.VideoWriter()
#  VideoWriter(filename, fourcc, fps, frameSize[, isColor]) -> <VideoWriter object>
#  参数说明：
#  第一个参数是要保存的文件的路径
#  fourcc 指定编码器
#  fps 要保存的视频的帧率
#  frameSize 要保存的文件的画面尺寸
#  isColor 指示是黑白画面还是彩色的画面

import cv2

# cap = cv2.VideoCapture('F:\\test.mp4')
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps =cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('./output.mp4',fourcc, fps, size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
# 原文链接：https://blog.csdn.net/linghugoolge/article/details/81165430
