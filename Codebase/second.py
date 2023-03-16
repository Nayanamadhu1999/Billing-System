from tkinter import *
from tkinter import messagebox,Tk
#from third import Choice
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x700+100+50")

        #Login Frame
        Frame_login = Frame(self.root, bg= "light green")
        Frame_login.place(x=200, y=100, width=750, height=500)

        #Title and subtitle
        title= Label(Frame_login, text="---- HK RESTAURANT----", font=("Times New Roman", 35, "italic", "bold"),fg="#6162FF", bg="light green").place(x=90, y=30)
        subtitle = Label(Frame_login, text="We WILL Give YOU the BEST.", font=("Times New Roman", 25, "italic", "bold"),fg="#6162FF", bg="light green").place(x=150, y=100)

        # username
        lbl_Username = Label(Frame_login, text="Username", font=("Times New Roman", 13, "bold"), fg="black",bg="light green").place(x=100, y=230)
        self.username = Entry(Frame_login, font=("Times New Roman", 18, "bold"), fg="black", bg="white")
        self.username.place(x=100, y=260, width=320, height=35)

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("Times New Roman", 13, "bold"), fg="black",bg="light green").place(x=100, y=315)
        self.password = Entry(Frame_login, font=("Times New Roman", 18, "bold"), fg="black", bg="white")
        self.password.place(x=100, y=345, width=320, height=35)

        #Button
        submit = Button(Frame_login,command=self.check_function, text="Login", bd=0, font=("Times New Roman", 13), bg="light blue", fg="black").place(x=100, y=400, width=188, height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get()!="HKR" or self.password.get()!="12345":
            messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        else:
            self.root.destroy()
            from third import Choice
            Choice.checkthird(self)


    def checklogin(self):
        self.root.destroy
        root = Tk()
        obj = Login(root)
        root.mainloop()



