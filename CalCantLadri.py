import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calcular_LadrillosMuro(entry_longitud_muro, entry_altura_muro, entry_longitud_ladrillo_muro, entry_altura_ladrillo_muro, entry_espesor_ladrillo_muro,  label_resultado_muro):
    try:
        longitudMuro = float(entry_longitud_muro.get())
        alturaMuro = float(entry_altura_muro.get())
        
        longitudLadrillo = float(entry_longitud_ladrillo_muro.get())
        alturaLadrillo = float(entry_altura_ladrillo_muro.get())
        espesorLadrillo = float(entry_espesor_ladrillo_muro.get())        

        areaMuro = longitudMuro * alturaMuro

        cantidad_ladrillosSoga = round(areaMuro / ((longitudLadrillo+0.015)*(alturaLadrillo+0.015)),2)
        cantidad_ladrillosSoga1 = cantidad_ladrillosSoga
        cantidad_ladrillosCabeza = round(areaMuro / ((espesorLadrillo+0.015)*(alturaLadrillo+0.015)),2)
        cantidad_ladrillosCabeza1 = cantidad_ladrillosCabeza 
        cantidad_ladrillosCanto = round(areaMuro / ((longitudLadrillo+0.015)*(espesorLadrillo+0.015)),2)
        cantidad_ladrillosCanto1 = cantidad_ladrillosCanto 
        label_resultado_muro.config(text=f"Asentado tipo Soga : {cantidad_ladrillosSoga1: .2f} ladrillos \n"
                                                                f"\t+5% de desperdicio  {(1.05*cantidad_ladrillosSoga1): .2f} ladrillos \n\n"
                                    
                                                                f"Asentado tipo Cabeza : {cantidad_ladrillosCabeza1: .2f} ladrillos \n"
                                                                f"\t+5% de desperdicio {(1.05*cantidad_ladrillosCabeza1): .2f} ladrillos   \n\n"
                                
                                                                f"Asentado tipo Canto : {cantidad_ladrillosCanto1: .2f} ladrillos \n"
                                                                f"\t+5% de desperdicio {(1.05*cantidad_ladrillosCanto1): .2f} ladrillos ")
           
    except ValueError:
        label_resultado_muro.config(text="Por favor, introduce valores válidos.")

def calcular_LadrillosTecho(entry_ancho_techo, entry_longitud_techo, entry_ancho_ladrillo_techo, entry_longitud_ladrillo_techo, entry_ancho_vigueta_techo, label_resultadoTecho):
    try:
        anchoTecho = float(entry_ancho_techo.get())
        longitudTecho = float(entry_longitud_techo.get())
        anchoLadrillo = float(entry_ancho_ladrillo_techo.get())
        longitudLadrillo = float(entry_longitud_ladrillo_techo.get())
        anchoVigueta = float(entry_ancho_vigueta_techo.get())

        area_losa = anchoTecho * longitudTecho

        cantidad_ladrillos = round(area_losa / ((anchoLadrillo+anchoVigueta)*longitudLadrillo),2)
        cantidad_ladrillos1 = cantidad_ladrillos
        
        label_resultadoTecho.config(text=f"Para un techo de {anchoTecho}m. x {longitudTecho}m.\n\n"
                                    f"Se necesita: {cantidad_ladrillos1: .2f}  ladrillos \n"
                                    f"+5% de desperdicio se necesita {(1.05*cantidad_ladrillos1): .2f} ladrillos")
    except ValueError:
        label_resultadoTecho.config(text="Por favor, introduce valores válidos.")


def crear_interfaz():
    # Crea la ventana principal
    ventana = tk.Tk()
    ventana.title("Calculadora de Ladrillos")
    ventana.geometry("620x620")
 
    # Crear el widget de pestañas
    tab_control = ttk.Notebook(ventana)

    # Pestaña de Presentación
    tab_presentacion = ttk.Frame(tab_control)
    tab_control.add(tab_presentacion, text='Presentación')

    label_presentacion = tk.Label(tab_presentacion, text=" \n\n"
                                  "BIENVENIDO A LA APLICACIÓN \n"
                                  "Cálculo de Cantidad de Ladrillos", font=("Arial", 16,"bold"),fg="#003366")
    label_presentacion.pack(pady=20)
    # Cargar y mostrar la imagen como logo
    try:
        logo_image = Image.open("E:\CalCantLadri\MuroTecho.png")  # Ubicación de la imágen
        logo_image = logo_image.resize((250, 250), Image.LANCZOS)  # Redimensiona la imagen
        logo = ImageTk.PhotoImage(logo_image)
        label_logo = tk.Label(tab_presentacion, image=logo)
        label_logo.image = logo
        label_logo.pack(pady=10)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

   
    label_presentacion = tk.Label(tab_presentacion, text="CalCantLadri ", font=("Georgia", 28,"bold"),fg="#e69656")
    label_presentacion.pack(pady=20)


    # Pestaña  muro
    tab_muro = ttk.Frame(tab_control)
    tab_control.add(tab_muro, text="   Muro   ")

    # Datos de entrada para el muro
    label_titulo_muro = tk.Label(tab_muro, text="CANTIDAD DE LADRILLOS PARA UN MURO POR m²", font=("Arial", 16, "bold"), fg="#003366", anchor='center')
    label_titulo_muro.grid(row=0, columnspan=2, pady=10)
    tab_muro.grid_columnconfigure(0, weight=1)
    tab_muro.grid_columnconfigure(1, weight=1)

    label_longitud_muro = tk.Label(tab_muro, text="Longitud del muro (m) :")
    label_longitud_muro.grid(row=1,column=0, padx=10, pady=10, sticky='e')
    entry_longitud_muro = tk.Entry(tab_muro)
    entry_longitud_muro.grid(row=1, column=1, padx=10, pady=10,sticky='w')

    label_altura_muro = tk.Label(tab_muro, text="Altura del muro (m) :")
    label_altura_muro.grid(row=2, column=0, padx=10, pady=10, sticky='e')
    entry_altura_muro = tk.Entry(tab_muro)
    entry_altura_muro.grid(row=2, column=1, padx=10, pady=10,sticky='w')

    label_longitud_ladrillo_muro= tk.Label(tab_muro, text="Longitud del ladrillo (m) :")
    label_longitud_ladrillo_muro.grid(row=3, column=0, padx=10, pady=10, sticky='e')
    entry_longitud_ladrillo_muro = tk.Entry(tab_muro)
    entry_longitud_ladrillo_muro.grid(row=3, column=1, padx=10,  pady=10, sticky='w')
    
    label_altura_ladrillo_muro =  tk.Label(tab_muro, text="Altura del ladrillo (m) :")
    label_altura_ladrillo_muro.grid(row=4, column=0, padx=10, pady=10,sticky='e')
    entry_altura_ladrillo_muro = tk.Entry(tab_muro)
    entry_altura_ladrillo_muro.grid(row=4, column=1, padx=10, pady=10, sticky='w')
    
    label_espesor_ladrillo_muro=tk.Label(tab_muro, text="Espesor del ladrillo (m) :")
    label_espesor_ladrillo_muro.grid(row=5, column=0, padx=10, pady=10, sticky='e')
    entry_espesor_ladrillo_muro = tk.Entry(tab_muro)
    entry_espesor_ladrillo_muro.grid(row=5, column=1, padx=10, pady=10, sticky='w')

    label_resultado_muro = tk.Label(tab_muro, text="", font=("Arial", 14))
    label_resultado_muro.grid(row=8, columnspan=2, pady=10)
        
    boton_calcular_muro = tk.Button(tab_muro, text="    Calcular    ", command=lambda:calcular_LadrillosMuro(entry_longitud_muro, entry_altura_muro, entry_longitud_ladrillo_muro, entry_altura_ladrillo_muro, entry_espesor_ladrillo_muro,  label_resultado_muro))
    boton_calcular_muro.grid(row=7, columnspan=8, pady=20)


    # Pestaña techo
    tab_techo = ttk.Frame(tab_control)
    tab_control.add(tab_techo, text="   Techo   ")

    # Datos de entradas para el techo
    label_titulo_techo = tk.Label(tab_techo, text="CANTIDAD DE LADRILLOS PARA UN TECHO POR m²", font=("Arial", 14,"bold"),fg="#003366", anchor='center')
    label_titulo_techo.grid(row=0, columnspan=2, pady=10, sticky='nsew')
    tab_techo.grid_columnconfigure(0, weight=1)
    tab_techo.grid_columnconfigure(1, weight=1)

    label_ancho_techo=tk.Label(tab_techo, text="Ancho del techo (m):")
    label_ancho_techo.grid(row=1, column=0, padx=10, pady=10, sticky='e')
    entry_ancho_techo = tk.Entry(tab_techo)
    entry_ancho_techo.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    label_longitud_techo=tk.Label(tab_techo, text="Longitud del techo (m):")
    label_longitud_techo.grid(row=2, column=0, padx=10, pady=10, sticky='e')
    entry_longitud_techo = tk.Entry(tab_techo)
    entry_longitud_techo.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    label_ancho_ladrillo_techo = tk.Label(tab_techo, text="Ancho del ladrillo (m):")
    label_ancho_ladrillo_techo.grid(row=3, column=0, padx=10, pady=10, sticky='e')
    entry_ancho_ladrillo_techo = tk.Entry(tab_techo)
    entry_ancho_ladrillo_techo.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    tk.Label(tab_techo, text="Longitud del ladrillo (m):").grid(row=4, column=0, padx=10, pady=10, sticky='e')
    entry_longitud_ladrillo_techo = tk.Entry(tab_techo)
    entry_longitud_ladrillo_techo.grid(row=4, column=1, padx=10, pady=10, sticky='w')

    label_ancho_vigueta_techo = tk.Label(tab_techo, text="Ancho de vigueta (m):")
    label_ancho_vigueta_techo .grid(row=5, column=0, padx=10, pady=10, sticky='e')
    entry_ancho_vigueta_techo = tk.Entry(tab_techo)
    entry_ancho_vigueta_techo.grid(row=5, column=1, padx=10, pady=10, sticky='w')


    boton_calcular_techo = tk.Button(tab_techo, text="    Calcular    ", command=lambda: calcular_LadrillosTecho(entry_ancho_techo, entry_longitud_techo, entry_ancho_ladrillo_techo, entry_longitud_ladrillo_techo, entry_ancho_vigueta_techo, label_resultadoTecho))
    boton_calcular_techo.grid(row=6, columnspan=2, pady=20)

    label_resultadoTecho = tk.Label(tab_techo, text="", font=("Arial", 14))
    label_resultadoTecho.grid(row=7, columnspan=2, pady=10)


    # Pestaña ayuda
    tab_ayuda = ttk.Frame(tab_control)
    tab_control.add(tab_ayuda, text="   Ayuda   ")

    # Cargar y mostrar la imagen como logo
    try:
        logo_image = Image.open("E:\CalCantLadri\King-kong.png")  # Ubicación de la imagen
        logo_image = logo_image.resize((250, 250), Image.LANCZOS)  # Redimensiiona la imágen
        logo = ImageTk.PhotoImage(logo_image)
        label_logo = tk.Label(tab_ayuda, image=logo)
        label_logo.pack(pady=10)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

    # Texto en la pestaña ayuda
    ayudaTexto = """Instrucciones:
    1. La pestaña 'Muro'  calcula la cantidad de ladrillos para un muro.
    2. La pestaña 'Techo' calcula la cantidad de ladrillos para un techo.
    3. Debe ingresar las dimensiones del muro o techo y las dimensiones del ladrillo correspondiente.
    4. Al presionar el botón 'Calcular  ' tendrá los resultados necesarios.
    """
    tk.Label(tab_ayuda, text=ayudaTexto, justify=tk.LEFT).pack(padx=10, pady=10)

    # Pestaña  Acerca de 
    tab_Acerca_de = ttk.Frame(tab_control)
    tab_control.add(tab_Acerca_de, text="   Acerca de    ")
    label_Acerca_de = tk.Label(tab_Acerca_de, text=" \n\nCalCantLadri \n", font=("Arial", 16,"bold"),fg="#003366")
    label_Acerca_de.pack(pady=(10,0))

    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Cálculo de Cantidad de Ladrillos", font=("Arial", 14),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))

    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Versión: 1.0", font=("Arial", 14),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))
    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Cálcula la cantidad de ladrillos para muro y techo por m²", font=("Arial", 11),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))
    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Desarrollador : Leonel Coyla Idme", font=("Arial", 11),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))
    label_Acerca_de = tk.Label(tab_Acerca_de, text= " Elmer Coyla Idme", font=("Arial", 11),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))
    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Lanzamiento : 31 Octubre 2024", font=("Arial", 11),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))
    label_Acerca_de = tk.Label(tab_Acerca_de, text= "Contacto: lcoyla@unap.edu.pe", font=("Arial", 11),fg="#003366")
    label_Acerca_de.pack(pady=(1,10))

    # Empaqueta control de pestañas
    tab_control.pack(expand=1, fill='both')

    # Inicio del bucle principal de la interfaz
    ventana.mainloop()

def main():
    crear_interfaz()

if __name__ == "__main__":
    main()
