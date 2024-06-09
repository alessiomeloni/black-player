import youtube_dl
import os

os.add_dll_directory(
    r"C:\VLC"
)  # You need to install VLCx86 and ffmpeg in "C:" for start this script
import vlc
from threading import Thread
import time


class blackPlayer(object):
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
                "preferredquality": "192",
            }
        ],
        "outtmpl": "myMusic/%(title)s.%(ext)s",
    }
    player = None
    musicPlayerStats = False

    def downloader():
        ydl_opts = blackPlayer.ydl_opts
        while True:
            try:
                target = str(input("Give me the fucking link m8:\t"))
                break
            except ValueError:
                pass

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([target])

        print("Download completed")
        blackPlayer.main()

    def musicPlayer():
        blackPlayer.musicPlayerStats = True
        import glob
        import random

        musicStack = glob.glob("myMusic/*.m4a")
        random.shuffle(musicStack)
        for music in musicStack:
            if blackPlayer.musicPlayerStats is False:
                return
            blackPlayer.player = vlc.MediaPlayer(music)
            blackPlayer.player.play()
            time.sleep(1)
            time.sleep(blackPlayer.player.get_length() / 1000)
            blackPlayer.player.stop()

        blackPlayer.musicPlayerStats = False
        return

    def main():
        while True:
            choice = None

            #############################
            os.system("cls" if os.name == "nt" else "clear")
            print("#" * 25)
            print("1: Download some shit")
            print("2: Let's start your shitty playlist")
            print("3: Stop this fucking noise")
            print("#" * 25)
            #############################

            try:
                choice = int(input("WTF would you like to do?\t"))
            except ValueError:
                pass

            if choice == 1:
                blackPlayer.downloader()
            elif choice == 2:
                if blackPlayer.musicPlayerStats is False:
                    mPlayer = Thread(target=blackPlayer.musicPlayer)
                    mPlayer.start()
                else:
                    print("You are already listening!")
                    time.sleep(4)
            elif choice == 3:
                if blackPlayer.musicPlayerStats is True:
                    blackPlayer.player.stop()
                    blackPlayer.musicPlayerStats = False
            else:
                print("Are you retard?")


if __name__ == "__main__":
    # execute only if run as a script
    musicPlayer = blackPlayer
    musicPlayer.main()
