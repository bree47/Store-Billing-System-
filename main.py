from _tkinter import*
import math
import random
import os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.tittle("-----STORE BILLING SYSTEM-----")
        bg_color = "#074463"
        tittle= Lable(self.root,text="STORE BILLING SYSTEM",bd=12,relief=GROOVE, bg=bg_color, fg= "white",
                        font=("times new roman", 30, "bold"),pady=2).pack(fill=X)



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
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Customer Name", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                 column=1,
                                                                                                 pady=5,
                                                                                                 padx=10)

        Label(F1, text="Phone No.", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(row=0,
                                                                                                  column=3,
                                                                                                  pady=5,
                                                                                                  padx=10)

        Label(F1, text="Bill Number", bg=bg_color, fg="white"
              , font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)

        Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font="arial 12 bold").grid(row=0,
                                                                                                     column=6,
                                                                                                     padx=20,
                                                                                                     pady=10)

        #####cosmeticframe######
        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"),
                        fg="gold", bg=bg_color)
        F2.place(x=6, y=180, width=325, height=380)
