import datetime
from tkinter import messagebox

if 8 < datetime.datetime.now().time().hour < 19:
    messagebox.showinfo("Warning", "It is still bright out ,save electricity!")
else:
    print("")





