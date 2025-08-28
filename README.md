# Real-Time Text Detection and Recognition 👁️➡️🗣️



## ✨ Key Features

* **Real-Time Performance**: Operates smoothly at over 15 FPS thanks to a multithreaded architecture that prevents lag.
* **Text-to-Speech (TTS)**: Converts any detected text into clear, audible speech using an efficient offline engine.
* **High Accuracy**: Achieves a 76% accuracy rate on clear, printed text from various sources like books and signs. 
* **Dual Feedback System**: Provides both visual bounding boxes around detected text and audio confirmation, ensuring users know exactly what is being read.

## 🛠️ Technology Stack

The application is built using a combination of powerful and efficient technologies:

* **Python**: The core programming language, chosen for its simplicity and extensive libraries.
* **OpenCV**: Used for real-time video capture and image pre-processing. 
* **EasyOCR**: The heart of the system; a powerful deep-learning library for accurate text detection and recognition.
* **pyttsx3**: An efficient, offline text-to-speech (TTS) engine for immediate audio feedback.

## ⚙️ How It Works

The system follows a multi-threaded workflow to ensure a smooth user experience:

1.  **Frame Capture**: The webcam captures live video, which is optimized for processing.
2.  **Text Recognition**: A background thread uses **EasyOCR** to process frames and extract text. 
3.  **Text Pre-processing**: Detected text is cleaned to enhance clarity for speech synthesis. 
4.  **Speech Conversion**: The cleaned text is converted into audio in real-time using **pyttsx3**. 
5.  **Audio & Visual Feedback**: The speech is played back, and green boxes are drawn on the screen to highlight the recognized text.

## 🚀 Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Keshav1234-lab/Real-Time-Text-Recognition.git](https://github.com/Keshav1234-lab/Real-Time-Text-Recognition.git)
    cd Real-Time-Text-Recognition
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

## ▶️ Usage

Once the setup is complete, run the main script to start the application:

```bash
python main.py
```
Point your webcam at some text, and the application will start reading it aloud. Press **'q'** to quit.
