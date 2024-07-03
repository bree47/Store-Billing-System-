from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("-------Store Billing System-------")
        bg_color="#074463"
        title=Label(self.root,text="Store Billing System",bd=12,relief=GROOVE,bg=bg_color,fg="white",
                    font=("times new roman",30,"bold"),pady=2).pack(fill=X)


        #===========================Variables==============================
        #============================Cosmetics==============================
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        #===========================Grocery====================================
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        #============================Soft Drinks======================================
        self.coke=IntVar()
        self.pepsi=IntVar()
        self.fanta=IntVar()
        self.sprite=IntVar()
        self.canada_dry=IntVar()
        self.apple_juice=IntVar()

        #=================================Total Product Price & Tax Variable===============================
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.soft_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.soft_drink_tax=StringVar()

        #====================================Customer===========================================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()



        #=======================Customer Detail Frame======================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white"
                        ,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cphn_lbl = Label(F1, text="Phone No.", bg=bg_color, fg="white"
                          , font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15,textvariable=self.c_phone,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white"
                          , font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15,textvariable=self.search_bill,font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=20,pady=10)


       #===========================Cosmetic Frame========================================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=6,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold")
                        ,bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman", 16, "bold")
                         , bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt = Entry(F2, width=10,textvariable=self.face_cream,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1,
                                                                                                       padx=10, pady=10)

        Face_w_lbl = Label(F2, text="Face Wash", font=("times new roman", 16, "bold")
                         , bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_w_txt = Entry(F2, width=10,textvariable=self.face_wash,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1,
                                                                                                       padx=10, pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman", 16, "bold")
                         , bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2, width=10,textvariable=self.spray,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1,
                                                                                                       padx=10, pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman", 16, "bold")
                         , bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Hair_g_txt = Entry(F2, width=10,textvariable=self.gel,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1,
                                                                                                       padx=10, pady=10)

        Body_lbl = Label(F2, text="Body Lotion", font=("times new roman", 16, "bold")
                         , bg=bg_color, fg="lightgreen").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        Body_txt = Entry(F2, width=10,textvariable=self.lotion,font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1,
                                                                                                       padx=10, pady=10)
