from tkinter import *
from tkinter import ttk

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form For online services")
        self.root.geometry("800x800+500+100")

        title = Label(text ="HK Restaurant",font=('Times New Roman',30,'bold'), bg="black",fg='white',width=500, height=1).pack()
        title = Label(text ="---Free Delivery to your Doorstep---",font=('Times New Roman',20,'bold'), bg="black",fg='white',width=500, height=1).pack()

        #Login Frame
        Frame_Register = Frame(self.root, bg= "light grey")
        Frame_Register.place(x=100, y=100, width=600, height=600)
        onlinereg = Label(Frame_Register,text="Online Registration Form", font=('Times New Roman',20,'bold'), bg="light grey", fg="black").pack()
        Fullnamelb = Label(Frame_Register,text="Full Name", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=100)
        Addresslb = Label(Frame_Register,text="Address", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=150)
        Contactnumlb = Label(Frame_Register,text="Contact Num", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=200)
        NICnymlb = Label(Frame_Register,text="NIC", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=250)
        paymentmethodlb = Label(Frame_Register,text="Payment Method", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=300)
        dateoforderlb = Label(Frame_Register,text="Date", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=350)
        timelb = Label(Frame_Register,text="Time", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=400)
        mealtypelb = Label(Frame_Register,text="Meal type", font=('Times New Roman',15), bg="white", fg="black").place(x=50, y=450)

        Full_Name = StringVar()
        Address = StringVar()
        Contact_Num = IntVar()
        NICnum = IntVar()
        Payment_Method = StringVar()
        Date_Of_Order = IntVar()
        Time_Order = IntVar()
        Meal_Type = StringVar()

        self.Fullnameentry = Entry(Frame_Register,textvariable=Full_Name,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Fullnameentry.place(x=300, y=100)

        self.Addressentry = Entry(Frame_Register,textvariable=Address,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Addressentry.place(x=300, y=150)

        self.Contactnumentry = Entry(Frame_Register,textvariable=Contact_Num,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Contactnumentry.place(x=300, y=200)

        self.NICnumentry = Entry(Frame_Register,textvariable=NICnum,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.NICnumentry.place(x=300, y=250)

        self.Paymentmethodentry = Entry(Frame_Register,textvariable=Payment_Method,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Paymentmethodentry.place(x=300, y=300)
        # self.cboPaymentmethodentry = ttk.Combobox(textvariable = "Payment Method", state = 'readonly',font=('Times New Roman',15),width=18)
        # self.cboPaymentmethodentry['value'] = ('', 'Card Payment', 'Cash Payment', 'Cash on delivery')
        # self.cboPaymentmethodentry.current(0)
        # self.cboPaymentmethodentry.place(x=400, y=400)

        self.Dateordentry = Entry(Frame_Register,textvariable=Date_Of_Order,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Dateordentry.place(x=300, y=350)

        self.Timeentry = Entry(Frame_Register,textvariable=Time_Order,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Timeentry.place(x=300, y=400)

        self.Mealtypeentry = Entry(Frame_Register,textvariable=Meal_Type,font=('Times New Roman',15),bd=1,bg="white", fg="black")
        self.Mealtypeentry.place(x=300, y=450)

        #====================================================making buttons======================================

        button1 = Button(text="Save",command=self.adddata,font=('Times New Roman',15),bd=3,bg="cadet blue", fg="black").place(x=400,y=600)
        button2 = Button(text="Confirm  order", command = self.backmymenu,font=('Times New Roman',15),bd=3,bg="cadet blue", fg="black").place(x=500,y=600)


    def adddata(self):
        FullNameinf = self.Fullnameentry.get()
        Addressinfo = self.Addressentry.get()
        Contnuminfo = self.Contactnumentry.get()
        NICnuminfo = self.NICnumentry.get()
        Paymentmethodinfo = self.Paymentmethodentry.get()
        Dateordinfo = self.Dateordentry.get()
        Timeinfo = self.Timeentry.get()
        Mealtpeinfo = self.Mealtypeentry.get()

        print(FullNameinf,Addressinfo,Contnuminfo, NICnuminfo, Paymentmethodinfo, Dateordinfo, Timeinfo,  Mealtpeinfo)

        file = open("user.txt", "a")
       #   file.write("Name of customer = " + nameinfo)
       # file.write("\n")
        file.write("Customer Name : " + FullNameinf)
        file.write("\n")
        file.write("Customer Address : " + Addressinfo)
        file.write("\n")
        file.write("Contact Number : " + Contnuminfo)
        file.write("\n")
        file.write("NIC number : " + NICnuminfo)
        file.write("\n")
        file.write("Payment Method : " + Paymentmethodinfo)
        file.write("\n")
        file.write("Order Time : " + Timeinfo)
        file.write("\n")
        file.write("Mealtype : " + Mealtpeinfo)
        file.write("\n")
        file.write("\n")
        file.close()

    def backmymenu(self):
        self.root.destroy()
        from fifth import Order
        Order.checkfifth(self)












    def checksixth(self):
        # root = Tk()
        obj = Menu(root)
        # root.mainloop()


root = Tk()
obj = Register(root)
root.mainloop()
