#!/usr/bin/env python3
import chonkify
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

ws = tk.Tk()
ws.title('Chonky Text Filter')
ws.geometry('600x440')
ws.config()

struggle = tk.DoubleVar(value=.50)
lisp = tk.DoubleVar(value=.50)
stutter = tk.DoubleVar(value=.50)
slur = tk.DoubleVar(value=.50)
vowels = tk.DoubleVar(value=.50)
eating = tk.DoubleVar(value=.50)
extragas = tk.DoubleVar(value=0)
gas = tk.IntVar(value=1)

def chonkit():
  chonk = chonkify.Chonkify(struggle.get(),lisp.get(),stutter.get(),slur.get(),
                            vowels.get(),eating.get(),gas.get(),extragas.get())
  output.delete('1.0', tk.END)
  output.insert(tk.END, chonk.chonkify(input.get(1.0, "end-1c")))

fs = tk.Frame(ws)
fs.columnconfigure(2, weight=1)
tk.Label(fs,text="Struggle").grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=struggle).grid(column=1,row=0,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Lisp").grid(column=0,row=1,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=lisp).grid(column=1,row=1,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Stutter").grid(column=0,row=2,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=stutter).grid(column=1,row=2,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Slur").grid(column=0,row=3,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=slur).grid(column=1,row=3,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Vowels").grid(column=0,row=4,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=vowels).grid(column=1,row=4,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Eating").grid(column=0,row=5,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=eating).grid(column=1,row=5,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Extra Gas").grid(column=0,row=6,sticky=tk.W,padx=5,pady=5)
tk.Spinbox(fs, width=5, from_=0, to=1, increment=0.01, textvariable=extragas).grid(column=1,row=6,sticky=tk.E,padx=5,pady=5)
tk.Label(fs,text="Gas").grid(column=0,row=7,sticky=tk.W,padx=5,pady=5)
tk.Checkbutton(fs, variable=gas).grid(column=1,row=7,sticky=tk.E,padx=5,pady=5)
fs.pack(expand= True)

input = ScrolledText(fs,width=200,height=5)
input.insert("end","Type your message here...")
input.grid(column=2,row=0,rowspan=4,sticky='EWNS',padx=5,pady=5)

tk.Button(fs,text='Chonkify',command=chonkit).grid(column=2,row=4,sticky=tk.E)

output = ScrolledText(fs,width=200,height=60)
fs.rowconfigure(14, weight=1)
output.grid(column=2,row=5,rowspan=10,sticky='EWNS',padx=5,pady=5)

ws.mainloop()
