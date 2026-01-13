# AIForge 3D – Asisten AI untuk Blender

<p align="center">
  <img src="ui/icons/logo.png" alt="Logo AIForge 3D" width="128" height="128">
</p>

[![Versi](https://img.shields.io/badge/versi-1.3.1-blue.svg)](https://github.com/aiforge3d/blender-addon/releases)
[![Lisensi](https://img.shields.io/badge/lisensi-MIT-green.svg)](https://github.com/aiforge3d/blender-addon/blob/main/LICENSE)
[![Blender](https://img.shields.io/badge/Blender-4.0%2B-orange.svg)](https://www.blender.org/)
[![Discord](https://img.shields.io/badge/Discord-Gabung%20Komunitas-7289DA.svg)](https://discord.gg/dXAN23NwkM)

> **AIForge 3D** menghadirkan AI generatif langsung ke viewport 3D Blender, menawarkan chat real‑time, orkestrasi alat, dan agen spesialis untuk modeling, shading, animasi, dan lainnya.

🌐 **Bahasa:** [English](README.md) | **Bahasa Indonesia**

---

## 📖 Daftar Isi
- [🌟 Ikhtisar](#-ikhtisar)
- [✨ Fitur](#-fitur)
- [📦 Instalasi](#-instalasi)
- [🔑 Pengaturan API](#-pengaturan-api)
- [🚀 Mulai Cepat](#-mulai-cepat)
- [🖥️ Antarmuka Pengguna](#️-antarmuka-pengguna)
  - [Pemilih Agen](#pemilih-agen)
  - [Panel Chat & Streaming](#panel-chat--streaming)
  - [Panel Pengaturan](#panel-pengaturan)
- [🤖 Sistem Multi‑Agen](#-sistem-multiagen)
  - [Agen yang Tersedia](#agen-yang-tersedia)
  - [Mode Orkestrator](#mode-orkestrator)
- [💬 Contoh Penggunaan](#-contoh-penggunaan)
  - [Perintah Dasar](#perintah-dasar)
  - [Eksekusi Kode](#eksekusi-kode)
  - [Alur Kerja Lanjutan](#alur-kerja-lanjutan)
- [🔒 Keamanan Thread & Keamanan](#-keamanan-thread--keamanan)
- [📁 Arsitektur](#-arsitektur)
- [🛠️ Pengembangan](#️-pengembangan)
- [✅ Pengujian & CI](#-pengujian--ci)
- [❓ Pemecahan Masalah](#-pemecahan-masalah)
- [🤝 Berkontribusi](#-berkontribusi)
- [📄 Lisensi](#-lisensi)
- [🙌 Penghargaan](#-penghargaan)
- [📞 Dukungan](#-dukungan)

---

## 🌟 Ikhtisar

AIForge 3D adalah **add‑on Blender** yang mengintegrasikan backend model bahasa besar (MiniMax, OpenAI, dll.) untuk membantu seniman dan pengembang langsung di dalam Blender. Add‑on ini mengubah instruksi bahasa alami menjadi operasi Blender, memungkinkan Anda untuk:

- **Membuat objek 3D** menggunakan perintah bahasa Indonesia/Inggris sederhana
- **Memodifikasi scene** dengan transformasi, material, dan animasi
- **Menanyakan scene Anda** untuk informasi dan properti objek
- **Mengeksekusi kode Python** dengan aman dalam lingkungan sandbox
- **Mengorkestrasi alur kerja kompleks** menggunakan delegasi tugas bertenaga AI

---

## ✨ Fitur

### Kemampuan Inti
| Fitur | Deskripsi |
|-------|-----------|
| **Kontrol Bahasa Alami** | Buat, modifikasi, dan animasikan objek menggunakan bahasa sehari‑hari |
| **Respons Streaming** | Lihat respons AI secara real‑time saat dihasilkan |
| **Sistem Multi‑Agen** | Beralih antar agen spesialis (Modeler, Shading, Animator, Director) |
| **Mode Orkestrator** | Dekomposisi tugas tingkat tinggi dan delegasi otomatis |
| **Integrasi Alat** | Pencarian web, operasi file, dan tampilan hasil inline |
| **Eksekusi Kode** | Eksekusi Python sandbox yang aman dengan undo/rollback |
| **Rendering Markdown** | Teks kaya dengan blok kode, tabel, gambar, dan kutipan |

### Fitur Teknis
- **Thread‑safe** – Semua akses `bpy.context` melalui `bpy.app.timers.register`
- **Penyimpanan aman** – Kunci API terenkripsi di `WindowManager` Blender
- **UI auto‑resize** – Panel chat beradaptasi dengan konten secara dinamis
- **Indikator aktivitas** – Umpan balik visual selama pemrosesan AI
- **Logging ekstensif** – Output debug ke konsol sistem
- **CI/CD siap** – GitHub Actions untuk pengujian lintas platform

---

## 📦 Instalasi

### Persyaratan
| Komponen | Versi |
|----------|-------|
| Blender | **4.0** atau lebih tinggi |
| Kunci API | MiniMax atau OpenAI |
| OS | Windows, macOS, Linux |

### Langkah Instalasi

1. **Unduh add‑on**
   ```
   aiforge3d_v1.3.1.zip
   ```
   Dapatkan rilis terbaru dari [halaman Releases](https://github.com/aiforge3d/blender-addon/releases).

2. **Instal di Blender**
   - Buka Blender
   - Navigasi ke `Edit > Preferences > Add‑ons`
   - Klik **Install…**
   - Pilih file ZIP yang diunduh
   - Aktifkan checkbox **AIForge 3D**

3. **Restart Blender**
   - Tutup dan buka kembali Blender untuk inisialisasi penuh

4. **Verifikasi Instalasi**
   - Buka sidebar 3D Viewport (tekan `N`)
   - Cari tab **AIForge**

> 💡 **Tips:** Tekan `Ctrl+Alt+R` untuk memuat ulang UI tanpa restart Blender.

---

## 🔑 Pengaturan API

### Langkah 1: Dapatkan Kunci API

#### MiniMax (Direkomendasikan)
1. Kunjungi [api.minimaxi.com](https://api.minimaxi.com)
2. Buat akun
3. Navigasi ke bagian API Keys
4. Buat kunci API baru

#### OpenAI (Alternatif)
1. Kunjungi [platform.openai.com](https://platform.openai.com)
2. Buat akun
3. Buka API Keys
4. Buat secret key baru

### Langkah 2: Konfigurasi Add‑on
1. Buka Blender
2. Buka `View3D > Sidebar (N)` → tab **AIForge 3D**
3. Klik ikon **Pengaturan** (⚙️)
4. Tempel kunci API Anda di field **API Key**
5. Klik **Save** atau **Authenticate**

> 🔐 Kunci API Anda disimpan dengan aman dan terenkripsi secara lokal.

---

## 🚀 Mulai Cepat

### Interaksi Pertama Anda

1. **Buka panel AIForge** (Sidebar → tab **AIForge**)

2. **Pilih Agen** dari dropdown:
   - *Generalist* – Asisten serba guna
   - *Modeler* – Spesialis mesh dan topologi
   - *Shading* – Ahli material dan node
   - *Animator* – Spesialis keyframe dan gerakan
   - *Director* – Ahli pencahayaan dan kamera
   - *Orchestrator* – Koordinator tugas multi‑langkah

3. **Ketik prompt** di kotak teks:
   ```
   Buat kubus merah di titik origin
   ```

4. **Tekan Enter** atau klik **Send**

5. **Lihat respons** mengalir secara real‑time

6. **Lihat scene 3D Anda** diperbarui secara otomatis!

---

## 🖥️ Antarmuka Pengguna

### Pemilih Agen
<p align="center">
  <img src="assets/agent_selector.gif" alt="Pemilih Agen" width="400">
</p>

- **Lokasi:** Bagian atas panel AIForge
- **Fungsi:** Beralih antar agen AI spesialis
- **Sumber:** Dikonfigurasi di `llm/agent_prompts.py`
- **Properti:** Memperbarui properti scene `vibe4d_active_agent`

### Panel Chat & Streaming
- **Rendering markdown** dengan blok kode syntax‑highlighted
- **Gambar inline** (URL atau base64 encoded)
- **Tabel dan daftar** untuk data terstruktur
- **Auto‑resize** untuk menyesuaikan konten
- **Navigasi scroll** untuk percakapan panjang

### Panel Pengaturan
| Pengaturan | Deskripsi |
|------------|-----------|
| API Key | Kunci MiniMax/OpenAI Anda (terenkripsi) |
| Model | Pilih versi model AI |
| Custom Instructions | Tentukan aturan perilaku persisten |
| Theme | Toggle mode Terang/Gelap |

---

## 🤖 Sistem Multi‑Agen

### Agen yang Tersedia

| Agen | Spesialisasi | Terbaik Untuk |
|------|--------------|---------------|
| **Generalist** | Serba guna | Pertanyaan umum, tugas sederhana |
| **Modeler** | Mesh & Topologi | Membuat/mengedit geometri 3D |
| **Shading** | Material & Node | Tekstur, shader, setup node |
| **Animator** | Keyframe & Gerakan | Animasi, rigging, timing |
| **Director** | Pencahayaan & Kamera | Rendering, komposisi, pencahayaan |
| **Orchestrator** | Koordinasi Tugas | Alur kerja multi‑langkah kompleks |

### Mode Orkestrator

**Orkestrator** adalah meta‑agen yang dapat:

1. **Mendekomposisi** tugas kompleks menjadi subtugas
2. **Mendelegasikan** ke agen spesialis secara otomatis
3. **Mengkoordinasikan** hasil lintas operasi
4. **Mensintesis** respons komprehensif akhir

#### Contoh Prompt Orkestrator:
```
Desain interior pesawat luar angkasa sci‑fi dengan:
- Kokpit detail dengan panel kontrol
- Material aluminium brushed metalik
- Lampu berkedip animasi
- Pencahayaan spotlight dramatis
```

Orkestrator akan secara otomatis:
- Menggunakan **Modeler** untuk geometri
- Menggunakan **Shading** untuk material
- Menggunakan **Animator** untuk animasi lampu
- Menggunakan **Director** untuk setup pencahayaan

---

## 💬 Contoh Penggunaan

### Perintah Dasar

#### Membuat Objek
```
Buat kubus di (0, 0, 0)
Tambahkan sphere UV dengan radius 2 di lokasi (5, 0, 0)
Buat torus dengan major_radius=3, minor_radius=0.5
Buat silinder dengan depth=4 dan radius=1
```

#### Query Scene
```
Daftar semua objek di scene
Tampilkan semua objek mesh
Berapa lokasi Camera?
Berapa jumlah vertex pada Cube?
```

#### Transformasi
```
Pindahkan kubus ke (0, 0, 2)
Rotasi sphere 45 derajat pada sumbu Z
Scale semua objek terpilih menjadi 0.5
Mirror mesh sepanjang sumbu X
```

#### Material
```
Buat material merah glossy bernama "Ruby"
Assign material Ruby ke Cube
Buat material kaca dengan IOR 1.45
Buat sphere memancarkan cahaya biru
```

#### Animasi
```
Sisipkan keyframe di frame 1 untuk lokasi
Animasikan kubus dari (0,0,0) ke (0,0,5) selama 100 frame
Set timeline ke frame 50
Buat animasi memantul untuk sphere
```

#### Rendering
```
Capture viewport saat ini
Ambil screenshot dari kamera aktif
Render scene di 1920x1080
Setup rig pencahayaan 3 titik
```

### Eksekusi Kode

Eksekusi kode Python secara langsung:
```python
import bpy

# Buat grid kubus
for x in range(5):
    for y in range(5):
        bpy.ops.mesh.primitive_cube_add(
            size=0.8,
            location=(x * 2, y * 2, 0)
        )
```

### Alur Kerja Lanjutan

#### Lanskap Prosedural
```
Buat lanskap gunung prosedural dengan:
- Plane tersubdivisi dengan displacement
- Material berbatu dengan variasi
- Partikel rumput di area datar
- Kabut atmosfer
```

#### Setup Karakter
```
Setup karakter biped dasar:
- Buat armature dengan spine, lengan, dan kaki
- Tambahkan constraint IK untuk kaki dan tangan
- Buat control shape untuk animator
```

---

## 🔒 Keamanan Thread & Keamanan

### Keamanan Thread
- Semua akses **`bpy.context`** terjadi di main thread
- Operasi background menggunakan `bpy.app.timers.register`
- Kunci API diekstrak di main thread, diteruskan ke worker
- Penanganan error mencegah kegagalan diam

### Keamanan Kunci API
- Kunci disimpan terenkripsi di `WindowManager`
- Tidak pernah ditransmisikan kecuali ke endpoint API
- Tidak termasuk dalam file scene atau ekspor
- Dapat dihapus melalui panel Pengaturan

### Keamanan Eksekusi Kode
- Lingkungan Python sandbox
- Dukungan undo untuk semua operasi
- Capture dan tampilan error
- Tidak ada akses level sistem

---

## 📁 Arsitektur

```
aiforge3d/
├── __init__.py           # Entry point utama addon
├── api/
│   └── client.py         # Wrapper HTTP, header, penanganan error
├── auth/
│   └── manager.py        # Autentikasi dan penyimpanan kredensial
├── llm/
│   ├── agent_prompts.py  # Definisi agen spesialis
│   ├── chat_client.py    # Handler streaming background
│   └── response_handler.py # Parsing respons, panggilan alat
├── operators/
│   └── *.py              # Definisi operator Blender
├── tools/
│   ├── definitions.py    # Skema alat untuk AI
│   ├── executor.py       # Engine eksekusi alat
│   └── helpers.py        # Fungsi utilitas
├── ui/
│   ├── manager.py        # Orkestrasi UI, timer
│   ├── ui_factory.py     # Pembuatan dan manajemen view
│   ├── components/
│   │   ├── agent_selector.py    # Dropdown agen
│   │   ├── markdown_message.py  # Rendering teks kaya
│   │   └── *.py                 # Komponen UI lainnya
│   └── views/
│       ├── main_view.py  # Antarmuka chat utama
│       └── auth_view.py  # View login/pengaturan
├── utils/
│   ├── error_utils.py    # Helper penanganan error
│   ├── history_manager.py # Persistensi percakapan
│   └── secure_storage.py # Penyimpanan kunci terenkripsi
└── external/             # Library pihak ketiga
```

### Tanggung Jawab Modul Utama

| Modul | Tanggung Jawab |
|-------|----------------|
| `api/client.py` | HTTP level rendah, header autentikasi |
| `llm/chat_client.py` | Streaming thread background |
| `llm/response_handler.py` | Parse respons, handle panggilan alat |
| `ui/manager.py` | Koordinasi update UI via timer Blender |
| `ui/components/markdown_message.py` | Render markdown dengan auto‑resize |

---

## 🛠️ Pengembangan

### Setup Lingkungan Pengembangan

```bash
# Clone repository
git clone https://github.com/aiforge3d/blender-addon.git
cd blender-addon

# Instal dependensi (menggunakan Python Blender)
blender --background --python - <<PY
import sys, subprocess, pathlib
sys.path.append(str(pathlib.Path('.').resolve()))
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
PY
```

### Menjalankan Test

```bash
# Jalankan semua unit test
blender --background --python -m unittest discover -s tests

# Jalankan file test tertentu
blender --background --python -m unittest tests.test_chat_client
```

### Membangun ZIP Release

```powershell
# PowerShell
Compress-Archive -Path 'aiforge3d' -DestinationPath 'aiforge3d_latest.zip' -Force
```

```bash
# Bash/Linux
zip -r aiforge3d_latest.zip aiforge3d/
```

### Gaya Kode
- Ikuti panduan PEP 8
- Gunakan type hint jika memungkinkan
- Dokumentasikan fungsi publik dengan docstring
- Jalankan `flake8` sebelum commit

---

## ✅ Pengujian & CI

### Cakupan Test
| Area | Cakupan |
|------|---------|
| Chat Client | Unit test untuk streaming, penanganan error |
| Response Handler | Parsing panggilan alat, logika kelanjutan |
| Komponen UI | Rendering, resizing, penanganan event |
| API Client | Pembuatan request, parsing respons |

### Continuous Integration
- **GitHub Actions** berjalan di setiap push dan PR
- Test di Windows, macOS, dan Linux
- Beberapa versi Blender (4.0, 4.1, 4.2)
- Linting dengan `flake8`
- Pengecekan tipe dengan `mypy`

---

## ❓ Pemecahan Masalah

### Masalah Umum

| Gejala | Penyebab | Solusi |
|--------|----------|--------|
| Tidak ada respons | Kunci API tidak valid/hilang | Masukkan ulang kunci di Pengaturan |
| UI freeze | Masalah registrasi timer | Tekan `Ctrl+Alt+R` atau restart Blender |
| Gambar tidak loading | URL tidak dapat diakses | Periksa aksesibilitas URL; gunakan base64 untuk gambar lokal |
| Streaming berhenti | Gangguan jaringan | Periksa internet; coba ulang prompt |
| "Thinking" tidak selesai | Timeout API | Tingkatkan timeout di pengaturan; coba ulang |

### Melihat Log
1. Buka **Window > Toggle System Console** (Windows) atau jalankan Blender dari terminal (macOS/Linux)
2. Cari pesan dengan awalan `[AIForge]`
3. Aktifkan verbose logging di Pengaturan jika diperlukan

### Mereset Add‑on
1. Nonaktifkan add‑on di Preferences
2. Hapus folder add‑on secara manual
3. Restart Blender
4. Instal ulang dari ZIP

---

## 🤝 Berkontribusi

Kami menyambut kontribusi! Berikut caranya:

### Memulai
1. **Fork** repository
2. **Clone** fork Anda secara lokal
3. **Buat** branch fitur
   ```bash
   git checkout -b feature/fitur-keren
   ```
4. **Buat** perubahan Anda
5. **Test** secara menyeluruh
6. **Commit** dengan pesan jelas
   ```bash
   git commit -m "Tambah fitur keren yang melakukan X"
   ```
7. **Push** ke fork Anda
8. **Buka** Pull Request

### Panduan
- Ikuti gaya kode yang ada
- Tulis test untuk fitur baru
- Perbarui dokumentasi sesuai kebutuhan
- Jaga PR tetap fokus dan atomik
- Bersikap sopan dalam diskusi

Lihat `CONTRIBUTING.md` untuk detail lengkap.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah **Lisensi MIT**.

```
MIT License

Copyright (c) 2024 Tim AIForge

Izin dengan ini diberikan, secara gratis, kepada siapa pun yang memperoleh salinan
perangkat lunak ini dan file dokumentasi terkait ("Perangkat Lunak"), untuk berurusan
dengan Perangkat Lunak tanpa batasan, termasuk tanpa batasan hak
untuk menggunakan, menyalin, memodifikasi, menggabungkan, menerbitkan, mendistribusikan, mensublisensikan, dan/atau menjual
salinan Perangkat Lunak, dan untuk mengizinkan orang yang kepadanya Perangkat Lunak
diberikan untuk melakukannya, dengan tunduk pada ketentuan berikut:

Pemberitahuan hak cipta di atas dan pemberitahuan izin ini harus disertakan dalam semua
salinan atau bagian substansial dari Perangkat Lunak.

PERANGKAT LUNAK INI DISEDIAKAN "SEBAGAIMANA ADANYA", TANPA JAMINAN APA PUN, TERSURAT MAUPUN
TERSIRAT, TERMASUK TETAPI TIDAK TERBATAS PADA JAMINAN KELAYAKAN JUAL,
KESESUAIAN UNTUK TUJUAN TERTENTU DAN KETIADAAN PELANGGARAN. DALAM HAL APA PUN
PENULIS ATAU PEMEGANG HAK CIPTA TIDAK BERTANGGUNG JAWAB ATAS KLAIM, KERUSAKAN ATAU
KEWAJIBAN LAINNYA, BAIK DALAM TINDAKAN KONTRAK, PERBUATAN MELAWAN HUKUM ATAU LAINNYA, YANG TIMBUL DARI,
KELUAR DARI ATAU SEHUBUNGAN DENGAN PERANGKAT LUNAK ATAU PENGGUNAAN ATAU URUSAN LAINNYA DALAM
PERANGKAT LUNAK.
```

---

## 🙌 Penghargaan

- **MiniMax** – Untuk menyediakan API LLM yang powerful
- **OpenAI** – Untuk dukungan model alternatif
- **Blender Foundation** – Untuk platform 3D yang luar biasa
- **Kontributor Komunitas** – Untuk testing, feedback, dan kontribusi kode

---

## 📞 Dukungan

Butuh bantuan? Hubungi melalui channel berikut:

| Channel | Link |
|---------|------|
| 💬 Discord | [Gabung komunitas kami](https://discord.gg/dXAN23NwkM) |
| 🌐 Website | [aiforge3d.com](https://aiforge3d.com) |
| 🐛 Issues | [GitHub Issues](https://github.com/aiforge3d/blender-addon/issues) |
| 📧 Email | support@aiforge3d.com |

---

<p align="center">
  <strong>Dibuat dengan ❤️ oleh Tim AIForge</strong>
</p>

<p align="center">
  <a href="#aiforge-3d--asisten-ai-untuk-blender">⬆️ Kembali ke Atas</a>
</p>
