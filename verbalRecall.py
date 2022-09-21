'''verbalRecall.py presents a small box for subjects to type in 
words from the previous experiment. It then gives them an option to choose
whether that word was old or new'''

import os
import time
import tkinter as tk
from tkinter import PhotoImage

# query experimenter for subNum and create file name
sessName    = input('Please enter the subject number: ')
currDate    = time.strftime("%Y%m%d")
fileName    = 'cobra1_' + sessName + '_' + currDate
# set the location
savePath = 'C:\\Users\\Owner\\Desktop\\prototypeDat'
completeName = os.path.join(savePath, fileName)
subjectFile = open(completeName + '.txt', 'a')

root = tk.Tk()

#canvas1 = tk.Canvas(root, width = 435, height = 300)
bg = PhotoImage(file = 'cannaPaper.gif')
canvas1 = tk.Canvas(root, width = 870, height = 500, bg='white')
canvas1.create_image(20, 20, anchor='nw', image=bg)

canvas1.pack()

label1 = tk.Label(root, text='Please enter a word from the previous experiment')
#label1.config(font=('helvetica', 14))
label1.config(font=('helvetica', 28),bg='black', fg='white')
#canvas1.create_window(200, 25, window=label1)
canvas1.create_window(440, 80, window=label1)

label2 = tk.Label(root, text='Was this word old or new?')
#label2.config(font=('helvetica', 14))
label2.config(font=('helvetica', 28),bg='black', fg='white')
#canvas1.create_window(200, 125, window=label2)
canvas1.create_window(440, 280, window=label2)


entry1 = tk.Entry(root, font=('helvetica', 20)) 
#canvas1.create_window(200, 75, window=entry1)
canvas1.create_window(440, 180, window=entry1)


entry2 = tk.Entry(root, font=('helvetica', 20))
#canvas1.create_window(200, 175, window=entry2)
canvas1.create_window(440, 380, window=entry2)


def logicEngine(event):
    word  = entry1.get()
    oldNew = entry2.get()
    subjectFile.write(word + ',' + oldNew + '\n')
    entry1.delete(0, "end")
    entry2.delete(0, "end")

# using enter and tab to navigate since subject won't have a mouse
root.bind('<Return>', logicEngine)
#button1 = tk.Button(text='Submit', command=logicEngine, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
#canvas1.create_window(200, 225, window=button1)

root.mainloop()

subjectFile.close()




    
    