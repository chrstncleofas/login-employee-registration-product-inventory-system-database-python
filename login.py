from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Employee Form")

        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2.6
        y = (self.root.winfo_screenheight() -
             self.root.winfo_reqheight()) / 2.9
        self.root.geometry("390x320+%d+%d" % (x, y))

        self.root.resizable(False, False)

        # Frames
        self.title_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.title_frame.place(x=0, y=0, width=391, height=331)

        # Title Head
        self.lbl_title = Label(
            self.title_frame, text="Login Form", bd=4, relief=RIDGE,  bg="navy", fg="#fc5c00", font=("roboto sans-serif", 23), pady=14)
        self.lbl_title.pack(side=TOP, fill=X)

        # Form Frame
        self.form_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.form_frame.place(x=0, y=75, width=391, height=250)

        # Space to be Center lahat ng input build
        self.fname_label = Label(self.form_frame, text='',
                                 font=('bold', 14), bg="navy", fg="white", padx=15, pady=2).grid(row=2, column=2, sticky=W)
        # Username
        self.username_text = StringVar()
        self.username_label = Label(self.form_frame, text='Username :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=5, pady=10).grid(
            row=3, column=3, sticky=W)
        self.username_entry = Entry(
            self.form_frame, textvariable=self.username_text, width=30, bd=5)
        self.username_entry.grid(row=3, column=4)

        # Password
        self.password_text = StringVar()
        self.password_label = Label(self.form_frame, text='Password :',
                                    font=("roboto sans-serif", 14), bg="navy", fg="white", padx=5, pady=14).grid(
            row=4, column=3, sticky=W)
        self.password_entry = Entry(
            self.form_frame, textvariable=self.password_text, width=30, bd=5, show="*")
        self.password_entry.grid(row=4, column=4)

        # Buttons and Frame
        # Frame
        self.btn_frame = Frame(
            self.form_frame, bd=2, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=0, y=150, width=382, height=90)

        # Space Label para ma-move down
        self.space_lbl = Label(self.btn_frame, text='',
                               bg="navy", padx=12).grid(row=2, column=0)

        # Buttons
        self.register_btn = Button(self.btn_frame, text='Login Now', width=15, height=2,  bd=2,
                                   relief=FLAT, bg="#fc5c01", fg="white", command=self.fields, font=("roboto sans-serif", 10, "bold"))
        self.register_btn.grid(row=2, column=1, padx=19, pady=23)

        self.back_btn = Button(self.btn_frame, text='Register Now', width=15, height=2,
                               bg="#fc5c01", fg="white", bd=2, relief=FLAT, command=self.register, font=("roboto sans-serif", 10, "bold"))
        self.back_btn.grid(row=2, column=2)

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    # Para makapasok sa crud page
    def fields(self):

        if self.username_entry.get() == '' or self.password_entry.get() == '':
            messagebox.showerror(
                'Required Fields', 'Please include all fields')
            self.clear()
        else:
            try:
                con = pymysql.connect(
                    host="localhost", user="root", password="", database="register")
                cur = con.cursor()
                cur.execute("select * from user where username=%s and password=%s",
                            (self.username_text.get(), self.password_text.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror(
                        'Error', 'Undefined Username and Password, Please Try Again Later')
                    self.clear()
                else:
                    messagebox.showinfo(
                        'Success', 'Welcome to Product Database')
                    self.clear()
                    self.root.destroy()
                    import field
                con.close()
            except Exception as es:
                messagebox.showerror(
                    'Error', f'Error due to: {str(es)}')

    # para makapasok sa register page

    def register(self):

        self.root.destroy()
        import register


root = Tk()
obj = Login(root)
root.deiconify()
root.mainloop()
