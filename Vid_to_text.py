import modules
import speech_recognition as sr 
import moviepy.editor as mp
import os

def vid_to_audio(Plink):
    

    base = os.path.splitext(Plink)[0]
    
    AudFileName = base + '.wav'

    print(AudFileName)

    clip = mp.AudioFileClip(Plink) 
 
    clip.write_audiofile(AudFileName)

    r = sr.Recognizer()

    audio = sr.AudioFile(AudFileName)

    with audio as source:
        audio_file = r.record(source)
        r.recognize_google(audio_file)

