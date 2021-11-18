import cv2

def Real_Time_Face_Detection():
    #We use built-in haarcascade classifier from cv2 library to detect the frontal face
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    capture = cv2.VideoCapture(0)
    while (True):
        ret, frame = capture.read()
        # We turn the frame into gray to use the cascade.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # We use this line from the documentation
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
         
            # Location of the frame is as shown below
            # y and x are the starting points, h as height to the up, and w as width to the right
            
               # This is the color of the rectangle specified in BGR.
            color = (255, 0, 0)
            # This determines the thickness of the rectangle we draw around the face
            stroke = 2
            # These are the face coordinates as explained above
            end_cord_x = x + w
            end_cord_y = y + h
    		# With this .rectangle() method we are able to draw the rectangle around the face with the color, thickness and the coordinates
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()