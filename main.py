import tkinter as tk
import access_db
from dbmanage import ManagePeople,ManageProduct

#Application class with necessary components to make pages
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('500x500')
        self.resizable(0,0)
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #all frames are held inside this dictionary
        self.frames = {}

        for F in (StartPage,LoginPage,StaffView,OwnerView,CustomerView,StaffManageProduct):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        #raise the chosen frame to the top
        frame = self.frames[cont]
        frame.tkraise()

# Main window on startup     
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Login As").pack(pady=10,padx=10)
        ## buttons 
        obtn = tk.Button(self,width=50,height=5,bg='red',text='Owner',command=lambda:controller.show_frame(LoginPage))
        rbtn = tk.Button(self,width=50,height=5,bg='lightgreen',text='Employee',command=lambda:controller.show_frame(LoginPage))
        dbtn = tk.Button(self,width=50,height=5,bg='lightblue',text='Customer',command=lambda:controller.show_frame(LoginPage))

        obtn.pack(padx=10)
        rbtn.pack(pady=10,padx=10)
        dbtn.pack(padx=10)

#Login Page
class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        ##
        username_label = tk.Label(self,text="Enter Username")
        username = tk.Entry(self,width=40)
        username_label.pack()
        username.pack(ipady=5,ipadx=5)
        ##
        password_label = tk.Label(self,text="Enter Password")
        password = tk.Entry(self,width=40,text='hi')
        password_label.pack()
        password.pack(ipady=5,ipadx=5)
        ###
        login_btn = tk.Button(self,text='Login',width=30,height=2,bg='lightgreen',command=lambda: controller.show_frame(StaffView)).pack(pady=10)
        goback = tk.Button(self,width=30,height=2,bg='orange',text='Menu',command=lambda: controller.show_frame(StartPage)).pack()

# Staff window upon authenication
class StaffView(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
    
        ##Initialise the frames and listbox
        frame1 = tk.Frame(self,height=200,width=500)
        frame2 = tk.Frame(self,height=250,width=250)
        frame3 = tk.Frame(self,height=350,width=250)
        #pack all frames
        frame1.pack(side =tk.TOP,pady=10)
        frame2.pack(side =tk.RIGHT,padx=5)
        frame3.pack(side=tk.LEFT,padx=5)
        
        scroll = tk.Scrollbar(frame3)
        scroll.pack(side=tk.RIGHT,padx=5)
        ##
        self.lst_box = tk.Listbox(frame3,width=300,height=20,bg='lightblue',bd=5,yscrollcommand = scroll.set)
        self.lst_box.pack(padx=5)
        self.lst_box.bind('<<ListboxSelect>>',ManagePeople(self).get_selected_row)
        ##
        scroll.config(command = self.lst_box.yview)
        
        ## ADDING ENTRY BOXES
        #name
        name_label = tk.Label(frame1,text='Name').grid(row=0,column=0,sticky=tk.W,padx=5)
        self.name = tk.Entry(frame1,width=25)
        self.name.grid(row=1,column=0,pady=5,padx=5,ipady=5)
        #age
        age_label = tk.Label(frame1,text='Age').grid(row=0,column=1,sticky=tk.W,padx=5)
        self.age = tk.Entry(frame1,width=25)
        self.age.grid(row=1,column=1,pady=5,padx=5,ipady=5)
        #phone
        phone_label = tk.Label(frame1,text='Phone Number').grid(row=0,column=2,sticky=tk.W,padx=5)
        self.phone = tk.Entry(frame1,width=25)
        self.phone.grid(row=1,column=2,pady=5,padx=5,ipady=5)
        #email address
        email_label = tk.Label(frame1,text='Email Address').grid(row=2,column=0,sticky=tk.W,padx=5)
        self.email = tk.Entry(frame1,width=25)
        self.email.grid(row=3,column=0,pady=5,padx=5,ipady=5)
        #home address
        address_label = tk.Label(frame1,text='Home Address').grid(row=2,column=1,sticky=tk.W,padx=5)
        self.address = tk.Entry(frame1,width=25)
        self.address.grid(row=3,column=1,pady=5,padx=5,ipady=5)
        #password
        password_label = tk.Label(frame1,text='Password').grid(row=2,column=2,sticky=tk.W,padx=5)
        self.password = tk.Entry(frame1,width=25,show="*")
        self.password.grid(row=3,column=2,pady=5,padx=5,ipady=5)

        #second frame buttons
        add_cust = tk.Button(frame2,width=15,height=3,text='Add Customer',command=lambda:ManagePeople(self).insert_data('Customer'))
        update = tk.Button(frame2,width=15,height=3,text='Update Customer',command=lambda:ManagePeople(self).update_data('Customer'))
        srch_cust = tk.Button(frame2,width=15,height=3,text='Search Customer',command=lambda:ManagePeople(self).search_data('Customer'))
        delete = tk.Button(frame2,width=15,height=3,text='Delete Customer',command=lambda:ManagePeople(self).delete_data('Customer'))
        view_staff = tk.Button(frame2,width=15,height=3,text='View all Staff',command=lambda:ManagePeople(self).view_data('Staff'))
        mng_product = tk.Button(frame2,width=15,height=3,bg='lightblue',text='Manage Products',command=lambda: controller.show_frame(StaffManageProduct))
        exit = tk.Button(frame2,width=15,height=3,text="Exit",bg='red',command=lambda:controller.show_frame(StartPage))
        #place all the buttons
        add_cust.grid(row=0,column=0,padx=5,pady=5)
        update.grid(row=0,column=1,padx=5,pady=5) 
        delete.grid(row=1,column=0,padx=5,pady=5)
        srch_cust.grid(row=1,column=1,padx=5,pady=5)
        view_staff.grid(row=2,column=0,padx=5,pady=5)
        mng_product.grid(row=2,column=1,padx=5,pady=5)
        exit.grid(row=3,column=0,columnspan=3)

#Owner window upon authentication
class OwnerView(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        ##Initialise the frames and listbox
        frame1 = tk.Frame(self,height=200,width=500)
        frame2 = tk.Frame(self,height=250,width=250)
        frame3 = tk.Frame(self,height=350,width=250)
        #pack all frames
        frame1.pack(side =tk.TOP,pady=10)
        frame2.pack(side =tk.RIGHT,padx=5)
        frame3.pack(side=tk.LEFT,padx=5)
        
        scroll = tk.Scrollbar(frame3)
        scroll.pack(side=tk.RIGHT,padx=5)
        ##
        self.lst_box = tk.Listbox(frame3,width=50,height=20,bg='lightgreen',bd=5,yscrollcommand = scroll.set)
        self.lst_box.pack(padx=5)
        self.lst_box.bind('<<ListboxSelect>>',ManagePeople(self).get_selected_row)
        ##
        scroll.config(command = self.lst_box.yview)
        
        ## ADDING ENTRY BOXES
        #name
        name_label = tk.Label(frame1,text='Name')
        name_label.grid(row=0,column=0,sticky=tk.W,padx=5)
        self.name = tk.Entry(frame1,width=25)
        self.name.grid(row=1,column=0,pady=5,padx=5,ipady=5)
        #DOB
        age_label = tk.Label(frame1,text='Age').grid(row=0,column=1,sticky=tk.W,padx=5)
        self.age = tk.Entry(frame1,width=25)
        self.age.grid(row=1,column=1,pady=5,padx=5,ipady=5)
        #Phone number
        phone_label = tk.Label(frame1,text='Phone Number').grid(row=0,column=2,sticky=tk.W,padx=5)
        self.phone = tk.Entry(frame1,width=25)
        self.phone.grid(row=1,column=2,pady=5,padx=5,ipady=5)
        #Home address
        address_label = tk.Label(frame1,text='Home Address').grid(row=2,column=0,sticky=tk.W,padx=5)
        self.address = tk.Entry(frame1,width=25)
        self.address.grid(row=3,column=0,pady=5,padx=5,ipady=5)
        #Email address
        email_label = tk.Label(frame1,text='Email Address').grid(row=2,column=1,sticky=tk.W,padx=5)
        self.email = tk.Entry(frame1,width=25)
        self.email.grid(row=3,column=1,pady=5,padx=5,ipady=5)
        #Login Password
        password_label = tk.Label(frame1,text='Password').grid(row=2,column=2,sticky=tk.W,padx=5)
        self.password = tk.Entry(frame1,width=25,show="*")
        self.password.grid(row=3,column=2,pady=5,padx=5,ipady=5)

        #second frame buttons
        add_staff = tk.Button(frame2,width=15,height=3,text='Add Staff',command=lambda: ManagePeople(self).insert_data('Staff'))
        update = tk.Button(frame2,width=15,height=3,text='Update',command= lambda: ManagePeople(self).update_data('Staff'))
        view_staff = tk.Button(frame2,width=15,height=3,text='Search Staff',command=lambda: ManagePeople(self).search_data('Staff'))
        view_cust = tk.Button(frame2,width=15,height=3,text='Search Customer' )
        menu = tk.Button(frame2,width=15,height=3,bg='lightblue',text='Menu',command=lambda: controller.show_frame(StartPage))
        exit = tk.Button(frame2,width=15,height=3,bg='Red',text='Exit',command=self.destroy)
        
        add_staff.grid(row=0,column=0,padx=5,pady=5)
        update.grid(row=0,column=1,padx=5,pady=5) 
        view_staff.grid(row=1,column=0,padx=5,pady=5)
        view_cust.grid(row=1,column=1,padx=5,pady=5)
        menu.grid(row=2,column=0,padx=5,pady=5)
        exit.grid(row=2,column=1,padx=5,pady=5)

class StaffManageProduct(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
    
        ##Initialise the frames and listbox
        frame1 = tk.Frame(self,height=200,width=500)
        frame2 = tk.Frame(self,height=250,width=250)
        frame3 = tk.Frame(self,height=350,width=250)
        #pack all frames
        frame1.pack(side =tk.TOP,pady=10)
        frame2.pack(side =tk.RIGHT,padx=5)
        frame3.pack(side=tk.LEFT,padx=5)
        
        scroll = tk.Scrollbar(frame3)
        scroll.pack(side=tk.RIGHT,padx=5)
        ##
        self.lst_box = tk.Listbox(frame3,width=300,height=20,bg='lightblue',bd=5,yscrollcommand = scroll.set)
        self.lst_box.pack(padx=5)
        self.lst_box.bind('<<ListboxSelect>>',ManageProduct(self).get_selected_row)
        ##
        scroll.config(command = self.lst_box.yview)
        
        ## ADDING ENTRY BOXES
        #name
        name_label = tk.Label(frame1,text='Name').grid(row=0,column=0,sticky=tk.W,padx=5)
        self.name = tk.Entry(frame1,width=25)
        self.name.grid(row=1,column=0,pady=5,padx=5,ipady=5)
        #Price
        price_label = tk.Label(frame1,text='Price').grid(row=0,column=1,sticky=tk.W,padx=5)
        self.price = tk.Entry(frame1,width=25)
        self.price.grid(row=1,column=1,pady=5,padx=5,ipady=5)
        #ISBN
        isbn_label = tk.Label(frame1,text='ISBN').grid(row=0,column=2,sticky=tk.W,padx=5)
        self.isbn = tk.Entry(frame1,width=25)
        self.isbn.grid(row=1,column=2,pady=5,padx=5,ipady=5)
        #address
        address_label = tk.Label(frame1,text='Address (for events)').grid(row=2,column=0,sticky=tk.W,padx=5)
        self.address = tk.Entry(frame1,width=25)
        self.address.grid(row=3,column=0,pady=5,padx=5,ipady=5)
        #Category
        catg_label = tk.Label(frame1,text='Category').grid(row=2,column=1,sticky=tk.W,padx=5)
        self.category = tk.StringVar(value="Select")
        self.dropdown = tk.OptionMenu(frame1,self.category,"Product","Event")
        self.dropdown.config(width=15,bg='lightgreen')
        self.dropdown.grid(row=3,column=1,pady=5,padx=5,ipady=5,sticky=tk.W)
        
        #second frame buttons
        add_product = tk.Button(frame2,width=15,height=3,text='Add Product',command=lambda:ManageProduct(self).insert_data('Product'))
        update_product = tk.Button(frame2,width=15,height=3,text='Update Product',command=lambda:ManageProduct(self).update_data('Product'))
        srch_product = tk.Button(frame2,width=15,height=3,text='Search Product',command=lambda:ManageProduct(self).search_data('Product'))
        delete_product = tk.Button(frame2,width=15,height=3,text='Delete Product',command=lambda:ManageProduct(self).delete_data('Product'))
        view_all = tk.Button(frame2,width=15,height=3,text='View all',command=lambda:ManageProduct(self).view_data('Product'))
        mng_people = tk.Button(frame2,width=15,height=3,bg='lightblue',text='Manage People',command=lambda: controller.show_frame(StaffView))
        exit = tk.Button(frame2,width=15,height=3,text="Exit",bg='red',command=lambda:controller.show_frame(StartPage))
        #place all the buttons
        add_product.grid(row=0,column=0,padx=5,pady=5)
        update_product.grid(row=0,column=1,padx=5,pady=5) 
        delete_product.grid(row=1,column=0,padx=5,pady=5)
        srch_product.grid(row=1,column=1,padx=5,pady=5)
        view_all.grid(row=2,column=0,padx=5,pady=5)
        mng_people.grid(row=2,column=1,padx=5,pady=5)
        exit.grid(row=3,column=0,columnspan=3)

#Customer window upon authentication
class CustomerView(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        nav = tk.Frame(self)
        nav.grid(row=0,column=0,padx=25,pady=10)
        
        prodcuts = tk.Button(nav,text="Products",width=20,height=2,bg='orange',command=lambda: self.show_frame(ProductView)).grid(row=0,column=0)
        events = tk.Button(nav,text="Events",width=20,height=2,bg='lightblue',command=lambda: self.show_frame(EventView)).grid(row=0,column=1,padx=5)
        contact = tk.Button(nav,text="Contact",width=20,height=2,bg='red',command=lambda: self.show_frame(Contact)).grid(row=0,column=2)

        container = tk.Frame(self)
        container.grid(row=1,column=0,sticky=tk.W)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #all frames are held inside this dictionary
        self.frames = {}

        for F in (ProductView,EventView,Contact):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(ProductView)

    def show_frame(self, cont):
        # raise the chosen frame to the top
        frame = self.frames[cont]
        frame.tkraise()

# Products Object frame layouts product details
class ProductView(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        #making frames for different sections of the layout
        #product category frame
        pcf = tk.Frame(self)
        pcf.grid(row=0,column=0,padx=5)
        #product name frame
        pnf = tk.Frame(self)  
        pnf.grid(row=0,column=1,padx=5)
        #order details frame
        od = tk.Frame(self)
        od.grid(row=1,column=1,padx=5,pady=10,sticky=tk.W)

        #set scrollbar and listbox
        scroll = tk.Scrollbar(pnf)
        scroll.grid(row=2,column=3,columnspan=1,sticky='w',padx=5)
        customer_lstbox = tk.Listbox(pnf,width=50,height=20,bg='lightblue',bd=5)
        customer_lstbox.grid(row=2,column=0,pady=5,rowspan=3,columnspan=3,sticky='w')
        #customer_lstbox.config(yscrollcommand = scroll.set)
        scroll.configure(command = customer_lstbox.yview)
        
        #initialise product name frame (pnf) when called
        to_basket = tk.Button(od,text="Add to basket",width=20,height=2,bg='orange').grid(row=0,column=0)
        view_basket = tk.Button(od,text="View Basket",width=20,height=2,bg='lightblue').grid(row=0,column=1,padx=5)

# Events Object frame layouts product details
class EventView(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lbl = tk.Label(self,text='This Events page').pack()

# Contacts page providing contact details
class Contact(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lbl = tk.Label(self,text='Contact Us').pack()
        phn = tk.Label(self,text="Phone : 078113699245").pack()
        email = tk.Label(self,text="Email : theopnomi@gmail.com").pack()
        address = tk.Label(self,text="Address : 16 Newport road").pack()

app = App()
app.mainloop()