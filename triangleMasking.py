####################################
#
#       IMPORT LIBRARIES
#
###################################
import cv2
import numpy as np
import lineDetect as LD
from matplotlib import pyplot as pyplot

####################################
#
#     Same Function Parameters
#
###################################
FILE_PATH = './img/test_video.mp4'      #This parameter holds path for algorithm.
#Interesting Area Triangle 
IA_X1 = 240                             #            (x3,y3)
IA_Y1 = 705                             #               /\                                       
IA_X2 = 1075                            #              /  \
IA_Y2 = 705                             #             /    \                                        
IA_X3 = 560                             #            /______\
IA_Y3 = 275                             #        (x1,y1) (x2,y2)
IA_Triangle = [(IA_X1, IA_Y1),          #This parameters holds interesting area position on image.
               (IA_X2, IA_Y2),
               (IA_X3, IA_Y3)]

#Interersting Area Rectangle
#       -----------. (x2, y2)
#       |          |
#       |          |
#(x1,y1).----------|
#(X1, Y1)
IA_X1 = 550
IA_Y1 = 685
#(X2, Y2)
IA_X2 = 1090
IA_Y2 = 380
IA_Rectangle = [(IA_X1, IA_Y1),          #This parameters holds interesting area position on image.
               (IA_X2, IA_Y2)]
####################################
#
#        MAIN Function
#
###################################
if __name__ == '__main__':
    #load Video
    cap = cv2.VideoCapture(FILE_PATH)

    while True:
        #read video frame by frame
        ret, frame = cap.read()
        #Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Select Interesting Area
        interestArea = LD.interestAreaTriangle(gray, IA_Triangle)
        #Find Line
        lines = LD.findLine(interestArea)
        #Draw Line
        lineImg = LD.drawLine(frame, lines)
        #Show img 
        cv2.imshow('Line Triangle Img', lineImg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

