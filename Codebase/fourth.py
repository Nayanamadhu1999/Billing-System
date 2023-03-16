from tkinter import *

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Choice")
        self.root.geometry("1500x1500+10+10")

        #Login Frame
        Frame_Menu = Frame(self.root, bg= "light grey")
        Frame_Menu.place(x=50, y=50, width=1400, height=1400)

        #title and sub titles
        title= Label(Frame_Menu, text="---- HK RESTAURANT----", font=("Times New Roman", 25, "italic", "bold"),fg="black", bg="light grey").place(x=500, y=30)
        subtitle = Label(Frame_Menu, text="Seven Unique Flavors for Seven Days.", font=("Times New Roman", 20, "italic"),fg="black", bg="light grey").place(x=470, y=70)

        #Sunday Menu
        subtitle1 = Label(Frame_Menu, text="Sunday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=40, y=100)
        subtitle2 = Label(Frame_Menu, text="Chicken Fried Rice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=130)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=130)
        subtitle4 = Label(Frame_Menu, text="Chicken Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=160)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=160)
        subtitle6 = Label(Frame_Menu, text="Chicken Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=190)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=190)
        subtitle8 = Label(Frame_Menu, text="Chicken Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=220)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=220)
        subtitle10 = Label(Frame_Menu, text="Chicken Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=250)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=250)
        subtitle12 = Label(Frame_Menu, text="Devilled Chicken", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=280)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=280)
        subtitle14 = Label(Frame_Menu, text="Chicken Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=310)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=310)
        subtitle16 = Label(Frame_Menu, text="Fresh Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=20, y=340)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=200, y=340)


        #Monday Menu
        subtitle1 = Label(Frame_Menu, text="Monday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=350, y=100)
        subtitle2 = Label(Frame_Menu, text="SeaFood Mix Rice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=130)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=130)
        subtitle4 = Label(Frame_Menu, text="Beef Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=160)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=160)
        subtitle6 = Label(Frame_Menu, text="SeaFood Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=190)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=190)
        subtitle8 = Label(Frame_Menu, text="Margaritta Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=220)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=220)
        subtitle10 = Label(Frame_Menu, text="Cheese Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=250)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=250)
        subtitle12 = Label(Frame_Menu, text="Devilled Pork", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=280)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=280)
        subtitle14 = Label(Frame_Menu, text="Sweet corn Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=310)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=310)
        subtitle16 = Label(Frame_Menu, text="Papaya Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=330, y=340)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=510, y=340)

        #Tuesday Menu
        subtitle1 = Label(Frame_Menu, text="Tuesday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=660, y=100)
        subtitle2 = Label(Frame_Menu, text="Mixed Rice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=130)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=130)
        subtitle4 = Label(Frame_Menu, text="Veggy Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=160)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=160)
        subtitle6 = Label(Frame_Menu, text="Mixed Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=190)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=190)
        subtitle8 = Label(Frame_Menu, text="Chicken Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=220)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=220)
        subtitle10 = Label(Frame_Menu, text="Beef Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=250)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=250)
        subtitle12 = Label(Frame_Menu, text="Devilled Beef", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=280)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=280)
        subtitle14 = Label(Frame_Menu, text="Chicken Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=310)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=310)
        subtitle16 = Label(Frame_Menu, text="Mango Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=640, y=340)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=820, y=340)

        #Wednesday Menu
        subtitle1 = Label(Frame_Menu, text="Wednesday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=970, y=100)
        subtitle2 = Label(Frame_Menu, text="Nasigoreng", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=130)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=130)
        subtitle4 = Label(Frame_Menu, text="Spicy Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=160)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=160)
        subtitle6 = Label(Frame_Menu, text="Cheese Chicken Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=190)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=190)
        subtitle8 = Label(Frame_Menu, text="Cheesy Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=220)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=220)
        subtitle10 = Label(Frame_Menu, text="Hawaian Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=250)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=250)
        subtitle12 = Label(Frame_Menu, text="Devilled Thalapath", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=280)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=280)
        subtitle14 = Label(Frame_Menu, text="Veggie Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=310)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=310)
        subtitle16 = Label(Frame_Menu, text="Watermelon Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=950, y=340)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=1130, y=340)

        #Thursday Menu
        subtitle1 = Label(Frame_Menu, text="Thursday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=180, y=380)
        subtitle2 = Label(Frame_Menu, text="Mongolian Rice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=410)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=410)
        subtitle4 = Label(Frame_Menu, text="Beef Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=440)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=440)
        subtitle6 = Label(Frame_Menu, text="Cheese Mixed Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=470)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=470)
        subtitle8 = Label(Frame_Menu, text="Sausage Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=500)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=500)
        subtitle10 = Label(Frame_Menu, text="Mexican Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=530)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=530)
        subtitle12 = Label(Frame_Menu, text="Pork Curry", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=560)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=560)
        subtitle14 = Label(Frame_Menu, text="Chicken Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=590)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=590)
        subtitle16 = Label(Frame_Menu, text="Lime Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=160, y=620)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=340, y=620)

        #Friday Menu
        subtitle1 = Label(Frame_Menu, text="Friday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=490, y=380)
        subtitle2 = Label(Frame_Menu, text="Biriani", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=410)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=410)
        subtitle4 = Label(Frame_Menu, text="Chicken Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=440)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=440)
        subtitle6 = Label(Frame_Menu, text="Chicken Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=470)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=470)
        subtitle8 = Label(Frame_Menu, text="Chicken Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=500)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=500)
        subtitle10 = Label(Frame_Menu, text="Chicken Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=530)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=530)
        subtitle12 = Label(Frame_Menu, text="Pork Stew", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=560)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=560)
        subtitle14 = Label(Frame_Menu, text="Veggy Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=590)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=590)
        subtitle16 = Label(Frame_Menu, text="Avacado Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=470, y=620)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=650, y=620)

        #Saturday Menu
        subtitle1 = Label(Frame_Menu, text="Saturday Menu", font=("Times New Roman", 18, "italic"),fg="blue", bg="light grey").place(x=800, y=380)
        subtitle2 = Label(Frame_Menu, text="Mixed Rice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=410)
        subtitle3 = Label(Frame_Menu, text="750.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=410)
        subtitle4 = Label(Frame_Menu, text="Spicy Noodles", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=440)
        subtitle5 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=440)
        subtitle6 = Label(Frame_Menu, text="Seafood Kottu", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=470)
        subtitle7 = Label(Frame_Menu, text="890.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=470)
        subtitle8 = Label(Frame_Menu, text="Cheesy Pizza", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=500)
        subtitle9 = Label(Frame_Menu, text="1690.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=500)
        subtitle10 = Label(Frame_Menu, text="Cheese Burger", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=530)
        subtitle11 = Label(Frame_Menu, text="450.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=530)
        subtitle12 = Label(Frame_Menu, text="Chicken Fried", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=560)
        subtitle13 = Label(Frame_Menu, text="550.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=560)
        subtitle14 = Label(Frame_Menu, text="Chicken Soup", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=590)
        subtitle15 = Label(Frame_Menu, text="350.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=590)
        subtitle16 = Label(Frame_Menu, text="Pineapple Juice", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=780, y=620)
        subtitle17 = Label(Frame_Menu, text="150.00", font=("Times New Roman", 15),fg="Black", bg="light grey").place(x=960, y=620)

        #Login to the fifth(main system)
        click = Button(Frame_Menu,command =self.checkoder, text="Order", font=("Times New Roman",15), fg="black", bg="yellow").place(x=1100,y=500)

       # #logout button
       #  click = Button(Frame_Menu,command =self.menuout, text="Logout", font=("Times New Roman",15), fg="black", bg="white").place(x=1100,y=650)


    def checkoder(self):
        self.root.destroy()
        from fifth import Order
        Order.checkfifth(self)

    # def backbutton(self):
    #     self.root.destroy()
    #     from third import Choice
    #     Choice.checkthird(self)

    def checkfourth(self):
        root = Tk()
        obj = Menu(root)
        root.mainloop()





# root = Tk()
# obj = Menu(root)
# root.mainloop()

