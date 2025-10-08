# Tech Interview Question Vault 🚀

**Full Stack Web Development Project**  
*Submitted by: Arvapalli Venkata Naga Sai Harikrishna*  
*GitHub: [@harikrishna0428](https://github.com/harikrishna0428)*

---

A full-stack web application built with Flask to help users save, categorize, and track coding interview questions for efficient practice and preparation.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-purple.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-lightblue.svg)

---

## 📋 Project Overview

**Tech Interview Question Vault** is a comprehensive CRUD (Create, Read, Update, Delete) web application designed for developers preparing for technical interviews. This project demonstrates full-stack development skills including:

- **Backend Development**: Flask framework with RESTful routing
- **Database Management**: SQLite with optimized queries and indexing
- **Frontend Development**: Responsive UI with Bootstrap 5
- **JavaScript Integration**: jQuery for dynamic interactions and AJAX
- **Data Visualization**: Interactive charts using Chart.js

### Key Functionalities:
- Add new coding interview questions with detailed information
- Categorize questions by difficulty, company, and tags
- Mark questions as solved/unsolved with instant updates
- Filter and search through questions dynamically without page reload
- View statistics with interactive pie and bar charts
- Export questions to CSV format
- Get random questions for quick practice sessions

---

## ✨ Features

### Core Features
- **CRUD Operations**: Create, Read, Update, Delete questions
- **Smart Categorization**: Organize by difficulty (Easy/Medium/Hard), company, and tags
- **Status Tracking**: Mark questions as solved or unsolved
- **Advanced Filtering**: Filter by difficulty, company, or tag
- **Live Search**: Real-time search by title, company, or keywords
- **Statistics Dashboard**: Visual insights with Chart.js (pie & bar charts)

### Bonus Features
- **Random Question**: Get a random question for quick practice
- **CSV Export**: Export all questions with timestamp
- **Responsive Design**: Mobile-friendly Bootstrap 5 UI
- **Client-side Validation**: Instant form validation with jQuery
- **Confirmation Modals**: Safe deletion with confirmation dialogs

---

## 🛠️ Tech Stack

### Backend
- **Flask 3.0.0**: Python web framework
- **SQLite3**: Lightweight database
- **Jinja2**: Template engine

### Frontend
- **HTML5**: Semantic markup
- **Bootstrap 5.3.3**: Responsive UI framework
- **jQuery 3.6.4**: DOM manipulation and AJAX
- **Chart.js 4.4.0**: Data visualization

---

## 📁 Project Structure

```
Full stack Project/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation
├── questions.db           # SQLite database (auto-generated)
├── static/
│   ├── css/
│   │   └── style.css      # Custom styles
│   └── js/
│       └── main.js        # jQuery logic
└── templates/
    ├── base.html          # Base template with navbar
    ├── home.html          # Landing page
    ├── add.html           # Add question form
    ├── edit.html          # Edit question form
    ├── questions.html     # View all questions
    └── stats.html         # Statistics page
```

---

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

### Installation Steps

1. **Clone or Download the Project**
   ```bash
   cd "c:\Users\harik\OneDrive\Desktop\Full stack Project"
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Open in Browser**
   Navigate to: `http://127.0.0.1:5000/`

---

## 📖 Usage Guide

### Adding Questions
1. Click **"Add"** in the navbar
2. Fill in all required fields:
   - Question Title
   - Description
   - Solution
   - Difficulty (Easy/Medium/Hard)
   - Company name
   - Tags (comma-separated)
3. Click **"Add Question"**

### Viewing & Filtering Questions
1. Go to **"Questions"** page
2. Use filters:
   - **Search bar**: Search by title, company, or tags
   - **Difficulty dropdown**: Filter by difficulty level
   - **Company dropdown**: Filter by company
   - **Tag dropdown**: Filter by specific tag
3. All filters work in real-time without page reload

### Managing Questions
- **Edit**: Click "Edit" button to modify question details
- **Delete**: Click "Delete" button (confirmation required)
- **Toggle Status**: Click "Mark Solved/Unsolved" to update status instantly

### Viewing Statistics
1. Navigate to **"Stats"** page
2. View:
   - Total questions count
   - Solved vs Unsolved pie chart
   - Distribution by difficulty bar chart

### Additional Features
- **Random Question**: Click "Random" in navbar for practice
- **Export CSV**: Click "Export CSV" to download all questions

---

## 🗄️ Database Schema

### Table: `questions`

| Column      | Type    | Description                        |
|-------------|---------|-------------------------------------|
| id          | INTEGER | Primary key (auto-increment)        |
| title       | TEXT    | Question title                      |
| description | TEXT    | Full question description           |
| solution    | TEXT    | Solution/approach                   |
| difficulty  | TEXT    | Easy / Medium / Hard                |
| company     | TEXT    | Company name                        |
| tags        | TEXT    | Comma-separated tags                |
| solved      | INTEGER | 0 (unsolved) or 1 (solved)          |

---

## 🎨 Screenshots
<img width="1349" height="521" alt="Screenshot 2025-10-07 220915" src="https://github.com/user-attachments/assets/1ae4435d-faaa-451d-b7f2-99b669cef704" />

--This is the Home page--
<br><br><br>
<img width="1300" height="645" alt="Screenshot 2025-10-07 230507" src="https://github.com/user-attachments/assets/23cd7e4c-4a9b-4492-b391-b988be71839c" />

--This is the page where we added questions which we faced in interviews--
<br><br><br>
<img width="1339" height="444" alt="Screenshot 2025-10-07 230637" src="https://github.com/user-attachments/assets/032da5f9-7bbf-44ae-a05c-39882d446d77" />

--This is where we will see questions--
<br><br><br>
<img width="566" height="596" alt="Screenshot 2025-10-07 230839" src="https://github.com/user-attachments/assets/2d6dcd89-d1a3-4af5-85e6-714a2055690a" />

--In this page we can see the stats of the questions which we solved before--
<br><br><br>
<img width="1347" height="71" alt="Screenshot 2025-10-07 231008" src="https://github.com/user-attachments/assets/f0cebd34-9a41-453d-a536-ecd284d54225" />

--If we click on this we will get details of the questions in CSV files--
<br><br><br>
<img width="1339" height="621" alt="Screenshot 2025-10-07 232601" src="https://github.com/user-attachments/assets/780a4e46-b388-48ce-a3e3-d1b9fc93f2f8" />

--By clicking this random it will generate a random question--








### Home Page
- Quick stats overview
- Navigation to main features

### Questions Page
- Filterable table view
- Real-time search
- Action buttons for each question

### Statistics Page
- Visual charts showing progress
- Breakdown by difficulty

---

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file for production:
```
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

### Database Location
By default, `questions.db` is created in the project root. To change:
```python
# In app.py
DB_PATH = 'path/to/your/database.db'
```

---

## 🚢 Deployment

### Deploy on Render (Free)

1. Push code to GitHub
2. Create new Web Service on [Render](https://render.com)
3. Connect your repository
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add `gunicorn` to `requirements.txt`
7. Deploy!

### Deploy on PythonAnywhere

1. Upload files to PythonAnywhere
2. Create a new web app (Flask)
3. Configure WSGI file to point to `app.py`
4. Reload web app

---

## 🧪 Testing

### Manual Testing Checklist
- [ ] Add a new question
- [ ] Edit existing question
- [ ] Delete a question (with confirmation)
- [ ] Toggle solved status
- [ ] Filter by difficulty
- [ ] Filter by company
- [ ] Filter by tag
- [ ] Search functionality
- [ ] View statistics
- [ ] Export to CSV
- [ ] Random question feature

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

Created with ❤️ for interview preparation

---

## 🙏 Acknowledgments

- Flask documentation
- Bootstrap team
- Chart.js contributors
- jQuery community

---

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check existing documentation
- Review Flask documentation

---

## 🔮 Future Enhancements

- [ ] User authentication system
- [ ] Multiple user support
- [ ] Question sharing between users
- [ ] Timer for practice sessions
- [ ] Code editor integration
- [ ] Video solution links
- [ ] Difficulty rating system
- [ ] Progress tracking over time
- [ ] Email reminders for practice
- [ ] Dark mode toggle

---

**Happy Coding! 🎉**
