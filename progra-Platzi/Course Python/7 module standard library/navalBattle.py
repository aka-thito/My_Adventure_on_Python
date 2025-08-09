# Practica Clase 36

import tkinter as tk #Libreria tkinter
from tkinter import messagebox #Libreria messagebox
import random #Libreria random
import json #Libreria json

#El proyecto esta organizado en una clase principal "Batalla Naval" que maneja la logica del juego y su interfaz grafica con Tkinter.

#1.Configuracion Inicial - definimos la clase
class BatallaNaval:
    def __init__(self):
        self.window = tk.Tk() #Crear la ventana principal de Tkinter
        self.window.title("Batalla Naval") #Titulo de la ventana
        self.tamano_tablero = 5  #Tamaño Inicial del tablero
        self.num_barcos = 3  #Numero de barcos por defecto
        self.dificultad = "Facil" #Dificultad por defecto
        self.menu_principal() #Muestra el menu principal

     #2. Definiendo el Menu Principal
    def menu_principal(self):
     #Limpiamos la ventana actual
     for widget in self.window.winfo_children():
        widget.destroy()
    
     #Agregamos opciones al menu
     tk.Label(self.window, text="Batalla Naval", font=("Arial", 20)).pack(pady=20)
     tk.Button(self.window, text="Iniciar Juego", font=("Arial", 14), command=self.configurar_juego).pack(pady=10) #Configuramos el boton de start
     tk.Button(self.window, text="Cargar Partida", font=("Arial", 14), command=self.cargar_partida).pack(pady=10) #Configurar el boton de cargar partida
     tk.Button(self.window, text="Salir", font=("Arial", 14), command=self.window.quit).pack(pady=10) #Configuramos el boton de salir

      #3. definiendo la configuracion del Juego
    def configurar_juego(self):
      for widget in self.window.winfo_children():
        widget.destroy()
    
      tk.Label(self.window, text="Configurar Juego", font=("Arial", 18)).pack(pady=10)

     #Definimos el tamaño del tablero
      tk.Label(self.window, text="Tamaño del tablero:", font=("Arial", 14)).pack(pady=5)
      self.tamano_var = tk.IntVar(value=self.tamano_tablero)
      tk.OptionMenu(self.window, self.tamano_var, 5, 7, 10).pack()

     #Seleccionamos la dificultad
      tk.Label(self.window, text="Dificultad:", font=("Arial", 14)).pack(pady=5)
      self.dificultad_var = tk.StringVar(value=self.dificultad)
      tk.OptionMenu(self.window, self.dificultad_var, "Facil", "Dificil").pack()

     #Numero de Barcos
      tk.Label(self.window, text="Numero de barcos:", font=("Arial", 14)).pack(pady=5)
      self.num_barcos_var = tk.IntVar(value=self.num_barcos)
      tk.Spinbox(self.window, from_=1, to=10, textvariable=self.num_barcos_var).pack()

     #boton de iniciar
      tk.Button(self.window, text="Iniciar", font=("Arial", 14), command=self.iniciar_juego).pack(pady=20)

     #4. Iniciamos el juego
    def iniciar_juego(self):
     self.tamano_tablero = self.tamano_var.get()
     self.num_barcos = self.num_barcos_var.get()
     self.dificultad = self.dificultad_var.get()

     self.jugador_tablero = [[" "]*self.tamano_tablero for _ in range(self.tamano_tablero)] #Tablero del usuario
     self.sentinel_tablero = [[" "]*self.tamano_tablero for _ in range(self.tamano_tablero)] #Tablero de la maquina
     #Colocamos los barcos
     self.colocar_barcos(self.sentinel_tablero)
     self.colocar_barcos(self.jugador_tablero)
     self.turno_usuario = True

     self.mostrar_juego()

     #5. Colocar barcos
    def colocar_barcos(self, tablero):
     for _ in range(self.num_barcos):
        while True:
            x, y = random.randint(0, self.tamano_tablero - 1), random.randint(0, self.tamano_tablero - 1)
            if tablero[x][y] == " ":
                tablero[x][y] = "B" # Pone los barcos en posiciones aleatorias con la letra B
                break

     #6. Mostrar el tablero
    def mostrar_juego(self):
     for widget in self.window.winfo_children():
        widget.destroy()
    
     tk.Label(self.window, text="Tu Tablero", font=("Arial", 16)).grid(row=0, column=0, padx=10)
     tk.Label(self.window, text="Tablero de Sentinel", font=("Arial", 16)).grid(row=0, column=1, padx=10)

     for i in range(self.tamano_tablero):
        for j in range(self.tamano_tablero):
            cell = tk.Label(self.window, text=self.jugador_tablero[i][j], font=("Arial", 14), width=2, height=1, borderwidth=1, relief="solid")
            cell.grid(row=i+1, column=j)

     for i in range(self.tamano_tablero):
        for j in range(self.tamano_tablero):
            cell = tk.Button(self.window, text="?", font=("Arial", 14), width=2, height=1, command=lambda x=i, y=j: self.disparar(x, y))
            cell.grid(row=i+1, column=j+6)

      #7. Disparo del Usuario
    def disparar(self, x, y):
     if self.sentinel_tablero[x][y] == "B":
        messagebox.showinfo("Impacto!!", "Le diste a un Barco!!")
        self.sentinel_tablero[x][y] = "X"
     else:
        messagebox.showinfo("Fallaste", "Agua")
        self.sentinel_tablero[x][y] = "O"
    
     self.turno_usuario = False
     self.turno_sentinel()

     #8. Turno de Sentinel
    def turno_sentinel(self):
     if self.dificultad == "Facil":
        #Disparo Aleatorio
        while not self.turno_usuario:
            x, y = random.randint(0, self.tamano_tablero - 1), random.randint(0, self.tamano_tablero - 1)
            if self.jugador_tablero[x][y] == " ":
                if self .jugador_tablero[x][y] == "B":
                    messagebox.showinfo("Sentinel Impacta", f"Sentinel hundio tu barco ({x}, {y})")
                    self.jugador_tablero[x][y] = "X"
                else:
                    self.jugador_tablero[x][y] = "O"
                    self.turno_usuario = True
     elif self.dificultad == "Dificil":
        #Disparo Inteligente
        while not self.turno_usuario:
            #Buscar Disparo Inteligente
            disparos_previos = [(i, j) for i in range(self.tamano_tablero) for j in range(self.tamano_tablero) if self.jugador_tablero[i][j] == "X"]
            objetivo = None
            
            #Si se hizo impactos anteriores buscar adyacentes
            for x, y in disparos_previos:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.tamano_tablero and 0 <= ny < self.tamano_tablero and self.jugador_tablero[nx][ny] == " ":
                        objetivo = (nx, ny)
                        break
                if objetivo:
                    break
            if not objetivo:
                #Si no se hiz impactos antes, disparar aleatoriamente
                x, y = random.randint(0, self.tamano_tablero - 1), random.randint(0, self.tamano_tablero - 1)
                while self.jugador_tablero[x][y] != " ":
                    x, y = random.randint(0, self.tamano_tablero - 1), random.randint(0, self.tamano_tablero - 1)
                objetivo = (x, y)
            x, y = objetivo
            if self.jugador_tablero[x][y] == "B":
                messagebox.showinfo("Sentinel Impacta", f"Sentinel hundio tu barco en ({x}, {y})")
                self.jugador_tablero[x][y] = "O"
                self.turno_usuario = True
     self.mostrar_juego()

     #9. Configuramos para guarda la partida
    def guardar_partida(self):
     partida = {
        "tamaño_tablero": self.tamano_tablero,
        "num_barcos": self.num_barcos,
        "dificultad": self.dificultad,
        "jugador_tablero": self.jugador_tablero,
        "sentinel_tablero": self.sentinel_tablero
     }
     with open("batalla_naval_guardado.json", "w") as file:
        json.dump(partida, file)
     messagebox.showinfo("Guardar Partida", "La partida ha sido guardado con exito")

      #10. Configuramos para cargar la partida
    def cargar_partida(self):
     try:
        with open("batalla_naval_guardado.json", "r") as file:
            partida = json.load(file)
        self.tamano_tablero = partida["tamano_tablero"]
        self.num_barcos = partida["num_barcos"]
        self.dificultad = partida["dificultad"]
        self.jugador_tablero = partida["jugador_tablero"]
        self.sentinel_tablero = partida["sentinel_tablero"]

        self.mostrar_juego()
     except FileNotFoundError:
        messagebox.showerror("Error", "No se encontro ninguna partida guardada.")
    
      #11. ejecutamos 
    def run(self):
     self.window.mainloop()

      #12. Ejecutamos el juego
if __name__ == "__main__":
    juego = BatallaNaval()
    juego.run()


# NADA DE ESTO LO HICE YO, solo lo copie y pegue, no me vi capaz
# de hacer esta cosa, la profe se paso de mk, capaz con ayuda de
# chatgpt lo sacaba, pero para hacerlo con IA, mejor hacia esto XD

# más bien me puse a estudiar este codigo