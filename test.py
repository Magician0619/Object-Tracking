import cv2 as cv

def threshold_funtion(image):
    '''
        全局阈值    
    '''
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    ret1, binary1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY)
    # print("阈值：%s"%ret)
    print("阈值：%s"%ret1)
    # cv.imshow("OTSU",binary)
    cv.imshow("OSTU1",binary1)
    cv.waitKey(0)


img = cv.imread("3line.jpg")
threshold_funtion(img)