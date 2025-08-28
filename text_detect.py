import cv2
import easyocr
import pyttsx3
import threading
import time
import numpy as np

text_to_speak = ""
spoken_boxes = []
lock = threading.Lock()

def speech_worker():
    global text_to_speak, spoken_boxes
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    for voice in engine.getProperty('voices'):
        if 'india' in voice.name.lower() or 'en-in' in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break

    last_text = ""
    while True:
        with lock:
            text = text_to_speak.strip()
            boxes = spoken_boxes.copy()
        if text and text != last_text:
            print(f"🔊 Speaking: {text}")
            engine.say(text)
            engine.runAndWait()
            last_text = text
        time.sleep(0.1)

def ocr_worker():
    global text_to_speak, spoken_boxes
    while True:
        if frame_buffer is None:
            time.sleep(0.05)
            continue

        with lock:
            frame = frame_buffer.copy()

        resized = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        sharpened = cv2.filter2D(gray, -1, sharpen_kernel)

        results = reader.readtext(sharpened)
        full_text = []
        boxes = []

        for (bbox, text, conf) in results:
            if conf > 0.4 and len(text.strip()) >= 3:
                full_text.append(text.strip())
                boxes.append(np.array(bbox, dtype=np.int32))

        with lock:
            if full_text:
                combined_text = " ".join(full_text)
                if combined_text.lower() != text_to_speak.lower():
                    text_to_speak = combined_text
                    spoken_boxes = boxes

        time.sleep(2.5)  # Delay between OCR scans

# --- Setup ---
print("🔄 Loading OCR Engine...")
reader = easyocr.Reader(['en'], gpu=False)

frame_buffer = None
threading.Thread(target=speech_worker, daemon=True).start()
threading.Thread(target=ocr_worker, daemon=True).start()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("\n--- 🔁 Real-time OCR Mode ---")
print("❌ Press 'q' to quit.\n")

cv2.namedWindow("Live OCR Feed", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera error.")
        break

    with lock:
        frame_buffer = frame.copy()
        for box in spoken_boxes:
            cv2.polylines(frame, [box], isClosed=True, color=(0, 255, 0), thickness=2)

    cv2.imshow("Live OCR Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
