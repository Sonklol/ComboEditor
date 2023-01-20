#!/usr/bin/python3
#from tkinter import Tk,filedialog # Solo Windows

# Solo Windows
#def get_file(title:str,type:str):
#    """
#    Gets a filepath
#    Returns False if nothing was given
#    get_file(title="Combo File",type="Combo File")
#    """
#    root = Tk()
#    root.withdraw()
#    root.lift()
#    #root.iconbitmap(default=ICON_PATH)
#    response = filedialog.askopenfilename(title=title,filetypes=((type, '.txt'),('All Files', '.*'),))
#    root.destroy()
#    return response if response not in ("",()) else False

def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto=True
        except ValueError:
            print('ERROR - Introduce un numero entero')
     
    return num

def delimiter():
    correcto=False

    delim = input("Introduce un delimitador (|): ")

    #file_path = get_file("Combo File",type="Combo File") # Solo Windows
    file_path = "input.txt"
    file = open(file_path, "r")

    outfile = open('output.txt', "w")

    for i in file:
        try:
            x = i.split(" "  + delim)
            outfile.write(x[-2] + '\n')
        except IndexError:
            outfile.write(i + '\n')

def lineas_duplicadas():
    lines_seen = set()  # holds lines already seen

    outfile = open('output.txt', "w")

    #file_path = get_file("Combo File",type="Combo File") # Solo Windows
    file_path = "input.txt"
    infile = open(file_path, "r")

    lines_duplicadas = 0

    for line in infile:
        #print(line)
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
        else:
            lines_duplicadas += 1

    print(f'Se han borrado {lines_duplicadas} líneas duplicadas')

    outfile.close()

    #for line in open('output.txt', "r"):
        #print(line)

while True:
    print('-- ComboEditor --')
    print('1. Delimitador de lineas')
    print('2. Eliminar lineas duplicadas')
    print('3. Salir')

    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        delimiter()
        break
    elif opcion == 2:
        lineas_duplicadas()
        break
    elif opcion == 3:
        quit()
    else:
        print ("ERROR - Debes introducir un numero entre 1 y 3.")