
# 🖼️ MageCap – AI Image Captioning Tool

**MageCap** is a Python + Gradio-powered image captioning app that uses the **BLIP** model to generate intelligent, human-like captions for images. It offers multiple captioning styles, emotion tagging, and multilingual support — all through a simple, interactive UI.

## ✨ Features

- 📷 Upload an image and get an instant AI-generated caption
- 🧠 Powered by **BLIP** (Bootstrapped Language Image Pretraining)
- 🗣️ Caption styles: Formal, Funny, Descriptive, Short, etc.
- 😄 Emotion tags: Happy, Sad, Excited, Angry, etc.
- 🌍 Translate captions to multiple languages (e.g., Hindi, French, Spanish)
- 📋 One-click copy to clipboard
- 🧪 Built with **Gradio** for an intuitive web interface

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/MrCoss/magecap.git
cd magecap
````

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
# Activate:
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python magecap_app.py
```

Then open the link Gradio provides (usually `http://localhost:7860`) in your browser.

## 🧠 Tech Stack

* Python 3.7+
* Gradio
* Hugging Face Transformers
* BLIP (image captioning model)
* Torch
* PIL

## 📂 Project Structure

```
magecap/
├── magecap_app.py       # Main Gradio app
├── caption_generator.py # Caption logic using BLIP
├── requirements.txt     # Required packages
└── README.md            # Project overview
```

## 📝 Sample Use Cases

* Social media image descriptions
* Accessibility captioning
* Creative writing prompts
* Automatic meme creation

## 📌 License

This project is open-source and free to use for educational and personal purposes.

---

Made with ❤️ by Costas Pinto – MCA Student & Teacher

