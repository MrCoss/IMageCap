import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
import gradio as gr

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Translation models map
translation_models = {
    "Hindi": "Helsinki-NLP/opus-mt-en-hi",
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es",
    "Tamil": "Helsinki-NLP/opus-mt-en-ta",
    "Telugu": "Helsinki-NLP/opus-mt-en-te",
}

# Get translation pipeline for a language
translator_cache = {}
def get_translator(lang):
    if lang not in translator_cache:
        model_name = translation_models.get(lang)
        if model_name:
            translator_cache[lang] = pipeline("translation", model=model_name)
    return translator_cache.get(lang)

# ----------- FUNCTIONS ------------

def generate_caption(image, style="Formal", emotion="Neutral", lang="English"):
    # Base caption
    inputs = processor(image, return_tensors="pt").to(device)
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    # Style modifications
    if style == "Funny":
        caption = f"Look at this! {caption} Haha!"
    elif style == "Short":
        caption = caption.split(".")[0]
    elif style == "Poetic":
        caption = f"Behold... {caption}, as if whispered by nature."

    # Emotion additions
    emojis = {
        "Happy": "😊", "Sad": "😢", "Excited": "🤩", "Love": "❤️",
        "Surprised": "😲", "Calm": "😌", "Angry": "😠", "Neutral": ""
    }
    caption += f" {emojis.get(emotion, '')}"

    # Translation
    if lang != "English":
        translator = get_translator(lang)
        if translator:
            caption = translator(caption)[0]['translation_text']
        else:
            caption = f"(Translation for {lang} not supported)"

    return caption.strip()

# ----------- GRADIO UI ------------

with gr.Blocks() as demo:
    gr.Markdown("IMageCap")

    with gr.Row():
        image_input = gr.Image(label="Upload Image", type="pil")

        with gr.Column():
            style_dropdown = gr.Dropdown(
                choices=["Formal", "Funny", "Short", "Poetic"],
                label="Caption Style",
                value="Formal"
            )
            emotion_dropdown = gr.Dropdown(
                choices=["Neutral", "Happy", "Sad", "Excited", "Love", "Surprised", "Calm", "Angry"],
                label="Caption Emotion",
                value="Neutral"
            )
            lang_dropdown = gr.Dropdown(
                choices=["English", "Hindi", "French", "German", "Spanish", "Tamil", "Telugu"],
                label="Caption Language",
                value="English"
            )
            generate_btn = gr.Button("Generate Caption")

    caption_output = gr.Textbox(label="Caption", lines=2)
    copy_button = gr.Button("Copy Caption")

    # Generate caption and show it
    generate_btn.click(
        fn=generate_caption,
        inputs=[image_input, style_dropdown, emotion_dropdown, lang_dropdown],
        outputs=caption_output,
    )

    # Copy functionality
    copy_button.click(
        fn=lambda x: x,
        inputs=caption_output,
        outputs=caption_output,
    )

demo.launch()
