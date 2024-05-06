# ytmp3dl

Download mp3 audio from Youtube using any video's link directly in your terminal. The `links.txt` file will log everything in case you need to find a video again.

> NOTE: By default, the audio files downloaded from YouTube are in `.webm` format due to Youtube's way of doing things. If you want the audio files in `.mp3` format, you can set the `CONVERT` variable in the `downloader.py` file to `True`.

## How to setup

1. Clone: `https://github.com/jwt2706/ytmp3dl.git`
2. Install Python3 (tested on v3.10.12)
3. Read the note above.
4. Install ffmpeg (ONLY IF YOU PLAN ON USING THE CONVERSION FEATURE)
5. Install libs: `pip install -r requirements.txt`
6. Run `launch.sh`
7. Profit

If the shell script doesn't work, you might've forgotten to add python to your env variable.
