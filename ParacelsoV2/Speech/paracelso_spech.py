import speech_recognition as sr
import pyttsx3

says = pyttsx3.init()


class paracelso_recognition:
    def text_to_speech(self, fala):
        says.setProperty('languages', b'pt-BR')
        says.setProperty('voices', says.getProperty('voices')[1])
        says.say(fala)
        says.runAndWait()

    def speech_totext(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            source.CHUNK = 1024
            r.energy_threshold += 280
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="pt-BR")
                return text
            except sr.UnknownValueError:
                return "Não consegui te entender, poderia ser mais claro?"
            except sr.RequestError as e:
                print("erro; {0}".format(e))
