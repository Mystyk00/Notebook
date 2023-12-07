from tkinter import *
from tkinter import ttk, simpledialog
import time

counter = 1
startTime = 0

def saveNotes():
    text = notesContent.get('1.0', END)
    with open('data.txt', 'w') as f:
        f.write(text)

def loadNotes():
    try:
        with open('data.txt', 'r') as f:
            text = f.read()
            notesContent.delete('1.0', END)
            notesContent.insert(END, text)
    except FileNotFoundError:
        notesContent.insert(END, 'File not found')

def resetNotes():
    notesContent.delete('1.0', END)

def addTask():
    global counter
    task = simpledialog.askstring('+', 'Enter your task:')
    if task:
        tasks.insert('', END, values=(counter, task))
        counter += 1

def removeTask():
    global counter
    selected = tasks.selection()
    if selected:
        tasks.delete(selected)
        counter -= 1

def calcTime():
    global startTime
    startTime = time.time()
    workingTime['text'] = f'Started working at {time.strftime("%H:%M:%S")}'

def endTime():
    global startTime
    endTime  = time.time()
    if startTime != 0:
        workingTime['text'] = f'Worktime ended at {time.strftime("%H:%M:%S")} \n You have worked for: {(endTime - startTime)//60} mins, {round((endTime - startTime), 2)} secs'
        startTime = 0
    else:
        workingTime['text'] = 'Click `Start working day` button to start'
    

mainTab = Tk()
mainTab.configure(background= '#f4acb7')
icon = 'icon.ico'
mainTab.iconbitmap(icon)
mainTab.title('Notebook')

notebook = ttk.Notebook(mainTab)
notebook.pack(expand=True, fill='both')

notesFrame = Frame(notebook, bg= '#fcd5ce')
notebook.add(notesFrame, text='Notes')
notesContent = Text(notesFrame, wrap='word', height=10, width=50,  bg= '#f4acb7', font='Montressat')
notesContent.pack(padx=10, pady=10)
saveButton = Button(notesFrame, text='Save notes', width=14, height=1,bg='#f4acb7', command=saveNotes).pack(pady=3)

loadButton = Button(notesFrame, text='Load notes', width=14, height=1, bg='#f4acb7', command=loadNotes).pack(pady=3)
resetButton = Button(notesFrame, text='Clear notes', width=14, height=1, bg='#f4acb7', command=resetNotes).pack(pady=3)

taskFrame = Frame(notebook, bg= '#fcd5ce')
notebook.add(taskFrame, text='Todo list')
tasks = ttk.Treeview(taskFrame, columns=('Counter', 'Task'), show='headings')
tasks.heading('Counter', text='№', anchor=CENTER)
tasks.heading('Task', text='Task', anchor=CENTER)
tasks.pack(padx=10, pady=10)
addButton = Button(taskFrame, text='Add task', width=14, height=1, bg='#f4acb7', command=addTask).pack(pady=3)
deleteButton = Button(taskFrame, text='Remove task', width=14, height=1, bg='#f4acb7', command=removeTask).pack(pady=3)

workFrame= Frame(notebook, bg= '#fcd5ce')
notebook.add(workFrame, text='Working hours')
workingTime = Label(workFrame, text="You haven't worked today", anchor=CENTER, bg= '#fcd5ce')
workingTime.pack(pady=10)
startButton= Button(workFrame, text='Start working day', bg='#f4acb7',command=calcTime).pack(pady=3)
endButton = Button(workFrame, text='End working day', bg='#f4acb7', command=endTime).pack(pady=3)

mainTab.mainloop()