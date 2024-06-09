# blackPlayer

## Overview

`black-player` is a Python script designed to download audio from YouTube videos and play them using VLC. This script automates the process of downloading YouTube audio, organizing it into a playlist, and playing it back.

## Backstory

I created this script when I was young and broke (around 14 or 15 years old). I couldn't afford Spotify, so I decided to make my own music player. This script downloads entire YouTube playlists, saves the music in a folder, and uses VLC as a backend to play them.

## Features

- **Download YouTube Audio**: Downloads the best quality audio from YouTube videos.
- **Playlist Creation**: Automatically organizes downloaded audio files into a playlist.
- **Music Playback**: Plays the downloaded music using VLC.

## Requirements

- **VLC Media Player**: Install VLCx86 and ensure it's located in "C:\VLC".
- **FFmpeg**: Ensure FFmpeg is installed in "C:".
- **Python Libraries**: The script uses `youtube_dl`, `vlc`, `os`, `threading`, and `time`.

## Setup

1. **Install VLC**:

   - Download and install VLC Media Player (x86 version).
   - Ensure VLC is located in `C:\VLC`.

2. **Install FFmpeg**:

   - Download and install FFmpeg.
   - Ensure FFmpeg is located in `C:\`.

3. **Python Libraries**:

   - Install the required Python libraries:
     ```sh
     pip install youtube-dl python-vlc
     ```

4. **Directory Setup**:
   - Create a directory named `myMusic` in the script's root directory to store the downloaded audio files.

## Usage

1. **Run the Script**:

   - Execute the script:
     ```sh
     python black-player.py
     ```

2. **Main Menu**:
   - The script presents a menu with three options:
     1. **Download some shit**: Prompts you to enter a YouTube link to download audio.
     2. **Let's start your shitty playlist**: Starts playing the downloaded music.
     3. **Stop this fucking noise**: Stops the currently playing music.

## Notes

- This script was written when I was young and learning to code. It may not be well-structured or efficient.
- The script might not work with the latest versions of Python or the mentioned libraries.
- Use at your own risk.

## Disclaimer

This script is a product of my teenage coding efforts. It served its purpose back then but may require updates to work with current software versions. Feel free to modify and improve it as needed.
