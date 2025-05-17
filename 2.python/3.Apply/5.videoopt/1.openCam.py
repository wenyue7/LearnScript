# 程序说明：视频图像采集(opencv)

import cv2

cap = cv2.VideoCapture(0)
# 从视频流循环帧
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame)
    cv2.imshow("Gray", gray)
    # 退出：Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 清理窗口
cv2.destroyAllWindows()

# 原文链接：https://blog.csdn.net/hadoopdevelop/article/details/89064527
