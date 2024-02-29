import cv2 as cv

capture = cv.VideoCapture('Documents\\dag.mp4')

def rescaleFrame (frame, scale=.75):
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    diemensions = width, height
    return cv.resize(frame, diemensions, interpolation=cv.INTER_AREA)


def changeRes(widht, height):
    capture.set(3, widht)  # set the width
    capture.set(4, height)  # set the height

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()