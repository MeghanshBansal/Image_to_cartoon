import cv2 as cv

#Loading the image
image = cv.imread("IMG.jpg")

#resize the image
image = cv.resize(image, (800,600))

#converting image to grayscale
grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


#Smoothning the image
smoothgrayscaleimage = cv.medianBlur(grayscale_image, 5)


#getting the edges of the image
getedge = cv.adaptiveThreshold(smoothgrayscaleimage, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 9)


#Preparing the mask
colorImage = cv.bilateralFilter(image, 9, 300, 300)


#cartoon image
cartoon = cv.bitwise_and(colorImage, colorImage, mask=getedge)
cv.imshow("cartoon image", cartoon)

cv.waitKey(0)
cv.destroyAllWindows()
