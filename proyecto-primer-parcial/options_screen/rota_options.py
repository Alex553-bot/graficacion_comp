from tkinter import *
from tkinter import messagebox

from Objeto import *

class popup_rotacion(Frame):
    def __init__(self, out_val:list, objs:list, master: Tk, *args, **kargs):
        self.out = out_val
        super().__init__(master=master, *args, **kargs)
        self.top_level = Toplevel(master)
        self.irl = []
        for x in objs:
            self.irl.append(x.identificador + str(hex(id(x))))
        self.oo = objs        
        self.pts_clv()
        self.dpl(self.irl)

        Button(master=self.top_level, text='Cancelar', command=self.destroy).pack(side=RIGHT)
        Button(master = self.top_level, text='Aceptar', command=self.save_destroy).pack(side=RIGHT)
        self.top_level.protocol('MW_DELETE_WINDOW', self.destroy)
    
    def pts_clv(self):
        self.entt_impo = Frame(master=self.top_level)
        Label(master=self.entt_impo, text='A:').pack(side=LEFT)
        self.p_in_x = Entry(master=self.entt_impo)
        self.p_in_x.insert(0, '0')
        self.p_in_x.pack(side=LEFT)

        self.p_in_y = Entry(master=self.entt_impo)
        self.p_in_y.insert(0, '0')

        self.p_in_y.pack(side=LEFT)

        Label(master=self.entt_impo, text='rotar:').pack(side=LEFT)
        self.ang = Entry(master=self.entt_impo)
        self.ang.pack(side=LEFT)

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
            self.out.append(int(self.p_in_x.get()))
            self.out.append(int(self.p_in_y.get()))
            self.out.append(int(self.ang.get())%360)
            self.out.append(self.variable.get().split()[-1])
            print(self.out[-1])
            self.destroy()           
        except ValueError:
            self.mostrarError('Error en las entradas, solo admite numeros')
        except Exception:
            self.mostrarError('Error debe llenar las areas requeridas')


    def mostrarError(self, x:str):
        messagebox.showerror(title='Error de entrada', message=x)