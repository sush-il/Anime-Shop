import tkinter as tk
from tkinter.constants import E
import access_db
from dbmanage import ManageProduct

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

        for F in (StartPage,StaffView):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StaffView)

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

# Main window on startup     
class ManageProductView(tk.Frame):
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
        mng_people = tk.Button(frame2,width=15,height=3,bg='lightblue',text='Manage People',command="")
        exit = tk.Button(frame2,width=15,height=3,text="Exit",bg='red',command=lambda:controller.show_frame(StartPage))
        #place all the buttons
        add_product.grid(row=0,column=0,padx=5,pady=5)
        update_product.grid(row=0,column=1,padx=5,pady=5) 
        delete_product.grid(row=1,column=0,padx=5,pady=5)
        srch_product.grid(row=1,column=1,padx=5,pady=5)
        view_all.grid(row=2,column=0,padx=5,pady=5)
        mng_people.grid(row=2,column=1,padx=5,pady=5)
        exit.grid(row=3,column=0,columnspan=3)

app = App()
app.mainloop()