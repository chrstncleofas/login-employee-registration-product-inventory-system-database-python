from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql


class Database_User_Interface:
    def __init__(self, root):

        self.root = root
        self.root.title("Product Inventory System Application")
        self.root.withdraw()
        x = (self.root.winfo_screenwidth() -
             self.root.winfo_reqwidth()) / 10
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 30
        self.root.geometry("1130x665+%d+%d" % (x, y))

        # Head Label
        self.lbl_title = Label(
            self.root, text="Product Inventory Database System", bd=4, fg="white", relief=RIDGE,  bg="#fc5c00", font=("roboto sans-serif", 23), pady=7)
        self.lbl_title.pack(side=TOP, fill=X)

        # Frame Table
        self.detail_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.detail_frame.place(x=0, y=390, width=1130, height=276)

        # Frame Input
        self.txt_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="navy")
        self.txt_frame.place(x=0, y=55, width=1130, height=340)

        # Buttons Frame
        self.btn_frame = Frame(
            self.detail_frame, bd=3, relief=RIDGE, bg="navy")
        self.btn_frame.place(x=0, y=170, width=1122, height=98)

        # Button Here
        # Space for Buttons
        self.space_label = Label(self.btn_frame, text='',
                                 font=('', 10), bg="navy", fg="white").grid(row=1, column=2, pady=20, padx=5)
        # Edit
        self.edit_btn = Button(self.btn_frame, text='Change', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                               font=("roboto sans-serif", 13, "bold"), command=self.update_item)
        self.edit_btn.grid(row=1, column=3, pady=20, padx=10)

        # Delete
        self.delete_btn = Button(self.btn_frame, text='Delete', width=24, height=2, bd=2, relief=FLAT, bg="#fc5c01", fg="white",
                                 font=("roboto sans-serif", 13, "bold"), command=self.delete_item)
        self.delete_btn.grid(row=1, column=4, pady=20, padx=10)

        # Back
        self.bck_btn = Button(self.btn_frame, text='Back', width=24, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                              font=("roboto sans-serif", 13, "bold"), command=self.back)
        self.bck_btn.grid(row=1, column=5, padx=12)

        # Exit
        self.exit_btn = Button(self.btn_frame, text='Exit', width=24, height=2, bg="#fc5c01", fg="white", bd=2, relief=FLAT,
                               font=("roboto sans-serif", 13, "bold"), command=self.exit)
        self.exit_btn.grid(row=1, column=6, padx=12)

        # Space
        self.space_label = Label(self.txt_frame, text='',
                                 font=('', 10), bg="navy", fg="white").grid(row=0, column=2, pady=10, sticky=W, padx=43)
        # ID
        self.id_text = StringVar()
        self.id_label = Label(self.txt_frame, text='ID Number :',
                              font=('bold', 14), bg="navy", fg="white").grid(row=1, column=0, sticky=W, padx=55)
        self.id_entry = Entry(
            self.txt_frame, textvariable=self.id_text, width=25, bd=3, font=("bold", 15))
        self.id_entry.grid(row=1, column=1)

        # Product
        self.product_text = StringVar()
        self.product_label = Label(self.txt_frame, text='Product Name :',
                                   font=('bold', 14), bg="navy", fg="white").grid(row=2, column=0, sticky=W, padx=52)
        self.product_entry = Entry(
            self.txt_frame, textvariable=self.product_text, width=25, bd=3, font=("bold", 15))
        self.product_entry.grid(row=2, column=1)

        # Customer
        self.customer_text = StringVar()
        self.customer_label = Label(self.txt_frame, text='Customer Name :', font=(
            'bold', 14), bg="navy", fg="white").grid(row=1, column=2, sticky=W, padx=50)
        self.customer_entry = Entry(self.txt_frame, textvariable=self.customer_text,
                                    width=25, bd=3, font=("bold", 15))
        self.customer_entry.grid(row=1, column=3)

        # Retailer
        self.retailer_text = StringVar()
        self.retailer_label = Label(self.txt_frame, text='Retailer Name :', font=(
            'bold', 14), bg="navy", fg="white").grid(row=3, column=0, sticky=W, padx=50)
        self.retailer_entry = Entry(self.txt_frame, textvariable=self.retailer_text,
                                    width=25, bd=3, font=("bold", 15))
        self.retailer_entry.grid(row=3, column=1)

        # Price
        self.price_text = StringVar()
        self.price_label = Label(self.txt_frame, text='Product Price :', font=('bold', 14),
                                 bg="navy", fg="white").grid(row=2, column=2, sticky=W, padx=50, pady=20)
        self.price_entry = Entry(self.txt_frame, textvariable=self.price_text,
                                 width=25, bd=3, font=("bold", 15))
        self.price_entry.grid(row=2, column=3)

        # City
        self.city_text = StringVar()
        self.city_label = Label(self.txt_frame, text='Customer City :', font=('bold', 14),
                                bg="navy", fg="white").grid(row=4, column=0, sticky=W, padx=50,  pady=20)
        self.city_entry = Entry(self.txt_frame, textvariable=self.city_text,
                                width=25, bd=3, font=("bold", 15))
        self.city_entry.grid(row=4, column=1)

        # Province
        self.province_text = StringVar()
        self.province_label = Label(self.txt_frame, text='Province :', font=('bold', 14),
                                    bg="navy", fg="white").grid(row=5, column=0, sticky=W, padx=50)
        self.province_entry = Entry(self.txt_frame, textvariable=self.province_text,
                                    width=25, bd=3, font=("bold", 15))
        self. province_entry.grid(row=5, column=1)

        # Gender
        self.gender_text = StringVar()
        self.gender_label = Label(self.txt_frame, text='Gender :', font=('bold', 14),
                                  bg="navy", fg="white").grid(row=3, column=2, sticky=W, padx=50)
        self.gender_entry = Entry(self.txt_frame, textvariable=self.gender_text,
                                  width=25, bd=3, font=("bold", 15))
        self.gender_entry.grid(row=3, column=3)

        # Age
        self.age_text = StringVar()
        self.age_label = Label(self.txt_frame, text='Age :', font=('bold', 14),
                               bg="navy", fg="white").grid(row=4, column=2, sticky=W, padx=50)
        self.age_entry = Entry(self.txt_frame, textvariable=self.age_text,
                               width=25, bd=3, font=("bold", 15))
        self.age_entry.grid(row=4, column=3)

        # Listbox Frame
        self.list_frame = Frame(
            self.detail_frame, bd=2, relief=RIDGE, bg="navy")
        self.list_frame.place(x=0, y=0, width=1122, height=170)

        # Treeview Scrollbar
        scroll_x = Scrollbar(self.list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.list_frame, orient=VERTICAL)

        # Treeview
        self.data_list = ttk.Treeview(self.list_frame, height=12, columns=(
            "id", "product", "customer", "retailer", "price", "city", "province", "gender", "age"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.data_list.configure(yscrollcommand=scroll_x.set)
        scroll_x.configure(command=self.data_list.xview)

        self.data_list.configure(yscrollcommand=scroll_y.set)
        scroll_y.configure(command=self.data_list.yview)

        self.data_list.heading("id", text="ID")
        self.data_list.heading("product", text="Product Name")
        self.data_list.heading("customer", text="Customer Name")
        self.data_list.heading("retailer", text="Retailer Name")
        self.data_list.heading("price", text="Price")
        self.data_list.heading("city", text="City")
        self.data_list.heading("province", text="Province")
        self.data_list.heading("gender", text="Gender")
        self.data_list.heading("age", text="Age")

        self.data_list['show'] = 'headings'

        self.data_list.column("id", width=20)
        self.data_list.column("product", width=160)
        self.data_list.column("customer", width=146)
        self.data_list.column("retailer", width=140)
        self.data_list.column("price", width=66)
        self.data_list.column("city", width=80)
        self.data_list.column("province", width=80)
        self.data_list.column("gender", width=50)
        self.data_list.column("age", width=30)

        self.data_list.pack(fill=BOTH, expand=1)

        self.data_list.bind('<ButtonRelease-1>', self.select_item)

        # To show all Data in Treeview
        self.populate_data()

    # Database Function
    def populate_data(self):
        con = pymysql.connect(
            host="localhost", user="root", password="", database="register")
        cur = con.cursor()

        cur.execute("select * from crud")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.data_list.delete(*self.data_list.get_children())
            for row in rows:
                self.data_list.insert('', END, values=row)
            con.commit()
        con.close()

    def update_item(self):
        con = pymysql.connect(
            host="localhost", user="root", password="", database="register")
        cur = con.cursor()
        cur.execute(
            "update crud set product=%s, customer=%s, retailer=%s, price=%s, city=%s, province=%s, gender=%s, age=%s where id=%s",
            (self.product_text.get(),
             self.customer_text.get(),
             self.retailer_text.get(),
             self.price_text.get(),
             self.city_text.get(),
             self.province_text.get(),
             self.gender_text.get(),
             self.age_text.get(),
             self.id_text.get()
             ))
        con.commit()
        messagebox.showinfo("Success", "Update Successfuly")
        self.populate_data()
        self.clear_text()
        con.close()

    def delete_item(self):
        con = pymysql.connect(
            host="localhost", user="root", password="", database="register")
        cur = con.cursor()
        cur.execute("delete from crud where id=%s", self.id_text.get())
        # rows = cur.fetchone()
        con.commit()
        messagebox.askyesno(
            'Gadgets', 'Do you want to delete this file ')
        self.populate_data()
        self.clear_text()
        con.close()

    def select_item(self, ev):
        cursor_row = self.data_list.focus()
        contents = self.data_list.item(cursor_row)
        row = contents['values']
        self.id_text.set(row[0])
        self.product_text.set(row[1])
        self.customer_text.set(row[2])
        self.retailer_text.set(row[3])
        self.price_text.set(row[4])
        self.city_text.set(row[5])
        self.province_text.set(row[6])
        self.gender_text.set(row[7])
        self.age_text.set(row[8])

    def back(self):
        self.root.destroy()
        import field

    def exit(self):
        messagebox.askyesno(
            'Gadgets', 'Do you want to this window ')
        self.root.destroy()

    def clear_text(self):
        self.id_entry.delete(0, END)
        self.product_entry.delete(0, END)
        self.customer_entry.delete(0, END)
        self.retailer_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.province_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.age_entry.delete(0, END)


root = Tk()
obj = Database_User_Interface(root)
root.deiconify()
root.mainloop()
