# for documentation, see README

from pytube import YouTube
import os

CONVERT = False  # Set to True if you want to convert incoming webm files to mp3

if CONVERT:
    from pydub import AudioSegment

while True:
    v = input("Video link: ")
    yt = YouTube(v)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=".")

    if CONVERT:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        audio = AudioSegment.from_file(out_file, format="webm")
        audio.export(new_file, format="mp3")
        os.remove(out_file)
    else:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.webm'
        os.rename(out_file, new_file)

    with open("links.txt", "a") as links:
        links.write(v+"\n")