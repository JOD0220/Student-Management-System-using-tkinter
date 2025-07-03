from tkinter import *
from tkinter import ttk
import hashlib
import pymysql
from tkinter import messagebox
import tkinter as tk

class AdminLoginPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Admin Login")
        self.master.geometry("1900x1000+1+0")

        label_font = ('Arial', 24)
        self.label_username = tk.Label(master, text="Username:", font=label_font)
        self.label_password = tk.Label(master, text="Password :", font=label_font)

        self.label_username.place(relx=0.4, rely=0.4, anchor=tk.CENTER)
        self.label_password.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

        self.entry_username = tk.Entry(master,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        self.entry_password = tk.Entry(master, show="*", font=("times new roman",15,"bold"),bd=10,relief=GROOVE)

        self.entry_username.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
        self.entry_password.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

        self.logbtn = tk.Button(master, text="Login", command=self._login_btn_clicked, font=("times new roman",30,"bold"),bd=5,relief=GROOVE)
        self.logbtn.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        # handle closing of window
        self.master.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _login_btn_clicked(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username.strip() == "" or password.strip() == "":
            print("Username or password field is empty.")
            messagebox.showerror("Error", "All fields are required!!")
            return

        elif username == "admin" and password == "123":
            print("Login successful!")
            self.entry_password.delete(2, 'end') 
            messagebox.showinfo("Congratulations","Login Successful!!")
            self.master.destroy()

        else:
            print("Login failed.")
            self.entry_password.delete(0, 'end')  # Clear the password field
            messagebox.showerror("Error", "Invalid username or password!!")
            self.master.destroy()
            exit()

    # handle closing of window
    def _on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()
            exit()


root = tk.Tk()
login_page = AdminLoginPage(root)
root.mainloop()

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("THE PYTRONIC DATABASE")
        self.root.geometry("1920x1080+0+0")      

        title=Label(self.root,text="THE PYTRONIC DATABASE",bd=10,relief=GROOVE,font=("times new roman",50,"bold"),bg="navy",fg="white")
        title.pack(side=TOP,fill=X)

        #Vairables
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        self.search_by=StringVar()
        self.search_txt=StringVar()


        #Manage_Frame
        Manage_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="navy")
        Manage_Frame.place(x=10,y=110,width=700,height=900)

        m_title=Label(Manage_Frame,text="Manage Students",bg="navy",fg="white",font=("times new roman",50,"bold"))
        m_title.grid(row=0,columnspan=5,pady=20,padx=50)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_roll.grid(row=1,column=0,pady=20,padx=60,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=20,padx=60,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_name.grid(row=2,column=0,pady=20,padx=60,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=20,padx=60,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_Email.grid(row=3,column=0,pady=20,padx=60,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=20,padx=60,sticky="w")

        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=20,padx=60,sticky="w")
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"))
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=60,pady=20)

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=20,padx=60,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=20,padx=60,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="Result",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=20,padx=60,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=10,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=20,padx=60,sticky="w")

        
        lbl_Address=Label(Manage_Frame,text="Address",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_Address.grid(row=9,column=0,pady=20,padx=60,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("times new roman",11))
        self.txt_Address.grid(row=9,column=1,pady=20,padx=60,sticky="w")
        
        #Button_frame        
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="navy")
        btn_Frame.place(x=50,y=800,width=500)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=20,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=20,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=20,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=20,pady=10)

#=====Detail Frame=========
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="navy")
        Detail_Frame.place(x=720,y=110,width=1185,height=900)


        lbl_search=Label(Detail_Frame,text="Search By",bg="navy",fg="white",font=("times new roman",30,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")


        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",20,"bold"),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=15,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=15,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="navy")
        Table_Frame.place(x=15,y=70,width=1150,height=810)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="Result")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    def add_students(self):
        if self.Roll_No_var.get()==""or self.name_var.get()=="":
                messagebox.showerror("Error","All fields are required!!!")
        else:
                con = pymysql.connect(host="localhost",user="root",password="",database="stm")    
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_Address.get('1.0',END)
                                                                        ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")  
    def fetch_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm")    
        cur=con.cursor()
        cur.execute("select * from students"),
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(* self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var .set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)
    
    def get_cursor(self,ev):
        curosor_row = self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var .set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                        self.name_var.get(),
                                                                        self.email_var.get(),
                                                                        self.gender_var.get(),
                                                                        self.contact_var.get(),
                                                                        self.dob_var.get(),
                                                                        self.txt_Address.get('1.0',END),
                                                                        self.Roll_No_var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")    
        cur=con.cursor()

        query = "select * from students where "+self.search_by.get().lower()+" LIKE '"+str(self.search_txt.get())+"%'"
        print(query)

        cur.execute(query)
        rows=cur.fetchall()
        print(rows)
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        con.commit()
        con.close()


        
root=Tk()
ob=Student(root)
root.mainloop()