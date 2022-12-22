import modules
from gtts import gTTS 

def txtToaudio(summary):
    
    language = 'en'
    speech = gTTS(text = summary , lang = language, slow = False)
    speech.save("F:/research paper/py/output_files/Summarized_format.wav")

