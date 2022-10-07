import tkinter as tk

class EntryPopup(tk.Frame):
    def __init__(self,out_value:list,parent,*args,**kwargs):
        self.value = out_value
        super().__init__(master=parent,*args,**kwargs)
        self.toplevel = tk.Toplevel(parent)
        self.entry = tk.Entry(master=self.toplevel)
        self.entry.pack()
        tk.Button(text="Quit",master=self.toplevel,command=self.save_and_destroy).pack()
        self.toplevel.protocol("WM_DELETE_WINDOW",self.save_and_destroy)
    def save_value(self):
        self.value.append(self.entry.get())
    def save_and_destroy(self):
        self.save_value()
        self.toplevel.destroy()

##############

def show_popup() -> str:
    val = []
    x = EntryPopup(val,window)
    x.toplevel.wait_window()
    return val[-1]

def set_label():
    lab["text"] = show_popup()

##############

window = tk.Tk()
lab = tk.Label(text="Your text here")
lab.pack()
tk.Button(command=set_label,text="Set label text").pack()

window.mainloop()
