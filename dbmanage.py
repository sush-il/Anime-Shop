from os import access
import tkinter as tk
import access_db

class ManagePeople:
    def __init__(self,container):
        self.container = container

    def get_selected_row(self,event):
        #selected tuple is the selected item from listbox
        global selected_tuple
        index = self.container.lst_box.curselection()[0]
        selected_tuple = self.container.lst_box.get(index)
        
        #populating the fields with data upon selection
        self.container.name.delete(0,tk.END)
        self.container.name.insert(tk.END,selected_tuple[1])
        
        self.container.age.delete(0,tk.END)
        self.container.age.insert(tk.END,selected_tuple[2])
        
        self.container.phone.delete(0,tk.END)
        self.container.phone.insert(tk.END,selected_tuple[3])
        
        self.container.address.delete(0,tk.END)
        self.container.address.insert(tk.END,selected_tuple[4])

        self.container.email.delete(0,tk.END)
        self.container.email.insert(tk.END,selected_tuple[5])

        self.container.password.delete(0,tk.END)
        self.container.password.insert(tk.END,selected_tuple[6])
    
    def view_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.view(db):
            self.container.lst_box.insert(tk.END,row)

    def search_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.search(self.container.name.get(),self.container.age.get(),self.container.phone.get(),self.container.address.get(),self.container.email.get(),db):
            self.container.lst_box.insert(tk.END,row)

    def insert_data(self,db):
        access_db.insert(self.container.name.get(),self.container.age.get(),self.container.phone.get(),self.container.address.get(),self.container.email.get(),self.container.password.get(),db)
        self.container.lst_box.delete(0,tk.END)
        self.container.lst_box.insert(tk.END,(self.container.name.get(),self.container.age.get(),self.container.phone.get(),self.container.address.get(),self.container.email.get(),self.container.password.get()))

    def delete_data(self,db):
        #clearing the lisbox
        self.container.lst_box.delete(0,tk.END)
        #clearing the entry widgets
        self.container.name.delete(0,tk.END)
        self.container.age.delete(0,tk.END)
        self.container.phone.delete(0,tk.END)
        self.container.address.delete(0,tk.END)
        self.container.email.delete(0,tk.END)
        self.container.password.delete(0,tk.END)

        access_db.delete(selected_tuple[0],db)
    
    def update_data(self,db):
        access_db.update(selected_tuple[0],self.container.name.get(),self.container.age.get(),self.container.phone.get(),self.container.address.get(),self.container.email.get(),self.container.password.get(),db)

    def sort(self,db,factor):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.sort(db,factor):
            self.container.lst_box.insert(tk.END,row)

class ManageProduct:
    def __init__(self,container):
        self.container = container

    def get_selected_row(self,event):
        global selected_tuple
        index = self.container.lst_box.curselection()[0]
        selected_tuple = self.container.lst_box.get(index)
        
        #populating the fields upon selection
        self.container.name.delete(0,tk.END)
        self.container.name.insert(tk.END,selected_tuple[1])

        self.container.price.delete(0,tk.END)
        self.container.price.insert(tk.END,selected_tuple[2])
        try:
            self.container.isbn.delete(0,tk.END)
            self.container.isbn.insert(tk.END,selected_tuple[3])
        except:
            self.container.address.delete(0,tk.END)
            self.container.address.insert(tk.END,selected_tuple[4])

    def view_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.view_pd(db):
            self.container.lst_box.insert(tk.END,row)

    def search_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.search_pd(self.container.name.get(),self.container.price.get(),self.container.isbn.get(),self.container.address.get(),self.container.category.get(),db):
            self.container.lst_box.insert(tk.END,row)

    def insert_data(self,db):
        access_db.insert_pd(self.container.name.get(),self.container.price.get(),self.container.isbn.get(),self.container.address.get(),self.container.category.get(),db)
        self.container.lst_box.delete(0,tk.END)
        self.container.lst_box.insert(tk.END,(self.container.name.get(),self.container.price.get(),self.container.isbn.get(),self.container.address.get(),self.container.category.get()))

    def delete_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        access_db.delete_pd(selected_tuple[0],db)
    
    def update_data(self,db):
        access_db.update_pd(selected_tuple[0],self.container.name.get(),self.container.price.get(),self.container.isbn.get(),self.container.address.get(),self.container.category.get(),db)

class CustomerProductView:
    def __init__(self,container):
        self.container = container
    
    def search_data(self,db):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.search_pd(self.container.name.get(),self.container.price.get(),self.container.isbn.get(),"##","##",db):
            self.container.lst_box.insert(tk.END,row)

    def insert_order(self,user_id,product_type):
        product_id = selected_tuple[0]
        self.container.lst_box.delete(0,tk.END)
        access_db.create_order(user_id,selected_tuple[0],"Orders")
 
    def view_order(self,userid):
        total_price = 0
        self.lst_box.delete(0,tk.END)
        for row in access_db.view_order(userid):
            self.lst_box.insert(tk.END,row)
            total_price += row[1]
        
        return total_price

    def view_all_orders(self):
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.view_all_orders():
            self.container.lst_box.insert(tk.END,row)

class ManageOrder:
    def __init__(self,container):
        self.container = container

    def get_selected_row(self,event):
        global selected_tuple
        index = self.container.lst_box.curselection()[0]
        selected_tuple = self.container.lst_box.get(index)
        
        #populating the fields upon selection for users who made order
        try:
            self.container.userid.delete(0,tk.END)
            self.container.userid.insert(tk.END,selected_tuple[0])

            self.container.cust_name.delete(0,tk.END)
            self.container.cust_name.insert(tk.END,selected_tuple[1])

            self.container.cust_address.delete(0,tk.END)
            self.container.cust_address.insert(tk.END,selected_tuple[2])

            self.container.cust_email.delete(0,tk.END)
            self.container.cust_email.insert(tk.END,selected_tuple[3])
        
        #populating the fields upon selection for the products ordered
        except:
            self.container.prod_id.delete(0,tk.END)
            self.container.prod_id.insert(tk.END,selected_tuple[0])

            self.container.prod_name.delete(0,tk.END)
            self.container.prod_name.insert(tk.END,selected_tuple[1])

            self.container.prod_price.delete(0,tk.END)
            self.container.prod_price.insert(tk.END,selected_tuple[2])

            self.container.prod_isbn.delete(0,tk.END)
            self.container.prod_isbn.insert(tk.END,selected_tuple[3])

    def search_order(self):
        userid = self.container.userid.get()
        self.container.lst_box.delete(0,tk.END)
        for row in access_db.search_order(userid):
            self.container.lst_box.insert(tk.END,row)
        
    def display_items(self):
        total_price = 0
        all_items = access_db.view_ordered_items(selected_tuple[0])
        self.container.lst_box.delete(0,tk.END)
        for row in all_items:
            self.container.lst_box.insert(tk.END,row)
            total_price += row[2]
        
        return total_price

    def mark_complete(self):
        #clearing the lisbox
        self.container.lst_box.delete(0,tk.END)
        #clearing the entry widgets
        self.container.userid.delete(0,tk.END)
        self.container.cust_name.delete(0,tk.END)
        self.container.cust_address.delete(0,tk.END)
        self.container.cust_email.delete(0,tk.END)

        access_db.transfer_orders(selected_tuple[0])

    def download_invoice():
        pass


            









