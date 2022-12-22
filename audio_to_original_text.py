import modules
import speech_recognition as sr 


def AudToTxt(AudFile):
    
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    clean_support_call = sr.AudioFile(AudFile)
    with clean_support_call as source:
        clean_support_call_audio = recognizer.record(source)
    text = recognizer.recognize_google(clean_support_call_audio,language="en-US")
    
    with open('F:/research paper/py/output_files/Original_Text_conversion.txt','w') as f:
        f.write(text)
    
