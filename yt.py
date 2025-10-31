import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]',
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Mengunduh...")
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Masukkan Link YouTube: ")
    download_youtube_video(video_url)
    print("Selesai Mengunduh!")