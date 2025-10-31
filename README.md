# YouTube Video Downloader 🚀

Ini adalah sebuah script Python sederhana untuk mengunduh video dari YouTube dengan resolusi tertinggi yang tersedia. Script ini menggunakan `yt-dlp` untuk mengambil stream video dan audio terbaik secara terpisah, lalu menggabungkannya secara otomatis menggunakan `FFmpeg`.

## ✨ Fitur Utama

-   **Kualitas Terbaik**: Otomatis mengunduh resolusi video tertinggi (termasuk 1440p, 4K) dan audio terbaik yang tersedia.
-   **Penggabungan Otomatis**: Video dan audio yang terpisah akan digabungkan menjadi satu file MP4.
-   **Format Nama File**: File yang diunduh akan disimpan dengan format yang rapi: `Judul Video [Resolusi].mp4`.
-   **Sederhana**: Cukup jalankan script, masukkan URL, dan biarkan prosesnya berjalan.

---

## ⚙️ Kebutuhan Sistem (Prerequisites)

Sebelum menjalankan proyek ini, pastikan komputermu sudah memiliki:

1.  **Python 3.8+**
    -   Pastikan saat menginstal Python di Windows, kamu mencentang opsi **"Add Python to PATH"**.

2.  **FFmpeg**
    -   Ini **wajib** ada agar script bisa menggabungkan file video dan audio.
    -   **Cara Instal FFmpeg:**
        -   **Windows (via PowerShell):**
            ```powershell
            # Menggunakan Scoop (rekomendasi)
            scoop install ffmpeg
            # Atau menggunakan Chocolatey
            choco install ffmpeg
            ```
        -   **macOS (via Homebrew):**
            ```bash
            brew install ffmpeg
            ```
        -   **Linux (Debian/Ubuntu):**
            ```bash
            sudo apt update && sudo apt install ffmpeg
            ```

---

## 📋 Panduan Instalasi & Penggunaan

Ikuti langkah-langkah berikut untuk menjalankan script:

**1. Clone Repository Ini**
Buka terminal atau Git Bash, lalu jalankan:
```bash
git clone [https://github.com/KOEMIN/Youtube-Downloader.git](https://github.com/KOEMIN/Youtube-Downloader.git)
````

**2. Masuk ke Direktori Proyek**

```bash
cd Youtube-Downloader
```

**3. Buat File `requirements.txt`**
Buat sebuah file baru bernama `requirements.txt` di dalam folder proyek dan isi dengan teks berikut:

```txt
yt-dlp
```

**4. Buat dan Aktifkan Virtual Environment (Sangat Direkomendasikan)**
Ini akan menjaga dependensi proyekmu tetap terisolasi.

```bash
# Membuat environment
python -m venv .venv

# Mengaktifkan environment
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

**5. Install Dependensi Python**
Jalankan perintah ini untuk menginstal `yt-dlp` yang ada di file `requirements.txt`.

```bash
pip install -r requirements.txt
```

-----

## ▶️ Cara Menjalankan Script

1.  Pastikan virtual environment kamu sudah aktif (akan ada tulisan `(.venv)` di awal baris terminalmu).
2.  Jalankan script `yt.py`:
    ```bash
    python yt.py
    ```
3.  Saat diminta, masukkan URL video YouTube yang ingin kamu unduh, lalu tekan **Enter**.
4.  Tunggu hingga proses unduh dan penggabungan selesai. File video akan muncul di folder yang sama dengan script-mu.

<!-- end list -->

```

```
