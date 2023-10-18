from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.geometry("980x500")
root.resizable("false","false")
root.title("Contact book")
root.config(background="#C8A2C8")#7DF9FF
global count
count=0
contacts={"name":[],"number":[],"email":[],"address":[]}
#background_photo=PhotoImage(file=r"C:\Users\dms66\Downloads\icon.png")
#root.iconbitmap(r"C:\Users\dms66\Downloads\icon2.jfif")
#label=Label(root,image=background_photo)
#label.place(x=0,y=0,relwidth=1,relheight=1)
#name
name_label=Label(root,text="Name",font=("Castellar",16),background="#003262",width=10,height=1,fg="white")
name_label.place(x=10,y=50)
name= StringVar()
name.set("")
name_input =Entry(root,textvariable=name,width=20,font=("Arial",16),bd=0 )
name_input.place(x=220,y=50)
#phone number
number_label=Label(root,text="Phone Number",font=("Castellar",16),background="#003262",width=12,height=1,fg="white")
number_label.place(x=10,y=100)
number= StringVar()
number.set("")
number_input =Entry(root,textvariable=number,width=20,font=("Arial",16),bd=0 )
number_input.place(x=220,y=100)
#email
email_label=Label(root,text="Email",font=("Castellar",16),background="#003262",width=10,height=1,fg="white")
email_label.place(x=10,y=150)
email= StringVar()
email.set("")
email_input =Entry(root,textvariable=email,width=25,font=("Arial",16),bd=0 )
email_input.place(x=220,y=150)
#address
address_label=Label(root,text="Address",font=("Castellar",16),background="#003262",width=10,height=1,fg="white")
address_label.place(x=10,y=200)
address= StringVar()
address.set("")
address_input =Entry(root,textvariable=address,width=25,font=("Arial",16),bd=0 )
address_input.place(x=220,y=200)
#treeview
fram_1=Frame(root,bd=3,width=600,height=640,bg="#DAC8AE")
fram_1.place(x=550,y=40)
style=ttk.Style
treeview = ttk.Treeview (fram_1, columns=('Name', 'Phone','Email','Address'))
treeview.column("#0",width=2,minwidth=2)
treeview.column("Name",width=200,minwidth=100,anchor=W)
treeview.column("Phone",width=200,minwidth=100,anchor=CENTER)
treeview.column("Email",width=2,minwidth=2)
treeview.column("Address",width=2,minwidth=2)
treeview.heading('#0', text='')
treeview.heading('Name', text='Name')
treeview.heading('Phone', text='Phone Number')
treeview.heading('Email', text='')
treeview.heading('Address', text='')


def addcontact():
    global count
    treeview.insert(parent='',index=END,iid=count,text=count,values=(name_input.get(),number_input.get(),email_input.get(),address_input.get()))
    count+=1
    contacts["name"].append(str(name_input.get()).capitalize())
    name_input.delete(0,END)
    contacts["number"].append(str(number_input.get()))
    number_input.delete(0, END)
    contacts["email"].append(str(email_input.get()))
    email_input.delete(0, END)
    contacts["address"].append(str(address_input.get()))
    address_input.delete(0, END)
def deletecontact():
     #x=treeview.selection()[0]
    # print(x)
     #print(type(x))
     #index=int(x[0])
     #print(index)
     #print(type(index))
     treeview.delete(treeview.selection()[0])
     #print(contacts["name"])
     #contacts["name"].remove(index)
def searched():
    global index
    found=0
    search_item=str(search_input.get()).lower()
    for name in contacts["name"]:
        if name.lower()==search_item:
            found=1
            index=contacts["name"].index(name)
            break
    for phone in contacts["number"]:
        if phone==search_item:
            index = contacts["number"].index(phone)
            found=1
            break
    if found:
        name_input.delete(0, END)
        number_input.delete(0, END)
        email_input.delete(0, END)
        address_input.delete(0, END)
        name_input.insert(0, contacts["name"][index])
        number_input.insert(0, contacts["number"][index])
        email_input.insert(0, contacts["email"][index])
        address_input.insert(0, contacts["address"][index])
    else:
        messagebox.showinfo("Result","This contact is not found")
def view():
    name_input.delete(0, END)
    number_input.delete(0, END)
    email_input.delete(0, END)
    address_input.delete(0, END)
    to_be_viewed=treeview.focus()
    values=treeview.item(to_be_viewed,'values')
    name_input.insert(0,values[0])
    number_input.insert(0,values[1])
    email_input.insert(0,values[2])
    address_input.insert(0,values[3])
def update():
    to_be_viewed=treeview.focus()
    treeview.item(to_be_viewed, text="",values=(name_input.get(),number_input.get(),email_input.get(),address_input.get()))
    name_input.delete(0, END)
    number_input.delete(0, END)
    email_input.delete(0, END)
    address_input.delete(0, END)

treeview.pack()

#buttons
fram_2=Frame(root,bd=0,width=50,height=200,bg="#DAC8AE")#7DF9FF
fram_2.place(x=200,y=400)
#fram_2.pack(padx=50)
add_btn=Button(fram_2,text="ADD",font=("Castellar",16),background="#FADFAD",width=7,height=1,fg="black",bd=2,command=addcontact)
add_btn.grid(row=1,column=2)
view_btn=Button(fram_2,text="VIEW",font=("Castellar",16),background="#00FFBF",width=7,height=1,fg="black",bd=2,command=view)
view_btn.grid(row=1,column=3)
update_btn=Button(fram_2,text="UPDATE",font=("Castellar",16),background="#ffd800",width=7,height=1,fg="black",bd=2,command=update)
update_btn.grid(row=1,column=4)
delete_btn=Button(fram_2,text="DELETE",font=("Castellar",16),background="red",width=7,height=1,fg="black",bd=2,command=deletecontact)
delete_btn.grid(row=1,column=5)

#search
search_button=Button(root,text="Search",font=("Castellar",16),background="#79443B",width=10,height=1,fg="white",bd=2,command=searched)
search_button.place(x=10,y=250)
search= StringVar()
search.set("")
search_input =Entry(root,textvariable=search,width=25,font=("Arial",16),bd=0 )
search_input.place(x=220,y=250)




root.mainloop()