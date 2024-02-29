import cv2 as cv

"""img = cv.imread('Documents\\papagan.jpg')
cv.imshow("Original Image", img)
cv.waitKey(0)"""

capture = cv.VideoCapture('Documents\\dag.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Dag', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()