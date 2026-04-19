import heapq
from typing import List, Tuple, Dict, Optional

# =========================
# KONFIGURASI UMUM
# =========================
N = 5  # 5x5 board untuk 24-puzzle
BLANK = 0

State = Tuple[int, ...]


# =========================
# UTILITAS STATE
# =========================
def print_board(state: State) -> None:
    """Menampilkan papan 5x5 dengan rapi."""
    for i in range(N):
        row = state[i * N:(i + 1) * N]
        print(" ".join(f"{x:2d}" if x != BLANK else "  " for x in row))
    print()


def is_solvable(state: State) -> bool:
    """
    Mengecek apakah state solvable.
    Untuk puzzle ukuran ganjil (5x5), state solvable jika jumlah inversi genap.
    """
    arr = [x for x in state if x != BLANK]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions % 2 == 0


def get_neighbors(state: State) -> List[State]:
    """Menghasilkan semua state tetangga dari perpindahan blank 1 langkah."""
    zero_idx = state.index(BLANK)
    r, c = divmod(zero_idx, N)

    neighbors = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # atas, bawah, kiri, kanan

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            swap_idx = nr * N + nc
            new_state = list(state)
            new_state[zero_idx], new_state[swap_idx] = new_state[swap_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors


# =========================
# HEURISTIK H1
# =========================
def h1_misplaced_tiles(state: State, goal: State) -> int:
    """
    H1: jumlah keping yang salah posisi, abaikan blank (0).
    """
    return sum(1 for i in range(len(state)) if state[i] != BLANK and state[i] != goal[i])


# =========================
# A* SEARCH
# =========================
def reconstruct_path(came_from: Dict[State, State], current: State) -> List[State]:
    """Membangun jalur solusi dari goal ke start."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def a_star(start: State, goal: State) -> Optional[List[State]]:
    """
    Algoritma A* dengan heuristik H1.
    Menggunakan priority queue berdasarkan f(n)=g(n)+h(n).
    """
    open_heap = []
    heapq.heappush(open_heap, (h1_misplaced_tiles(start, goal), 0, start))

    came_from: Dict[State, State] = {}
    g_score: Dict[State, int] = {start: 0}
    closed_set = set()

    while open_heap:
        f_current, g_current, current = heapq.heappop(open_heap)

        if current in closed_set:
            continue
        closed_set.add(current)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g = g_current + 1

            if neighbor in closed_set and tentative_g >= g_score.get(neighbor, float("inf")):
                continue

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_neighbor = tentative_g + h1_misplaced_tiles(neighbor, goal)
                heapq.heappush(open_heap, (f_neighbor, tentative_g, neighbor))

    return None


# =========================
# CONTOH PENGGUNAAN
# =========================
def main():
    goal_state: State = (
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 23, 24, 0
    )

    # Contoh initial state (tinggal sesuaikan untuk laporanmu)
    start_state: State = (
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        11, 12, 13, 14, 15,
        16, 17, 18, 19, 20,
        21, 22, 0, 23, 24
    )

    print("=== INITIAL STATE ===")
    print_board(start_state)

    print("=== GOAL STATE ===")
    print_board(goal_state)

    if not is_solvable(start_state):
        print("State awal tidak solvable.")
        return

    path = a_star(start_state, goal_state)

    if path is None:
        print("Solusi tidak ditemukan.")
        return

    print(f"Solusi ditemukan dengan {len(path) - 1} langkah.\n")

    for i, state in enumerate(path):
        print(f"Langkah {i}:")
        print_board(state)

    print("=== RINGKASAN ===")
    print(f"Total langkah: {len(path) - 1}")
    print(f"H1 state awal: {h1_misplaced_tiles(start_state, goal_state)}")


if __name__ == "__main__":
    main()
