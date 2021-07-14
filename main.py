from tkinter import ttk
import tkinter as tk
import departamento_judicial
import requests
from PIL import ImageTk, Image
import io


TOKEN_DEPARTAMENTO_JUDICIAL = "pk.eyJ1IjoiamF2aWVycHlrZSIsImEiOiJja2N2ejQ2MDAwOHluMnltcDZnNmY3eTd1In0.tdo-BVp97WovMbdE8AJj0g"

class Aplicacion():
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.geometry("700x650")

        self.label_latitud = tk.Label(self.raiz,text="LATITUD")
        self.label_latitud.grid(stick="W",column=0,row=0)
        self.latitud_buscar = tk.StringVar()
        self.latitud = ttk.Entry(self.raiz,textvariable=self.latitud_buscar)
        self.latitud.grid(stick="W",column=0,row=1)

        self.label_longitud = tk.Label(self.raiz,text="LONGITUD")
        self.label_longitud.grid(stick="W",column=0,row=2)
        self.longitud_buscar = tk.StringVar()
        self.longitud = ttk.Entry(self.raiz,textvariable=self.longitud_buscar)
        self.longitud.grid(stick="W",column=0,row=3)

        self.buscar = ttk.Button(self.raiz,text="BUSCAR",command=self.buscar)
        self.buscar.grid(sticky="NW",column=0,row=4)

    def buscar(self):
        juzgado = departamento_judicial.calcular_departamento_cercano(float(self.latitud.get()),float(self.longitud.get()))
        url = "https://api.mapbox.com/styles/v1/mapbox/light-v10/static/{:f},{:f},14,12/500x500?access_token={:s}".format(
            juzgado.get_longitud(), juzgado.get_latitud(), TOKEN_DEPARTAMENTO_JUDICIAL)

        r = requests.get(url)
        im = Image.open(io.BytesIO(r.content))
        self.foto = ImageTk.PhotoImage(im)
        self.label_titulo = tk.Label(self.raiz,text="Nombre: {nom} / Numero: {num}".format(nom=juzgado.get_nombre(),num=juzgado.get_numero()))
        self.label_datos = tk.Label(self.raiz,text="Fuero: {fuero} / Tipo: {tipo} / Direccion: {dir}".format(fuero=juzgado.get_fuero(),tipo=juzgado.get_tipo_de_ente(),dir=juzgado.get_direccion()))
        self.label_datos2 = tk.Label(self.raiz,text="Localidad: {loc} / Departamento judicial: {dep}".format(loc=juzgado.get_localidad(),dep=juzgado.get_departamento_judicial()))
        self.label_datos3 = tk.Label(self.raiz,text="Telefono: {tel} / Latitud: {lat} / Longitud: {lon}".format(tel=juzgado.get_telefono(),lat=juzgado.get_latitud(),lon=juzgado.get_longitud()))
        self.label_resultado = tk.Label(self.raiz,image=self.foto)
        self.label_titulo.grid(stick="W",column=1,row=0)
        self.label_datos.grid(stick="W",column=1,row=1)
        self.label_datos2.grid(stick="W",column=1,row=2)
        self.label_datos3.grid(stick="W",column=1,row=3)
        self.label_resultado.grid(stick="W",column=1,row=4)
        
    def iniciar(self):
        self.raiz.mainloop()

def main():
    Aplicacion().iniciar()

main()


