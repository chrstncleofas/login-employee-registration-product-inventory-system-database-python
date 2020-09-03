from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Registration Form")

        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.9
        y = (self.root.winfo_screenheight() -
             self.root.winfo_reqheight()) / 4.4
        self.root.geometry("530x470+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # Title Head
        self.lbl_title = Label(
            self.root, text="Registration Form", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        self.lbl_title.pack(side=TOP, fill=X)

        # Frames
        self.title_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.title_frame.place(x=0, y=55, width=530, height=417)

        # Space to be Center lahat ng input build
        self.fname_label = Label(self.title_frame, text='',
                                 font=('bold', 14), bg="navy", fg="white", padx=12, pady=20).grid(
                                     row=2, column=2, sticky=W)

        # Firstname
        self.fname_text = StringVar()
        self.fname_label = Label(self.title_frame, text='First Name :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
                                     row=2, column=3, sticky=W)

        self.fname_entry = Entry(
            self.title_frame, textvariable=self.fname_text, width=32, bd=3,
            font=("bold", 10))
        self.fname_entry.grid(row=2, column=4)

        # Last Name
        self.lname_text = StringVar()
        self.lname_label = Label(self.title_frame, text='Last Name :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
            row=3, column=3, sticky=W)
        self.lname_entry = Entry(
            self.title_frame, textvariable=self.lname_text, width=32, bd=3,
            font=("bold", 10))
        self.lname_entry.grid(row=3, column=4)

        # Username
        self.username_text = StringVar()
        self.username_label = Label(self.title_frame, text='Username :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
            row=4, column=3, sticky=W)
        self.username_entry = Entry(
            self.title_frame, textvariable=self.username_text, width=32, bd=3,
            font=("bold", 10))
        self.username_entry.grid(row=4, column=4)

        # Email
        self.email_text = StringVar()
        self.email_label = Label(self.title_frame, text='Email :',
                                 font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
                                     row=5, column=3, sticky=W)
        self.email_entry = Entry(
            self.title_frame, textvariable=self.email_text, width=32, bd=3,
            font=("bold", 10))
        self.email_entry.grid(row=5, column=4)

        # Password
        self.password_text = StringVar()
        self.password_label = Label(self.title_frame, text='Create Password :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10, pady=20).grid(
            row=6, column=3, sticky=W)
        self.password_entry = Entry(
            self.title_frame, textvariable=self.password_text, width=32, bd=3, show="*",
            font=("bold", 10))
        self.password_entry.grid(row=6, column=4)

        # Confirm Password
        self.cpassword_text = StringVar()
        self.cpassword_label = Label(self.title_frame, text='Confirm Password :',
                                     font=("roboto sans-serif", 14), bg="navy", fg="white", padx=10).grid(
            row=7, column=3, sticky=W)
        self.cpassword_entry = Entry(
            self.title_frame, textvariable=self.cpassword_text, width=32, bd=3, show="*",
            font=("bold", 10))
        self.cpassword_entry.grid(row=7, column=4)

        # Space to be Center lahat ng input build
        self.space_lbl = Label(self.title_frame, text='',
                               font=('bold', 14), bg="navy", fg="white", padx=20).grid(
            row=8, column=2, sticky=W)

        # Frames para sa Buttons
        # Frames
        self.btn_frame = Frame(
            self.title_frame, bd=2, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=0, y=300, width=523, height=110)

        # Space Label para ma-move down
        self.space_lbl = Label(self.btn_frame, text='',
                               font=('bold', 14), bg="navy", fg="white", padx=32).grid(
            row=1, column=2, sticky=W)

        # Buttons
        self.register_btn = Button(self.btn_frame, text='Register Now', command=self.register_data, width=15, height=2,  bd=2,
                                   relief=FLAT, bg="#fc5c01", fg="white", font=("roboto sans-serif", 12, "bold"))
        self.register_btn.grid(row=2, column=3, padx=19)

        self.back_btn = Button(self.btn_frame, text='Back', width=15, height=2,
                               bg="#fc5c01", fg="white", bd=2, relief=FLAT, command=self.login_field, font=("roboto sans-serif", 12, "bold"))
        self.back_btn.grid(row=2, column=4)

    # Para bumalik sa Login Page
    def login_field(self):
        self.root.destroy()
        import login

    def clear(self):
        self.fname_entry.delete(0, END)
        self.lname_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.cpassword_entry.delete(0, END)

    # Para Ma-insert sa Register Table

    def register_data(self):

        # error trap lng naman
        if self.fname_text.get() == '' or self.lname_text.get() == '' or self.username_text.get() == '' or self.email_text.get() == '' or self.password_text.get() == '' or self.cpassword_text.get() == '':
            messagebox.showerror(
                'Required Fields', 'Please include all fields')
            self.clear()

        elif self.password_text.get() != self.cpassword_text.get():
            messagebox.showerror(
                'Error', 'Password should be same of Confirm Password')
            self.clear()
        # para mapunta sa database
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="register")
                cur = con.cursor()
                cur.execute("select * from user where email=%s",
                            self.email_text.get())
                row = cur.fetchone()

                # pag may dati ka ng email na pinang-register di niya i aallow ung email dapat new
                if row != None:
                    messagebox.showerror(
                        'Error', 'Your Email is Already Exist ')

                # Para pumasok sa database
                else:
                    cur.execute(
                        "insert into user (fname,lname,username,email,password) values(%s,%s,%s,%s,%s)",
                        (self.fname_text.get(),
                         self.lname_text.get(),
                         self.username_text.get(),
                         self.email_text.get(),
                         self.password_text.get()
                         ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfully")

            except Exception as es:
                messagebox.showerror(
                    'Error', f'Error due to: {str(es)}')

            # Clear
            self.clear()


root = Tk()
obj = Register(root)
root.deiconify()
root.mainloop()
