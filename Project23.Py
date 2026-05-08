import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: could not open webcam.")
    exit()

while True:
    ret, frame, = cap.read()
    if not ret:
        print("Error: Failed to capture the image!")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x + w, y + h), (225,0,0),2)

        smiles = smile_cascade.detectMultiScale(gray[y:y + h, x:x + w], scaleFactor=1.7, minNeighbors=20, minSize=(25,25))

        for (sx,sy,sw,sh) in smiles:
            cv2.putText(frame, 'Happy :)', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(0,255,0),2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'People count:{len(faces)}',(10,30),font, 1,(225,0,0),2)

    cv2.imshow('Face and Emotion Detection - Press q to Quit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()