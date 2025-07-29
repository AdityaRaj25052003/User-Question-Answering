🤖 USER QUESTION ANSWERING SYSTEM 

This project is a web-based QA system that uses NLP and Transformers to answer user questions based on a given passage. Built with Flask, it uses the Hugging Face question-answering pipeline to generate responses in real-time.

📁 PROJECT STRUCTURE

app.py           # Flask backend

templates/       # HTML UI (index.html)

static/          # CSS styling (style.css)


🎯 OBJECTIVES

Take input: passage + question

Predict answer using Hugging Face model

Display result instantly on the web page


📚 TECHNOLOGIES USED

Python, Flask

Hugging Face Transformers

HTML, CSS, JavaScript


🧰 LIBRARIES IMPORTED 

from flask import Flask, render_template, request, jsonify

from transformers import pipeline
