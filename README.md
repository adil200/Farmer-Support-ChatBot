

# Farmer Support ChatBot

Welcome to the "Farmer Support ChatBot" project! This repository focuses on developing a chatbot tailored for farmers, equipped with features such as language translation, speech recognition, and real-time communication. The project integrates a Flask backend and a React frontend, creating an interactive platform for farmers to seek information and assistance.

![Screenshot 2024-01-13 at 3 30 24 PM](https://github.com/adil200/Farmer-Support-ChatBot/assets/75264739/5dcf78d5-e627-4b6f-9174-56ea06431021)

## Overview

In this repository, you'll find a Flask backend (`chat.py`), a React frontend (`app.jsx`), and training scripts (`train.py`) for the machine learning model. The machine learning model is trained on agricultural intents to provide context-aware responses. The frontend offers an intuitive chat interface, supporting multiple languages and enhancing user interaction.

## Installation

To run the code in this project, ensure you have the following dependencies:

-   Python 3
-   Flask
-   React
-   Socket IO
-   SpeechRecognition (for speech recognition)
-   Googletrans (for language translation)

You can install the required Python packages using the following commands:

```bash
pip install flask flask-socketio speechrecognition googletrans==4.0.0-rc1
```

For the React frontend, navigate to the `frontend` directory and run:

```bash
npm install
```

## Usage

1.  Clone this repository:

```bash
git clone https://github.com/your-username/Farmer-Support-ChatBot.git
```

2.  Navigate to the project directory:

```bash
cd Farmer-Support-ChatBot
```

3.  Run the Flask backend:

```bash
python chat.py
``` 

4.  Run the React frontend:

```bash
npm run build
npm run dev
```

5.  Open your browser and access `http://localhost:5173/` to interact with the Farmer Support ChatBot.

## Features

-   Language Translation: The chatbot supports multiple languages for user convenience.
-   Speech Recognition: Users can interact with the chatbot using voice commands.
-   Real-time Communication: Utilizes Socket IO for seamless real-time communication.

## Acknowledgments

This collaborative effort is led by a dedicated team of four individuals:

-   **N Adil**
-   **Ananya S M**
-   **Kavya Kartik**
-   **Md Sarfraz Alam**

This project is a capstone project developed as a final-year project. The Farmer Support ChatBot aims to assist farmers by providing real-time solutions and advice on various farming issues. It leverages AI and machine learning to provide accurate and timely responses. Various tutorials and resources on chatbot development, language translation, and real-time communication inspire the code and techniques used in this project.
