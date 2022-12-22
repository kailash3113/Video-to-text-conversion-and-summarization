import modules
from youtube_link_vid import youtubeToVid
from Vid_to_text import vid_to_audio
from audio_to_original_text import AudToTxt
from original_to_summary import Summarize
from SummarizedTxt_to_audio import txtToaudio


def main(Ylink):
    
    youtubeToVid(Ylink)
    print("The convertion of Youtube Link to video is done successfully...!!!")
    
    vidLink = "F:/research paper/py/output_files/Youtube_vid.mp4"
    vid_to_audio(vidLink)
    print("The video has been successfully converted into audio...!!!")
    
    AudToTxt("F:/research paper/py/output_files/Youtube_vid.wav")
    print("Audio to Text Conversion Successful...!!!")
    
    with open("F:/research paper/py/output_files/Original_Text_conversion.txt",'r') as f:
        file = f.read()
    
    Summarize(file,0.5)
    print("The Summarization of original file is Successfull")
    
    with open("F:/research paper/py/output_files/Summarized_file.txt",'r') as f:
        file1 = f.read()
    
    txtToaudio(file1)
    print("The Summarized file is converted into audio file")
    
