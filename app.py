import os
import sqlite3
import csv
import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, g, send_file, make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'dev-secret-key-change-me')

# Make datetime available in all templates
@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

DB_PATH = os.path.join(app.root_path, 'questions.db')


def get_db():
    if 'db' not in g:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            solution TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            company TEXT NOT NULL,
            tags TEXT NOT NULL,
            solved INTEGER NOT NULL DEFAULT 0
        );
        """
    )
    # Helpful indexes for filtering/search
    db.execute("CREATE INDEX IF NOT EXISTS idx_questions_difficulty ON questions(difficulty);")
    db.execute("CREATE INDEX IF NOT EXISTS idx_questions_company ON questions(company);")
    db.execute("CREATE INDEX IF NOT EXISTS idx_questions_solved ON questions(solved);")
    db.commit()


def normalize_tags(raw: str) -> str:
    # Normalize comma-separated tags: lowercase, strip, remove empties, unique
    parts = [t.strip().lower() for t in raw.split(',')]
    uniq = []
    for p in parts:
        if p and p not in uniq:
            uniq.append(p)
    return ', '.join(uniq)


def get_stats(db):
    total = db.execute('SELECT COUNT(*) AS c FROM questions').fetchone()['c']
    solved = db.execute('SELECT COUNT(*) AS c FROM questions WHERE solved=1').fetchone()['c']
    unsolved = total - solved
    by_difficulty = dict(
        (row['difficulty'], row['c'])
        for row in db.execute('SELECT difficulty, COUNT(*) AS c FROM questions GROUP BY difficulty').fetchall()
    )
    return {
        'total': total,
        'solved': solved,
        'unsolved': unsolved,
        'by_difficulty': by_difficulty,
    }


@app.before_request
def ensure_db():
    # Ensure DB exists before first request
    if not os.path.exists(DB_PATH):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        init_db()


@app.route('/')
def home():
    db = get_db()
    stats = get_stats(db)
    return render_template('home.html', stats=stats)


@app.route('/add', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        solution = request.form.get('solution', '').strip()
        difficulty = request.form.get('difficulty', '').strip()
        company = request.form.get('company', '').strip()
        tags = normalize_tags(request.form.get('tags', ''))

        # Validation
        if not all([title, description, solution, difficulty, company, tags]):
            flash('All fields are required.', 'danger')
            return render_template('add.html', form=request.form)

        db = get_db()
        db.execute(
            'INSERT INTO questions (title, description, solution, difficulty, company, tags, solved) VALUES (?, ?, ?, ?, ?, ?, 0)',
            (title, description, solution, difficulty, company, tags)
        )
        db.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('questions'))

    return render_template('add.html')


@app.route('/questions')
def questions():
    db = get_db()

    # Optional server-side filters (also support client-side live filters)
    q = request.args.get('q', '').strip().lower()
    difficulty = request.args.get('difficulty', '').strip()
    company = request.args.get('company', '').strip()
    tag = request.args.get('tag', '').strip().lower()

    base_sql = 'SELECT * FROM questions'
    conditions = []
    params = []

    if q:
        conditions.append('(LOWER(title) LIKE ? OR LOWER(company) LIKE ? OR LOWER(description) LIKE ? OR LOWER(tags) LIKE ? )')
        like = f"%{q}%"
        params.extend([like, like, like, like])
    if difficulty:
        conditions.append('difficulty = ?')
        params.append(difficulty)
    if company:
        conditions.append('company = ?')
        params.append(company)
    if tag:
        conditions.append('LOWER(tags) LIKE ?')
        params.append(f"%{tag}%")

    if conditions:
        base_sql += ' WHERE ' + ' AND '.join(conditions)

    base_sql += ' ORDER BY solved ASC, id DESC'

    rows = db.execute(base_sql, params).fetchall()

    # For filter dropdowns
    companies = [r['company'] for r in db.execute('SELECT DISTINCT company FROM questions ORDER BY company ASC').fetchall()]
    # Aggregate unique tags
    tag_rows = db.execute('SELECT tags FROM questions').fetchall()
    tag_set = set()
    for tr in tag_rows:
        for t in tr['tags'].split(','):
            t = t.strip()
            if t:
                tag_set.add(t)
    tags = sorted(tag_set)

    return render_template('questions.html', questions=rows, companies=companies, tags=tags, preset={
        'q': q, 'difficulty': difficulty, 'company': company, 'tag': tag
    })


@app.route('/edit/<int:q_id>', methods=['GET', 'POST'])
def edit_question(q_id):
    db = get_db()
    row = db.execute('SELECT * FROM questions WHERE id=?', (q_id,)).fetchone()
    if not row:
        flash('Question not found.', 'danger')
        return redirect(url_for('questions'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        solution = request.form.get('solution', '').strip()
        difficulty = request.form.get('difficulty', '').strip()
        company = request.form.get('company', '').strip()
        tags = normalize_tags(request.form.get('tags', ''))
        solved = 1 if request.form.get('solved') == 'on' else 0

        if not all([title, description, solution, difficulty, company, tags]):
            flash('All fields are required.', 'danger')
            return render_template('edit.html', q=row)

        db.execute(
            'UPDATE questions SET title=?, description=?, solution=?, difficulty=?, company=?, tags=?, solved=? WHERE id=?',
            (title, description, solution, difficulty, company, tags, solved, q_id)
        )
        db.commit()
        flash('Question updated.', 'success')
        return redirect(url_for('questions'))

    return render_template('edit.html', q=row)


@app.route('/delete/<int:q_id>', methods=['POST'])
def delete_question(q_id):
    db = get_db()
    db.execute('DELETE FROM questions WHERE id=?', (q_id,))
    db.commit()
    flash('Question deleted.', 'success')
    return redirect(url_for('questions'))


@app.route('/toggle_solved/<int:q_id>', methods=['POST'])
def toggle_solved(q_id):
    db = get_db()
    row = db.execute('SELECT solved FROM questions WHERE id=?', (q_id,)).fetchone()
    if not row:
        return jsonify({'ok': False, 'error': 'Not found'}), 404
    new_val = 0 if row['solved'] else 1
    db.execute('UPDATE questions SET solved=? WHERE id=?', (new_val, q_id))
    db.commit()
    return jsonify({'ok': True, 'solved': bool(new_val)})


@app.route('/stats')
def stats():
    db = get_db()
    s = get_stats(db)
    # Prepare difficulty buckets explicitly for chart labels
    difficulty_labels = ['Easy', 'Medium', 'Hard']
    difficulty_counts = [s['by_difficulty'].get('Easy', 0), s['by_difficulty'].get('Medium', 0), s['by_difficulty'].get('Hard', 0)]
    return render_template('stats.html', stats=s, difficulty_labels=difficulty_labels, difficulty_counts=difficulty_counts)


@app.route('/export')
def export_csv():
    db = get_db()
    rows = db.execute('SELECT * FROM questions ORDER BY id ASC').fetchall()

    def generate():
        header = ['id', 'title', 'description', 'solution', 'difficulty', 'company', 'tags', 'solved']
        yield ','.join(header) + '\n'
        for r in rows:
            # Escape quotes and commas by wrapping fields in quotes and replacing internal quotes
            def esc(v):
                if v is None:
                    return ''
                s = str(v).replace('"', '""')
                return f'"{s}"'
            out = [esc(r['id']), esc(r['title']), esc(r['description']), esc(r['solution']), esc(r['difficulty']), esc(r['company']), esc(r['tags']), esc(r['solved'])]
            yield ','.join(out) + '\n'

    resp = make_response(generate())
    resp.headers['Content-Type'] = 'text/csv'
    resp.headers['Content-Disposition'] = f'attachment; filename=questions_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    return resp


@app.route('/random')
def random_question():
    db = get_db()
    row = db.execute('SELECT id FROM questions').fetchall()
    if not row:
        flash('No questions available yet. Add one first!', 'info')
        return redirect(url_for('add_question'))
    chosen = random.choice(row)['id']
    return redirect(url_for('edit_question', q_id=chosen))


if __name__ == '__main__':
    # Ensure DB set up when running directly
    if not os.path.exists(DB_PATH):
        with app.app_context():
            init_db()
    print("Starting Flask application...")
    print("Server running on http://127.0.0.1:5000")
    print("Press CTRL+C to quit")
    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=5000)
