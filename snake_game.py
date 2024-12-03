#Importanción de TKinter con un enfoque pedagogico
import tkinter as tki
from tkinter import *
from tkinter import font 
#Funcionamiento multi-hilo mejora la realización de cálculos y permite actualizar con mayor eficiencia la GUI  
import threading
import random
#Abrir, manipular y guardar archivos de imagens (pip install pillow)
from PIL import *
import time

#Función para desactivar el cierre de la ventana que se muestre en el momento
def desactivar_cierre_de_ventana():
    pass

#Funcion para cerrar una ventana y redireccionar al menú principal
def close_window(window):
    # Cerrar la ventana secundaria
    window.destroy()
    # Mostrar nuevamente la ventana principal
    main_menu_window.deiconify()

#Entrada y eliminacion de letras en un botón
def asig_name_single_player_menu(evento):
    if entry.get()=="Player Name":
        entry.delete(0, "end")
        entry.config(fg="#000000")
def rest_name_single_player_menu(evento):
    if entry.get() == "Player Name":
        entry.delete(0, "end")
        entry.config(fg="#000000")
#Guardar el nombre solicitado en una variable
def guardar_nombre(evento=None):
    global player_name
    player_name=entry.get()
player_name = ""

#Entrada y eliminacion de letras en un botón
def asig_name_player_1(evento):
     if entry_1.get()=="Player 1 Name":
          entry_1.delete(0, "end")
          entry_1.config(fg="#000000")
def rest_name_player_1(evento):
    if entry_1.get() == "Player 1 Name":
        entry_1.delete(0, "end")
        entry_1.config(fg="#000000")
#Guardar el nombre solicitado en una variable
def guardar_nombre_player_1(evento=None):
     global player_1_name
     player_1_name=entry_1.get()
player_1_name=""

#Entrada y eliminacion de letras en un botón
def asig_name_player_2(evento):
     if entry_2.get()=="Player 2 Name":
          entry_2.delete(0, "end")
          entry_2.config(fg="#000000")
def rest_name_player_2(evento):
    if entry_2.get() == "Player 2 Name":
        entry_2.delete(0, "end")
        entry_2.config(fg="#000000")
#Guardar el nombre solicitado en una variable
def guardar_nombre_player_2(evento=None):
     global player_2_name
     player_2_name=entry_2.get()
player_2_name=""

#Instancia única de Tkinter para toda la aplicación
main_menu_window=tki.Tk()
#Desactivar la modificación manual de las dimenciones de la ventana
main_menu_window.resizable(False, False)
#protocol es un widget de las ventanas de TKinter que define como actuará la ventana ante ciertos eventos, "WM_DELETE_WINDOW"  se activa cuando se intenta cerrar la ventana utilizando el botón de cierre de la ventana y la funcion desactivar_cierre_de_ventana se activa
main_menu_window.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
#ImageTK (Modulo de integración entre PILLOW y TK) Photoimage (Clase de ImageTK que convierte la imagen PILLOW a un formato reconozible para TK) r (indica que el direccionamiento es crudo y debe tomarse literal)
main_menu_imagen=tki.PhotoImage(file="snake_game_main_menu.png")
#Label es un widget que puede mostrar una imagen, "image" establece lo que se mostrará
label=Label(image=main_menu_imagen).pack()
main_menu_window.title("Snake Game")
main_menu_window.geometry("1156x650")

#Función para la apertura de la ventana de un jugador
def open_single_player_window():
    #Se estrablece a la variable "entry" como global para que pueda ser utilizada fuera de su bloque de codigo establecido
    global entry
    #Cerrar la ventana principal
    main_menu_window.withdraw() # U ocultar la ventana principal

    # Generar la ventana para un jugador
    single_player_window = tki.Toplevel(main_menu_window)
    single_player_window.resizable(False, False)
    single_player_window.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
    single_player_window.single_player_image=tki.PhotoImage(file="alfa_snake_menu_single_player.png")
    label=Label(single_player_window, image=single_player_window.single_player_image).pack()
    #pack() establece al contenido de la variable de forma centrada
    single_player_window.title("Single Player")
    single_player_window.geometry("1156x650")
    
    #Contenido de la ventana de un jugador
    #lambda es utilizada como una funcion anónima que actua solo si un boton es precionado, haciendo que el comportamiento del boton y el desencadenante de este sea más controlable
    tki.Button(single_player_window, text="Main Menu", command=lambda: close_window(single_player_window), bg="#018042", fg="#000000", font=font.Font(size=15)).place(x=59, y=570)
    # Botón interactuable "Nombre del jugador"
    entry=tki.Entry(single_player_window,bg="#612c7d", fg="#000000")
    entry.insert(0, "Player Name")
    entry.bind("<FocusIn>", asig_name_single_player_menu)
    entry.bind("<FocusOut>", rest_name_single_player_menu)
    entry.bind("<Leave>", guardar_nombre)
    entry.config(font=font.Font(size=30))
    entry.place(x=370, y=480)

    #Funcion para el juego de un jugador
    def single_player_snake_game():
        #score es global para poder usarlo a lo largo del bloque de codigo y fuera del mismo
        global score
        score=0
        single_player_window.withdraw()
        #Variables del juego
        space_ancho, space_alto=40, 25 #ancho y alto del tablero (celdas)
        celda=20 #(20x20 pixeles de celda)
        #Snake
        body=[(space_ancho//2, space_alto//2)]
        #Ruta de inicio 
        #direccion es global para poder usarla fuera de este bloque
        global direccion
        #direccion espera contenido
        direccion=""
        #Spawn e la comida de la serpiente
        food_x=random.randint(0, space_ancho-1)
        food_y=random.randint(0, space_alto-1)
        #Ventana
        single_player_snake_game=tki.Toplevel(single_player_window)
        single_player_snake_game.resizable(False, False)
        single_player_snake_game.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
        canvas=tki.Canvas(single_player_snake_game, width=space_ancho*celda, height=space_alto*celda)
        canvas.pack()

        def dibujar_cuadricula():
            for i in range(space_ancho + 1):
                x=i*celda
                canvas.create_line(x, 0, x, space_alto * celda, fill="white")
            for i in range(space_alto + 1):
                y=i*celda
                canvas.create_line(0, y, space_ancho * celda, y, fill="white")

        #Movement settings
        def move_snake(event):
            global direccion
            #key (variable de guarde) event(evento vinculado a key) keysym(detecta una interacción con el teclado y la traduce)
            key=event.keysym
            if key=="w" and direccion != "ABAJO":
                    direccion="ARRIBA"
            elif key=="s" and direccion != "ARRIBA":
                    direccion="ABAJO"
            elif key=="a" and direccion != "DERECHA":
                    direccion="IZQUIERDA"
            elif key=="d" and direccion != "IZQUIERDA":
                    direccion="DERECHA"

        #Vincular eventos de movimiento
        single_player_snake_game.bind("<Key>", move_snake)

        #Bucle para movimiento, crecimiento, perdida, etc
        while True:
            #Snake movement in plane
            head_x, head_y=body[0]
            if direccion=="ARRIBA":
                head_y-=1
            elif direccion=="ABAJO":
                head_y+=1
            elif direccion=="DERECHA":
                head_x+=1
            elif direccion=="IZQUIERDA":
                head_x-=1
            new_head=(head_x, head_y)
            if (head_x, head_y)==(food_x, food_y):
                food_x, food_y=random.randint(0, space_ancho-1), random.randint(0, space_alto-1)
                score+=1
            else:
                body.pop()#simula el movimiento de la serpiente
            if head_x<0 or head_x>=space_ancho or head_y<0 or head_y>=space_alto or new_head in body:
                single_player_snake_game.destroy()
                over()
                break
            body.insert(0, new_head)

               #Tablero
            canvas.delete("all")#borra los elementos para poder actualizarlos
            dibujar_cuadricula()
            for segmento in body:
                   #este bucle recorre cada segmento del cuerpo de la serpiente, calcula las coordenadas de los vértices del rectángulo que representa el segmento en el lienzo y lo dibuja en consecuencia
                   #coordenadas de la cuadrícula a coordenadas de píxeles en el lienzo
                   x1, y1=segmento[0]*celda, segmento[1]*celda
                   x2, y2=x1+celda, y1+celda
                   canvas.create_rectangle(x1, y1, x2, y2, fill="green")
            canvas.create_rectangle(food_x*celda  , food_y*celda, (food_x+1)*celda, (food_y+1)*celda, fill="red")
            canvas.configure(bg="#000000")
            #actualiza la ventanawdfdddwwddddsddddwsadwdadwddwwaaadddddddwdwdaawswawaeefwawdawawwwwdawaswwwdwwwdwa
            single_player_snake_game.update()
            #Receptor de enventos de teclado
            canvas.focus_set()
            time.sleep(1/12)
    
    # Botón para jugar
    tki.Button(single_player_window, text="        Start Game        ", command=single_player_snake_game, bg="#612c7d", fg="#000000", font=font.Font(size=22)).place(x=435, y=557)
    
    def over():
        gamer_over=tki.Toplevel()
        gamer_over.resizable(False, False)
        gamer_over.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
        gamer_over.gamer_over_image=tki.PhotoImage(file="game_over_single_player.png")
        label=Label(gamer_over, image=gamer_over.gamer_over_image).pack()
        gamer_over.title("GAME OVER")
        label=tki.Label(gamer_over, text=f"{player_name} your score was: {score}", bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=50, y=140)
        gamer_over.geometry("400x320")
        tki.Button(gamer_over, text="Main Menu", command=lambda:close_window(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=130, y=260)
        tki.Button(gamer_over, text="Try Again", command=lambda: try_again(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=138, y=200)

    def try_again(window):
        window.destroy()
        single_player_snake_game()
        score=0
            
def open_two_players_window():
    global entry_1, entry_2
    # Cerrar la ventana principal
    main_menu_window.withdraw()  # Ocultar la ventana principal

    # Generar la ventana para dos jugadores
    two_players_window = tki.Toplevel(main_menu_window)
    two_players_window.resizable(False, False)
    two_players_window.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
    two_players_window.two_players_image=tki.PhotoImage(file="snake_menu_two_players.png")
    label=Label(two_players_window, image=two_players_window.two_players_image).pack()
    two_players_window.title("Two Players")
    two_players_window.geometry("1156x650")

    # Contenido de la ventana de dos jugadores
    tki.Button(two_players_window, text="Main Menu", command=lambda: close_window(two_players_window), bg="#018042", fg="#000000", font=font.Font(size=15)).place(x=59, y=560)

    entry_1=tki.Entry(two_players_window,bg="#612c7d", fg="#000000")
    entry_1.insert(0, "Player 1 Name")
    entry_1.bind("<FocusIn>", asig_name_player_1)
    entry_1.bind("<FocusOut>", rest_name_player_1) 
    entry_1.bind("<Leave>", guardar_nombre_player_1)
    entry_1.config(font=font.Font(size=30))
    entry_1.place(x=40, y=430)

    entry_2=tki.Entry(two_players_window,bg="#612c7d", fg="#000000")
    entry_2.insert(0, "Player 2 Name")
    entry_2.bind("<FocusIn>", asig_name_player_2)
    entry_2.bind("<FocusOut>", rest_name_player_2)
    entry_2.bind("<Leave>", guardar_nombre_player_2)
    entry_2.config(font=font.Font(size=30))
    entry_2.place(x=670, y=430)
    


    def two_players_snake_game():
        global direccion_player_1, direccion_player_2, score_player_1, score_player_2 #AQUI
        two_players_window.withdraw()
        space_ancho, space_alto = 40, 25
        celda = 20
        body_player_1 = [(space_ancho // 2-15, space_alto // 2)]
        body_player_2 = [(space_ancho // 2+15, space_alto // 2)]
        direccion_player_1 = ""
        direccion_player_2 = ""
        food_x = random.randint(0, space_ancho - 1)
        food_y = random.randint(0, space_alto - 1)
        game_window = tki.Toplevel(two_players_window)#AQUI
        game_window.resizable(False, False)
        game_window.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
        canvas = tki.Canvas(game_window, width=space_ancho * celda, height=space_alto * celda)
        canvas.pack()

        def dibujar_cuadricula():
            for i in range(space_ancho + 1):
                x=i*celda
                canvas.create_line(x, 0, x, space_alto * celda, fill="white")
            for i in range(space_alto + 1):
                y=i*celda
                canvas.create_line(0, y, space_ancho * celda, y, fill="white")

        def move_snake(event):
            global direccion_player_1, direccion_player_2
            key = event.keysym
            if key == "w" and direccion_player_1 != "ABAJO_1":
                direccion_player_1 = "ARRIBA_1"
            elif key == "s" and direccion_player_1 != "ARRIBA_1":
                direccion_player_1 = "ABAJO_1"
            elif key == "a" and direccion_player_1 != "DERECHA_1":
                direccion_player_1 = "IZQUIERDA_1"
            elif key == "d" and direccion_player_1 != "IZQUIERDA_1":
                direccion_player_1 = "DERECHA_1"
            elif key == "i" and direccion_player_2 != "ABAJO_2":
                direccion_player_2 = "ARRIBA_2"
            elif key == "k" and direccion_player_2 != "ARRIBA_2":
                direccion_player_2 = "ABAJO_2"
            elif key == "j" and direccion_player_2 != "DERECHA_2":
                direccion_player_2 = "IZQUIERDA_2"
            elif key == "l" and direccion_player_2 != "IZQUIERDA_2":
                direccion_player_2 = "DERECHA_2"

        game_window.bind("<Key>", move_snake)

        #Bucle para que sea posible la interacción
        def game_loop():
            nonlocal  food_x, food_y
            head_1x, head_1y = body_player_1[0]
            if direccion_player_1 == "ARRIBA_1":
                head_1y -= 1
            elif direccion_player_1 == "ABAJO_1":
                head_1y += 1
            elif direccion_player_1 == "IZQUIERDA_1":
                head_1x -= 1
            elif direccion_player_1 == "DERECHA_1":
                head_1x += 1
            new_head_player_1 = (head_1x, head_1y)
            if (head_1x, head_1y) == (food_x, food_y):
                food_x, food_y = random.randint(0, space_ancho - 1), random.randint(0, space_alto - 1)
            else:
                body_player_1.pop()
            if head_1x < 0 or head_1x >= space_ancho or head_1y < 0 or head_1y >= space_alto or new_head_player_1 in body_player_1 or new_head_player_1 in body_player_2:
                game_window.destroy()
                game_over_for_1()
                return
            body_player_1.insert(0, new_head_player_1)

            head_2x, head_2y = body_player_2[0]
            if direccion_player_2 == "ARRIBA_2":
                head_2y -= 1
            elif direccion_player_2 == "ABAJO_2":
                head_2y += 1
            elif direccion_player_2 == "IZQUIERDA_2":
                head_2x -= 1
            elif direccion_player_2 == "DERECHA_2":
                head_2x += 1
            new_head_player_2 = (head_2x, head_2y)
            if (head_2x, head_2y) == (food_x, food_y):
                food_x, food_y = random.randint(0, space_ancho - 1), random.randint(0, space_alto - 1)
            else:
                body_player_2.pop()
            if head_2x < 0 or head_2x >= space_ancho or head_2y < 0 or head_2y >= space_alto or new_head_player_2 in body_player_2 or new_head_player_2 in body_player_1:
                game_window.destroy()
                game_over_for_2()
                return
            body_player_2.insert(0, new_head_player_2)

            canvas.delete("all")
            dibujar_cuadricula()
            for segmento in body_player_1:
                x1_1, y1_1 = segmento[0] * celda, segmento[1] * celda
                x2_1, y2_1 = x1_1 + celda, y1_1 + celda
                canvas.create_rectangle(x1_1, y1_1, x2_1, y2_1, fill="green")
            for segmento in body_player_2:
                x1_2, y1_2 = segmento[0] * celda, segmento[1] * celda
                x2_2, y2_2 = x1_2 + celda, y1_2 + celda
                canvas.create_rectangle(x1_2, y1_2, x2_2, y2_2, fill="pink")
            canvas.create_rectangle(food_x * celda, food_y * celda, (food_x + 1) * celda, (food_y + 1) * celda, fill="red")
            canvas.configure(bg="#000000")
            game_window.update()
            canvas.focus_set()
            game_window.after(100, game_loop)

        game_loop()
    tki.Button(two_players_window, text="        Start Game        ", command=two_players_snake_game, bg="#612c7d", fg="#000000", font=font.Font(size=22)).place(x=445, y=557)

    def game_over_for_2():
        global score_player_1, score_player_2
        gamer_over=tki.Toplevel()
        gamer_over.resizable(False, False)
        gamer_over.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
        gamer_over.gamer_over_image=tki.PhotoImage(file="game_over_single_player.png")
        label=Label(gamer_over, image=gamer_over.gamer_over_image).pack()
        gamer_over.title("GAME OVER")
        label=tki.Label(gamer_over, text=f"¡{player_1_name} win!w", bg="#612c7d", fg="#000000", font=font.Font(size=15)).place(x=50, y=140)
        gamer_over.geometry("400x320")
        tki.Button(gamer_over, text="Main Menu", command=lambda:close_window(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=130, y=260)
        tki.Button(gamer_over, text="Try Again", command=lambda: try_again_two_players(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=138, y=200)
    def game_over_for_1():
        global score_player_1, score_player_2
        gamer_over=tki.Toplevel()
        gamer_over.resizable(False, False)
        gamer_over.protocol("WM_DELETE_WINDOW", desactivar_cierre_de_ventana)
        gamer_over.gamer_over_image=tki.PhotoImage(file="game_over_single_player.png")
        label=Label(gamer_over, image=gamer_over.gamer_over_image).pack()
        gamer_over.title("GAME OVER")
        label=tki.Label(gamer_over, text=f"¡{player_2_name} win!", bg="#612c7d", fg="#000000", font=font.Font(size=15)).place(x=50, y=140)
        gamer_over.geometry("400x320")
        tki.Button(gamer_over, text="Main Menu", command=lambda:close_window(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=130, y=260)
        tki.Button(gamer_over, text="Try Again", command=lambda: try_again_two_players(gamer_over), bg="#612c7d", fg="#000000", font=font.Font(size=18)).place(x=138, y=200)
    def try_again_two_players(window):
        window.destroy()
        two_players_snake_game()
        score=0


# Contenido de la ventana principal
tki.Button(main_menu_window, text="               Single Player               ", command=open_single_player_window, bg="#612c7d", fg="#000000", font=font.Font(size=25)).place(x=370, y=460)
tki.Button(main_menu_window, text="             Player vs Player             ", command=open_two_players_window, bg="#612c7d", fg="#000000", font=font.Font(size=25)).place(x=367, y=550)
tki.Button(main_menu_window, text="   Exit   ", command=main_menu_window.quit, bg="#018042", fg="#000000", font=font.Font(size=15)).place(x=59, y=570)

# Iniciar el bucle principal de la aplicación
main_menu_window.mainloop()


#Proceso para hacer una ejecutable (.exe) 
#1. Almacenar todas las imagenes, iconos y código en una carpeta 
#2. En el explorador del archivos (ubicarse en la carpeta creada) abrir un cmd en dicha dirección (a traves de comandos o del propio explorador) 
#3. Instalar pyinstaller mediante el siguiente comando "pip install pyinstaller" 
#4. Utilizar el siguiente comando para realizar un ejecutable integrando todo el contenido de la carpeta (pyinstaller --onefile --add-data "snake_game_main_menu.png;." --add-data "alfa_snake_menu_single_player.png;." --add-data "snake_menu_two_players.png;." --add-data "game_over_single_player.png;." snake_game.py) 
#5. Se abrán creado dos nuevas carpetas en el directorio actual, uno de ellos contiene el archivo ejecutable, se debe copiar las imagenes y ponerlas dentro de la carpeta que lo contiene, a partir de ese momento el .exe es válido 
#6. Comprimir la carpeta para poder compartir
