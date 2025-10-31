import yt_dlp
import traceback

def download_youtube_video(url):
    """
    Mengunduh video YouTube dengan resolusi video terbaik dan audio terbaik,
    lalu menggabungkannya ke dalam satu file MP4.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s [%(resolution)s].%(ext)s',
        

        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        'noplaylist': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Mencari informasi video...")
            ydl.download([url])
            print("\n✅ Selesai Mengunduh!")
            
    except Exception as e:
        print("\n❌ Terjadi kesalahan:")

        print(traceback.format_exc())

if __name__ == "__main__":
    video_url = input("Masukkan Link YouTube: ")
    if video_url:
        download_youtube_video(video_url)
    else:
        print("URL tidak boleh kosong.")
