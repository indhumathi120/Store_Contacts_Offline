from tkinter import *
#from tkinter import everything

def details():
    def save():
        txt=n1.get()
        #getting input from Entry variable n1
        
        txt1=num1.get()
        #getting number from the Entry
        
        txt2=mail1.get()
        #getting mail input from the Entry
        
        with open("Docu.txt","a+") as file:
        #opening the file named "Docu.txt" in append mode.
            file.write("-Name:"+txt+"\n"+"Ph.no:"+txt1+"\n"+"Email:"+txt2+"-"+"\n\n")
            #writing the details
            
        d.destroy()
        #to close tkinter window
    
    d=Tk()
    #creating another tkinter window named d
    
    d.title("Details")
    #setting title for the tkinter window
    
    name=Label(d, text="Name:")
    n1=Entry(d, width=25)
    num=Label(d, text="Ph.no:")
    num.grid(row=2,column=0)
    num1=Entry(d, width=25)
    num1.grid(row=2,column=1)
    mail=Label(d, text="Email:")
    mail.grid(row=3,column=0)
    mail1=Entry(d, width=25)
    mail1.grid(row=3,column=1)
    name.grid(row=1,column=0)
    n1.grid(row=1, column=1)
    #creating the blocks of Label and entry to get user input.
    
    s=Button(d, text="Save", width=15, command=save)
    s.grid(row=4,column=1)
    #Creating a button with function call "save".
    
    d.mainloop()
    #completing the d tkinter window

def search():
    s=new.get()
    #getting input from the Entry named new
    
    with open('Docu.txt','r+') as file:
    #opening the file named "Docu.txt" in read and append mode
        
        txt=file.read()
        #reading the content the file
        
        txt=txt.split("-")
        #spliting the content with respect to "-"
        
        for i in txt:
            if s in i:
            #Checks the relevent content in file.
                
                new2.delete(1.0, END)
                #deleting the pre-existing data
                
                new2.insert(END,i)
                #inserting and displaying updates data.
        
def Display():
    with open('Docu.txt','r+') as file:\
    #opening the file named "Docu.txt" in read and append mode
        
        txt=file.read()
        #reads the content in the file
        
        txt=txt.split("-")
        #spliting the content by means of "-"
        
        new2.delete(1.0, END)
        #deleting the pre existing content.
        
        for i in txt:
            new2.insert(END, i)
            #Displaying the content.
        
def Delete():
    def confirm():
        p=se.get()
        #getting content in entry as input

        o=[]
        #creating a empty list
        
        with open('Docu.txt','r+') as f:
        #opening a file named "Docu.txt" in read and append mode
            
            content=f.read()
            #reading the content in the file
            
            content=content.split("-")
            #spliting the content with respect to "-"
            
            k=""
            #creating the empty string
            
            c=[]
            #creating empty list
            
            for i in content:
                k="-"+i+"-"
                c.append(k)
                #getting string the appending the file.
                
            for i in c:
                if p in i:
                    o.append("--")
                    o.append(i)
                    o.append("-\n\n-")
                    #appending "--" ,"content in the list c","\n\n" in list 'o'
                    
            f.seek(0)
            #pointing to the oth position of the file
            
            for i in c:
                if not any(j in i  for j in o):
                    f.write(i)
                    f.write("\n\n")
        
            f.truncate()
            #deleting the content to be deleted in the file.
            
        l.destroy()
        #closing the tkinter window.
    

    def delet():
        s=se.get()
        #getting input from Entry se
        
        with open('Docu.txt','r+') as file:
            #opening file named "Docu.txt" in read and append mode.
            
            txt=file.read()
            #reading the content of the file.
            
            txt=txt.split("-")
            #spliting the content with respect to "-"
            
            new3.delete(1.0,END)
            #deleting the pre existing content in text space.
            
            for i in txt:
                if s in i:
                #checking the content to be deleted in the file
                    
                    new3.insert(END,i)
                    #displaying the content to be deleted.

        conf=Button(l, text="Confirm Delete", width=20, command=confirm)
        conf.pack()
        #Creating Cofirm Delete button with function call "confirm"
        
        new3.pack()


    l=Tk()
    #Creating a new tkinter window
    
    l.geometry("200x250")
    #Setting dimensions for the tkinter window
    
    l.title("Delete")
    #Setting title for the tkinter window
    
    en=Label(l, text="Enter the name of contact to delete:")
    #Creating label to notofy the user.
    
    se=Entry(l, width=35)
    #Creating to entry to display content to be deleted.
    
    cd=Button(l, text="Delete", width=20, command=delet)
    #Creating Delete button with function call "delet"
    
    new3=Text(l, height=10, width=35)
    #creating text space.
    
    en.pack()
    se.pack()
    cd.pack()
    l.mainloop()
    #completing the l tkinter window

con=Tk()
#mainroot name of tkinter window

con.geometry("400x300")
#setting geometry for the tkinter window

con.title('Contact list')
#title for tkinter window

f=Frame(con)
#making frame for tkinter window

f.pack()

var=StringVar()
#Declaration of string variable

new2=Text(con, height=10, width=35)
#creating text space of given dimension

new=Entry(con, width=35)
#creating Entry

add=Button(f, text="Add", command=details)
add.pack(side=LEFT)
#creating Add button with function call "details".

sear=Button(f, text="Search", command=search)
sear.pack(side=LEFT)
#creating Search button with function call of "search"


new1=Label(con, text="Enter name or contact to search")
new1.pack()
#Creating label to notify the user

dis=Button(f, text="Display", command=Display)
dis.pack(side=LEFT)
#creating Display button with function call of "Display".

dele=Button(f, text="Delete", command=Delete)
dele.pack(side=LEFT)
#creating Delete button with function call of "Delete"

new.pack()
new2.pack()

con.mainloop()
#completing the con tkinter window
