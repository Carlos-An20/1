from tkinter import *
  
window = Tk() 
  
window.title('GFG') 
  
canvas = Canvas(window, width=300, height=200) 
canvas.pack() 
  
canvas.create_line(0, 0, 300, 200) 
canvas.create_line(0, 200, 300, 0) 
  
canvas.create_oval(50, 25, 250, 175, fill="yellow") 
  
window.mainloop()
