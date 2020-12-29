####################################
#
#       IMPORT LIBRARIES
#
###################################
import cv2
import numpy as np
import matplotlib.pyplot as plt

####################################
#
#       SOME PARAMETERS
#
###################################
#Gaussian Blur
KERNEL_SIZE = 9                         #This parameter holds value of kernel size for GaussianBlur method (it must be odd number).
#Canny Edge Detection
THRESHOLD_LOW = 50                      #This parameter holds value of threshold low for canny edge detection method.
THRESHOLD_HIGH = 150                    #This parameter holds value of threshold high for canny edge detection method.
#Hough Line P
RHO = 1                                 #This parameter is distance resolution in pixels of the Hough grid.
THETA = np.pi / 180                     #This parameter is angular resolution in radians of the Hough grid.
THRESHOLD = 15                          #This parameter is minimum number of votes.
MIN_LINE_LENGHT = 10                    #This parameter is minimum numbe of pixels making up a line.
MAX_LINE_GAP = 10                       #This parameter is maximum GAP in Pixels between connectable line segments.

#LINE Customization
LINE_COLOR = (150,150,0)                #This parameter holds line color (BGR format).
LINE_THICKNESS = 5                      #This parameter holds line thickness value (px).
####################################
#
#       FUNCTIONS
#
###################################
#Select Area of interest
# @fn       : interestArea
# @brief    : This function masking gray image.
# @param[0] : This parameter is image data for masking process. Image must convert gray scale.
# @param[1] : This parameter holds polygon point on image.
# 
# @return   : Masked image
# @NOTE     : This function just works gray scale image.

def interestArea(Image, Triangle):
    #create a mask that its size is same with Image.
    #0 - Create a polygon and get data of Image
    polygon = np.array([Triangle])
    IMG_HEIGHT = Image.shape[0]
    IMG_WIDTH = Image.shape[1]
    IMG_CHNL = 1
    #1 - Create a new zero array that size is same img to mask and set polygon in this array.
    mask = np.zeros([IMG_HEIGHT, IMG_WIDTH, IMG_CHNL], np.uint8)
    mask = cv2.fillPoly(mask, polygon, 255)
    #2 - 'And' operation with mask and img
    return cv2.bitwise_and(Image, Image, mask= mask)

#Find line from insteresting area of image
# @fn       : interestingArea
# @brief    : This function finds line in image.
# @param[0] : This parameter is image data for process. Image must convert gray scale and masked.
# 
# @return   : line information in image
# @NOTE     : This function just works gray scale image and you should use area of interest for more perform.
def findLine(Image):
    #1 - Blur to more understanding color changing in image.
    blur = cv2.GaussianBlur(Image, (KERNEL_SIZE,KERNEL_SIZE), 0)
    #2 - Canny Edge Detection to select color changing in image.
    edges = cv2.Canny(blur, THRESHOLD_LOW, THRESHOLD_HIGH)
    #3 - Hough Line P Find to Line in image
    return cv2.HoughLinesP(edges, RHO, THETA, THRESHOLD, np.array([]), MIN_LINE_LENGHT, MAX_LINE_GAP)

#Draw Line on image
# @fn       : drawLine
# @brief    : This function draws line in image.
# @param[0] : This parameter holds image data for process.
# @param[1] : This parameter holds line information in image.
#  
# @return   : image as draw line
# @NOTE     : This function just works gray scale image and you should use area of interest for more perform.
def drawLine(image, lines):
    lineImg = np.zeros_like(image)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(lineImg, (x1,y1), (x2,y2), LINE_COLOR, LINE_THICKNESS)
    linesEdges = cv2.addWeighted(image, 0.8, lineImg, 1, 0)
    return linesEdges
