from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Hospital:
    def __init__(self, tk):
        self.tk = tk
        self.tk.title("Hospital Management System")
        self.tk.geometry("1540x800+0+0")

        self.PatientName = StringVar()
        self.NameTablet = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NoOftablet = StringVar()
        self.issueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.Furtherinfo = StringVar()
        self.BloodPressure = StringVar()
        self.Prescribed = StringVar()  # Variable to track if medicine is prescribed

        lbltitle = Label(self.tk, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        Dataframe = Frame(self.tk, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        dataframeleft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("arial", 12, "bold"), text="Patient Information")
        dataframeleft.place(x=0, y=5, width=980, height=350)

        dataframeright = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("arial", 12, "bold"), text="Prescription")
        dataframeright.place(x=990, y=5, width=460, height=350)

        # ===============button frames ======================
        Buttonframe = Frame(self.tk, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ===============Details frames ======================
        Detailsframe = Frame(self.tk, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ===================== DataframeLeft=====================================
        lblPatientName = Label(dataframeleft, text="Patient Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPatientName.grid(row=0, column=0)

        entryPatientName = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.PatientName, width=35)
        entryPatientName.grid(row=0, column=1)

        lblNameTablet = Label(dataframeleft, text="Name of tablet", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=1, column=0)

        comNametablet = ttk.Combobox(dataframeleft, textvariable=self.NameTablet, font=("times new roman", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNametablet.grid(row=1, column=1)

        lblref = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Reference No :", padx=2, pady=4)
        lblref.grid(row=2, column=0, sticky=W)
        entryRef = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.ref, width=35)
        entryRef.grid(row=2, column=1)

        lblDose = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Dose :", padx=4, pady=4)
        lblDose.grid(row=3, column=0, sticky=W)
        entryDose = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.Dose, width=35)
        entryDose.grid(row=3, column=1)

        lblNoOftablet = Label(dataframeleft, font=("times new roman", 12, "bold"), text="No of Tablets :", padx=2, pady=6)
        lblNoOftablet.grid(row=4, column=0, sticky=W)
        entryNoOftablet = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.NoOftablet, width=35)
        entryNoOftablet.grid(row=4, column=1)

        lblissueDate = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Issue Date :", padx=4, pady=4)
        lblissueDate.grid(row=5, column=0, sticky=W)
        entryIssueDate = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.issueDate, width=35)
        entryIssueDate.grid(row=5, column=1)

        lblExpDate = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Expiry date :", padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        entryExpDate = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.ExpDate, width=35)
        entryExpDate.grid(row=6, column=1)

        lblDailyDose = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Daily Dose :", padx=2, pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        entryDailyDose = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.DailyDose, width=35)
        entryDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Side Effect :", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        entrySideEffect = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.SideEffect, width=35)
        entrySideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Further info :", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        entryFurtherinfo = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.Furtherinfo, width=35)
        entryFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(dataframeleft, font=("times new roman", 12, "bold"), text="Blood Pressure :", padx=4, pady=4)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        entryBloodPressure = Entry(dataframeleft, font=("times new roman", 12, "bold"), textvariable=self.BloodPressure, width=35)
        entryBloodPressure.grid(row=1, column=3)

        # ====================== Dataframeright===================
        self.prescribe_button = Button(dataframeright, text="Mark as Prescribed", font=("times new roman", 12, "bold"), command=self.iMarkAsPrescribed)
        self.prescribe_button.pack(pady=20)

        # ==========================buttons =====================
        btnAdd = Button(Buttonframe, command=self.iAddData, text="Add", bg="green", foreground="white",
                        font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnAdd.grid(row=0, column=0)

        btnDisplay = Button(Buttonframe, command=self.iDisplayData, text="Display", bg="green", foreground="white",
                            font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnDisplay.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, command=self.iUpdateData, text="Update", bg="green", foreground="white",
                           font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, command=self.iDeleteData, text="Delete", bg="green", foreground="white",
                           font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, command=self.iClearData, text="Clear", bg="green", foreground="white",
                          font=("times new roman", 12, "bold"), width=25, height=1, padx=1, pady=1)
        btnClear.grid(row=0, column=4)

        # ==========================Details frame================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("PatientName", "NameTablet", "ref", "Dose", "NoOftablet", "issuedate", "Expdate", "dailydose", "SideEffect", "Furtherinfo", "BloodPressure", "Prescribed"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("NameTablet", text="Name of tablets")
        self.hospital_table.heading("ref", text="Reference No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("NoOftablet", text="Number of tablets")
        self.hospital_table.heading("issuedate", text="Issue date")
        self.hospital_table.heading("Expdate", text="Expiry date")
        self.hospital_table.heading("dailydose", text="Daily dose")
        self.hospital_table.heading("SideEffect", text="Side Effect")
        self.hospital_table.heading("Furtherinfo", text="Further info")
        self.hospital_table.heading("BloodPressure", text="Blood Pressure")
        self.hospital_table.heading("Prescribed", text="Prescribed")

        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.column("PatientName", width=120)
        self.hospital_table.column("NameTablet", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("NoOftablet", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("Expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("SideEffect", width=100)
        self.hospital_table.column("Furtherinfo", width=100)
        self.hospital_table.column("BloodPressure", width=100)
        self.hospital_table.column("Prescribed", width=100)

        self.hospital_table.bind("<ButtonRelease-1>", self.iGetCursor)

    def iAddData(self):
        if self.PatientName.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ankit@56", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO hospital (PatientName, NameTablet, ref, Dose, NoOftablet, issuedate, Expdate, dailydose, SideEffect, Furtherinfo, BloodPressure, Prescribed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.PatientName.get(),
                    self.NameTablet.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.NoOftablet.get(),
                    self.issueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.SideEffect.get(),
                    self.Furtherinfo.get(),
                    self.BloodPressure.get(),
                    self.Prescribed.get()  # Adding Prescribed field
                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    def iDisplayData(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Ankit@56", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM hospital")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for row in rows:
                    self.hospital_table.insert('', END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}")

    def iUpdateData(self):
        if self.PatientName.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "Patient Name and Reference No are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Ankit@56", database="mydata")
            my_cursor = conn.cursor()

            # Check if the record exists
            my_cursor.execute("SELECT * FROM hospital WHERE PatientName=%s AND ref=%s",
                              (self.PatientName.get(), self.ref.get()))
            result = my_cursor.fetchone()
            if not result:
                messagebox.showerror("Error", "Record not found")
                conn.close()
                return

            # Debugging print statement
            print("Updating record with the following details:")
            print(f"PatientName: {self.PatientName.get()}")
            print(f"NameTablet: {self.NameTablet.get()}")
            print(f"ref: {self.ref.get()}")
            print(f"Dose: {self.Dose.get()}")
            print(f"NoOftablet: {self.NoOftablet.get()}")
            print(f"issuedate: {self.issueDate.get()}")
            print(f"Expdate: {self.ExpDate.get()}")
            print(f"dailydose: {self.DailyDose.get()}")
            print(f"SideEffect: {self.SideEffect.get()}")
            print(f"Furtherinfo: {self.Furtherinfo.get()}")
            print(f"BloodPressure: {self.BloodPressure.get()}")
            print(f"Prescribed: {self.Prescribed.get()}")

            update_query = """
                UPDATE hospital SET 
                NameTablet=%s, Dose=%s, NoOftablet=%s, issuedate=%s, Expdate=%s, dailydose=%s, SideEffect=%s, 
                Furtherinfo=%s, BloodPressure=%s, Prescribed=%s 
                WHERE PatientName=%s AND ref=%s
            """
            values = (
                self.NameTablet.get(),
                self.Dose.get(),
                self.NoOftablet.get(),
                self.issueDate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.SideEffect.get(),
                self.Furtherinfo.get(),
                self.BloodPressure.get(),
                self.Prescribed.get(),
                self.PatientName.get(),
                self.ref.get()
            )

            my_cursor.execute(update_query, values)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", f"Error due to: {e}")
    def iDeleteData(self):
        if self.PatientName.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Ankit@56", database="mydata")
                my_cursor = conn.cursor()
                my_cursor.execute("DELETE FROM hospital WHERE PatientName=%s AND ref=%s", (
                    self.PatientName.get(),
                    self.ref.get()
                ))

                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Record has been deleted")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")

    def iClearData(self):
        self.PatientName.set("")
        self.NameTablet.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NoOftablet.set("")
        self.issueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.Furtherinfo.set("")
        self.BloodPressure.set("")
        self.Prescribed.set("")

    def iMarkAsPrescribed(self):
        # Toggle between "Yes" and "No"
        current_value = self.Prescribed.get()
        new_value = "Yes" if current_value != "Yes" else "No"
        self.Prescribed.set(new_value)
        messagebox.showinfo("Success", f"Prescription status updated to {new_value}")

    def iGetCursor(self, event):
        cursor_row = self.hospital_table.focus()
        contents = self.hospital_table.item(cursor_row)
        selected_item = contents['values']

        self.PatientName.set(selected_item[0])
        self.NameTablet.set(selected_item[1])
        self.ref.set(selected_item[2])
        self.Dose.set(selected_item[3])
        self.NoOftablet.set(selected_item[4])
        self.issueDate.set(selected_item[5])
        self.ExpDate.set(selected_item[6])
        self.DailyDose.set(selected_item[7])
        self.SideEffect.set(selected_item[8])
        self.Furtherinfo.set(selected_item[9])
        self.BloodPressure.set(selected_item[10])
        self.Prescribed.set(selected_item[11])  # Set prescription status

tk = Tk()
ob = Hospital(tk)
tk.mainloop()
