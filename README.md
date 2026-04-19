# 24-Puzzle Solver

**Sebuah aplikasi web interaktif untuk menyelesaikan puzzle 5×5 menggunakan algoritma A* Search dengan heuristik H1.**

![Build Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-2.3.3-lightblue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 Daftar Isi
- [Fitur Utama](#fitur-utama)
- [Tech Stack](#tech-stack)
- [Instalasi](#instalasi)
- [Cara Menggunakan](#cara-menggunakan)
- [Deployment](#deployment)
- [Struktur Proyek](#struktur-proyek)
- [Tim Pengembang](#tim-pengembang)
- [Referensi](#referensi)

---

## ✨ Fitur Utama

### 1. **Interactive Puzzle Solver**
- Interface 5×5 puzzle yang intuitif
- Input manual konfigurasi puzzle
- Validasi solvability puzzle secara real-time
- Visualization step-by-step solusi

### 2. **A* Search Algorithm**
- Implementasi optimal A* Search
- Heuristik H1 (Misplaced Tiles)
- Cost tracking dan node exploration monitoring
- Performa optimal untuk hard cases

### 3. **Educational Content**
- Halaman algoritma dengan penjelasan detail
- Formula evaluasi f(n) = g(n) + h(n)
- Pseudocode dan analisis kompleksitas
- Perbandingan A* vs Uniform-Cost Search

### 4. **Responsive Design**
- Mobile-friendly dengan hamburger menu
- Dark theme konsisten
- Grid pattern background aesthetic
- Breakpoints: 768px, 480px optimization

### 5. **Multi-Page Architecture**
- **Home**: Puzzle solver interactive
- **Algoritma**: Penjelasan A* & H1 detail
- **Tentang**: Project context & references
- **Kontak**: Team members & communication

---

## 🛠️ Tech Stack

### Backend
- **Flask** 2.3.3 - Web framework
- **Python** 3.8+ - Language
- **Gunicorn** 22.0.0 - Production WSGI server

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Dark theme styling dengan CSS variables
- **Vanilla JavaScript** - No frameworks, pure logic
- **Canvas Confetti** - Celebration animation

### Algorithm
- **A* Search** - Optimal pathfinding
- **H1 Heuristic** - Misplaced tiles estimation
- Time Complexity: O(b^d) worst case
- Space Complexity: O(b^d) for open/closed sets

---

## 📦 Instalasi

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Langkah-Langkah

#### 1. Clone Repository
```bash
git clone https://github.com/gamely017/CodePuzzle.git
cd CodePuzzle
```

#### 2. Setup Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run Locally
```bash
python app.py
```

Server akan berjalan di `http://localhost:5000`

---

## 🎮 Cara Menggunakan

### Input Puzzle Manual
1. Buka halaman **Home**
2. Klik tab **"Manual"** di bagian Input
3. Klik sel untuk mengubah nilai (1-24 untuk ubin, 0 untuk blank)
4. Klik **"Validasi"** untuk cek solvability
5. Klik **"Solve"** untuk mencari solusi

### Input Preset
1. Pilih tab **"Preset"** 
2. Pilih salah satu level: Easy, Medium, Hard
3. Klik **"Solve"** langsung

### Visualisasi Solusi
- Lihat step-by-step perubahan puzzle
- Klik step untuk melihat state tertentu
- Info H1 value & solve time di header
- Status & metrics di panel kanan

### Navigasi Halaman
- **Home**: Solver utama
- **Algoritma**: Penjelasan A* & complexity analysis
- **Tentang**: Project overview & references
- **Kontak**: Team members & documentation

---

## 🚀 Deployment

### Deploy ke Render (Free Tier)

#### 1. Push ke GitHub
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

#### 2. Setup di Render Dashboard
1. Login ke [render.com](https://render.com)
2. Klik **"New Web Service"**
3. Connect GitHub repository
4. Configure form:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance**: Free tier (512 MB RAM, 0.5 CPU)
5. Klik **"Create Web Service"**

#### 3. Deployment Selesai
- URL: `https://codepuzzle-xxx.onrender.com`
- Auto-sleep: Setelah 15 min inactivity (free tier default)
- Health check: Automatic setiap 5 menit

### Environment Variables
Jika perlu, set di Render dashboard:
```
FLASK_ENV=production
```

---

## 📁 Struktur Proyek

```
CodePuzzle/
├── app.py                 # Flask main application
├── puzzle_solver.py       # A* algorithm implementation
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── README.md             # Documentation
│
├── templates/
│   ├── index.html        # Home page + puzzle solver
│   ├── algorithm.html    # Algorithm explanation
│   ├── about.html        # Project context
│   └── contact.html      # Team members & contact
│
└── static/
    └── (CSS embedded di templates)
```

### File Descriptions

**app.py**
- 4 routes: /, /algorithm, /about, /contact
- 3 API endpoints: /api/solve, /api/validate, /api/goal-state
- GOAL_STATE hardcoded: (1,2,3,...,24,0)

**puzzle_solver.py**
- `a_star()` - Main A* implementation
- `is_solvable()` - Check puzzle solvability
- `h1_misplaced_tiles()` - Heuristic function
- `get_neighbors()` - Generate next states

**index.html**
- 5×5 grid input interface
- Manual & Preset modes
- Solution visualization
- Responsive hamburger menu (mobile)

**algorithm.html**
- f(n) = g(n) + h(n) explanation
- H1 heuristic detail
- A* pseudocode
- Complexity analysis & performance table

**about.html**
- Project overview
- References list
- Space state calculation (25!/2)
- Algorithm statistics

**contact.html**
- Email & GitHub links
- Team members (2×2 grid)
- Setup instructions
- NPM info untuk setiap member

---

## 👥 Tim Pengembang

| Peran | Nama | NPM | Role |
|-------|------|-----|------|
| **Ketua** | Gani Abi Saputra Van Sigu | 24081010033 | Project Lead |
| **Anggota 1** | Sendy Luis Armando | 24081010102 | Backend Dev |
| **Anggota 2** | Ratna Yuliana Triyono | 24081010052 | Frontend Dev |
| **Anggota 3** | Natasya Jollyn Karisya Agustin | 24081010181 | QA/Testing |

---

## 📚 Referensi

1. **Nilsson, N. J.** (1980). *Principles of Artificial Intelligence*. Morgan Kaufmann.

2. **Russell, S. J., & Norvig, P.** (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.

3. **Wikipedia: A* search algorithm**
   - https://en.wikipedia.org/wiki/A*_search_algorithm

4. **Wikipedia: 15 puzzle / n-puzzle**
   - https://en.wikipedia.org/wiki/15_puzzle

### Key Concepts
- **A* Search**: Optimal pathfinding dengan f(n) = g(n) + h(n)
- **Heuristic H1**: Jumlah ubin salah posisi (admissible & consistent)
- **State Space**: 25!/2 ≈ 1.24 × 10²⁴ possible configurations
- **Branching Factor**: Max 4 (Up, Down, Left, Right)

---

## 📝 Lisensi

Project ini dilisensikan di bawah **MIT License**. Bebas untuk digunakan, dimodifikasi, dan didistribusikan.

---

## 🤝 Kontribusi

Untuk kontribusi atau bug reports, silakan:
1. Fork repository
2. Buat branch feature (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📧 Support & Questions

Untuk pertanyaan atau bantuan:
- **Email**: gamely017@gmail.com
- **GitHub**: [gamely017/CodePuzzle](https://github.com/gamely017/CodePuzzle)
- **Deployed**: [codepuzzle.onrender.com](https://codepuzzle.onrender.com)

---

## 🎯 Roadmap (Future Features)

- [ ] Save/Load puzzle state
- [ ] Step-by-step tutorial
- [ ] Statistics tracking
- [ ] Leaderboard (hardest puzzles solved)
- [ ] Dark/Light theme toggle
- [ ] Offline PWA support
- [ ] Multi-language support

---

**Last Updated**: April 20, 2026  
**Status**: Active Development  
**Version**: 1.0.0

---

*Built with ❤️ by Kelompok 4*