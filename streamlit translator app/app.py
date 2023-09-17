import streamlit as st
from gtts import gTTS
from googletrans import Translator, LANGUAGES
import tempfile
import os
import speech_recognition as sr

st.set_page_config(page_title='TTS & TTT Translation', layout='wide', initial_sidebar_state='expanded')

#For background
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Supported language codes and full names
languages = {
    "af": "Afrikaans",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "hy": "Armenian",
    "az": "Azerbaijani",
    "be": "Belarusian",
    "bn": "Bengali",
    "bg": "Bulgarian",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "ny": "Chichewa",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    "da": "Danish",
    "nl": "Dutch",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "tl": "Filipino",
    "fi": "Finnish",
    "fr": "French",
    "ka": "Georgian",
    "de": "German",
    "el": "Greek",
    "gu": "Gujarati",
    "haw": "Hawaiian",
    "iw": "Hebrew",
    "hi": "Hindi",
    "hu": "Hungarian",
    "id": "Indonesian",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "kk": "Kazakh",
    "rw": "Kinyarwanda",
    "ko": "Korean",
    "la": "Latin",
    "ms": "Malay",
    "ml": "Malayalam",
    "mr": "Marathi",
    "mn": "Mongolian",
    "my": "Myanmar (Burmese)",
    "ne": "Nepali",
    "no": "Norwegian",
    "fa": "Persian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sr": "Serbian",
    "si": "Sinhala",
    "sl": "Slovenian",
    "so": "Somali",
    "es": "Spanish",
    "su": "Sundanese",
    "sw": "Swahili",
    "sv": "Swedish",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tr": "Turkish",
    "tk": "Turkmen",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "ug": "Uyghur",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "cy": "Welsh",
}


# Create a Streamlit web app
#Side bar introduction
#st.balloons()
#st.snow()
with st.sidebar:
    st.header("Mahnoor Shoukat")
    st.header("PGD DATA SCIENCE WITH AI")
    st.write("NED UNIVERSITY OF ENGINEERING AND TECHNOLOGY")

#Title
st.title(":balloon: Translation App:balloon:")
    
# Create a radio button to select the translation mode
translation_mode = st.radio("Select Translation Mode:", ("Text to Text", "Text to Speech"))

if translation_mode == "Text to Text":
    # Text-to-Text Translation
    st.header("Text to Text Translation")

    # Create a dropdown for selecting the source languages
    source_lang = st.selectbox("Select the source language:", list(languages.values()))

    # Create input text box
    input_text = st.text_area("Enter text to translate:")

    # Create a dropdown for selecting the target languages
    target_lang = st.selectbox("Select the target language:", list(languages.values()))

    # Create a button to trigger translation
    if st.button("Translate"):
        if input_text:
            try:
                # Translate the input text
                translator = Translator()
                source_code = next(key for key, value in languages.items() if value == source_lang)
                target_code = next(key for key, value in languages.items() if value == target_lang)
                translated_text = translator.translate(input_text, src=source_code, dest=target_code).text

                # Display the translated text
                st.success(f"Translated Text: {translated_text}")

            except Exception as e:
                st.error("An error occurred during translation. Please try again later.")
        else:
            st.warning("Please enter text to translate.")

elif translation_mode == "Text to Speech":
    # Text-to-Speech Translation
    st.header("Text to Speech Translation")

    # Create a dropdown for selecting the source languages
    source_lang = st.selectbox("Select the source language:", list(languages.values()))

    # Create input text box
    input_text = st.text_area("Enter text to translate:")

    # Create a dropdown for selecting the target languages
    target_lang = st.selectbox("Select the target language:", list(languages.values()))

    # Create a button to trigger translation and text-to-speech
    if st.button("Translate"):
        st.markdown("Audio File")
        if input_text:
            try:
                # Translate the input text
                translator = Translator()
                source_code = next(key for key, value in languages.items() if value == source_lang)
                target_code = next(key for key, value in languages.items() if value == target_lang)
                translated_text = translator.translate(input_text, src=source_code, dest=target_code).text

                # Convert translated text to speech and save it to a temporary file
                tts = gTTS(translated_text, lang=target_code)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                    tts.save(temp_audio.name)

                # Play the synthesized speech
                st.audio(temp_audio.name, format="audio/mp3")

                # Display the translated text
                st.success(f"Translated Text: {translated_text}")

                # Delete the temporary audio file
                os.remove(temp_audio.name)

            except Exception as e:
                st.error("An error occurred during translation. Please try again later.")
        else:
            st.warning("Please enter text to translate.")
