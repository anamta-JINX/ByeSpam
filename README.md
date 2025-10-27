# Spam Detection App

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Running the App](#running-the-app)
6. [Usage Guide](#usage-guide)
7. [Color Theme & UI Aesthetic](#color-theme--ui-aesthetic)
8. [Model Details](#model-details)
9. [Contributing](#contributing)
10. [Authors](#authors)
11. [License](#license)

---

## Project Overview

The **Spam Detection App** is a Python-based desktop application that classifies text messages or emails as **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)** and **Machine Learning (Naive Bayes)**.

The application combines a **user-friendly Tkinter GUI**, file upload functionality, and live model performance visualization, making it ideal for educational, practical, and demo purposes.

---

## Features

* **Spam Classification:** Detects spam messages using a trained Naive Bayes model with TF-IDF vectorization.
* **File Upload:** Analyze multiple messages at once by uploading `.txt` files.
* **Accuracy Display:** Visualizes the model’s accuracy with an interactive graph.
* **Custom GUI:** Interactive buttons with hover effects, matching a modern color aesthetic.
* **Lightweight & Portable:** Runs locally without heavy dependencies.

---

## Tech Stack

* **Programming Language:** Python 3.x
* **GUI:** Tkinter
* **Machine Learning:** scikit-learn (Naive Bayes, TF-IDF Vectorizer)
* **Data Visualization:** matplotlib
* **Image Handling:** PIL (Python Imaging Library)

---

## Installation

Follow these steps to set up the app:

1. **Clone the Repository**

```bash
git clone https://github.com/anamta-JINX/spam-detection-app.git
cd spam-detection-app
```

2. **Create and Activate a Virtual Environment** (recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install Required Libraries**

```bash
pip install -r requirements.txt
```

> **Dependencies include:** `tkinter`, `pillow`, `scikit-learn`, `matplotlib`, `numpy`, `pandas`.

---

## Running the App

1. Ensure your virtual environment is active.
2. Run the main Python file:

```bash
python main.py
```

3. The GUI window will open, displaying the input box, buttons, and graph section.

---

## Usage Guide

1. **Detect Spam in a Single Message**

   * Type or paste your message into the input box.
   * Click **Detect Spam**.
   * The result will display **“Spam”** or **“Not Spam”**.

2. **Analyze Messages from a File**

   * Click the **Upload** button.
   * Select a `.txt` file containing messages.
   * The app will process each message and display results.

3. **View Model Accuracy**

   * The app automatically displays a **bar graph of model performance** using your dataset.
   * Bars are color-coded for clarity and match the GUI color theme.

---

## Color Theme & UI Aesthetic

* **Spam Messages:** Light Red (#FF6961)
* **Not Spam Messages:** Green (#77DD77)
* **Buttons & Hover Effects:** Yellow (#FFD700)
* Modern UI design ensures readability and pleasant interaction.

---

## Model Details

* **Algorithm:** Multinomial Naive Bayes
* **Vectorization:** TF-IDF
* **Performance:** Accuracy is displayed dynamically in the app.
* The model can be retrained by updating the dataset and rerunning the preprocessing script.

---

## Contributing

We welcome contributions:

1. Fork the repository.
2. Create a new feature branch:

```bash
git checkout -b feature/your-feature
```

3. Commit your changes:

```bash
git commit -m "Add new feature"
```

4. Push to your branch:

```bash
git push origin feature/your-feature
```

5. Open a Pull Request for review.

---

## Authors

* **Name:** Anamta Gohar
* **GitHub:** [anamta-JINX](https://github.com/anamta-JINX)
* **Email:** anamta.gohar25@gmail.com

---

## License

This project is **open-source** under the **MIT License**.
You are free to use, modify, and distribute this project for personal or educational purposes.

Do you want me to do that next?
