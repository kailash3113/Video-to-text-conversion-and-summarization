import modules
import pytube

def youtubeToVid(link):
    Ylink = "F:/research paper/py/output_files/Youtube_vid.mp4"
    data = pytube.YouTube(link)
    audio = data.streams.get_audio_only()
    audio.download(filename = Ylink)
    