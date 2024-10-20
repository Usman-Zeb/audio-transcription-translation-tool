# **Audio Transcription and Translation Tool**

A Python desktop application built using Tkinter for transcribing and translating audio files. This tool leverages OpenAI's Whisper model for transcription and GPT models for translation across multiple languages.

## **Features**

- **Multi-format audio support**: Supports `.wav`, `.mp3`, `.flac`, `.ogg`, `.m4a`, and more.
- **Real-time transcription and translation**: Provides transcription in several languages, with real-time translation of transcribed text.
- **User-friendly interface**: Simple, intuitive GUI built with Tkinter.
- **Multi-language support**: Transcription and translation in over 10 languages including Persian, English, French, Spanish, and more.

## **Technologies Used**

- **Python 3.x**
- **Tkinter** for the desktop interface.
- **OpenAI Whisper API** for transcription.
- **OpenAI GPT-4 API** for translation.

## **Screenshot**
<img src="https://github.com/user-attachments/assets/9a81bd21-838c-4d57-9c71-0b5e8cc01429" alt="Screenshot" width="600"/>

---

## **Getting Started**

Follow these instructions to get a copy of the project up and running on your local machine.

### **Prerequisites**

- **Python 3.x**
- **OpenAI API key**: You need an OpenAI API key for accessing the Whisper and GPT-4 models.
- Install the required Python packages:
  
  ```bash
  pip install -r requirements.txt
  ```

### **Installation**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Usman-Zeb/audio-transcription-translation-tool.git
   cd audio-transcription-translation-tool
   ```

2. **Set up your environment**:
   
   - **Option 1**: Create a `.env` file in the `root` directory to store your OpenAI API key securely.

     **.env**:
     ```bash
     OPENAI_API_KEY=your-api-key-here
     ```

   - **Option 2**: Export your API key as an environment variable.

     - On **Linux/macOS**:
       ```bash
       export OPENAI_API_KEY='your-api-key-here'
       ```
     - On **Windows**:
       ```bash
       setx OPENAI_API_KEY "your-api-key-here"
       ```

3. **Install dependencies**:
   
   Ensure you have all the necessary packages installed by running:
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   Navigate to the `src` directory and run the app using:

   ```bash
   cd src
   python main_ui.py
   ```

---

## **Usage**

1. **Upload an Audio File**:
   - Click the **"Upload Audio File"** button to upload an audio file. Supported formats include `.wav`, `.mp3`, `.flac`, `.ogg`, `.m4a`.
   
2. **Select Transcription Language**:
   - Choose the language for transcription from the dropdown menu. Supported languages include English, Persian, Urdu, French, Spanish, and more.

3. **Select Translation Language**:
   - Choose the language for translation from the second dropdown menu. The default translation language is **English**.

4. **Start Transcription and Translation**:
   - Click the **"Start Processing"** button to begin. The application will transcribe the audio and translate the transcription in real time.

5. **View Results**:
   - The transcribed text will be displayed in the **Transcribed Text** window, and the translated text will be shown in the **Translated Text** window.

---

## **File Structure**

```
.
├── .gitignore            # Ignore unnecessary files such as .env and virtual environment
├── README.md             # Documentation
├── .env                  # Environment variables (ignored in .gitignore)
├── requirements.txt      # Python dependencies
└── src                   # Source code directory
    ├── main_ui.py        # Main Tkinter GUI file
    ├── openai_functions.py  # Functions for interacting with OpenAI APIs
    ├── file_handling.py  # File handling and audio processing
    └── __init__.py       # (Optional) If your directory is structured as a package
```

---

## **Supported Languages**

### **Transcription**:
- **Persian** (`fa`)
- **Urdu** (`ur`)
- **English** (`en`)
- **French** (`fr`)
- **Spanish** (`es`)
- **German** (`de`)
- **Italian** (`it`)
- **Chinese** (`zh`)
- **Russian** (`ru`)
- **Arabic** (`ar`)
- **Japanese** (`ja`)
- **Korean** (`ko`)

### **Translation**:
- Default translation is to **English**, but more languages are supported based on the GPT model.

---

## **Contributing**

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit the changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Contact**

If you have any questions or need further clarification, feel free to contact me via GitHub.
