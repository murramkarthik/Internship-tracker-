# 🎓 Internship Tracker

A modern, dynamic web application to **track and manage internships** — built using **Flask (Python)** for the backend and **HTML/CSS/JavaScript** for the frontend.  
This app allows users to add, view, edit, and delete internship records with a sleek UI and responsive design.

---

## 🚀 Features

✅ Add, edit, and delete internships dynamically  
✅ Toggle internship status (Ongoing / Completed)  
✅ Search internships by company name  
✅ Preloaded internships (Google, Microsoft, Amazon, Infosys, TCS)  
✅ Beautiful responsive design with animations and glassmorphism  
✅ SQLite database with Flask backend  
✅ Fully dynamic – no page reloads required  

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5  
- CSS3 (Glassmorphism, Animations, Responsive Design)  
- JavaScript (Fetch API for dynamic updates)

**Backend:**
- Python (Flask Framework)
- Flask-CORS (for API access)
- Flask-SQLAlchemy (ORM for SQLite)

**Database:**
- SQLite (auto-generated `database.db` file)

---

## 📁 Folder Structure

```
internship-tracker/
│
├── backend/
│   ├── app.py              # Flask server with API routes
│   ├── models.py           # Database schema (Internship model)
│   ├── requirements.txt    # Backend dependencies
│   └── database.db         # Auto-created SQLite DB file
│
├── frontend/
│   ├── index.html          # Main frontend page
│   ├── style.css           # Beautiful modern UI styling
│   └── script.js           # Dynamic behavior using Fetch API
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Extract Project

If downloaded as ZIP:
```bash
unzip internship-tracker.zip
cd internship-tracker/backend
```

Or clone from GitHub:
```bash
git clone https://github.com/yourusername/internship-tracker.git
cd internship-tracker/backend
```

---

### 2️⃣ Backend Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Run Flask server:
```bash
python app.py
```

✅ Server runs at:
```
http://127.0.0.1:5000
```

---

### 3️⃣ Frontend Setup

Open the file:
```
frontend/index.html
```
in your browser (or use **VS Code Live Server**).

You can now interact with the web app.

---

## 💡 How It Works

1. The frontend uses **Fetch API** to talk with the Flask backend.
2. The backend handles CRUD operations using **SQLite**.
3. All data updates instantly — no manual refresh needed.

---

## 🧠 API Endpoints

| Method | Endpoint | Description |
|--------|-----------|-------------|
| **GET** | `/internships` | Get all internship records |
| **POST** | `/internships` | Add a new internship |
| **DELETE** | `/internships/<id>` | Delete an internship |
| **PATCH** | `/internships/<id>` | Update status or fields |

---

## 🧩 Sample Data (Preloaded)

| Company   | Role                        | Duration | Status     |
|------------|-----------------------------|-----------|-------------|
| Google     | Software Engineering Intern | 3 months | Completed  |
| Microsoft  | Data Science Intern         | 2 months  | Ongoing    |
| Amazon     | Cloud Computing Intern      | 4 months  | Completed  |
| Infosys    | Web Developer Intern        | 2 months  | Ongoing    |
| TCS        | Cybersecurity Intern        | 3 months  | Ongoing    |

---

## 🎨 Screenshots (UI Overview)

✨ **Dashboard View:** Displays all internships as stylish cards  
✨ **Add Form:** Quickly add new internship details  
✨ **Search Bar:** Filters internships as you type  
✨ **Dynamic Status Toggle:** Instantly switch between Completed and Ongoing  

---

## 🧭 Future Enhancements

- Add user authentication (Flask-Login)
- Export internship data to CSV/Excel
- Add analytics dashboard (charts & progress)
- Theme toggle (light/dark mode)
- Deployment via Render / Vercel

---

## 👨‍💻 Author

**Developed by:** [Your Name]  
**Tech Stack:** Flask + HTML + CSS + JavaScript  
**Version:** 1.0.0  

---

## 🏁 License

This project is open-source and available under the **MIT License**.
