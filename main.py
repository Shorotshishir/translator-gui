import tkinter as tk
from tkinter import ttk, font
from tkinter.scrolledtext import ScrolledText

from googletrans import Translator, LANGCODES
from ttkthemes import ThemedStyle


def translate():
    pass


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ThemedStyle(self.root)
        self.style.set_theme('equilux')
        self.root.resizable(width=False, height=False)
        self.root.title('Translator')
        self.root.geometry("850x600")
        self.root.config(bg=self.style.lookup('Tframe', 'background'))
        self.combo_box = ttk.Combobox()
        self.view_description()
        self.input_text = ScrolledText()
        self.view_text = tk.Label()
        self.set_font()
        self.view_form()
        self.root.mainloop()

    def view_description(self):
        enter_info = ttk.Label(self.root, text="Please enter your Text: ")
        enter_info.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

    def view_form(self):
        self.data_entry()
        self.data_view()
        self.choose_language()
        self.data_translate()

    def data_entry(self):
        input_label = ttk.Label(self.root, text="Input", )
        input_label.grid(row=1, column=1, padx=5, pady=5)
        self.input_text = ScrolledText(self.root, bd=1, height=5)
        self.input_text.grid(row=1, column=2, columnspan=3, padx=5, pady=5)

    def data_view(self):
        view_label = ttk.Label(self.root, text="Translated")
        view_label.grid(row=2, column=1, padx=5, pady=5)
        self.view_text = ttk.Label(self.root, text='', wraplength=600, justify='left', state="active")
        self.view_text.grid(row=2, column=2, columnspan=3, padx=5, pady=5, sticky="NSEW")

    def choose_language(self):
        self.box_value = tk.StringVar()
        combo_values = '\n'.join(LANGCODES.keys())
        self.combo_box = ttk.Combobox(self.root, width=10, textvariable=self.box_value, values=combo_values,
                                      font=self.defaultFont)
        self.combo_box.current(0)
        self.combo_box.grid(row=1, column=5, rowspan=1, padx=5, pady=5)

    def data_translate(self):
        translate_button = ttk.Button(self.root, text="translate", command=self.on_click)
        translate_button.grid(row=2, column=5, rowspan=1, padx=5, pady=5)

    def on_click(self):
        txt = self.input_text.get("1.0", 'end-1c')
        lang = self.combo_box.get()
        translator = Translator()
        if txt != '':
            if lang != '':
                translated = translator.translate(text=txt, dest=LANGCODES.get(lang))
                self.view_text.config(text=translated.text)

    def set_font(self):
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Calibri",
                                   size=9,
                                   weight=font.NORMAL)

if __name__ == '__main__':
    Gui()
