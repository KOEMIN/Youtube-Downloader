from pytube import YouTube
link = input("Masukkan Link YouTube: ")
yt = YouTube(link)
    
print(f"Mengunduh")
downloader = yt.streams.get_highest_resolution()
    
downloader.download(output_path=".", filename="Video_Download.mp4")
print("Selesai Mengunduh!")