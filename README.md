🧠 AI Notes Summarizer
A Django-based Intelligent Text Summarization Web Application

🚀 Overview
AI Notes Summarizer is a web-based application built using Django, designed to automatically summarize long text or notes.
This project uses a simple but effective Extractive NLP summarization algorithm (word frequency + sentence scoring).
The app helps students, researchers, and writers quickly convert long paragraphs into short, meaningful summaries.

This project is part of my Diploma Final Year Major Project, showcasing skills in:

Python
Django Framework
Basic Natural Language Processing (NLP)
UI/UX using Bootstrap
CRUD operations
Deployment
✨ Features
🔹 1. AI-Based Automatic Summaries
Paste any long text → system generates a meaningful summary using rule-based NLP.
🔹 2. Save Notes & Summaries
Each summary is stored in the database.
View previous notes anytime.
🔹 3. Recent Summaries Section
Right sidebar shows last 5 summaries.
🔹 4. Clean UI & Responsive Design
Built using Bootstrap 5.
Works on mobile + desktop.
🔹 5. Detailed Notes Page
Shows:
✔ Title
✔ Original text
✔ Generated Summary
🔹 6. Simple & Fast Algorithm
No external API
100% offline
No hidden cost / API key
🛠️ Technologies Used
Technology	Purpose
Python 3	Backend logic
Django	Web framework
SQLite	Default database
Bootstrap 5	UI Styling
HTML + CSS	Templates
Git & GitHub	Version control
🧠 How It Works (Summarization Logic)
The summarizer uses extractive summarization:

Clean text
Split into sentences
Count word frequency (ignoring stopwords)
Score sentences
Select top N sentences
Located in:

summarizer/utils.py

📝 Future Enhancements
Add multilingual summarization
Add login system
Export to PDF
AI-powered key-points generator
Dark mode UI
Voice input → Auto summary
