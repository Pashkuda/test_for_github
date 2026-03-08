import tkinter as tk
from tkinter import ttk, messagebox
#test

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

REVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

class MorseCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.root.geometry("500x400")
        
        # Text to Morse
        ttk.Label(root, text="Text to Morse:", font=("Arial", 10, "bold")).pack(pady=5)
        self.text_input = tk.Text(root, height=4, width=50)
        self.text_input.pack(pady=5)
        
        ttk.Button(root, text="Convert to Morse", command=self.text_to_morse).pack(pady=5)
        
        self.morse_output = tk.Text(root, height=4, width=50)
        self.morse_output.pack(pady=5)
        
        # Morse to Text
        ttk.Label(root, text="Morse to Text:", font=("Arial", 10, "bold")).pack(pady=5)
        self.morse_input = tk.Text(root, height=3, width=50)
        self.morse_input.pack(pady=5)
        
        ttk.Button(root, text="Convert to Text", command=self.morse_to_text).pack(pady=5)
        
        self.text_output = tk.Text(root, height=2, width=50)
        self.text_output.pack(pady=5)
    
    def text_to_morse(self):
        text = self.text_input.get("1.0", "end-1c").upper()
        morse = ' '.join(MORSE_CODE_DICT.get(char, '?') for char in text if char != ' ')
        self.morse_output.delete("1.0", "end")
        self.morse_output.insert("1.0", morse)
    
    def morse_to_text(self):
        morse = self.morse_input.get("1.0", "end-1c").split()
        text = ''.join(REVERSE_MORSE_DICT.get(code, '?') for code in morse)
        self.text_output.delete("1.0", "end")
        self.text_output.insert("1.0", text)

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeApp(root)
    root.mainloop()