import random

def read_file(path):
    lines = []
    try:
        with open(path, "r") as f:
            l = f.readlines()
            for line in l: 
                lines.append(line.rstrip("\n"))
            f.close()
            return lines
    except IOError:
        print("No existe parametro")
        exit()

def div_numbers(lst, num):
    return len(lst) // num  

def rem_numbers(lst, num):
    return len(lst) % num  

def distribution(std, theme, n):
    std_div = div_numbers(std, n)
    std_rem = rem_numbers(std, n)
    theme_div = div_numbers(theme, n)
    theme_rem = rem_numbers(theme, n)

    cont = []
    #dividir temas 
    for i in range(n):
        for j in range(theme_div):
            temp = []
            choice = random.choice(theme)
            theme.remove(choice)
            temp.append(choice)
            j +=1  
        cont.append([temp])

    for i in cont:
        print(i)
    print("==============================================================")
    '''
    if theme_rem != 1: 
        l = list(range(0,n))
        random.shuffle(l)
        for i in range(theme_rem):
            choice = random.choice(theme)
            theme.remove(choice)
            num = l.pop()
            cont[num].append(choice)
    '''
    #dividir estudiantes 
    for i in range(n):
        for j in range(std_div):
            temp = []
            choice = random.choice(std)
            std.remove(choice)
            temp.append(choice)
            j +=1  
        cont[i].append([temp])
    
    for i in cont:
        print(i)
    print("==============================================================")


if __name__ == '__main__':
    while True:
        #poner try por si ponene un coso que no va y tambien si no ponene y poner un try si no exsite documento 
        try:
            group_number = int(input("Cantidad de grupos: ")) #Pedir cantidad de grupos
            break
        except ValueError:
            print("Parametro no valido")
            exit()

    while True:
        std_path = input("Inserte archivos de estudiantes: ") #Pedir path de archivo de estudiantes
        std_list = read_file(std_path) #Lista estudiantes 

        themes_path = input("Inserte archivos de estudiantes: ") #Pedir path de archivo de temas   
        themes_list = read_file(themes_path) #Lista temas

        if group_number <= len(std_list) and len(themes_list) >= group_number : #Si entradas no cuimplen con requerimientos 
            break
        else: 
            print("Parametro no valido")
            exit()

    #C:\Users\Emily\Desktop\Prueba\pub.txt
    #C:\Users\Emily\Desktop\Prueba\tht.txt
    
    distribution(std_list, themes_list, group_number)

#Puedo hacer que la distirbucion / funcion random pueda ser una funcion o sea , el loop 








   


