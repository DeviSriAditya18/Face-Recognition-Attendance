from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        # First Image
        img=Image.open(r"college_images\s10.jpeg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=800,height=200)
        
        # Second Image
        img1=Image.open(r"college_images\s11.jpeg")
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=800,y=0,width=800,height=200)
        
        # BG Image
        img3=Image.open(r"college_images\AI.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,'bold'),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Student Attendance Details",font=("times new roman",13,'bold'))
        Left_frame.place(x=10,y=10,width=730,height=580)
        
        img_left=Image.open(r"college_images\s12.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_label=Label(Left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)
        
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=0,y=135,width=720,height=370)
        
        # Label and Entry
        # Attendance id
        attendanceId_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 13, 'bold'), bg='white')
        attendanceId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)
        
        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,'bold'))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("times new roman", 13, 'bold'), bg='white')
        roll_label.grid(row=0, column=2, padx=10,pady=5,sticky=W)
        
        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,'bold'))
        roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 13, 'bold'), bg='white')
        name_label.grid(row=1, column=0, padx=10,pady=5,sticky=W)
        
        name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,'bold'))
        name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Department
        dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 13, 'bold'), bg='white')
        dep_label.grid(row=1, column=2, padx=10,pady=5,sticky=W)
        
        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,'bold'))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 13, 'bold'), bg='white')
        time_label.grid(row=2, column=0, padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,'bold'))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 13, 'bold'), bg='white')
        date_label.grid(row=2, column=2, padx=10,pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,'bold'))
        date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        # Attendance Status
        attenst_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, 'bold'), bg='white')
        attenst_label.grid(row=3, column=0, padx=10,pady=5,sticky=W)
        
        # attenst_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",13,'bold'))
        # attenst_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        attenst_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman", 13, 'bold'), state='read only',width=18)
        attenst_combo['values'] = ('Status', 'Present', 'Absent')
        attenst_combo.current(0)
        attenst_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Buttons Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=300,width=715,height=35)
        
        import_btn=Button(btn_frame,text='Import csv',command=self.importCsv,width=17,font=("times new roman", 13, 'bold'), bg='blue',fg='white')
        import_btn.grid(row=0,column=0)
        
        export_btn=Button(btn_frame,text='Export csv',command=self.exportCsv,width=17,font=("times new roman", 13, 'bold'), bg='blue',fg='white')
        export_btn.grid(row=0,column=1)
        
        update_btn=Button(btn_frame,text='Update',width=17,command=self.update_data,font=("times new roman", 13, 'bold'), bg='blue',fg='white')
        update_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text='Reset',width=17,command=self.reset_data,font=("times new roman", 13, 'bold'), bg='blue',fg='white')
        reset_btn.grid(row=0,column=3)
        
        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text="Attendance Details",font=("times new roman",13,'bold'))
        Right_frame.place(x=750,y=10,width=720,height=580)
        
        # Buttons Frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=700,height=455)
        
        # Scroll Bar Table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Id","Roll","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("Id",text="Attendance ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # Fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    # import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your data exported to"+os.path.basename(fln)+"successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
            
    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    # Update Function
    def update_data(self):
        pass
        
    # Reset Function
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()