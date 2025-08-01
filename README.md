# IMageCap – An Intelligent AI Image Captioning Tool

[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://shields.io/)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Framework: Gradio](https://img.shields.io/badge/Framework-Gradio-orange)](https://www.gradio.app/)
[![Model: Hugging Face BLIP](https://img.shields.io/badge/Model-Hugging%20Face%20BLIP-yellow?logo=huggingface)](https://huggingface.co/Salesforce/blip-image-captioning-large)

**MageCap** is a modern, interactive web application that leverages the power of the **BLIP (Bootstrapped Language Image Pretraining)** model to generate intelligent, human-like captions for any image. Built with Python and Gradio, it offers multiple captioning styles, emotion tagging, and multilingual support through a simple and accessible user interface.

---

## Table of Contents
- [1. Project Vision & Objective](#1-project-vision--objective)
- [2. Core Features & Capabilities](#2-core-features--capabilities)
- [3. The Technical Pipeline: How It Works](#3-the-technical-pipeline-how-it-works)
- [4. The BLIP Model Explained](#4-the-blip-model-explained)
- [5. Project Structure Explained](#5-project-structure-explained)
- [6. Technical Stack](#6-technical-stack)
- [7. Local Setup & Usage Guide](#7-local-setup--usage-guide)
- [8. Sample Use Cases](#8-sample-use-cases)
- [9. Author & License](#9-author--license)

---

## 1. Project Vision & Objective

The goal of MageCap is to democratize access to state-of-the-art computer vision and natural language processing. While powerful models like BLIP exist, they often require technical expertise to use. This project bridges that gap by wrapping a complex AI model in a simple, user-friendly web interface.

The objective is to provide a tool that is not only functional but also creative, allowing users to generate captions for a wide range of purposes—from improving accessibility to sparking creative content creation.

---

## 2. Core Features & Capabilities

-   **Intelligent Captioning:** Powered by the BLIP model, the app goes beyond simple object recognition to understand context, relationships, and actions within an image, producing descriptive and relevant captions.
-   **Creative Caption Styles:** Users can select from multiple styles (e.g., Formal, Funny, Descriptive, Short) to tailor the caption's tone and content to their specific needs.
-   **Emotion Tagging:** The application analyzes the image and caption to suggest relevant emotion tags (e.g., Happy, Sad, Adventurous), adding another layer of context.
-   **Multilingual Support:** Captions can be instantly translated into multiple languages like Hindi, French, and Spanish, making the tool globally accessible.
-   **Interactive & Simple UI:** Built with Gradio, the interface allows users to easily upload an image, select options, and get results without any code.
-   **One-Click Copy:** A convenient "Copy to Clipboard" button makes it easy to use the generated captions elsewhere.

---

## 3. The Technical Pipeline: How It Works

MageCap operates on a seamless pipeline from user input to final output, orchestrated by the main Gradio application.

1.  **User Input:** The user interacts with the Gradio interface (`magecap_app.py`) to upload an image and select their desired caption style and language.
2.  **Image Preprocessing:** The uploaded image is loaded using the `PIL` library. It's then preprocessed to match the specific input format (e.g., resolution, normalization) required by the BLIP model.
3.  **Caption Generation (`caption_generator.py`):**
    - The preprocessed image tensor is fed into the pre-trained **BLIP model**, loaded from Hugging Face Transformers.
    - The model performs a forward pass to generate a base, descriptive caption for the image.
4.  **Styling & Post-processing:** Based on the user's selected "style," the base caption can be modified. This might involve using prompt engineering with another language model or applying rule-based templates to change the tone.
5.  **Translation:** If a language other than English is selected, the final caption is passed to a translation model or API to be converted.
6.  **Output Display:** The final generated caption, emotion tags, and translated text are returned to the Gradio interface and displayed clearly to the user.

---

## 4. The BLIP Model Explained

**BLIP (Bootstrapped Language-Image Pre-training)** is a powerful vision-language model developed by Salesforce Research. It's unique because it's pre-trained on a massive dataset of images and text, allowing it to understand the deep semantic connection between what an image contains and how to describe it in natural language. It excels at generating captions that are not only accurate but also contextually rich.

---

## 5. Project Structure Explained

The repository is organized into a clean, modular structure.

```

magecap/
├── magecap\_app.py        \# The main Gradio application script that defines the UI and handles user interaction.
├── caption\_generator.py  \# A separate module containing the core logic for loading the BLIP model and generating captions.
├── requirements.txt      \# A list of all Python dependencies required to run the project.
└── README.md             \# This detailed project documentation.

````

---

## 6. Technical Stack

-   **Core Language:** Python
-   **Web UI Framework:** Gradio
-   **AI/ML Framework:** PyTorch
-   **NLP & Vision Models:** Hugging Face Transformers (for accessing the BLIP model)
-   **Image Processing:** Pillow (PIL)

---

## 7. Local Setup & Usage Guide

To run this application on your local machine, please follow these steps.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MrCoss/magecap.git](https://github.com/MrCoss/magecap.git)
    cd magecap
    ```

2.  **Create and Activate a Virtual Environment** (Recommended):
    ```bash
    # Create the environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    *Note: `torch` can be a large download. This may take some time.*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Gradio App:**
    ```bash
    python magecap_app.py
    ```
    After running the script, Gradio will provide a local URL in your terminal (usually `http://127.0.0.1:7860`). Open this link in your web browser to use the application.

---

## 8. Sample Use Cases

-   **Social Media:** Instantly generate engaging captions for Instagram, Twitter, or Facebook posts.
-   **Accessibility:** Create descriptive alt-text for images to make web content accessible to visually impaired users.
-   **Content Creation:** Use the generated captions as creative prompts for stories, poems, or blog posts.
-   **Digital Asset Management:** Automatically tag and describe large image libraries for easier searching.

---

## 9. Author & License

-   **Author:** Made with ❤️ by **Costas Pinto** – MCA Student & Teacher.
-   **License:** This project is open-source and available for educational and personal use.
````
