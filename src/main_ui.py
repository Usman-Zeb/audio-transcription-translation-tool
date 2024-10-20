import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox, ttk
import threading
import time
from file_handling import audio_to_wav
from openai_functions import transcribe_audio, translate_text

# Supported language codes for transcription and translation
LANGUAGE_OPTIONS = {
    'Persian': 'fa',
    'Urdu': 'ur',
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Italian': 'it',
    'Chinese': 'zh',
    'Russian': 'ru',
    'Arabic': 'ar',
    'Japanese': 'ja',
    'Korean': 'ko'
}

# Global variable to store the uploaded file path
uploaded_file_path = None

# Function to process the uploaded audio file: transcribe and translate
def process_audio_file(sample_rate, transcription_lang_code, translation_lang_code, output_transcription, output_translation, progress_bar, label_status):
    try:
        if not uploaded_file_path:
            messagebox.showerror("Error", "Please upload an audio file first.")
            return

        label_status.config(text="Processing...")
        progress_bar['value'] = 0

        # Convert the audio file to WAV if necessary
        wav_file_path = audio_to_wav(uploaded_file_path, sample_rate)
        progress_bar['value'] = 25
        window.update_idletasks()

        # Transcribe the audio
        output_transcription.insert(tk.END, "Transcribing audio...\n")
        transcription_text = transcribe_audio(wav_file_path, sample_rate, transcription_lang_code)
        output_transcription.insert(tk.END, transcription_text + "\n")
        output_transcription.see(tk.END)
        progress_bar['value'] = 50
        window.update_idletasks()

        # Translate the text
        output_translation.insert(tk.END, "Translating text...\n")
        translated_text = translate_text(transcription_text, translation_lang_code)
        output_translation.insert(tk.END, translated_text + "\n")
        output_translation.see(tk.END)
        progress_bar['value'] = 100
        window.update_idletasks()

        label_status.config(text="Processing complete.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        progress_bar['value'] = 100
        label_status.config(text="Processing complete.")

# File upload dialog
def upload_audio_file():
    global uploaded_file_path
    """
    Opens a file dialog to select and upload any supported audio file.
    """
    uploaded_file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.flac *.ogg *.m4a *.rec")])
    if uploaded_file_path:
        messagebox.showinfo("File Uploaded", f"File uploaded successfully: {uploaded_file_path}")

# UI Setup using Tkinter
def create_ui():
    global window
    window = tk.Tk()
    window.title("Audio File Transcription and Translation")
    
    # Set minimum size for the window
    window.minsize(700, 700)
    window.geometry("700x600")
    window.configure(bg='#2e2e2e')  # Set background color for the window

    # Set window transparency
    #window.attributes('-alpha', 0.95)  # Adjust alpha (between 0.0 and 1.0) to make the window semi-transparent

    # Use ttk for a more modern look
    style = ttk.Style()
    style.theme_use("clam")  # Try "vista", "clam", "alt" for modern themes

    # Customize ttk styles
    style.configure("TButton", foreground="white", background="#5b9bd5", font=("Helvetica", 10, "bold"))
    style.configure("TLabel", foreground="white", background="#2e2e2e", font=("Helvetica", 12))
    style.configure("TFrame", background="#2e2e2e")
    style.configure("TCombobox", font=("Helvetica", 10))

    # Configure grid layout for dynamic resizing
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(2, weight=1)

    # Frame for Language selection
    frame_languages = ttk.Frame(window, padding="10")
    frame_languages.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    frame_languages.grid_columnconfigure(0, weight=1)
    frame_languages.grid_columnconfigure(1, weight=1)

    # Language selection for transcription
    lbl_transcription_lang = ttk.Label(frame_languages, text="Select Transcription Language:")
    lbl_transcription_lang.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    transcription_lang_combo = ttk.Combobox(frame_languages, values=list(LANGUAGE_OPTIONS.keys()), state='readonly')
    transcription_lang_combo.current(0)
    transcription_lang_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Language selection for translation (default set to English)
    lbl_translation_lang = ttk.Label(frame_languages, text="Select Translation Language (default: English):")
    lbl_translation_lang.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    
    translation_lang_combo = ttk.Combobox(frame_languages, values=list(LANGUAGE_OPTIONS.keys()), state='readonly')
    translation_lang_combo.current(2)  # Default to English
    translation_lang_combo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    # Frame for Text Areas (transcription and translation results)
    frame_text = ttk.Frame(window, padding="10")
    frame_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    window.grid_rowconfigure(1, weight=1)
    frame_text.grid_columnconfigure(0, weight=1)
    frame_text.grid_rowconfigure(1, weight=1)
    frame_text.grid_rowconfigure(3, weight=1)

    # Transcribed text display
    lbl_transcription = ttk.Label(frame_text, text="Transcribed Text:")
    lbl_transcription.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    output_transcription = scrolledtext.ScrolledText(frame_text, height=10, bg="#1e1e1e", fg="white", insertbackground="white")
    output_transcription.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    # Translated text display
    lbl_translation = ttk.Label(frame_text, text="Translated Text:")
    lbl_translation.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    
    output_translation = scrolledtext.ScrolledText(frame_text, height=10, bg="#1e1e1e", fg="white", insertbackground="white")
    output_translation.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

    # Frame for Buttons and Progress Bar
    frame_buttons = ttk.Frame(window, padding="10")
    frame_buttons.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

    # Align buttons, progress bar, and status label in one row
    frame_buttons.grid_columnconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(1, weight=2)
    frame_buttons.grid_columnconfigure(2, weight=1)
    frame_buttons.grid_columnconfigure(3, weight=1)

    # Button to upload the audio file
    btn_upload = ttk.Button(frame_buttons, text="Upload Audio File", command=upload_audio_file)
    btn_upload.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

    # Progress bar to show the status of transcription and translation
    progress_bar = ttk.Progressbar(frame_buttons, orient="horizontal", mode="determinate")
    progress_bar.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    # Status label to display progress status
    label_status = ttk.Label(frame_buttons, text="Waiting for input...", padding="5")
    label_status.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    # Button to start the transcription and translation process
    btn_start = ttk.Button(frame_buttons, text="Start Processing", 
                           command=lambda: threading.Thread(
                               target=process_audio_file, 
                               args=(16000, 
                                     LANGUAGE_OPTIONS[transcription_lang_combo.get()], 
                                     LANGUAGE_OPTIONS[translation_lang_combo.get()], 
                                     output_transcription, output_translation,
                                     progress_bar, label_status), 
                               daemon=True).start())
    btn_start.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

    # Make the last row fill remaining space
    window.grid_rowconfigure(3, weight=1)

    window.mainloop()

# Main entry point
if __name__ == "__main__":
    create_ui()
