from tkinter import *
from tkinter import messagebox

from Objeto import *

class popup_traslacion(Frame):
    def __init__(self, out_val:list, objs:list, master: Tk, *args, **kargs):
        self.out = out_val
        super().__init__(master=master, *args, **kargs)
        self.top_level = Toplevel(master)
                
        self.pts_clv()
        self.dpl(objs)

        Button(master=self.top_level, text='Cancelar', command=self.destroy).pack(side=RIGHT)
        Button(master = self.top_level, text='Aceptar', command=self.save_destroy).pack(side=RIGHT)
        self.top_level.protocol('MW_DELETE_WINDOW', self.destroy)
    
    def pts_clv(self):
        self.entt_impo = Frame(master=self.top_level)
        Label(master=self.entt_impo, text='tx:').pack(side=LEFT)
        self.t_in_x = Entry(master=self.entt_impo)
        self.t_in_x.pack(side=LEFT)

        Label(master=self.entt_impo, text='ty:').pack(side=LEFT)
        self.t_in_y = Entry(master=self.entt_impo)
        self.t_in_y.pack(side=LEFT)

        self.entt_impo.pack(side=TOP)

    def dpl(self, aux:list):
        self.variable = StringVar(self.top_level)
        self.variable.set(aux[0])
        self.option_men = OptionMenu(self.top_level, self.variable, *aux)
        self.option_men.pack(side=TOP)

    def destroy(self):
        self.top_level.destroy()

    def save_destroy(self):
        try:
            self.out.append(int(self.t_in_x.get()))
            self.out.append(int(self.t_in_y.get()))
            self.out.append(self.variable.get())
            self.destroy()           
        except ValueError:
            self.mostrarError('Error en las entradas, solo admite numeros')
        except Exception:
            self.mostrarError('Error debe llenar las areas requeridas')


    def mostrarError(self, x:str):
        messagebox.showerror(title='Error de entrada', message=x)