import tkinter
import codecs
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename
from tkinter.messagebox import showerror 
from tkinter import messagebox
from settings import *

app = tkinter.Tk()
text = tkinter.Text(app, width=WIDTH - 50, height=HEIGHT)

class Text_editor():
    def __init__(self):
        self.file_name = 'Без названия'
    def new_file(self): 
        text.delete('1.0', tkinter.END)
    def open_file(self):
        inp = askopenfilename()
        if inp == '': 
            return
        with codecs.open(inp, encoding='utf-8') as forename_file: 
            data = forename_file.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)
    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output = open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()
    def save_as_file(self):
        output = asksaveasfile(mode='w')
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception: 
            showerror(title='Ошибка', message='Ошибка при сохранении')
    def get_info(self):
        messagebox.showinfo('Справка', 'Тута нечего нет')