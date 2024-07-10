from tkinter import *
import math
import random
import os
from tkinter import messagebox, SUNKEN, Tk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")

        bg_color = "#4A6921"
        Label(self.root, text="STORE BILLING SYSTEM", bd=12, relief=FLAT, bg=bg_color, fg="white",
              font=("times new roman", 30, "bold"), pady=2).pack(fill=X)



        ######variables####

        #####cosmetics#####
        self.body_wash = IntVar()
        self.face_cream = IntVar()
        self.mouthwash = IntVar()
        self.perfume = IntVar()
        self.hair_spray = IntVar()
        self.lotion = IntVar()

        #####grocery#####
        self.rice = IntVar()
        self.bread = IntVar()
        self.salt = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #####soft drink#####
        self.coke = IntVar()
        self.pepsi = IntVar()
        self.fanta = IntVar()
        self.sprite = IntVar()
        self.canada_dry = IntVar()
        self.apple_juice = IntVar()

        ######total price and tax variables#####
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.soft_drink_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.soft_drink_tax = StringVar()

        #####customer details#####
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill = StringVar()

        #####customerframe####
        F1 = LabelFrame(self.root, bd=10, relief=FLAT, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=FLAT).grid(
            row=0, column=1, pady=5, padx=10)

        Label(F1, text="Phone No.", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=FLAT).grid(
            row=0, column=3, pady=5, padx=10)

        Label(F1, text="Bill Number", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=FLAT).grid(
            row=0, column=5, pady=5, padx=10)

        Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(
            row=0, column=6, padx=20, pady=10)

        #####cosmeticframe######
        F2 = LabelFrame(self.root, bd=10, relief=FLAT, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=6, y=180, width=325, height=375)

        Label(F2, text="Body Wash", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.body_wash, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        Label(F2, text="Face cream", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.face_cream, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        Label(F2, text="Mouthwash", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.mouthwash, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        Label(F2, text="Perfume", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.perfume, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        Label(F2, text="Hair Spray", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.hair_spray, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        Label(F2, text="Body Lotion", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(F2, width=10, textvariable=self.lotion, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=5, column=1, padx=10, pady=10)

        ######groceryframe#####
        F3 = LabelFrame(self.root, bd=10, relief=FLAT, text="Grocery", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F3.place(x=360, y=180, width=325, height=375)

        Label(F3, text="Rice", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.rice, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        Label(F3, text="Bread", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.bread, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        Label(F3, text="Salt", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.salt, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        Label(F3, text="Wheat", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.wheat, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        Label(F3, text="Sugar", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.sugar, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        Label(F3, text="Tea", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(F3, width=10, textvariable=self.tea, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=5, column=1, padx=10, pady=10)

        ######softdrinkframe#####
        F4 = LabelFrame(self.root, bd=10, relief=FLAT, text="Soft Drinks", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F4.place(x=715, y=180, width=325, height=375)

        Label(F4, text="Coke", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.coke, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=0, column=1, padx=10, pady=10)

        Label(F4, text="Pepsi", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.pepsi, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=1, column=1, padx=10, pady=10)

        Label(F4, text="Fanta", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.fanta, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=2, column=1, padx=10, pady=10)

        Label(F4, text="Sprite", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.sprite, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=3, column=1, padx=10, pady=10)

        Label(F4, text="Canada Dry", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.canada_dry, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=4, column=1, padx=10, pady=10)

        Label(F4, text="Apple Juice", font=("times new roman", 16, "bold")
              , bg=bg_color, fg="light green").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Entry(F4, width=10, textvariable=self.apple_juice, font=("times new roman", 16, "bold"), bd=5,
              relief=FLAT).grid(row=5, column=1, padx=10, pady=10)

        #####billframe######
        F5 = Frame(self.root, bd=10, relief=FLAT)
        F5.place(x=1000, y=180, width=350, height=380)

        Label(F5, text="Bill Receipt", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        ####totalandtaxframe######
        F6 = LabelFrame(self.root, bd=10, relief=FLAT, text="Bill Menu", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=200)

        Label(F6, text="Total Cosmetic Price", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=FLAT).grid(
            row=0, column=1, padx=10, pady=1)

        Label(F6, text="Total Grocery Price", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=FLAT).grid(
            row=1, column=1, padx=10, pady=1)

        Label(F6, text="Total Soft Drinks Price", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, textvariable=self.soft_drink_price, font="arial 10 bold", bd=7,
              relief=FLAT).grid(row=2, column=1, padx=10, pady=1)

        Label(F6, text="Cosmetic Tax", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, font="arial 10 bold", textvariable=self.cosmetic_tax, bd=7, relief=FLAT).grid(
            row=0, column=3, padx=10, pady=1)

        Label(F6, text="Grocery Tax", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, font="arial 10 bold", textvariable=self.grocery_tax, bd=7, relief=FLAT).grid(
            row=1, column=3, padx=10, pady=1)

        Label(F6, text="Soft Drinks Tax", bg=bg_color, fg="white",
              font=("times new roman", 15, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        Entry(F6, width=18, font="arial 10 bold", textvariable=self.soft_drink_tax, bd=7, relief=FLAT).grid(
            row=2, column=3, padx=10, pady=1)

        btn_F = Frame(F6, bd=7, relief=RAISED)
        btn_F.place(x=760, width=750, height=105)

        Button(btn_F, command=self.total, text="Total", bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=0, padx=5, pady=5)
        Button(btn_F, text="Bill", command=self.bill_area, bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=1, padx=5, pady=5)
        Button(btn_F, text="Clear", command=self.clear_data, bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=2, padx=5, pady=5)
        Button(btn_F, text="Exit", command=self.Exit_app, bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=3, padx=5, pady=5)
        Button(btn_F, text="Email", command=self.Exit_app, bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=4, padx=5, pady=5)
        Button(btn_F, text="Print", command=self.Exit_app, bg="#E9AC16", fg="white", bd=5,
               pady=15, width=6, font="arial 14 bold").grid(row=0, column=5, padx=5, pady=5)
        self.welcome_bill()


    def total(self):

        self.c_bw_p = self.body_wash.get() * 23.49
        self.c_fc_p = self.face_cream.get() * 57.25
        self.c_mw_p = self.mouthwash.get() * 10.50
        self.c_pr_p = self.perfume.get() * 140
        self.c_hs_p = self.hair_spray.get() * 90
        self.c_bl_p = self.lotion.get() * 56

        self.total_cosmetic_price = float(
            self.c_bw_p +
            self.c_fc_p +
            self.c_mw_p +
            self.c_pr_p +
            self.c_hs_p +
            self.c_bl_p)
        self.cosmetic_price.set("$. " + str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)
        self.cosmetic_tax.set("$. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * 15
        self.g_b_p = self.bread.get() * 2.75
        self.g_st_p = self.salt.get() * 3.15
        self.g_w_p = self.wheat.get() * 12
        self.g_s_p = self.sugar.get() * 10.75
        self.g_t_p = self.tea.get() * 8.58

        self.total_grocery_price = float(
            self.g_r_p +
            self.g_b_p +
            self.g_st_p +
            self.g_w_p +
            self.g_s_p +
            self.g_t_p)
        self.grocery_price.set("$. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.01), 2)
        self.grocery_tax.set("$. " + str(self.g_tax))

        self.d_c_p = self.coke.get() * 5
        self.d_pp_p = self.pepsi.get() * 2.50
        self.d_f_p = self.fanta.get() * 3.25
        self.d_s_p = self.sprite.get() * 4
        self.d_cd_p = self.canada_dry.get() * 5
        self.d_aj_p = self.apple_juice.get() * 3.15

        self.total_soft_drink_price = float(
            self.d_c_p +
            self.d_pp_p +
            self.d_f_p +
            self.d_s_p +
            self.d_cd_p +
            self.d_aj_p)
        self.soft_drink_price.set("$. " + str(self.total_soft_drink_price))
        self.d_tax = round((self.total_soft_drink_price * 0.05), 2)
        self.soft_drink_tax.set("$. " + str(self.d_tax))

        self.Total_bill = float(
            self.total_cosmetic_price +
            self.total_grocery_price +
            self.total_soft_drink_price +
            self.c_tax +
            self.g_tax +
            self.d_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t    Welcome, Abashola Store\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()} ")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()} ")
        self.txtarea.insert(END, f"\n ************************************************")
        self.txtarea.insert(END, f"\n Products\t\tQuantity\t\tPrice")
        self.txtarea.insert(END, f"\n ************************************************")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror(title="Error",message= "Customer Details are must!!!")
        elif self.cosmetic_price.get() == "$. 0.0" and self.grocery_price.get() == "$. 0.0" and self.soft_drink_price.get() == "$. 0.0":
            messagebox.showerror(title="Error", message="No Product Purchased!!!")
        else:
            self.welcome_bill()

            #####cosmetic#####
            if self.body_wash.get() != 0:
                self.txtarea.insert(END, f"\n Bath Wash\t\t{self.body_wash.get()}\t\t{self.c_bw_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.mouthwash.get() != 0:
                self.txtarea.insert(END, f"\n Mouthwash\t\t{self.mouthwash.get()}\t\t{self.c_mw_p}")
            if self.perfume.get() != 0:
                self.txtarea.insert(END, f"\n Perfume\t\t{self.perfume.get()}\t\t{self.c_pr_p}")
            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t{self.hair_spray.get()}\t\t{self.c_hs_p}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            ####grocery#####
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.bread.get() != 0:
                self.txtarea.insert(END, f"\n Bread\t\t{self.bread.get()}\t\t{self.g_b_p}")
            if self.salt.get() != 0:
                self.txtarea.insert(END, f"\n Salt\t\t{self.salt.get()}\t\t{self.g_st_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t{self.lotion.get()}\t\t{self.g_t_p}")

            #####softdrinks#####
            if self.coke.get() != 0:
                self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f"\n Pepsi\t\t{self.pepsi.get()}\t\t{self.d_pp_p}")
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
            if self.canada_dry.get() != 0:
                self.txtarea.insert(END, f"\n Canada Dry\t\t{self.canada_dry.get()}\t\t{self.d_cd_p}")
            if self.apple_juice.get() != 0:
                self.txtarea.insert(END, f"\n Apple Juice\t\t{self.apple_juice.get()}\t\t{self.d_aj_p}")

            self.txtarea.insert(END, f"\n ------------------------------------------------")
            if self.cosmetic_tax.get() != "$. 0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "$. 0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")

            if self.soft_drink_tax.get() != "$. 0.0":
                self.txtarea.insert(END, f"\n Soft Drink Tax\t\t\t{self.soft_drink_tax.get()}")
            self.txtarea.insert(END, f"\n ------------------------------------------------")

            self.txtarea.insert(END, f"\n Total Bill Is :\t\t\t $. {self.Total_bill}")
            self.txtarea.insert(END, f"\n ------------------------------------------------")
            self.save_bill()


    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no : {self.bill_no.get()} saved Successfully")
        else:
            return




    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill Number.")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            #####Cosmetics####
            self.body_wash.set(0)
            self.face_cream.set(0)
            self.mouthwash.set(0)
            self.perfume.set(0)
            self.hair_spray.set(0)
            self.lotion.set(0)

            ########grocery#####
            self.rice.set(0)
            self.bread.set(0)
            self.salt.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            #####Soft Drinks#####
            self.coke.set(0)
            self.pepsi.set(0)
            self.fanta.set(0)
            self.sprite.set(0)
            self.canada_dry.set(0)
            self.apple_juice.set(0)

            #######Total Product Price & Tax Variable######
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.soft_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.soft_drink_tax.set("")

            ######customer#####
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()

    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()



root = Tk()
obj = Bill_App(root)
root.mainloop()
