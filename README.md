# ytmp3dl

Download mp3 audio from Youtube using any video's link directly in your terminal. The `links.txt` file will log everything in case you need to find a video again.

> NOTE: By default, the audio files downloaded from YouTube are in `.webm` format due to Youtube's way of doing things. After download, the audio files are converted to in `.mp3` format for your convenience.

## How to setup

1. Clone: `https://github.com/jwt2706/ytmp3dl.git`
2. Install ffmpeg and Python3 (tested on v3.10.12)
3. Install libs: `pip install -r requirements.txt`
4. Run `launch.sh`
5. Profit

If the shell script doesn't work, you might've forgotten to add python to your env variable.
