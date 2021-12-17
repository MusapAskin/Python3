
import cv2
import numpy as np
import pyautogui
Screen_Size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*XVID)
out=cv2.VideoWriter("Output.avi",fourcc,20.0,(Screen_Size))
while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitkey(1)==ord("q"):
        break

cv2.destroyAllWindows()
out.release()