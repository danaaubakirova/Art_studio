import speech_recognition as sr
import json

with open('symbol_mapping.json', 'r') as f:
    symbol_mapping = json.load(f)

def translate_to_symbols(text, symbol_mapping):
    symbol_text = ""
    for letter in text:
        if letter.lower() in symbol_mapping:
            symbol_text += symbol_mapping[letter.lower()]
        else:
            symbol_text += letter
    return symbol_text 

r = sr.Recognizer()

with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    while True:
        print("Speak now or type 'stop' to exit:")
        # record the audio
        audio = r.listen(source)

        try:
            # use the recognizer to convert speech to text
            text = r.recognize_google(audio)
            print("You said: " + text)
            if text.lower() == "stop":
                break
            rnd_language = translate_to_symbols(text, symbol_mapping)
            print("Rnd language: " + rnd_language)
            # Return the completed text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

