from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.geometry("500x555")
root.title("UPG Utility")
root.resizable(False,False)

def generator():
    #this is the base code for the unique password generator
    full_dict = []
    raw_pass = []
    
    l1 = [chr(a) for a in range(97,123)]
    l2 = [chr(a) for a in range(65,91)]
    l3 = [chr(a) for a in range(48,58)]
    l4 = ["@","#","$","%"]


    if(smallValue.get() == 0 and capValue.get() == 0 and numValue.get() == 0 and specialValue.get() == 0):
        messagebox.showerror("Unique Password Status","At least one box needs to be checked.")
    elif(passlengthValue.get()<4):
        messagebox.showerror("Unique Password Status","Password Length cannot be less than 4.")
    else:
        if(smallValue.get() == 1):
            raw_pass.append(random.choice(l1))
            full_dict.extend(l1)

        if(capValue.get() == 1):
            raw_pass.append(random.choice(l2))
            full_dict.extend(l2)

        if(numValue.get() == 1):
            raw_pass.append(random.choice(l3))
            full_dict.extend(l3)

        if(specialValue.get() == 1):
            raw_pass.append(random.choice(l4))
            full_dict.extend(l4)

        random.shuffle(full_dict)

        x = int(passlengthValue.get())
        shuffle_pass = []
        final_pass = ""
        start_val = smallValue.get() + capValue.get() + numValue.get() + specialValue.get()

        for _ in range(start_val,x):
            raw_pass.append(random.choice(full_dict))

        shuffle_pass = random.sample(raw_pass,len(raw_pass))
        final_pass = final_pass.join(map(str,shuffle_pass))
        #print(final_pass)
        password.delete('1.0', 'end') #clear the output text text widget
        password.insert(END, final_pass)
        if(passlengthValue.get()>=8):
            messagebox.showinfo("Unique Password Status","New Password Generated Successfully.")
        else:
            messagebox.showwarning("Unique Password Status","The Generated Password is weak.\nChoose a password of length greater than 8.")
    

#Heading
Label(root,text="UNIQUE PASSWORD GENERATOR", font="comicsansms 20 bold").grid(row=0, column=1, padx=(15,0), pady=(25,15))

#Texts for the application
p = Label(root, text="PASSWORD:",font="comicsansms 12").grid(row=1, column=1, padx=(40,0), sticky=W)
p_length = Label(root, text="PASSWORD LENGTH:",font="comicsansms 12").grid(row=2, column=1, padx=(40,0), pady=(10,0), sticky=W)
Label(root, text="PASSWORD MUST CONTAIN:",font="comicsansms 12").grid(row=3, column=1, padx=(40,0), pady=(20,10), sticky=W)

#Tkinter variables for storing entries
passlengthValue = IntVar()
smallValue = IntVar()
capValue = IntVar()
numValue = IntVar()
specialValue = IntVar()

#Entry and Password display for our program
plengthEntry = Entry(root, textvariable=passlengthValue, bg = "light grey").grid(row=2, column=1, pady=(10,0), padx=(0,25), sticky=E)
password = Text(root, height = 3, width = 30, bg = "light grey")
password.grid(row=1, column=1, padx=(0,25), sticky=E)

#Checkboxes
Label(root, text= "SMALL LETERS [a-z]",font="comicsansms 10").grid(row=6, column=1, padx=(50,0), pady=5, sticky=W)
Label(root, text= "CAPITAL LETERS [A-Z]",font="comicsansms 10").grid(row=7, column=1, padx=(50,0), pady=5, sticky=W)
Label(root, text= "NUMBERS [0-9]",font="comicsansms 10").grid(row=8, column=1, padx=(50,0), pady=5, sticky=W)
Label(root, text= "SPECIAL CHARACTERS",font="comicsansms 10").grid(row=9, column=1, padx=(50,0), pady=5, sticky=W)
lowercase = Checkbutton(root, variable=smallValue, selectcolor="light grey").grid(row=6,column=1,padx=(30,0))
uppercase = Checkbutton(root, variable=capValue, selectcolor="light grey").grid(row=7,column=1,padx=(30,0))
numbers = Checkbutton(root, variable=numValue, selectcolor="light grey").grid(row=8,column=1,padx=(30,0))
specialChars = Checkbutton(root, variable=specialValue, selectcolor="light grey").grid(row=9,column=1,padx=(30,0))

#Buttons
Button(root, text="GENERATE PASSWORD", font="comicsansms 15", bg="light grey", command=generator).grid(row=10,column=1,pady=30)
Button(root, text="QUIT", font="comicsansms 15", bg="light grey", command=root.destroy).grid(row=11,column=1)

root.mainloop()