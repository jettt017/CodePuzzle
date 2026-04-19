# 24-Puzzle Solver dengan A* dan H1 Heuristic

Aplikasi web interaktif untuk menyelesaikan puzzle 5x5 (24-Puzzle) menggunakan algoritma A* dengan heuristik H1 (Misplaced Tiles).

## 📋 Fitur

- ✅ **Input Manual**: Masukkan puzzle secara manual melalui web interface
- ✅ **Preset Puzzles**: Pilih dari preset yang tersedia (Easy, Medium, Hard, Random)
- ✅ **Validasi Puzzle**: Cek apakah puzzle dapat diselesaikan sebelum mencari solusi
- ✅ **A* Solver**: Algoritma A* dengan heuristik H1 untuk mencari solusi optimal
- ✅ **Visualisasi Solusi**: Lihat setiap langkah solusi dalam bentuk visual grid
- ✅ **Statistik**: Tampilkan jumlah langkah, H1 value, dan status solvable
- ✅ **Responsive Design**: Interface yang responsif untuk desktop dan mobile

## 🛠️ Instalasi

### Prerequisites
- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Setup

1. **Clone atau download project ini**
   ```bash
   cd d:\0.SEMESTER 4\CodePuzzle
   ```

2. **Buat virtual environment (opsional tapi recommended)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Menjalankan Aplikasi

1. **Jalankan Flask app**
   ```bash
   python app.py
   ```

2. **Buka browser dan akses**
   ```
   http://localhost:5000
   ```

3. **Gunakan aplikasi**
   - Masukkan puzzle atau pilih preset
   - Klik "Validasi" untuk cek apakah puzzle dapat diselesaikan
   - Klik "Cari Solusi" untuk mencari solusi menggunakan A*
   - Lihat visualisasi setiap langkah solusi

## 📁 Struktur Project

```
CodePuzzle/
├── app.py                 # Flask backend
├── puzzle_solver.py       # Logika A* dan puzzle
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html        # Web interface
└── README.md             # File ini
```

## 📖 Cara Penggunaan

### Input Manual
- Klik pada kotak untuk mengubah nilainya
- Gunakan angka 1-24 untuk tiles dan 0 untuk blank
- Klik "Validasi" untuk mengecek apakah puzzle dapat diselesaikan

### Preset
Pilih salah satu preset:
- **Easy**: Puzzle yang dapat diselesaikan dalam 1 langkah
- **Medium**: Puzzle yang memerlukan ~5 langkah
- **Hard**: Puzzle yang memerlukan ~10 langkah
- **Random**: Puzzle acak yang dapat diselesaikan

### Solving
- Klik "Cari Solusi" untuk menjalankan algoritma A*
- Aplikasi akan menampilkan:
  - Total langkah yang diperlukan
  - H1 value dari state awal
  - Visualisasi setiap langkah
- Klik pada setiap step untuk melihat detailnya

## 🔧 API Endpoints

### POST `/api/solve`
Mencari solusi untuk puzzle

**Request:**
```json
{
  "initial_state": [1, 2, 3, ..., 24, 0]
}
```

**Response (Success):**
```json
{
  "success": true,
  "solution_path": [[...], [...], ...],
  "steps": 15,
  "h1_initial": 10,
  "goal_state": [1, 2, 3, ..., 24, 0]
}
```

### POST `/api/validate`
Validasi apakah puzzle dapat diselesaikan

**Request:**
```json
{
  "initial_state": [1, 2, 3, ..., 24, 0]
}
```

**Response:**
```json
{
  "valid": true,
  "solvable": true,
  "h1_value": 10,
  "message": "Puzzle dapat diselesaikan"
}
```

### GET `/api/goal-state`
Mendapatkan goal state

**Response:**
```json
{
  "goal_state": [1, 2, 3, ..., 24, 0]
}
```

## 🧮 Algoritma

### A* Search
```
f(n) = g(n) + h(n)

Dimana:
- g(n) = biaya dari start ke node n
- h(n) = heuristik yang memperkirakan biaya dari n ke goal
- f(n) = estimasi total biaya solusi melalui n
```

### H1 Heuristic (Misplaced Tiles)
```
H1(state) = jumlah tiles yang tidak di posisi goal (abaikan blank)
```

## 📊 Kompleksitas

- **Waktu Kompleksitas**: O(N log N) untuk A* search
- **Space Kompleksitas**: O(N) untuk closed set dan priority queue
- **Puzzle Board Size**: 5x5 (25 tiles)

## ⚙️ Solvability Check

Untuk puzzle 5x5 (ukuran ganjil):
- **Solvable**: Jika jumlah inversi (banyaknya pasangan tiles yang urutan tertukarnya) adalah genap

```
Inversi = banyaknya (i, j) dimana i < j dan arr[i] > arr[j]
```

## 🎨 Interface Features

- **Real-time Validation**: Input puzzle dan langsung validasi solvability-nya
- **Interactive Grid**: Klik untuk edit nilai tiles
- **Step-by-Step Visualization**: Lihat solusi step demi step
- **Responsive Design**: Nyaman digunakan di desktop dan mobile
- **Dark Theme Option**: Interface dengan color scheme modern

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
Solusi: Install dependencies dengan `pip install -r requirements.txt`

### "Address already in use: port 5000"
Solusi: 
- Ubah port di `app.py` line: `app.run(port=5001)`
- Atau close aplikasi yang sudah pakai port 5000

### Puzzle tidak bisa diselesaikan
Solusi: Cek dengan klik "Validasi", puzzle mungkin unsolvable (jumlah inversi ganjil)

## 📝 Contoh Penggunaan

1. Buka http://localhost:5000
2. Pilih "Preset" → "Easy (1 langkah)"
3. Klik "Cari Solusi"
4. Lihat visualisasi solusi yang muncul

## 📄 License

Proyek ini dibuat untuk keperluan akademik.

## 👤 Author

Dibuat untuk Code Puzzle Challenge

---

**Happy Puzzling!** 🧩
