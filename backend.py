import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Function to capture audio and recognize speech


def recognize_speech_from_mic():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(
            source, duration=1)  # Adjust to noise

        print("Listening...")
        audio = recognizer.listen(source)  # Capture the audio

        try:
            print("Recognizing...")
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")


# Run the function
recognize_speech_from_mic()
