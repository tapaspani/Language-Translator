
# Language Translator (Updated for Python 3.13)
# Uses deep-translator instead of googletrans

from deep_translator import GoogleTranslator
from tkinter import *
from tkinter import messagebox


def translate_function():
    text_v = text_entry.get("1.0", "end-1c").strip()
    src_v = src_entry.get("1.0", "end-1c").strip().lower()
    dest_v = dest_entry.get("1.0", "end-1c").strip().lower()

    if not text_v:
        messagebox.showerror("Error", "Enter valid text")
        return

    # Default behavior
    if not dest_v:
        dest_v = "en"  # English as default
    if not src_v:
        src_v = "auto"  # Auto-detect language

    try:
        translated_text = GoogleTranslator(source=src_v, target=dest_v).translate(text_v)
        messagebox.showinfo("Translated Text", translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")


def clear():
    dest_entry.delete("1.0", "end")
    src_entry.delete("1.0", "end")
    text_entry.delete("1.0", "end")


# GUI setup
window = Tk()
window.geometry("500x300")
window.title("Language Translator")

title_label = Label(window, text="Language Translator", font=("Gayathri", 14, "bold"))
title_label.pack(pady=5)

text_label = Label(window, text="Text to translate:")
text_label.place(x=10, y=40)
text_entry = Text(window, width=40, height=5, font=("Ubuntu Mono", 12))
text_entry.place(x=130, y=40)

src_label = Label(window, text="Source language (leave empty: auto-detect):")
src_label.place(x=10, y=140)
src_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
src_entry.place(x=300, y=140)

dest_label = Label(window, text="Target language (leave empty: English):")
dest_label.place(x=10, y=170)
dest_entry = Text(window, width=20, height=1, font=("Ubuntu Mono", 12))
dest_entry.place(x=300, y=170)

button1 = Button(window, text="Translate", bg="yellow", command=translate_function)
button1.place(x=160, y=220)
button2 = Button(window, text="Clear", bg="yellow", command=clear)
button2.place(x=270, y=220)

window.mainloop()
