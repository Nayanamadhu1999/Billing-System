from tkinter import *


from fourth import Menu
# from fifth import Order


class Choice:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Choice")
        self.root.geometry("700x700+100+50")

        #Login Frame
        Frame_Choice = Frame(self.root, bg= "light grey")
        Frame_Choice.place(x=50, y=50, width=600, height=600)

        #Title and subtitle
        title= Label(Frame_Choice, text="---- HK RESTAURANT----", font=("Times New Roman", 25, "italic"),fg="blue", bg="light green").place(x=130, y=30)
        subtitle = Label(Frame_Choice, text="Here you can watch our Services.", font=("Times New Roman", 20, "italic", "bold"),fg="#6162FF", bg="light green").place(x=100, y=100)
        subtitle1 = Label(Frame_Choice, text="We do FREE Delivery to your Doorstep .", font=("Times New Roman", 18, "italic", "bold"),fg="black", bg="light grey").place(x=100, y=350)
        subtitle2 = Label(Frame_Choice, text="click here for your registration .", font=("Times New Roman", 18, "italic", "bold"),fg="Blue", bg="light grey").place(x=120, y=400)


        #Login to the menu list
        click = Button(Frame_Choice,command=self.checkmymenu, text="Menu List", font=("Times New Roman",15), fg="black", bg="yellow").place(x=120,y=200)

        #Login to the fifth(main system)
        click = Button(Frame_Choice,command =self.checkmymain, text="Direct Order", font=("Times New Roman",15), fg="black", bg="yellow").place(x=400,y=200)

         #Login to the sixth(online registration)
        click = Button(Frame_Choice,command =self.checkonliereg, text="Registration", font=("Times New Roman",15), fg="black", bg="light blue").place(x=220,y=450)

        #logout button
        click = Button(Frame_Choice,command =self.logout, text="Logout", font=("Times New Roman",15), fg="black", bg="white").place(x=240,y=550)


    def checkmymenu(self):
        self.root.destroy()
        Menu.checkfourth(self)

    def checkmymain(self):
        self.root.destroy()
        from fifth import Order
        Order.checkfifth(self)

    def checkonliereg(self):
        self.root.destroy()
        from sixth import Register
        Register.checksixth(self)


    def checkthird(self):
        self.root.destroy()
        root = Tk()
        obj = Choice(root)
        root.mainloop()

    def logout(self):
        root.destroy()
root = Tk()
obj = Choice(root)
root.mainloop()
