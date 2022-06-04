# Tugas Besar 2 Algoritma Lanjut
# Nama : Raka Yuda Pradipta
# NIM : 41519110143

from tkinter import *
from PIL import Image, ImageTk
import node

#show result from finding shortest path
def show_result():
    firstNode = e1.get().upper()
    secondNode = e2.get().upper()
    all_path = node.get_all_path(node.graphNode,firstNode,secondNode)
    shortest_path = node.get_shortest_path(all_path)
    labelValueResult['text'] = shortest_path
    return shortest_path


root = Tk()
root.title("Tugas Besar II")
root.geometry('640x600')

text = Label(root, text='Find shortest way!')
text.grid(row=0, column=0,columnspan=2)

load = Image.open("node-map.png")
render = ImageTk.PhotoImage(load)
labelPhoto = Label(root, image=render)
labelPhoto.grid(row=1, column=0,columnspan=2)

labelImage = Label(root, text='Graph Node Image', pady=20)
labelImage.grid(row=2, column=0,columnspan=2)

labelFirst = Label(root, text='Input first node :')
labelSecond = Label(root, text='Input second node :')
labelFirst.grid(row=3,column=0, sticky=W, padx=76)
labelSecond.grid(row=4,column=0, sticky=W,  padx=76)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=3, column=1, padx=76)
e2.grid(row=4, column=1)

labelTextResult = Label(root, text="Shortest path is :")
labelTextResult.grid(row=5, column=0, columnspan=2, sticky=W,  padx=76, pady=6)


labelValueResult = Label(root, text="")
labelValueResult.grid(row=5, column=1, columnspan=2, sticky=W,  padx=(90,0), pady=6)

Button(root,
          text='Quit',
          command=root.quit).grid(row=6,
                                    column=0,
                                    sticky='news',
                                    padx=(76,12),
                                    pady=12
                                  )

Button(root, text='Show', command=show_result).grid(row=6,
                                                       column=1,
                                                       sticky='news',
                                                       padx=(12,92),
                                                       pady=12
                                                    )


root.mainloop()

