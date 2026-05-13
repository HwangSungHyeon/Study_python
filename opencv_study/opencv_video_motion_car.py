
import cv2

cap = cv2.VideoCapture("opencv_study/videos/motion_car.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

delay = int(1000 / fps)

pre_frame = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (360,640))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5,5), 0)

    if pre_frame is None:
        pre_frame = gray
        continue

    diff = cv2.absdiff(pre_frame, gray)

    _, thresh = cv2.threshold(
        diff, 100, 255, cv2.THRESH_BINARY
    )

    thresh = cv2.dilate(thresh, None, iterations=8)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = frame.copy()

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 10: continue
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(
            result,
            (x,y),
            (x+w,y+h),
            (0,0,255),
            2
        )
        cv2.putText(
            result,
            "car",
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow("original", frame)
    cv2.imshow("diff",diff)
    cv2.imshow("box",result)

    if cv2.waitKey(delay) == 27:
        break

    pre_frame = gray

cap.release()
cv2.destroyAllWindows()