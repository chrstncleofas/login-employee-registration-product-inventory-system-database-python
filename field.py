from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Field_app:
    def __init__(self, root):

        self.root = root
        self.root.title("Product Fields System Application")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 4
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 5
        self.root.geometry("790x424+%d+%d" % (x, y))
        self.root.resizable(False, False)

        # Head Label
        self.lbl_title = Label(
            self.root, text="Product Field System", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        self.lbl_title.pack(side=TOP, fill=X)

        # Frame
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.txt_frame.place(x=0, y=55, width=790, height=370)

        # Space
        self.product_text = StringVar()
        self.product_label = Label(self.txt_frame, text='',
                                   font=('', 14), pady=10, padx=10, bg="navy", fg="white").grid(row=0, column=0, sticky=W)

        # Product
        self.product = StringVar()
        self.product_label = Label(self.txt_frame, text='Product Name :',
                                   font=('bold', 14), pady=10, padx=14, bg="navy", fg="white").grid(row=1, column=0, sticky=W)
        self.product_entry = Entry(
            self.txt_frame, textvariable=self.product, width=25, bd=3, font=("bold", 11))
        self.product_entry.grid(row=1, column=1)

        # Customer
        self.customer = StringVar()
        self.customer_label = Label(self.txt_frame, text='Customer Name :', font=(
            'bold', 14), padx=10, bg="navy", fg="white").grid(row=1, column=2, sticky=W)
        self.customer_entry = Entry(self.txt_frame, textvariable=self.customer,
                                    width=25, bd=3, font=("bold", 11))
        self.customer_entry.grid(row=1, column=3)

        # Retailer
        self.retailer = StringVar()
        self.retailer_label = Label(self.txt_frame, text='Retailer Name :', font=(
            'bold', 14), padx=12, bg="navy", fg="white").grid(row=2, column=0, sticky=W)
        self.retailer_entry = Entry(self.txt_frame, textvariable=self.retailer,
                                    width=25, bd=3, font=("bold", 11))
        self.retailer_entry.grid(row=2, column=1)

        # Price
        self.price = StringVar()
        self.price_label = Label(self.txt_frame, text='Product Price :', font=('bold', 14),
                                 padx=10, bg="navy", fg="white").grid(row=2, column=2, sticky=W)
        self.price_entry = Entry(self.txt_frame, textvariable=self.price,
                                 width=25, bd=3, font=("bold", 11))
        self.price_entry.grid(row=2, column=3)

        # City
        self.city = StringVar()
        self.city_label = Label(self.txt_frame, text='Customer City :', font=('bold', 14),
                                padx=10, pady=10, bg="navy", fg="white").grid(row=3, column=0, sticky=W)
        self.city_entry = Entry(self.txt_frame, textvariable=self.city,
                                width=25, bd=3, font=("bold", 11))
        self.city_entry.grid(row=3, column=1)

        # Province
        self.province = StringVar()
        self.province_label = Label(self.txt_frame, text='Province :', font=('bold', 14),
                                    padx=10, pady=10, bg="navy", fg="white").grid(row=3, column=2, sticky=W)
        self.province_entry = Entry(self.txt_frame, textvariable=self.province,
                                    width=25, bd=3, font=("bold", 11))
        self. province_entry.grid(row=3, column=3)

        # Gender
        self.gender = StringVar()
        self.gender_label = Label(self.txt_frame, text='Gender :', font=('bold', 14),
                                  padx=10, bg="navy", fg="white").grid(row=4, column=0, sticky=W)
        self.gender_entry = Entry(self.txt_frame, textvariable=self.gender,
                                  width=25, bd=3, font=("bold", 11))
        self.gender_entry.grid(row=4, column=1)

        # Age
        self.age = StringVar()
        self.age_label = Label(self.txt_frame, text='Age :', font=('bold', 14),
                               padx=10, bg="navy", fg="white").grid(row=4, column=2, sticky=W)
        self.age_entry = Entry(self.txt_frame, textvariable=self.age,
                               width=25, bd=3, font=("bold", 11))
        self.age_entry.grid(row=4, column=3)

        # Frame for Buttons
        self.btn_frame = Frame(
            self.txt_frame, bd=2, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=0, y=252, width=781, height=110)

        # Button
        # Space
        self.space_lbl = Label(self.btn_frame, text='',
                               font=('bold', 14), bg="navy", fg="white", padx=25).grid(
            row=1, column=1, sticky=W)

        self.add_btn = Button(self.btn_frame, text='Ok', width=20, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                              font=("roboto sans-serif", 12, "bold"), command=self.add_item)
        self.add_btn.grid(row=1, column=2, pady=26)

        self.delete_btn = Button(self.btn_frame, text='Clear', width=20, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                                 font=("roboto sans-serif", 12, "bold"), command=self.clear_text)
        self.delete_btn.grid(row=1, column=3, padx=22)

        self.view_btn = Button(self.btn_frame, text='View', width=20, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                               font=("roboto sans-serif", 12, "bold"), command=self.view_item)
        self.view_btn.grid(row=1, column=4)

    # Database Function
    def add_item(self):
        if self.product.get() == '' or self.customer.get() == '' or self.retailer.get() == '' or self.price.get() == '' or self.city.get() == '' or self.province.get() == '' or self.gender.get() == '' or self.age.get() == '':
            messagebox.showerror(
                'Required Fields', 'Please include all fields')
            return
        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="register")
            cur = con.cursor()

            cur.execute(
                "insert into crud (product ,customer, retailer, price, city, province, gender, age) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                (self.product.get(),
                 self.customer.get(),
                 self.retailer.get(),
                 self.price.get(),
                 self.city.get(),
                 self.province.get(),
                 self.gender.get(),
                 self.age.get()
                 ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Adding Items Successfuly")
        self.clear_text()
        # self.populate_list()

    def clear_text(self):
        self.product_entry.delete(0, END)
        self.customer_entry.delete(0, END)
        self.retailer_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.province_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.age_entry.delete(0, END)

    def view_item(self):
        self.root.destroy()
        import dbUI


root = Tk()
obj = Field_app(root)
root.deiconify()
root.mainloop()
