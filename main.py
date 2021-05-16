import random

def read_fie(path):
    with open(path, "r") as f:
        lines = f.readlines()
        f.close()
        return lines

def randomizer(lst):
    random.shuffle(lst)

def div_numbers(lst, num):
    return len(lst) // num  

def rem_numbers(lst, num):
    return len(lst) % num  

def distribution(lst1, lst2):
    print(lst)


if __name__ == '__main__':
    while True:
        #poner try por si ponene un coso que no va y tambien si no ponene y poner un try si no exsite documento 
        group_number = int(input("Cantidad de grupos: ")) #Pedir cantidad de grupos
        std_path = input("Inserte archivos de estudiantes: ") #Pedir path de archivo de estudiantes
        std_list = read_fie(std_path) #Lista estudiantes 
        std_nums = len(std_list) #Numeros de estudiantes 
        themes_path = input("Inserte archivos de estudiantes: ") #Pedir path de archivo de temas   
        themes_list = read_fie(themes_path) #Lista temas
        themes_nums = len(themes_list) #Numeros de estudiantes 

        if group_number <= std_nums and themes_nums >= group_number : #Si entradas no cuimplen con requerimientos 
            break
        else: 
            print("Parametro no valido")
            des = input("Desea seguir si/no: ") #Preguntar si desea salir del programa 
            if(des == 'no'):
                exit()

    #C:\Users\Emily\Desktop\Prueba\pub.txt
    #Poner en aleatoriedad las listas de estudiantes y temas 
    randomizer(std_list)
    randomizer(themes_list)

'''
buscar division de grupos 
- conseguir en cuanto se puede dividir la lista y en remanente
- 
'''
    







   


