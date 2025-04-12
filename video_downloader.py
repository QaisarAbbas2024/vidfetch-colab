!pip install yt-dlp
import yt_dlp
import os
import subprocess

def download_facebook_video(url):
    video_filename = None  # Will store final downloaded file name

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': True,
        'progress_hooks': [lambda d: set_video_filename(d)],
    }

    def set_video_filename(d):
        nonlocal video_filename
        if d['status'] == 'finished':
            video_filename = d['filename']

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if video_filename:
        print(f"Downloaded: {video_filename}")
        # Try to open with Chrome
        try:
            subprocess.run(['google-chrome', video_filename], check=True)
        except FileNotFoundError:
            print("Google Chrome not found. Please make sure it's installed and on your system PATH.")
        except Exception as e:
            print("Error opening in Chrome:", e)

def download_videos_from_list(url_list):
    for url in url_list:
        download_facebook_video(url)

# Example usage:
video_urls = [
"https://www.facebook.com/iCodeguru/videos/669248146050460"]

download_videos_from_list(video_urls)
