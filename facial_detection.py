import cv2
import numpy as np

cap = cv2.VideoCapture(0)
MOUTH_OPEN_THRESHOLD = 50

def calculate_mouth_openness(mouth_region):
    _, _, _, mouth_height = cv2.boundingRect(mouth_region)
    return mouth_height

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        mouth_region = np.array([
            (x + w // 4, y + 3 * h // 4),
            (x + 3 * w // 4, y + 3 * h // 4),
            (x + w // 2, y + h)
        ], np.int32)
        mouth_height = calculate_mouth_openness(mouth_region)
        if mouth_height > MOUTH_OPEN_THRESHOLD:
            cv2.putText(frame, "Gasping", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
        else:
            cv2.putText(frame, "Not Gasping", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Gasping Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
