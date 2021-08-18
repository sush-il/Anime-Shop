import tkinter as tk
import access_db

class ManagePeople:
    def __init__(self,container):
        self.container = container

    def get_selected_row(self,event):
        global selected_tuple
        index = self.container.lst_box.curselection()[0]
        selected_tuple = self.container.lst_box.get(index)
        
        #populating the fields upon selection
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
        access_db.delete(selected_tuple[0],db)
    
    def update_data(self,db):
        access_db.update(selected_tuple[0],self.container.name.get(),self.container.age.get(),self.container.phone.get(),self.container.address.get(),self.container.email.get(),self.container.password.get(),db)

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

        self.container.isbn.delete(0,tk.END)
        self.container.isbn.insert(tk.END,selected_tuple[3])

        self.container.address.delete(0,tk.END)
        self.container.address.insert(tk.END,selected_tuple[4])
        
        #self.container.category.delete(0,tk.END)
        #self.container.dropdown.insert(tk.END,selected_tuple[5])

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
        access_db.delete_pd(selected_tuple[0],db)
    
    def update_data(self,db):
        access_db.update_pd(selected_tuple[0],self.container.name.get(),self.container.price.get(),self.container.isbn.get(),self.container.address.get(),self.container.category.get(),db)
