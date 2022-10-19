from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor

class popup_sqo(Frame):
    def __init__(self, out_val:list, master: Tk, *args, **kargs):
        self.out = out_val
        super().__init__(master=master, *args, **kargs)
        self.top_level = Toplevel(master)
        self.colorr = '#000000'
        self.puntos_input()

        self.grosor_color_frame()
        
        self.segmentado_input()        
        #fin modificaciones
        Button(master=self.top_level, text='Cancelar', command=self.destroy).pack(side=RIGHT)
        Button(master = self.top_level, text='Aceptar', command=self.save_destroy).pack(side=RIGHT)
        self.top_level.protocol('MW_DELETE_WINDOW', self.destroy)
    
    def puntos_input(self):
        self.entt_impo = Frame(master=self.top_level)
        self.a = Label(master=self.entt_impo, text='Punto A:')
        self.a.pack(side=LEFT)

        self.a_in_x = Entry(master=self.entt_impo)
        self.a_in_x.pack(side=LEFT)
        self.a_in_y = Entry(master=self.entt_impo)
        self.a_in_y.pack(side=LEFT)
        
        self.b = Label(master=self.entt_impo, text='Punto B:')
        self.b.pack(side=LEFT)
        self.b_in_x = Entry(master=self.entt_impo)
        self.b_in_x.pack(side=LEFT)
        self.b_in_y = Entry(master=self.entt_impo)
        self.b_in_y.pack(side=LEFT)
        
        self.entt_impo.pack(side=TOP)

    def grosor_color_frame(self):
        self.gro_col = Frame(master=self.top_level)
        Label(master=self.gro_col, text='grosor:').pack(side=LEFT)
        self.var = StringVar(master = self.gro_col)
        option = ['1', '2', '3']
        self.var.set('1')
        self.grosor = OptionMenu(self.gro_col,self.var,*option,command=self.redef)
        self.var.set('1')
        self.grosor.pack(side=LEFT)
        Label(master=self.gro_col, text='color: ').pack(side=LEFT)
        self.color = Entry(master=self.gro_col)
        self.color.insert(0, '#000000')
        self.color.pack(side=LEFT)
        Button(master=self.gro_col, text='cod_col', command=self.getColor).pack(side=RIGHT)
        self.gro_col.pack(side=TOP)

    def getColor(self):
        self.colorr = askcolor()[1]
        if self.colorr!=None:
            self.color.delete(0, END)
            self.color.insert(0, self.colorr)
        else:
            self.colorr = self.color.get()

    def segmentado_input(self):
        self.segmentado_out = False
        self.seg = Frame(master=self.top_level)
        Label(master=self.seg, text='Segmentado').pack(side=LEFT)
        varr = IntVar()

        self.segmentado = Checkbutton(master=self.seg,variable=varr, onvalue=1, offvalue=0, command=self.cambiar)
        self.segmentado.pack(side=LEFT)
        self.seg.pack(side=TOP)

    def cambiar(self):
        print(self.segmentado_out)
        self.segmentado_out = not (self.segmentado_out)

    def redef(self, selection):
        self.grosor_out = selection

    def destroy(self):
        self.top_level.destroy()
    
    def save_destroy(self):
        try:
            self.out.append(int(self.a_in_x.get()))
            self.out.append(int(self.a_in_y.get()))
            self.out.append(int(self.b_in_x.get()))
            self.out.append(int(self.b_in_y.get()))
            app = []
            app.append(int(self.var.get()))
            app.append(self.colorr)
            app.append(self.segmentado_out)
            self.out.append(app)
            print(self.out)
            self.destroy()
        except ValueError:
            self.mostrarError('Error en las entradas, solo admite numeros')
        except Exception:
            self.mostrarError('Error debe llenar las areas requeridas')

    def mostrarError(self, x:str):
        messagebox.showerror(title='Error de entrada', message=x)

