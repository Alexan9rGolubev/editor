import tkinter 
from tkinter import *
from settings import *
from Text_editor import *
editing = Text_editor()

app.title(APP_NAME)
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

scroll = Scrollbar(app, orient=VERTICAL, command=text.yview)
scroll.pack(side='right', fill='y')
text.configure(yscrollcommand=scroll.set)
text.pack()

menuBar = tkinter.Menu(app)
app_menu = tkinter.Menu(menuBar)

app_menu.add_command(label='Новый файл', command=editing.new_file)
app_menu.add_command(label='Открыть', command=editing.open_file)
app_menu.add_command(label='Сохранить', command=editing.save_file)
app_menu.add_command(label='Сохранить как', command=editing.save_as_file)

menuBar.add_cascade(label='Файл', menu=app_menu)
menuBar.add_cascade(label='Справка', command=editing.get_info)
menuBar.add_cascade(label='Выход', command=app.quit)

app.config(menu=menuBar)
app.mainloop()