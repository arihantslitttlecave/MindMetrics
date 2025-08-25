````markdown
# 🧠 MindMetrics — Memory Game

MindMetrics is a browser-based memory game where you test how sharp your recall is.  
The frontend is built with **HTML, CSS, and JavaScript**, while the backend is a **Flask server** that saves results into an Excel file (`game_data.xlsx`) using **pandas**.

---

## 🚀 Features
- Memory sequence gameplay 🎮  
- Neon-style UI  
- Results saved into Excel (`game_data.xlsx`)  
- Built with HTML, CSS, JS, Flask, and Pandas  

---

## 📦 Requirements
Install Python 3.8+ and run:
```bash
pip install flask flask-cors pandas openpyxl
````

---

## ⚙️ How to Run

### 1. Download or clone this project

```bash
git clone https://github.com/YOUR-USERNAME/MindMetrics.git
cd MindMetrics
```

(or download ZIP and extract)

### 2. Start the backend

```bash
python data-server.py
```

Runs a Flask server at 👉 `http://localhost:5000`

### 3. Run the frontend

Open `index.html` in your browser.

If direct open doesn’t work (CORS issue), run:

```bash
python -m http.server 8080
```

Then visit 👉 `http://localhost:8080`

---




---

## 🖼️ Screenshots

Here are some previews of **MindMetrics** in action:

### 🎮 Game UI


### 🧠 Gameplay Banners for the event
main.png
right.png
left.png

---

