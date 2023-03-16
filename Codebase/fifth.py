from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time;

class Order:
        def __init__(self,root):
            self.root = root
            self.root.title("Restaurant Billing System")
            self.root.geometry("1350x750+0+0")
            self.root.config(background="light green")

            ABC =Frame(self.root, bg="light green", bd=20, relief=RIDGE)
            ABC.grid()
            ABC1 =Frame(ABC, bd=14, width=1350, height=100, padx=10, bg="light green", relief=RIDGE)
            ABC1.grid(row=0, column=0, columnspan=4, sticky=W)
            ABC2 =Frame(ABC, bd=14, width=450, height=488, padx=10, bg="light green", relief=RIDGE)
            ABC2.grid(row=1, column=0, sticky=W)
            ABC3 =Frame(ABC, bd=14, width=450, height=488, padx=10, bg="light green", relief=RIDGE)
            ABC3.grid(row=1, column=1, sticky=W)
            ABC4 =Frame(ABC, bd=14, width=460, height=488, padx=10, bg="light green", relief=RIDGE)
            ABC4.grid(row=1, column=2, sticky=W)
            ABC5 =Frame(ABC4, bd=14, width=370, height=340, padx=10, bg="light green", relief=RIDGE)
            ABC5.grid(row=0, column=0, sticky=W)
            ABC6 =Frame(ABC4, bd=14, width=370, height=120, padx=10, bg="light green", relief=RIDGE)
            ABC6.grid(row=1, column=0, sticky=W)

            Date1 =StringVar()
            Time1 =StringVar()
            Date1.set(time.strftime("%d/%m/%y"))
            Time1.set(time.strftime("%H:%M:%S"))

            #==========================================================================================================
            CustomerRef = StringVar()
            Firstname = StringVar()
            Surname= StringVar()
            Address = StringVar()
            Postcode = StringVar()
            Mobile = StringVar()
            Email = StringVar()
            Nationality = StringVar()
            # DOB = StringVar()
            # IDType = StringVar()
            Gender = StringVar()
            # Checkindate = StringVar()
            # Checkoutdate = StringVar()
            Meal = StringVar()
            # Roomtype = StringVar()
            # RoomNo = StringVar()
            # RoomExtNo = StringVar()
            TotalCost = StringVar()
            Subtotal = StringVar()
            PaidTax = StringVar()
            Totaldays = StringVar()

            CustomerRef.set(random.randint(19800,9875648))

            var1 = IntVar()
            var2 = IntVar()
            var3 = IntVar()
            var4 = IntVar()
            var5 = IntVar()
            var6 = IntVar()
            var7 = IntVar()
            var8 = IntVar()
            var9 = IntVar()
            var10 = IntVar()
            var11 = IntVar()
            var12 = IntVar()
            var13 = IntVar()
            var14 = IntVar()

            E_Fried_Rice = StringVar()
            E_Noodles = StringVar()
            E_Kottu = StringVar()
            E_Pizza = StringVar()
            E_Burgers = StringVar()
            E_Special_dish = StringVar()
            E_Soups = StringVar()
            E_Fresh_Juice = StringVar()

            E_Fried_Rice.set("0")
            E_Noodles.set("0")
            E_Kottu.set("0")
            E_Pizza.set("0")
            E_Burgers.set("0")
            E_Special_dish.set("0")
            E_Soups.set("0")
            E_Fresh_Juice.set("0")
            #========================================================================================================================
            self.lblTitle = Label(ABC1, textvariable=Date1, font=('Times New Roman',30,'bold'),pady=9,bd=5, bg="white",fg='black').grid(row=0, column=0)
            self.lblTitle = Label(ABC1, text="\tRestaurant Billing System\t\t", font=('Times New Roman',30,'bold'),pady=9,bd=5, bg="white",fg='black',justify=CENTER).grid(row=0, column=1)
            self.lblTitle = Label(ABC1, textvariable=Time1, font=('Times New Roman',30,'bold'),pady=9,bd=5, bg="white",fg='black').grid(row=0, column=2)
            #===================================Exit=====================================================================================
            def iExit ():
                iExit= tkinter.messagebox.askyesno("Restaurant Billing System", "Confirm if you want to exit")
                if iExit > 0:
                    root.destroy()
                    return
            #=================================================================================================================
            def Reset ():
                self.txtReceipt.delete("1.0",END)
                E_Fried_Rice.set("0")
                E_Noodles.set("0")
                E_Kottu.set("0")
                E_Pizza.set("0")
                E_Burgers.set("0")
                E_Special_dish.set("0")
                E_Soups.set("0")
                E_Fresh_Juice.set("0")

                var1.set(0)
                var2.set(0)
                var3.set(0)
                var4.set(0)
                var5.set(0)
                var6.set(0)
                var7.set(0)
                var8.set(0)

                CustomerRef.set("")
                Firstname.set("")
                Surname.set("")
                Address.set("")
                Postcode.set("")
                Mobile.set("")
                Email.set("")
                Nationality.set("")
                Gender.set("")
                Meal.set("")
                TotalCost.set("")
                Subtotal.set("")
                PaidTax.set("")
                Totaldays.set("")
            #========================================================================================================
            def chFriedRice():
                if (var1.get() == 1):
                    self.txtFried_Rice.configure(state=NORMAL)
                    self.txtFried_Rice.focus()
                    self.txtFried_Rice.delete('0', END)
                    E_Fried_Rice.set("")
                elif var1.get() ==0:
                    self.txtFried_Rice.configure(state=DISABLED)
                    E_Fried_Rice.set("0")

            def chNoodles():
                if (var2.get() == 1):
                    self.txtNoodles.configure(state=NORMAL)
                    self.txtNoodles.focus()
                    self.txtNoodles.delete('0', END)
                    E_Noodles.set("")
                elif var2.get() ==0:
                    self.txtNoodles.configure(state=DISABLED)
                    E_Noodles.set("0")

            def chKottu():
                if (var3.get() == 1):
                    self.txtKottu.configure(state=NORMAL)
                    self.txtKottu.focus()
                    self.txtKottu.delete('0', END)
                    E_Kottu.set("")
                elif var3.get() ==0:
                    self.txtKottu.configure(state=DISABLED)
                    E_Kottu.set("0")
            def chPizza():
                if (var4.get() == 1):
                    self.txtPizza.configure(state=NORMAL)
                    self.txtPizza.focus()
                    self.txtPizza.delete('0', END)
                    E_Pizza.set("")
                elif var4.get() ==0:
                    self.txtPizza.configure(state=DISABLED)
                    E_Pizza.set("0")

            def chBurgers():
                if (var5.get() == 1):
                    self.txtBurgers.configure(state=NORMAL)
                    self.txtBurgers.focus()
                    self.txtBurgers.delete('0', END)
                    E_Burgers.set("")
                elif var5.get() ==0:
                    self.txtBurgers.configure(state=DISABLED)
                    E_Burgers.set("0")

            def chSpecialDish():
                if (var6.get() == 1):
                    self.txtSpecial_Dish.configure(state=NORMAL)
                    self.txtSpecial_Dish.focus()
                    self.txtSpecial_Dish.delete('0', END)
                    E_Special_dish.set("")
                elif var6.get() ==0:
                    self.txtSpecial_Dish.configure(state=DISABLED)
                    E_Special_dish.set("0")

            def chSoups():
                if (var7.get() == 1):
                    self.txtSoups.configure(state=NORMAL)
                    self.txtSoups.focus()
                    self.txtSoups.delete('0', END)
                    E_Soups.set("")
                elif var7.get() ==0:
                    self.txtSoups.configure(state=DISABLED)
                    E_Soups.set("0")

            def chFreshJuice():
                if (var8.get() == 1):
                    self.txtFresh_Juice.configure(state=NORMAL)
                    self.txtFresh_Juice.focus()
                    self.txtFresh_Juice.delete('0', END)
                    E_Fresh_Juice.set("")
                elif var8.get() ==0:
                    self.txtFresh_Juice.configure(state=DISABLED)
                    E_Fresh_Juice.set("0")
            #=========================================================================================================
            def costOfItem():
                CustomerRef.set(random.randint(19800,9875648))
                Item1 = float(E_Fried_Rice.get())
                Item2 = float(E_Noodles.get())
                Item3 = float(E_Kottu.get())
                Item4 = float(E_Pizza.get())
                Item5 = float(E_Burgers.get())
                Item6 = float(E_Special_dish.get())
                Item7 = float(E_Soups.get())
                Item8 = float(E_Fresh_Juice.get())

                PriceofPackages = (Item1*750) + (Item2*550) + (Item3*890) + (Item4*1500) + (Item5*450) + (Item6*550) + (Item7*350) + (Item8*250)
                SubtotalofItems = "Rs",str('%.2f'% PriceofPackages)
                Subtotal.set(SubtotalofItems)
                Tax = "Rs",str('%.2f'% ((PriceofPackages) * 0.05))
                PaidTax.set(Tax)
                TTax = ((PriceofPackages) * 0.05)
                Tcost = "Rs",str('%.2f'% (PriceofPackages + TTax))
                TotalCost.set(Tcost)
            #======================================reciptmaking====================================================
                self.txtReceipt.insert(END,'Items\t\t\t\t' + "Cost of Items\n")
                self.txtReceipt.insert(END, 'Customer Ref.set: \t\t\t\t\t' + CustomerRef.get()+ "\n")
                self.txtReceipt.insert(END, 'Fried Rice: \t\t\t\t\t' + E_Fried_Rice.get()+ "\n")
                self.txtReceipt.insert(END, 'Noodles: \t\t\t\t\t' + E_Noodles.get()+ "\n")
                self.txtReceipt.insert(END, 'Kottu: \t\t\t\t\t' + E_Kottu.get()+ "\n")
                self.txtReceipt.insert(END, 'Pizza: \t\t\t\t\t' + E_Pizza.get()+ "\n")
                self.txtReceipt.insert(END, 'Burgers: \t\t\t\t\t' + E_Burgers.get()+ "\n")
                self.txtReceipt.insert(END, 'Special Dish: \t\t\t\t\t' + E_Special_dish.get()+ "\n")
                self.txtReceipt.insert(END, 'Soups: \t\t\t\t\t' + E_Soups.get()+ "\n")
                self.txtReceipt.insert(END, 'Fresh Juice: \t\t\t\t\t' + E_Fresh_Juice.get()+ "\n")

                self.txtReceipt.insert(END, '\nTax Paid: \t\t\t\t' + PaidTax.get()+ "\n")
                self.txtReceipt.insert(END, '\nSubTotal: \t\t\t\t' + str(Subtotal.get()) + "\n")
                self.txtReceipt.insert(END, '\nTotal Cost: \t\t\t\t' + str(TotalCost.get()) + "\n")
            #=====================================================================================================

                file = open("orderdetails.txt", "a")
       #   file.write("Name of custom = " + nameinfo)
       # file.write("\n")
                file.write("Customer ref : " +CustomerRef.get()+"\n")
                file.write("Number of Fried Rice : " + E_Fried_Rice.get()+ "\n")
                file.write("Number of Noodles : " + E_Noodles.get()+ "\n")
                file.write("Number of Kottu : " + E_Kottu.get()+ "\n")
                file.write("Number of Pizza : " + E_Pizza.get()+ "\n")
                file.write("Number of Burgers : " + E_Burgers.get()+ "\n")
                file.write("Number of Specialdishes : " + E_Special_dish.get()+ "\n")
                file.write("Number of Soups : " + E_Soups.get()+ "\n")
                file.write("Number of Freshjuices : " + E_Fresh_Juice.get()+ "\n")
                file.write("Paid Tax : " + PaidTax.get()+ "\n")
                file.write("Sub total : " + str(Subtotal.get())+ "\n")
                file.write("Total Cost : " + str(TotalCost.get())+ "\n")
                file.write("\n")
                file.write("\n")
                file.close()



            #===================================Text==================================================================
            self.txtReceipt = Text(ABC5,height=19, width=43, bd=10, font=("Times New Roman", 9, 'bold'))
            self.txtReceipt.grid(row=0, column=0)
            #========================================================================================================


            #========================================================================================================


            self.lblCus_Ref = Label(ABC2,font=('Times New Roman',12,'bold'), text="Customer Ref:",padx=2, fg="black", bg="light yellow")
            self.lblCus_Ref.grid(row=0, column=0 , sticky=W)
            self.txtCus_Ref = Entry(ABC2, font=("Times New Roman",12,'bold'), textvariable= CustomerRef,width=20)
            self.txtCus_Ref.grid(row=0, column=1,pady=3, padx=20)

            self.lblFirstname = Label(ABC2,font=('Times New Roman',12,'bold'), text="Firstname:",padx=2, fg="black", bg="light yellow")
            self.lblFirstname.grid(row=1, column=0 , sticky=W)
            self.txtFirstname = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable=Firstname,width=20)
            self.txtFirstname.grid(row=1, column=1,pady=3, padx=20)

            self.lblSurname = Label(ABC2,font=('Times New Roman',12,'bold'), text="Surname:",padx=2, fg="black", bg="light yellow")
            self.lblSurname.grid(row=2, column=0 , sticky=W)
            self.txtSurname = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable = Surname,width=20)
            self.txtSurname.grid(row=2, column=1,pady=3, padx=20)

            self.lblAddress = Label(ABC2,font=('Times New Roman',12,'bold'), text="Address:",padx=2, fg="black", bg="light yellow")
            self.lblAddress.grid(row=3, column=0 , sticky=W)
            self.txtAddress = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable = Address,width=20)
            self.txtAddress.grid(row=3, column=1,pady=3, padx=20)

            self.lblPcode = Label(ABC2,font=('Times New Roman',12,'bold'), text="Postcode:",padx=2, fg="black", bg="light yellow")
            self.lblPcode.grid(row=4, column=0 , sticky=W)
            self.txtPcode = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable= Postcode,width=20)
            self.txtPcode.grid(row=4, column=1,pady=3, padx=20)

            self.lblMobile = Label(ABC2,font=('Times New Roman',12,'bold'), text="Mobile:",padx=2, fg="black", bg="light yellow")
            self.lblMobile.grid(row=5, column=0 , sticky=W)
            self.txtMobile = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable= Mobile,width=20)
            self.txtMobile.grid(row=5, column=1,pady=3, padx=20)

            self.lblEmail = Label(ABC2,font=('Times New Roman',12,'bold'), text="Email:",padx=2, fg="black", bg="light yellow")
            self.lblEmail.grid(row=6, column=0 , sticky=W)
            self.txtEmail = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable= Email,width=20)
            self.txtEmail.grid(row=6, column=1,pady=3, padx=20)

            self.lblPcode = Label(ABC2,font=('Times New Roman',12,'bold'), text="Postcode:",padx=2, fg="black", bg="light yellow")
            self.lblPcode.grid(row=7, column=0 , sticky=W)
            self.txtPcode = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable= Postcode,width=20)
            self.txtPcode.grid(row=7, column=1,pady=3, padx=20)

            self.lblN = Label(ABC2,font=('Times New Roman',12,'bold'), text="Nationality:",padx=2,pady=2, fg="black", bg="light yellow")
            self.lblN.grid(row=8, column=0 , sticky=W)
            self.txtN = Entry(ABC2, font=("Times New Roman",12,'bold'),textvariable= Nationality,width=20)
            self.cboN =ttk.Combobox(ABC2, textvariable= "Nationality",state='readonly', font=('Times New Roman',12,'bold'),width=18)
            self.cboN['value'] = ('','Sri Lankan', 'Indian', 'Italian', 'Russian','British','France','Other')
            self.cboN.current(0)
            self.cboN.grid(row=8, column=1,pady=3, padx=20)

            self.lblGender = Label(ABC2,font=('Times New Roman',12,'bold'), text="Gender:",padx=2,pady=2, fg="black", bg="light yellow")
            self.lblGender.grid(row=9, column=0 , sticky=W)
            self.cboGender =ttk.Combobox(ABC2, textvariable= Gender, state='readonly', font=('Times New Roman',12,'bold'),width=18)
            self.cboGender['value'] = ('','Male', 'Female')
            self.cboGender.current(0)
            self.cboGender.grid(row=9, column=1,pady=3, padx=20)

            self.lblMeal = Label(ABC2,font=('Times New Roman',12,'bold'), text="Meal:",padx=2,pady=2, fg="black", bg="light yellow")
            self.lblMeal.grid(row=10, column=0 , sticky=W)
            self.cboMeal =ttk.Combobox(ABC2, textvariable= Meal, state='readonly', font=('Times New Roman',12,'bold'),width=18)
            self.cboMeal['value'] = ('','Breakfast', 'Lunch', 'Dinner')
            self.cboMeal.current(0)
            self.cboMeal.grid(row=10, column=1,pady=3, padx=20)

            #========================================================================================================================
            self.Fried_Rice = Checkbutton(ABC3,text="Fried_Rice", variable=var1, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue",command=chFriedRice).grid(row=0, sticky=W)
            self.txtFried_Rice = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Fried_Rice, bd=8, width=20, justify='left', state= DISABLED)
            self.txtFried_Rice.grid(row=0, column=1)

            self.Noodles = Checkbutton(ABC3,text="Noodles", variable=var2, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue", command =chNoodles).grid(row=1, sticky=W)
            self.txtNoodles = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Noodles, bd=8, width=20, justify='left', state= DISABLED)
            self.txtNoodles.grid(row=1, column=1)

            self.Kottu = Checkbutton(ABC3,text="Kottu", variable=var3, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue", command=chKottu).grid(row=2, sticky=W)
            self.txtKottu = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Kottu, bd=8, width=20, justify='left', state= DISABLED)
            self.txtKottu.grid(row=2, column=1)

            self.Pizza = Checkbutton(ABC3,text="Pizza", variable=var4, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue",command=chPizza).grid(row=3, sticky=W)
            self.txtPizza = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Pizza, bd=8, width=20, justify='left', state= DISABLED)
            self.txtPizza.grid(row=3, column=1)

            self.Burgers = Checkbutton(ABC3,text="Burger", variable=var5 , onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue", command=chBurgers).grid(row=4, sticky=W)
            self.txtBurgers = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Burgers, bd=8, width=20, justify='left', state= DISABLED)
            self.txtBurgers.grid(row=4, column=1)

            self.Special_Dish = Checkbutton(ABC3,text="Special Dish", variable=var6, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue", command=chSpecialDish).grid(row=5, sticky=W)
            self.txtSpecial_Dish = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Special_dish, bd=8, width=20, justify='left', state= DISABLED)
            self.txtSpecial_Dish.grid(row=5, column=1)

            self.Soups = Checkbutton(ABC3,text="Soup", variable=var7, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue" , command = chSoups).grid(row=6, sticky=W)
            self.txtSoups = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Soups, bd=8, width=20, justify='left', state= DISABLED)
            self.txtSoups.grid(row=6, column=1)

            self.Fresh_Juice = Checkbutton(ABC3,text="Fresh Juice", variable=var8, onvalue= 1, offvalue=0, font=('Times New Roman',12,'bold') , bg="powder blue", command = chFreshJuice).grid(row=7, sticky=W)
            self.txtFresh_Juice = Entry(ABC3, font=("Times New Roman",12, 'bold'), textvariable = E_Fresh_Juice, bd=8, width=20, justify='left', state= DISABLED)
            self.txtFresh_Juice.grid(row=7, column=1)

            self.lblspace = Label(ABC3, text="Tax and Total Sum", font=("Times New Roman",18,'bold'), pady=1,bd=9,bg="cadet blue",fg="black", width=26, justify=CENTER).grid(row=8, column=0, columnspan=4)
            #============================================receipt=======================================================================
            self.lblPaidTax = Label(ABC3,font=("Times New Roman",12,'bold'), text="Paid Tax", bd=7, bg="powder blue",fg="black",)
            self.lblPaidTax.grid(row=10, column=0, sticky=W)
            self.txtPaidTax = Entry(ABC3,font=("Times New Roman",12,'bold'),textvariable=PaidTax, bd=7, bg='white',width=20, justify=LEFT)
            self.txtPaidTax.grid(row=10, column=1)

            self.lblSubTotal = Label(ABC3,font=("Times New Roman",12,'bold'), text="Sub Total", bd=7, bg="powder blue",fg="black",)
            self.lblSubTotal.grid(row=11, column=0, sticky=W)
            self.txtSubTotal = Entry(ABC3,font=("Times New Roman",12,'bold'),textvariable=Subtotal, bd=7, bg='white',width=20, justify=LEFT)
            self.txtSubTotal.grid(row=11, column=1)

            self.lblTotalCost = Label(ABC3,font=("Times New Roman",12,'bold'), text="Total Cost", bd=7, bg="powder blue",fg="black",)
            self.lblTotalCost.grid(row=12, column=0, sticky=W)
            self.txtTotalCost = Entry(ABC3,font=("Times New Roman",12,'bold'),textvariable=TotalCost, bd=7, bg='white',width=20, justify=LEFT)
            self.txtTotalCost.grid(row=12, column=1)



            #============================================= making buttons=======================================================================
            self.btnTotal = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('Times New Roman',16,'bold'),width=5, height=2,bg="light blue",text="Total", command=costOfItem).grid(row=0, column=0)
            self.btnReset = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('Times New Roman',16,'bold'),width=5, height=2,bg="light blue",text="Reset",command=Reset).grid(row=0, column=1)
            self.btnExit = Button(ABC6, padx=14, pady=7, bd=5, fg="black", font=('Times New Roman',16,'bold'),width=5, height=2,bg="light blue",text="Exit", command=iExit).grid(row=0, column=2)


if __name__ == '__main__':
        root=Tk()
        application = Order(root)
        root.mainloop()














        def checkfifth(self):
                root = Tk()
                obj = Order()
                root.mainloop()


root = Tk()
obj = Order(root)
root.mainloop()
