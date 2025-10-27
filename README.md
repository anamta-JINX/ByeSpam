# ByeSpam – Smart Spam Detection App

**“ByeSpam:“We were on a break… from spam!”**

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features & Advantages](#features--advantages)
3. [Tech Stack & Libraries](#tech-stack--libraries)
4. [Installation](#installation)
5. [How It Works](#how-it-works)
6. [Running the App](#running-the-app)
7. [Usage Guide](#usage-guide)
8. [Color Theme & UI Aesthetic](#color-theme--ui-aesthetic)
9. [Model Details](#model-details)
10. [Authors](#authors)
11. [License](#license)

---

## Project Overview

**ByeSpam** is a **Python-based desktop application** that intelligently detects spam messages in emails, texts, or files. Using **Natural Language Processing (NLP)** and **Machine Learning**, it classifies messages as **Spam** or **Not Spam**, providing users a quick and reliable way to filter unwanted messages.

---

## Features & Advantages

* **Real-time Spam Detection:** Instantly classifies messages as Spam or Not Spam.
* **Batch Analysis:** Upload `.txt` files to analyze multiple messages at once.
* **Interactive Accuracy Graph:** Visualizes model performance dynamically.
* **User-friendly GUI:** Modern interface with hover effects and color-coded outputs.
* **Portable & Lightweight:** Runs locally, no heavy infrastructure needed.
* **Educational & Practical:** Ideal for learning ML, NLP, and GUI development.

---

## Tech Stack & Libraries

| Library        | Purpose                                                                    |
| -------------- | -------------------------------------------------------------------------- |
| `tkinter`      | Core GUI framework to build interactive desktop app windows and buttons.   |
| `pillow (PIL)` | Handles images for buttons, icons, or backgrounds in the GUI.              |
| `scikit-learn` | Implements Machine Learning models (Naive Bayes) and TF-IDF vectorization. |
| `matplotlib`   | Generates graphs to visualize model accuracy and performance.              |
| `pandas`       | Loads, cleans, and manipulates datasets.                                   |
| `numpy`        | Supports numerical operations for ML preprocessing and calculations.       |

**Install all libraries at once:**

```bash
pip install tkinter pillow scikit-learn matplotlib pandas numpy
```

> Note: `tkinter` is included with most Python installations. If you face issues, install via your OS package manager.

---

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/anamta-JINX/ByeSpam.git
cd ByeSpam
```

2. **Create & Activate a Virtual Environment** (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

or use the copy-paste command above for all libraries.

---

## How It Works

1. **Preprocessing:** Input messages are cleaned and converted into a numerical format using **TF-IDF Vectorizer**.
2. **Model Prediction:** A **Multinomial Naive Bayes classifier** predicts whether a message is Spam or Not Spam.
3. **Result Display:** The app GUI shows the classification result in color-coded format.
4. **Accuracy Visualization:** Model performance is visualized in a bar graph for reference.

**Underlying Logic:**

* Spam messages typically contain certain keywords, excessive links, or unusual formatting.
* TF-IDF measures the importance of words relative to the dataset.
* Naive Bayes uses probability to determine whether a message is spam.

---

## Running the App

```bash
python main.py
```

* The GUI window will open.
* Enter a message or upload a `.txt` file.
* Click **Detect Spam** to see the result.
* Check the **accuracy graph** for model performance insights.

---

## Usage Guide

1. **Single Message Detection:**

   * Type or paste a message in the input box.
   * Click **Detect Spam**.
   * See the result displayed instantly.

2. **File Upload Detection:**

   * Click **Upload** and select a `.txt` file with multiple messages.
   * Results for all messages are displayed in sequence.

3. **Model Performance:**

   * Accuracy and other metrics are displayed dynamically with a bar graph.

---

## Color Theme & UI Aesthetic

* **Spam Messages:** Light Red (#FF6961)
* **Not Spam Messages:** Green (#77DD77)
* **Buttons & Hover Effects:** Yellow (#FFD700)
* Clean, modern, and visually appealing design ensures easy readability.

---

## Model Details

* **Algorithm:** Multinomial Naive Bayes
* **Vectorization:** TF-IDF
* **Dataset:** Preprocessed SMS/Email datasets
* **Performance:** Accuracy and predictions are displayed in-app.

---

## Authors

* **Name:** Anamta Gohar
* **GitHub:** [anamta-JINX](https://github.com/anamta-JINX)
* **Email:** anamta.gohar25@gmail.com

---

## License
          
This project is **MIT Licensed**.
Feel free to use, modify, or distribute it for personal or educational purposes, as long as you give credit.

