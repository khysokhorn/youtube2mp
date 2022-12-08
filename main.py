from pytube import YouTube
import os
from pathlib import Path


def youtube2m3download(url, is_remove=False):
    yt = YouTube(url, on_progress_callback=a)
    video = yt.streams.filter(abr='160kbps').last()
    if not os.path.exists('video'):
        os.makedirs('video')
    out_file = video.download(output_path='video')
    base, ext = os.path.splitext(out_file)
    file_name = f'{base}.mp3'
    new_file = Path(file_name)
    os.rename(out_file, new_file)
    # @ Check success of download
    if new_file.exists():
        print(f'{yt.title} has been successfully downloaded.')
        if is_remove:
            os.remove(file_name)
        return file_name, yt.title, yt.description
    else:
        print(f'ERROR: {yt.title}could not be downloaded!')
        return '', '', ''


def a(b, c,  time):
    print(time)


# youtube2m3download('https://www.youtube.com/watch?v=0I5w0Xj_WCc')
