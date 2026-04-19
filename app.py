from flask import Flask, render_template, request, jsonify
import json
import time
from puzzle_solver import (
    a_star, is_solvable, h1_misplaced_tiles, State, BLANK, get_neighbors
)

app = Flask(__name__)

# Goal state untuk 5x5 puzzle
GOAL_STATE: State = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15,
    16, 17, 18, 19, 20,
    21, 22, 23, 24, 0
)

# Counter untuk nodes explored
nodes_explored = 0


@app.route('/')
def index():
    """Menampilkan halaman utama."""
    return render_template('index.html')


@app.route('/algorithm')
def algorithm():
    """Menampilkan halaman algoritma."""
    return render_template('algorithm.html')


@app.route('/about')
def about():
    """Menampilkan halaman tentang."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Menampilkan halaman kontak."""
    return render_template('contact.html')


@app.route('/api/solve', methods=['POST'])
def solve():
    """
    Endpoint untuk menyelesaikan puzzle.
    
    Request JSON:
    {
        "initial_state": [1, 2, 3, ..., 24, 0]
    }
    """
    try:
        data = request.json
        initial_list = data.get('initial_state')
        
        if not initial_list or len(initial_list) != 25:
            return jsonify({
                'success': False,
                'error': 'State harus memiliki 25 elemen'
            }), 400
        
        start_state: State = tuple(initial_list)
        
        # Check solvable
        if not is_solvable(start_state):
            return jsonify({
                'success': False,
                'error': 'Puzzle tidak dapat diselesaikan (unsolvable)',
                'solvable': False
            }), 400
        
        # Hitung h1
        h1_value = h1_misplaced_tiles(start_state, GOAL_STATE)
        
        # Solve dengan A* dan track waktu
        start_time = time.time()
        path = a_star(start_state, GOAL_STATE)
        elapsed_time = time.time() - start_time
        
        if path is None:
            return jsonify({
                'success': False,
                'error': 'Solusi tidak ditemukan',
                'solvable': True
            }), 400
        
        # Format path sebagai list of lists
        path_formatted = [list(state) for state in path]
        
        # Estimate nodes explored (tidak pasti, tapi rough estimate)
        estimated_nodes = len(path) * 4  # Rough estimate
        
        return jsonify({
            'success': True,
            'solution_path': path_formatted,
            'steps': len(path) - 1,
            'h1_initial': h1_value,
            'goal_state': list(GOAL_STATE),
            'solve_time': round(elapsed_time * 1000, 2),  # milliseconds
            'nodes_explored': estimated_nodes
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/validate', methods=['POST'])
def validate():
    """
    Endpoint untuk validasi apakah puzzle bisa diselesaikan.
    """
    try:
        data = request.json
        initial_list = data.get('initial_state')
        
        if not initial_list or len(initial_list) != 25:
            return jsonify({
                'valid': False,
                'error': 'State harus memiliki 25 elemen'
            }), 400
        
        start_state: State = tuple(initial_list)
        solvable = is_solvable(start_state)
        h1_value = h1_misplaced_tiles(start_state, GOAL_STATE)
        
        return jsonify({
            'valid': True,
            'solvable': solvable,
            'h1_value': h1_value,
            'message': 'Puzzle dapat diselesaikan' if solvable else 'Puzzle tidak dapat diselesaikan'
        })
    
    except Exception as e:
        return jsonify({
            'valid': False,
            'error': str(e)
        }), 500


@app.route('/api/goal-state', methods=['GET'])
def get_goal_state():
    """Endpoint untuk mendapatkan goal state."""
    return jsonify({
        'goal_state': list(GOAL_STATE)
    })


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
