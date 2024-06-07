from tkinter import *
from tkinter import ttk
from PIL import Image,ImageDraw, ImageFont, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
    
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,'bold'),bg="blue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        img_top=Image.open(r"college_images\Help.jpeg")
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)
        
        help_label=Label(f_label,text="Email:bdsaditya56@gmail.com",font=("times new roman",20,'bold'),fg='blue',bg='white')
        help_label.place(x=580,y=350)
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()