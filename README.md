# 🌐 AI Website Creator using Streamlit & Gemini

This project is an AI-powered Website Generator built using Streamlit, Google Gemini API, and LangChain.
It allows users to generate a complete mini-website (HTML, CSS, JavaScript) automatically based on text input and optional PDF content.

The application produces cleanly separated frontend files and packages them into a downloadable ZIP file, making it ideal for rapid prototyping, learning, and automation-based web development.

---

# 🚀 Features

* AI-driven website generation using Google Gemini
* Interactive Streamlit UI for user-friendly input
* PDF upload support (uses PDF content as reference for website generation)
* Strict separation of HTML, CSS, and JavaScript
* Automatic ZIP file creation containing:

  * index.html
  * style.css
  * script.js
* Serverless workflow – no backend setup required
* Generates modern, responsive, and clean UI code

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* LangChain
* PyPDF
* dotenv

---

# ⚙️ How It Works

* User enters website requirements in the text area
* Optional: User uploads a PDF whose content is used as reference
* A strict system prompt ensures structured AI output
* Gemini generates:

  * HTML layout
  * External CSS styling
  * JavaScript functionality
* Code blocks are extracted safely
* Files are written and bundled into a ZIP
* User downloads the complete website in one click

---

# 📦 Output Structure

* website.zip

  * index.html
  * style.css
  * script.js

---

# 🔐 Environment Setup

* Create a `.env` file and add your Google Gemini API key
* Example:

  * gemini=YOUR_GOOGLE_API_KEY

---

# ▶️ Run the App

* Install dependencies:

  * pip install streamlit langchain-google-genai python-dotenv pypdf
* Run the application:

  * streamlit run app.py

---

# 🎯 Why This Project?

* Demonstrates real-world AI integration for frontend automation
* Shows how modern LLMs can generate production-ready web assets
* Useful for learning, rapid prototyping, and automation projects

---

# ✨ Notes

* Built as part of an AI & Automation learning journey
* Feel free to fork, experiment, and enhance this project

