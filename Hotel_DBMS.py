from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import datetime
import time
import tkinter.messagebox
# import DatabaseHotel
from datetime import datetime, timedelta
import sqlite3


def HotelData():
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Hotel(id INTEGER PRIMARY KEY,CusId text,Firstname text,LastName text,Address text,Gender text,Mobile Text,Nationality text,ProveofId text,DateIn text,DateOut text,Email text)")
    con.commit()
    con.close()


def addHotelRec(CusId, Firstname, Lastname, Address, Gender, Mobile, Nationality, ProveofId, DateIn, DateOut, Email):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Hotel VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)", \
                (CusId, Firstname, Lastname, Address, Gender, Mobile, Nationality, ProveofId, DateIn, DateOut, Email))
    con.commit()
    con.close()


def viewdata():
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Hotel")
    rows = cur.fetchall()
    con.close()
    return rows


def deleteRec(id):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Hotel WHERE id=?", (id,))
    con.commit()
    con.close()


def SearchData(CusId="", Firstname="", Lastname=""):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Hotel WHERE CusId=? OR Firstname=? OR Lastname=? ", \
                (CusId, Firstname, Lastname))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(CusId="", Firstname="", Lastname="", Address="", Gender="", Mobile="", Nationality="", ProveofId="",
               DateIn="", DateOut="", Email=""):
    con = sqlite3.connect("booking.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE Hotel SET CusId=? OR Firstname=? OR Lastname=? OR Address=? OR Gender=? OR Mobile=? OR Nationality=? OR ProveofId=? OR DateIn=? OR DateOut =? OR Email=?", \
        (CusId, Firstname, Lastname, Address, Gender, Mobile, Nationality, ProveofId, DateIn, DateOut, Email))
    con.commit()
    con.close()


HotelData()


# Frontend

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel DataBase Management System")
        self.root.geometry("1350x800+0+0")

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=10, width=1350, height=550, padx=2, relief=RIDGE)
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=5, width=400, height=550, pady=1, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=5, width=800, height=550, pady=4, relief=RIDGE)
        RightFrame.pack(side=RIGHT)

        RightFrame1 = Frame(RightFrame, bd=5, width=800, height=100, padx=10, relief=RIDGE)
        RightFrame1.grid(row=0, column=0)
        RightFrame2 = Frame(RightFrame, bd=5, width=800, height=100, padx=3, pady=3, relief=RIDGE)
        RightFrame2.grid(row=1, column=0)
        RightFrame3 = Frame(RightFrame, bd=5, width=800, height=400, padx=0, relief=RIDGE)
        RightFrame3.grid(row=3, column=0)

        ButtonFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=0, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        global hd
        CusID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Emailid = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        ProveofID = StringVar()
        Gender = StringVar()
        DateIn = StringVar()
        DateOut = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNumber = StringVar()
        RoomExtNumber = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()
        DateIn.set(time.strftime("%d/%m/%y"))
        DateOut.set(time.strftime("%d/%m/%y"))
        x = random.randint(1190, 9746)
        randomRef = str(x)
        CusID.set("Hotel" + randomRef)

        def iExit():
            Exit = tkinter.messagebox.askyesno("Hotel Database Management System", "Confirm if you want to exit")
            if Exit == True:
                root.destroy()

        def Reset():

            self.cboMeal.set("")
            self.cboRoomType.set("")
            self.cboRoomNumber.set("")
            self.cboRoomExtNumber.set("")
            self.cboProveofID.set("")

            self.txtDateofBirth.delete(0, END)
            self.txtFirstName.delete(0, END)
            self.txtLastName.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtPinCode.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtEmailid.delete(0, END)
            self.txtPaidTax.delete(0, END)
            self.txtSubTotal.delete(0, END)
            self.txtTotalCost.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtNationality.delete(0, END)
            DateIn.set(time.strftime("%d/%m/%y"))
            DateOut.set(time.strftime("%d/%m/%y"))
            x = random.randint(1190, 9746)
            randomRef = str(x)
            CusID.set("Hotel" + randomRef)

        def addData():
            if (len(CusID.get()) != 0):
                addHotelRec(CusID.get(), FirstName.get(), LastName.get(), Address.get(), Gender.get(), Mobile.get(),
                            Nationality.get(), ProveofID.get(), DateIn.get(), DateOut.get(), Emailid.get())
                lstHotel.delete(0, END)
                lstHotel.insert(END, (
                CusID.get() + " ", FirstName.get() + " ", LastName.get() + " ", Address.get() + " ", Gender.get() + " ",
                Mobile.get() + " ", Nationality.get() + " ", ProveofID.get() + " ", DateIn.get() + " ",
                DateOut.get() + " ", Emailid.get() + " "))

        def displayData():
            lstHotel.delete(0, END)
            for row in viewdata():
                lstHotel.insert(END, row, str(""))

        def HotelRec():
            global hd
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)
            self.txtCusID.delete(0, END)
            self.txtCusID.insert(END, hd[1])
            self.txtFirstName.delete(0, END)
            self.txtFirstName.insert(END, hd[2])
            self.txtLastName.delete(0, END)
            self.txtLastName.insert(END, hd[3])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, hd[4])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, hd[5])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, hd[6])
            self.txtNationality.delete(0, END)
            self.txtNationality.insert(END, hd[7])
            self.txtProveofID.delete(0, END)
            self.txtProveofID.insert(END, hd[8])
            self.txtDateIn.delete(0, END)
            self.txtDateIn.insert(END, hd[9])
            self.txtDateOut.delete(0, END)
            self.txtDateOut.insert(END, hd[10])
            self.txtEmailid.delete(0, END)
            self.txtEmailid.insert(END, hd[11])

        def deleteData():
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)
            if (len(CusID.get()) != 0):
                deleteRec(hd[0])
                Reset()
                displayData()

        def searchData():
            lstHotel.delete(0, END)
            for row in SearchData(CusID.get(), FirstName.get(), LastName.get()):
                lstHotel.insert(END, row, str(""))

        def update():
            searchHdb = lstHotel.curselection()[0]
            hd = lstHotel.get(searchHdb)
            if (len(CusID.get()) != 0):
                deleteRec(hd[0])
            if (len(CusID.get()) != 0):
                # dataUpdate(CusID.get(),FirstName.get(),LastName.get(),Address.get(),Gender.get(),Mobile.get(),Nationality.get(),ProveofID.get(),DateIn.get(),DateOut.get(),Emailid.get())
                addData()
            # lstHotel.delete(0,END)
            # lstHotel.insert(END,(CusID.get()+" ",FirstName.get()+" ",LastName.get()+" ",Address.get()+" ",Gender.get()+" ",Mobile.get()+" ",Nationality.get()+" ",ProveofID.get()+" ",DateIn.get()+" ",DateOut.get()+" ",Emailid.get()+" "))

        def TotalCostandAddData():
            addData()

            InDate = DateIn.get()
            OutDate = DateOut.get()
            InDate = datetime.strptime(InDate, "%d/%m/%y")
            OutDate = datetime.strptime(OutDate, "%d/%m/%y")
            TotalDays.set(abs((OutDate - InDate).days))
            if (Meal.get() == "BREAKFAST" and RoomType.get() == "SINGLE"):
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "BREAKFAST" and RoomType.get() == "DOUBLE"):
                q1 = float(35)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "BREAKFAST" and RoomType.get() == "FAMILY"):
                q1 = float(45)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "LUNCH" and RoomType.get() == "SINGLE"):
                q1 = float(29)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "LUNCH" and RoomType.get() == "DOUBLE"):
                q1 = float(37)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "LUNCH" and RoomType.get() == "FAMILY"):
                q1 = float(46)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "DINNER" and RoomType.get() == "SINGLE"):
                q1 = float(28)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "DINNER" and RoomType.get() == "DOUBLE"):
                q1 = float(30)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)
            elif (Meal.get() == "DINNER" and RoomType.get() == "FAMILY"):
                q1 = float(43)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 + q4)
                Tax = "RUPEES " + str('%.2f' % ((q5) * 75))
                ST = "RUPEES " + str('%.2f' % (q5))
                TT = "RUPEES " + str('%.2f' % (q5 + (q5) * 75))
                PaidTax.set((Tax))
                SubTotal.set(ST)
                TotalCost.set(TT)

        # ----------------------------------------------------#WIDGET#----------------------------------------------------------#-
        self.lblCusID = Label(LeftFrame, text="CUSTOMER REFERENCE:", font=('arial', 12, 'bold'), padx=1)
        self.lblCusID.grid(row=0, column=0, sticky=W)
        self.txtCusID = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=CusID)
        self.txtCusID.grid(row=0, column=1, pady=3, padx=20)

        self.lblFirstName = Label(LeftFrame, font=('arial', 12, 'bold'), text="FIRST NAME:", padx=1)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=FirstName)
        self.txtFirstName.grid(row=1, column=1, pady=3, padx=20)

        self.lblLastName = Label(LeftFrame, font=('arial', 12, 'bold'), text="LAST NAME:", padx=1)
        self.lblLastName.grid(row=2, column=0, sticky=W)
        self.txtLastName = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=LastName)
        self.txtLastName.grid(row=2, column=1, pady=3, padx=20)

        self.lblAddress = Label(LeftFrame, font=('arial', 12, 'bold'), text="ADDRESS:", padx=1, pady=2)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=Address)
        self.txtAddress.grid(row=3, column=1, pady=3, padx=20)

        self.lblDateofBirth = Label(LeftFrame, font=('arial', 12, 'bold'), text="DATE OF BIRTH:", padx=2, pady=2)
        self.lblDateofBirth.grid(row=4, column=0, sticky=W)
        self.txtDateofBirth = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=DOB)
        self.txtDateofBirth.grid(row=4, column=1, pady=3, padx=20)

        self.lblPinCode = Label(LeftFrame, font=('arial', 12, 'bold'), text="PINCODE:", padx=2, pady=2)
        self.lblPinCode.grid(row=5, column=0, sticky=W)
        self.txtPinCode = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18)
        self.txtPinCode.grid(row=5, column=1, pady=3, padx=20)

        self.lblMobile = Label(LeftFrame, font=('arial', 12, 'bold'), text="MOBILE:", padx=2, pady=2)
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=Mobile)
        self.txtMobile.grid(row=6, column=1, pady=3, padx=20)

        self.lblEmailid = Label(LeftFrame, font=('arial', 12, 'bold'), text="EMAIL ID:", padx=2, pady=2)
        self.lblEmailid.grid(row=7, column=0, sticky=W)
        self.txtEmailid = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=Emailid)
        self.txtEmailid.grid(row=7, column=1, pady=3, padx=20)

        self.lblNationality = Label(LeftFrame, font=('arial', 12, 'bold'), text="NATIONALTITY:", padx=2, pady=2)
        self.lblNationality.grid(row=8, column=0, sticky=W)
        self.txtNationality = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=Nationality)
        self.txtNationality.grid(row=8, column=1, pady=3, padx=20)

        self.lblGender = Label(LeftFrame, font=('arial', 12, 'bold'), text="GENDER:", padx=2, pady=2)
        self.lblGender.grid(row=9, column=0, sticky=W)
        self.txtGender = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=Gender)
        self.txtGender.grid(row=9, column=1, pady=3, padx=20)

        self.lblDateIn = Label(LeftFrame, font=('arial', 12, 'bold'), text="CHECK-IN DATE:", padx=2, pady=2)
        self.lblDateIn.grid(row=10, column=0, sticky=W)
        self.txtDateIn = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=DateIn)
        self.txtDateIn.grid(row=10, column=1, pady=3, padx=20)

        self.lblDateOut = Label(LeftFrame, font=('arial', 12, 'bold'), text="CHECK-OUT DATE:", padx=2, pady=2)
        self.lblDateOut.grid(row=11, column=0, sticky=W)
        self.txtDateOut = Entry(LeftFrame, font=('arial', 12, 'bold'), width=18, textvariable=DateOut)
        self.txtDateOut.grid(row=11, column=1, pady=3, padx=20)

        self.lblProveofID = Label(LeftFrame, font=('arial', 12, 'bold'), text="TYPE OF ID:", padx=2, pady=2)
        self.lblProveofID.grid(row=12, column=0, sticky=W)
        self.cboProveofID = ttk.Combobox(LeftFrame, textvariable=ProveofID, state='readonly',
                                         font=('arial', 12, 'bold'), width=16)
        self.cboProveofID['value'] = (' ', 'AADHAR CARD', 'DRIVING LICENCE', 'VOTER ID', 'STUDENT ID', 'PASSPORT')
        self.cboProveofID.current(0)
        self.cboProveofID.grid(row=12, column=1, pady=3, padx=20)

        self.lblMeal = Label(LeftFrame, font=('arial', 12, 'bold'), text="MEAL:", padx=2, pady=2)
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.cboMeal = ttk.Combobox(LeftFrame, textvariable=Meal, state='readonly', font=('arial', 12, 'bold'),
                                    width=16)
        self.cboMeal['value'] = (' ', 'BREAKFAST', 'LUNCH', 'DINNER')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, pady=3, padx=20)

        self.lblRoomType = Label(LeftFrame, font=('arial', 12, 'bold'), text="ROOM TYPE:", padx=2, pady=2)
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, textvariable=RoomType, state='readonly', font=('arial', 12, 'bold'),
                                        width=16)
        self.cboRoomType['value'] = (' ', 'SINGLE', 'DOUBLE', 'FAMILY')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, pady=3, padx=20)

        self.lblRoomNumber = Label(LeftFrame, font=('arial', 12, 'bold'), text="ROOM NUMBER:", padx=2, pady=2)
        self.lblRoomNumber.grid(row=15, column=0, sticky=W)
        self.cboRoomNumber = ttk.Combobox(LeftFrame, textvariable=RoomNumber, state='readonly',
                                          font=('arial', 12, 'bold'), width=16)
        self.cboRoomNumber['value'] = (' ', '001', '002', '003', '004', '005', '006')
        self.cboRoomNumber.current(0)
        self.cboRoomNumber.grid(row=15, column=1, pady=3, padx=20)

        self.lblRoomExtNumber = Label(LeftFrame, font=('arial', 12, 'bold'), text="ROOM EXTENSION NUMBER:", padx=2,
                                      pady=2)
        self.lblRoomExtNumber.grid(row=16, column=0, sticky=W)
        self.cboRoomExtNumber = ttk.Combobox(LeftFrame, textvariable=RoomExtNumber, state='readonly',
                                             font=('arial', 12, 'bold'), width=16)
        self.cboRoomExtNumber['value'] = (' ', '101', '102', '103', '104', '105', '106')
        self.cboRoomExtNumber.current(0)
        self.cboRoomExtNumber.grid(row=16, column=1, pady=3, padx=20)

        # ----------------------------------------------------#WIDGET#----------------------------------------------------------#

        self.lblLabel = Label(RightFrame1, font=('arial', 8, 'bold'), padx=20, pady=10,
                              text="CUSTOMER REFRENCE       FIRST NAME       LAST NAME       ADDRESS       GENDER       MOBILE       NATIONALITY       PROVEOFID       DATEIN       DATEOUT       EMAILID")
        self.lblLabel.grid(row=0, column=0, columnspan=10)

        scrollbar = Scrollbar(RightFrame2)
        scrollbar.grid(row=0, column=0, sticky='ns')
        lstHotel = Listbox(RightFrame2, width=150, height=20, font=('arial', 8, 'bold'), yscrollcommand=scrollbar.set)
        lstHotel.bind("<<ListboxSelect>>", HotelRec)
        lstHotel.grid(row=0, column=0, padx=0, sticky='nsew')
        scrollbar.config(command=lstHotel.xview)

        # ----------------------------------------------------#WIDGET#----------------------------------------------------------#
        self.lblDays = Label(RightFrame3, font=('arial', 12, 'bold'), text="NUMBER OF DAYS:", padx=2, pady=2)
        self.lblDays.grid(row=0, column=0, sticky=W)
        self.txtDays = Entry(RightFrame3, font=('arial', 12, 'bold'), width=79, textvariable=TotalDays, justify=LEFT)
        self.txtDays.grid(row=0, column=1, pady=3, padx=20)

        self.lblPaidTax = Label(RightFrame3, font=('arial', 12, 'bold'), text="PAID TAX:", padx=2, pady=2)
        self.lblPaidTax.grid(row=1, column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame3, font=('arial', 12, 'bold'), width=79, textvariable=PaidTax, justify=LEFT)
        self.txtPaidTax.grid(row=1, column=1, pady=3, padx=20)

        self.lblSubTotal = Label(RightFrame3, font=('arial', 12, 'bold'), text="SUBTOTAL:", padx=2, pady=2)
        self.lblSubTotal.grid(row=2, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame3, font=('arial', 12, 'bold'), width=79, textvariable=SubTotal, justify=LEFT)
        self.txtSubTotal.grid(row=2, column=1, pady=3, padx=20)

        self.lblTotalCost = Label(RightFrame3, font=('arial', 12, 'bold'), text="TOTAL COST:", padx=2, pady=2)
        self.lblTotalCost.grid(row=3, column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame3, font=('arial', 12, 'bold'), width=79, textvariable=TotalCost,
                                  justify=LEFT)
        self.txtTotalCost.grid(row=3, column=1, pady=3, padx=20)
        # ----------------------------------------------------#WIDGET#----------------------------------------------------------#

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="AddNew/Total", command=TotalCostandAddData).grid(row=0, column=0, padx=8,
                                                                                                pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="Display", command=displayData).grid(row=0, column=1, padx=8, pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="Update", command=update).grid(row=0, column=2, padx=8, pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="Delete", command=deleteData).grid(row=0, column=3, padx=8, pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="Search", command=searchData).grid(row=0, column=4, padx=8, pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2,
                                         text="Reset", command=Reset).grid(row=0, column=5, padx=8, pady=1)

        self.btnTotalandAddData = Button(ButtonFrame, bd=4, font=('arial', 16, 'bold'), width=13, height=2, text="Exit",
                                         command=iExit).grid(row=0, column=6, padx=8, pady=1)


if __name__ == '__main__':
    root = Tk()
    application = Hotel(root)
    root.mainloop()