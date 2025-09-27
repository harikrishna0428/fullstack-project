# Quick Start Guide 🚀

## Option 1: Automated Setup (Recommended)

1. **Double-click `setup.bat`** to automatically:
   - Create virtual environment
   - Install all dependencies
   - Prepare the project

2. **Double-click `run.bat`** to start the application

3. **Open browser** to `http://127.0.0.1:5000/`

---

## Option 2: Manual Setup

### Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### Step 2: Activate Virtual Environment
```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application
```bash
python app.py
```

### Step 5: Open Browser
Navigate to: `http://127.0.0.1:5000/`

---

## First Steps After Launch

1. **Home Page** - View quick statistics (initially all zeros)
2. **Add Question** - Click "Add" to create your first question
3. **View Questions** - Browse, filter, and search questions
4. **Statistics** - View charts and progress tracking
5. **Random** - Get a random question for practice
6. **Export CSV** - Download all questions

---

## Troubleshooting

### Python not found?
- Install Python 3.8+ from [python.org](https://www.python.org/downloads/)
- Make sure "Add Python to PATH" is checked during installation

### Port already in use?
- Change port in `app.py`: `app.run(debug=True, port=5001)`

### Dependencies fail to install?
- Upgrade pip: `python -m pip install --upgrade pip`
- Try again: `pip install -r requirements.txt`

### Flask debug mode error (watchdog)?
- Upgrade watchdog: `pip install --upgrade watchdog`
- This fixes the `EVENT_TYPE_OPENED` import error

### PowerShell script execution disabled?
- Use Git Bash: `source venv/Scripts/activate`
- Or enable scripts: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## Project Features Checklist

- ✅ Add new questions with full details
- ✅ Edit existing questions
- ✅ Delete questions (with confirmation)
- ✅ Mark questions as solved/unsolved
- ✅ Filter by difficulty, company, tag
- ✅ Real-time search functionality
- ✅ Statistics dashboard with charts
- ✅ Export to CSV
- ✅ Random question generator
- ✅ Responsive Bootstrap UI
- ✅ SQLite database
- ✅ Git version control

---

**Need help? Check README.md for detailed documentation!**
