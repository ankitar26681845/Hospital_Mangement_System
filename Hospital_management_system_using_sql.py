from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,tk):
        self.tk = tk
        self.tk.title("Hospital Management System")
        self.tk.geometry("1540x800+0+0")



        self.NameTablet = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NoOftablet = StringVar()
        self.lot = StringVar()
        self.issueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.Furtherinfo = StringVar()
        self.BloodPressure = StringVar()


        lbltitle = Label(self.tk,bd  = 20,relief = RIDGE,text = "HOSPITAL MANAGEMENT SYSTEM",fg = "red",bg = "white",font = ("times new roman",50,"bold"))
        lbltitle.pack(side = TOP,fill = X)

        Dataframe = Frame(self.tk,bd = 20,relief = RIDGE)
        Dataframe.place(x = 0,y = 130,width=1530,height = 400)

        dataframeleft = LabelFrame(Dataframe,bd = 10,relief=RIDGE,padx=10,
                                   font=("arial", 12, "bold"), text="Patient Information")
        dataframeleft.place(x = 0,y =5,width = 980,height = 350)

        dataframeright = LabelFrame(Dataframe,bd = 10,relief=RIDGE,padx=10,
                                   font=("arial", 12, "bold"), text="Prescription")
        dataframeright.place(x = 990,y =5,width = 460,height = 350)

        # ===============button frames ======================
        Buttonframe = Frame(self.tk, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ===============Details frames ======================
        Detailsframe = Frame(self.tk, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)


        # ===================== DataframeLeft=====================================


        lblNameTablet = Label(dataframeleft,text = "Names of tablet",  font = ("times new roman",12,"bold"),padx = 2,pady = 6)
        lblNameTablet.grid(row = 0,column=0)



        lblNameTablet = Label(dataframeleft, text="Names of tablet", font=("times new roman", 12, "bold"), padx=2,pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(dataframeleft,textvariable=self.NameTablet,font=("times new roman", 12, "bold"),
                                                                                 width=33)

        comNametablet["values"]=("Nice"," Corona Vaccine"," Acetaminophen"," Adderall","Amlodipine","Ativan")
        comNametablet.grid(row =0,column=1)



        lblref = Label(dataframeleft,font=("times new roman", 12, "bold"),text = "Refrence No :",padx = 2,pady=4)
        lblref.grid(row = 1,column=0,sticky=W)
        lblref =Entry(dataframeleft,font=("times new roman", 12, "bold"),textvariable=self.ref,width = 35)
        lblref.grid(row = 1,column = 1)

        lblDose = Label(dataframeleft,font=("times new roman", 12, "bold"), text="Dose :", padx=4,pady = 4)
        lblDose.grid(row=2, column=0, sticky=W)
        lblDose = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.Dose, width=35)
        lblDose.grid(row=2, column=1)

        lblNoOftablet = Label(dataframeleft, font=("times new roman", 12, "bold"), text="No of Tablets:  :", padx=2,pady = 6)
        lblNoOftablet.grid(row=3, column=0, sticky=W)
        lblNoOftablet = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.NoOftablet,width=35)
        lblNoOftablet.grid(row=3, column=1)

        lbllot = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Lot :", padx=4, pady=4)
        lbllot.grid(row=4, column=0, sticky=W)
        lbllot = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.lot, width=35)
        lbllot.grid(row=4, column=1)

        lblissueDate = Label(dataframeleft,font=("times new roman", 12, "bold"), text="Issue Date :", padx=4, pady=4)
        lblissueDate.grid(row=5, column=0, sticky=W)
        lblissueDate = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.issueDate, width=35)
        lblissueDate.grid(row=5, column=1)

        lblExpDate = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Expiry date :", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        lblExpDate = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.ExpDate, width=35)
        lblExpDate.grid(row=6, column=1)

        lblDailyDose = Label(dataframeleft, font=("times new roman", 12, "bold"), text=" Daily Dose :", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        lblDailyDose = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.DailyDose, width=35)
        lblDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Side Effect :", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        lblSideEffect = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.SideEffect, width=35)
        lblSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Further info :", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        lblFurtherinfo = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.Furtherinfo, width=35)
        lblFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(dataframeleft,font=("times new roman", 12, "bold"), text="Blood Pressure :", padx=4, pady=4)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        lblBloodPressure = Entry(dataframeleft, font=("times new roman", 12, "bold"),textvariable=self.BloodPressure, width=35)
        lblBloodPressure.grid(row=1, column=3)


        #====================== Dataframeright===================

        self.txtPrescription = Text(dataframeright, font=("times new roman", 12, "bold"),width =25,height =1, padx= 2,pady = 6)
        self.txtPrescription.grid(row =0,column=0)

        # ==========================buttons =====================

        btnPrescription = Button(Buttonframe, text=" Prescription  ", bg="green", foreground="white",
                                     font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.iPrescriptionData, text=" Prescription Data ", bg="green", foreground="white",
                                 font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text=" Update ", bg="green", foreground="white",
                                 font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text=" Delete ", bg="green", foreground="white",
                                 font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text=" Clear ", bg="green", foreground="white",
                                 font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text=" Exit ", bg="green", foreground="white",
                                 font=("times new roman", 12, "bold"), width=21, height=1, padx=1, pady=1)
        btnExit.grid(row=0, column=5)

        # ========================================Table ====================================

        # ======================scroll bar ==========================
        scroll_x= ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,columns=("NameTablet","ref","Dose","NoOftablet","lot","issuedate","Expdate","dailydose","SideEffect","Furtherinfo","BloodPressure"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side = BOTTOM,fill = X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("NameTablet",text ="Name of tabets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOftablet",text="Number of tablets ")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue date")
        self.hospital_table.heading("Expdate", text="Expiry date")
        self.hospital_table.heading("dailydose", text="Daily dose")

        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("Furtherinfo", text="Further info")
        self.hospital_table.heading("BloodPressure", text="Blood Pressure")


        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill = BOTH,expand=1)
        self.hospital_table.column("NameTablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("NoOftablet", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("Expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("SideEffect", width=100)
        self.hospital_table.column("Furtherinfo",width=100)
        self.hospital_table.column("BloodPressure", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

          #========================== Functionality declaration ============
    def iPrescriptionData(self):
        if  self.ref.get() == "":
            messagebox.showerror("Error","All Field are required")
        else:
            conn = mysql.connector.connect(host="localhost",username = "root",password ="Ankit@56",database = "mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%i,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.NameTablet.get(),
                                                                                                self.ref.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NoOftablet.get(),
                                                                                                self.lot.get(),
                                                                                                self.issueDate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.SideEffect.get(),
                                                                                                self.Furtherinfo.get(),
                                                                                                self.BloodPressure.get()

                                                                                                ))

            conn.commit()

            conn.close()
            messagebox.showinfo("Success","Record has been inserted")




            




tk = Tk()
ob = Hospital(tk)
tk.mainloop()
