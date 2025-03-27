from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def issueBook(): 
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4, relheight=0.08)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black', command=lambda: issue(root, inf1, inf2))
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def issue(root, bid_entry, issueto_entry):
    bid = bid_entry.get()
    issueto = issueto_entry.get()

    if not bid or not issueto:
        messagebox.showinfo("Error", "Please fill in all fields")
        return

    try:
        # Use the same connection details as in main.py
        con = pymysql.connect(host="localhost", user="root", password="lalit", database="library")
        cur = con.cursor()

        # Check if book exists and is available
        cur.execute("SELECT status FROM books WHERE bid = %s", (bid,))
        result = cur.fetchone()
        
        if not result:
            messagebox.showinfo("Error", "Book ID not found")
            return
            
        status = result[0].lower()
        
        if status != 'avail':
            messagebox.showinfo("Message", "Book is not available for issuing")
            return

        # Issue the book
        cur.execute("INSERT INTO books_issued VALUES (%s, %s)", (bid, issueto))
        cur.execute("UPDATE books SET status = 'issued' WHERE bid = %s", (bid,))
        con.commit()
        
        messagebox.showinfo('Success', "Book Issued Successfully")
        root.destroy()
        
    except pymysql.Error as e:
        messagebox.showinfo("Database Error", f"Error occurred: {str(e)}")
    finally:
        if 'con' in locals() and con:
            con.close()