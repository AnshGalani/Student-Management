import imp
from logging import root
from operator import imod
from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import ttk,messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1530x800+0+0")
        
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
        
        btn_exit=Button(self.root,text="Exit",command=self.exit,font=("times new roman",20,"bold"),bg="crimson",fg="white",cursor="hand2").place(x=1365,y=15,height=50,width=150)
        
        #===================All Variable==========================
        
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        self.searchby_var=StringVar()
        self.searchtxt_var=StringVar()
        
        #===================Manage Frame==============================
        
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=650)
        
        m_title=Label(Manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state="readonly")
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
        
        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_dob=Label(Manage_Frame,text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        
        self.txt_Address=Text(Manage_Frame,width=21,height=4,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        #=================Button====================
       
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=570,width=420)
        
        Addbtn=Button(btn_Frame,text="Add",command=self.add_student,width=10,cursor="hand2",font=("times new roman",10)).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",command=self.update,width=10,cursor="hand2",font=("times new roman",10)).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",command=self.delete,width=10,cursor="hand2",font=("times new roman",10)).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",command=self.clear,width=10,cursor="hand2",font=("times new roman",10)).grid(row=0,column=3,padx=10,pady=10)
       
        #===================Detail Frame==============================
        
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=1000,height=650)
    
        lbl_Search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,width=15,textvariable=self.searchby_var,font=("times new roman",14,"bold"),state="readonly")
        combo_search['values']=("Select","roll_no","name","contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search=Entry(Detail_Frame,textvariable=self.searchtxt_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=Button(Detail_Frame,command=self.search,text="Search",width=15,cursor="hand2",font=("times new roman",14)).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,command=self.show_all,text="Show All",width=15,cursor="hand2",font=("times new roman",14)).grid(row=0,column=4,padx=10,pady=10)
       
        #=========Table Frame=======================
        
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=970,height=560)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll_no","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll_no",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        
        self.Student_table['show']='headings'
        
        self.Student_table.column("roll_no",width=100)
        self.Student_table.column("name",width=150)
        self.Student_table.column("email",width=150)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=150)
        self.Student_table.column("dob",width=150)
        self.Student_table.column("address",width=150)
        
        self.Student_table.pack(fill=BOTH,expand=1)
        
        self.Student_table.bind("<ButtonRelease-1>",self.get_data)
          
        self.show() 
        
        #===================Footer===========================
        
        footer=Label(self.root,text="Student Management System | Developed By Ansh\nFor Any Technical Issue Contact: anshgalani@yahoo.com",font=("times new roman",13,"bold"),bg="#4d636d",fg="white",bd=3,relief=GROOVE).place(x=0,y=750,height=50,width=1535)
    
    #=========================Add Button==============================
     
    def add_student(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.Roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
                messagebox.showerror("Error","All Filed Are Required",parent=self.root)
            else:
                cur.execute("Select * from student where roll_no=?",(self.Roll_no_var.get(),))
                row=cur.fetchone()
            if row!=None:
                    messagebox.showerror("Error","This Student Roll No already assigned , try Different",parent=self.root)
            else:
                cur.execute("Insert into student (roll_no,name,email,gender,contact,dob,address) values(?,?,?,?,?,?,?)",(
                                        self.Roll_no_var.get(),
                                        self.name_var.get(),
                                        self.email_var.get(),
                                        self.gender_var.get(),
                                        self.contact_var.get(),
                                        self.dob_var.get(),
                                        self.txt_Address.get('1.0',END)            
                                ))
                con.commit()
                messagebox.showinfo("Success","Student Addedd Successfully",parent=self.root)  
                self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
    #===========================Show Data============================================
    def show(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    #=========================Show Data in Manage Student===========================
    
    def get_data(self,ev):
        f=self.Student_table.focus()
        content=(self.Student_table.item(f)) 
        row=content['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6])          
        
    #=============================Delete Button===================================
    
    def delete(self):            
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.Roll_no_var.get()=="":
                messagebox.showerror("Error","Student Roll No. Must be required",parent=self.root)
            else:
                cur.execute("Select * from student where roll_no=?",(self.Roll_no_var.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Roll No.",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:    
                        cur.execute("delete from student where roll_no=?",(self.Roll_no_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student Delete Successfully",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
          
    #========================Clear==========================
    
    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete('1.0',END)  
        self.searchby_var.set("Select")
        self.searchtxt_var.set("")        
        self.show()   
        
    #================================Update=============================
    
    def update(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.Roll_no_var.get()=="":
                messagebox.showerror("Error","Student Roll No. Must be required",parent=self.root)
            else:
                cur.execute("Select * from student where roll_no=?",(self.Roll_no_var.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Roll No.",parent=self.root)
                else:
                    cur.execute("Update student set name=?,email=?,gender=?,contact=?,dob=?,address=? where roll_no=?",(
                                        self.name_var.get(),
                                        self.email_var.get(),
                                        self.gender_var.get(),
                                        self.contact_var.get(),
                                        self.dob_var.get(),
                                        self.txt_Address.get('1.0',END),
                                        self.Roll_no_var.get()         
                                ))
                    con.commit()
                    messagebox.showinfo("Success","Student Update Successfully",parent=self.root)  
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    #===========================Search=======================
    
    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.searchby_var.get()=="Select":
                messagebox.showerror("Error","Select Search Option",parent=self.root)
            elif self.searchtxt_var.get=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from student where "+self.searchby_var.get()+" LIKE '%"+self.searchtxt_var.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for row in rows:
                        self.Student_table.insert('',END,values=row) 
                else:
                    messagebox.showerror("Error","No Record found...!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    
    #=========================Show All=================================
        
    def show_all(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            #cur.execute("select pid,name,price,qty,status from product where status='Active'")
            cur.execute("select * from student")
            rows=cur.fetchall()
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
    #==================Exit=====================
    
    def exit(self):
        self.root.destroy()  
            
root=Tk()
ob=Student(root)
root.mainloop()