import win32com.client
import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import cv2
from openai import OpenAI
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def ai():
    api_key = "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"
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "generate a resignation letter for me very short\n"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "[Your Name]\n[Your Address]\n[City, State ZIP Code]\n[Email Address]\n[Phone Number]\n[Date]\n\n[Recipient's Name]\n[Recipient's Job Title]\n[Company Name]\n[Company Address]\n[City, State ZIP Code]\n\nDear [Recipient's Name],\n\nI hope this letter finds you well. I am writing to officially resign from my position as [Your Job Title] at [Company Name], effective [Last Working Day - typically two weeks from the date of the letter, unless otherwise specified].\n\nIt is with mixed emotions that I submit my resignation. Over the past [X years/months], I have genuinely enjoyed working at [Company Name]. The experiences, challenges, and knowledge gained during this time have been invaluable to my personal and professional growth. I am grateful for the opportunities I have received and the collaborative work environment that has fostered my career development.\n\nAfter much consideration, I have decided to pursue a new opportunity that aligns more closely with my long-term career aspirations. While it was a difficult decision to make, I firmly believe it is the right path for my professional growth and development.\n\nI am committed to making a smooth transition during the notice period. I will do my best to ensure that all pending projects and tasks are either completed"
            },
            {
                "role": "assistant",
                "content": "or handed over to a designated team member before my departure. Please let me know if there is anything specific I can do to facilitate a seamless transition.\n\nI am grateful for the invaluable experience and support I have received from you and the entire team at [Company Name]. I will always cherish the relationships I have built here and the knowledge I have gained. I am confident that [Company Name] will continue to thrive and achieve great success in the future.\n\nThank you once again for the opportunity to be part of the [Company Name] family. I wish you and the entire team nothing but the best for the future.\n\nSincerely,\n[Your Name]"
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)


def test_camera(index):
    cap = cv2.VideoCapture(index)

    if not cap.isOpened():
        print(f"Camera at index {index} is not available.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Failed to grab frame from camera {index}.")
            break

        cv2.imshow(f"Camera {index}", frame)

        # Check if the user pressed the close button
        if cv2.getWindowProperty(f"Camera {index}", cv2.WND_PROP_VISIBLE) < 1:
            break

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' key or ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print("Listening...")
        try:
            audio = r.listen(source, timeout=2)  # Increase the timeout to 5 seconds
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return "error occurred"


def say(text):
    os.system(f"say {text}")
speaker.speak("hello i am JARVIS")
while True:
    print("Enter the word you want to speak it out by the computer")
    query=takeCommand()
    sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"],"instagram","https://www.instagram.com/?hl=en"]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.Speak(f"opening {site[0]}")
            webbrowser.open(f"{site[1]}")
    if "open music".lower() in query.lower():
        path = "C:\\Users\\Abdul Jabbar Khan\\PycharmProjects\\jarvisAI\\musicpy.mp3"
        os.startfile(path)
    if " time".lower() in query:
        strfTime=datetime.datetime.now().strftime("%H:%M:%S")
        speaker.Speak(f"sir the time is{strfTime}")
    print(query.lower())
    if "chrome".lower() in query.lower():
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.run([chrome_path])
    if "spotify".lower() in query.lower():
        spotify_path = r"C:\Users\Abdul Jabbar Khan\AppData\Roaming\Spotify\Spotify.exe"
        subprocess.run([spotify_path])
    if "camera".lower() in query.lower():

        print(f"Testing camera at index {0}...")
        test_camera(0)
    if "Using artificial intelligence".lower() in query.lower():

    speaker.Speak(query)



