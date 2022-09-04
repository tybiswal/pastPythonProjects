import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'You Fool!', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 100, window=label1)
    label2 = tk.Label(root, text= 'Who Clicks A Big Red Button?', fg='red', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label2)

    
button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()