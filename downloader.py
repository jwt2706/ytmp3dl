# for documentation, see README

from pytube import YouTube
from pydub import AudioSegment
import os

while True:
    v = input("Video link: ")
    yt = YouTube(v)

    streams = yt.streams.filter(only_audio=True)

    # select the stream with the highest bitrate
    selected_stream = sorted(streams, key=lambda stream: int(stream.abr.replace('kbps', '')) if stream.abr else 0, reverse=True)[0]
    
    out_file = selected_stream.download(output_path=".")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    audio = AudioSegment.from_file(out_file)
    audio.export(new_file, format="mp3")
    os.remove(out_file)

    with open("links.txt", "a") as links:
        links.write(v+"\n")