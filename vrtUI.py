from tkinter import *
import tkinter.scrolledtext as scr
import vrtSeasonDownload as vsd 

myFont = ("Arial", 15)

w = Tk()
w.title("VRT SEASON DOWNLOADER")

# HEADING
lblhead = Label(w, text="Uw VRT.nu login gegevens:", font=myFont)
lblhead.grid(row=0, column=1, pady=(30, 10))

# Email label
lbl = Label(w, text="Email:", font=myFont)
lbl.grid(row=1, column=0, pady=(0,10), padx=(30, 10))
# Email Field
txt = Entry(w, width=50, font=myFont)
txt.grid(row=1, column=1, pady=(0,10), padx=(0, 40))
txt.focus()

# Password Label
lbl2 = Label(w, text="Password:", font=myFont)
lbl2.grid(row=2, column=0, pady=(0,10), padx=(30, 10))
# Password Field
txt2 = Entry(w, width=50, show="*", font=myFont)
txt2.grid(row=2, column=1, pady=(0,10), padx=(0, 40))

#Link to page
lbl3 = Label(w, text="De link naar de VRT.nu pagina:", font=myFont)
lbl3.grid(row=3, column=1, pady=(20,10))
# Link Fiels
txt3 = Entry(w, width=50, font=myFont)
txt3.grid(row=4, column=1, pady=(0,20), padx=(0, 40))

# Path Label
lbl4 = Label(w, text="Bestandslocatie:", font=myFont)
lbl4.grid(row=5, column=1, pady=(0,10), padx=(0, 40))
# Path
txt4 = Entry(w, width=50, font=myFont)
txt4.insert(END, "H:\\Films\\")
txt4.grid(row=6, column=1, pady=(0,20), padx=(0, 40))

# Output Window
out = scr.ScrolledText(w, width=50, height=10, font=("Arial", 12))
out.grid(row=8, column=1, padx=(0, 40), pady=(20, 30))

# button
def clickHelper(l):
    # show info to user
    stemp = "#############################################\n"
    stemp += "## Downloading these videos ######################\n"
    stemp += "#############################################\n\n"
    out.insert(INSERT, stemp)
    for x in li:
        out.insert(INSERT, x + "\n")
        
def click():
    url = txt3.get()
    li = vsd.getList(url)
    clickHelper(li)
    
    mail = txt.get()
    pw = txt2.get()
    path = txt4.get()
    vsd.downloadList(li, path, mail, pw)
    
    return True

btn = Button(w, text="Download", font=myFont, command=click, bg="#ccc")
btn.grid(row=7, column=1, padx=(0, 40))

w.mainloop()


