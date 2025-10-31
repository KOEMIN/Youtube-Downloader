import yt_dlp
import traceback

def download_youtube_video(url):
    """
    Mengunduh video YouTube dengan resolusi video terbaik dan audio terbaik,
    lalu menggabungkannya ke dalam satu file MP4.
    """
    ydl_opts = {
        # 1. 'bestvideo+bestaudio/best':
        #    - Mencari video kualitas terbaik DAN audio kualitas terbaik, lalu menggabungkannya.
        #    - '/best' adalah fallback jika tidak ada stream terpisah.
        'format': 'bestvideo+bestaudio/best',
        
        # 2. 'outtmpl':
        #    - Menentukan format nama file yang akan disimpan.
        #    - Contoh: "Judul Video [1080p].mp4"
        'outtmpl': '%(title)s [%(resolution)s].%(ext)s',
        
        # 3. 'postprocessors':
        #    - Perintah yang dijalankan setelah download selesai.
        #    - Di sini kita memberitahu yt-dlp untuk menggabungkan video dan audio ke format mp4.
        #    - Membutuhkan ffmpeg untuk bekerja.
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
        # Mencetak detail error untuk debugging
        print(traceback.format_exc())

if __name__ == "__main__":
    video_url = input("Masukkan Link YouTube: ")
    if video_url:
        download_youtube_video(video_url)
    else:
        print("URL tidak boleh kosong.")