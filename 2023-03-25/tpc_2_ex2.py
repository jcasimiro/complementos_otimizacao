import math

#ler o ficheiro
def read_input(filename):
    data = []
    try:
        file = open(filename, encoding="utf-8")
        records_len = int(file.readline())
        for i in range(records_len):
            data.append(file.readline().replace("\n", "").split(" "))
    except Exception:
        return None
    finally:
        if file != None:
            file.close()
    return data

#escrever o ficheiro de output
def write_output(filename, areas):
    file = open(filename, "w")
    for i in range(len(areas)):
        file.write(str(areas[i]) + "\n")
    file.close()

#calcular a distancia de um quadrado para um circulo
def calculate_distance_square_2_circle(x_square, y_square, l_square, x_circle, y_circle):
    d_begin = math.sqrt((x_square-x_circle)**2+(y_square-y_circle)**2)
    d_end = math.sqrt((x_square+l_square-x_circle)**2+(y_square+l_square-y_circle)**2)
    return d_begin, d_end

#determinar se um quadrado esta dentro de um circulo
def is_square_inside_circle(x_square, y_square, l_square, x_circle, y_circle, r_circle):
    distance = calculate_distance_square_2_circle(x_square, y_square, l_square, x_circle, y_circle)
    return distance[0] <= r_circle and distance[1] <= r_circle

#determinar se um circulo esta dentro de um quadrado
def is_full_circle_inside_square(x_square, y_square, l_square, x_circle, y_circle, r_circle):
    square_top_right = (x_square + l_square, y_square + l_square)
    distances = [
        abs(x_circle - x_square), #distancia para o lado esquerdo
        abs(x_circle - square_top_right[0]),  #distancia para o lado direito
        abs(y_circle - y_square),  #distancia para baixo
        abs(y_circle - square_top_right[1]),  #distancia para cima
    ]
    #se o centro do circulo esta dentro do quadrado
    inside = x_circle >= x_square and x_circle <= x_square+l_square and y_circle >= y_square and y_circle <= y_square+l_square
    #verificar se todas as distancias sao superiores ou iguais ao raio
    for i in range(len(distances)):
        inside = inside and distances[i] >= r_circle   
    return inside

#verifica se o quadrado e circulo nao se intersetam
def square_and_circle_not_intersect(x_square, y_square, l_square, x_circle, y_circle, r_circle):
    #calcular a distancia entre o centro do quadrado e o centro do circulo
    distance_x = abs(((x_square+l_square)/2)-x_circle)
    distance_y = abs(((y_square+l_square)/2)-x_circle)
    distance = math.sqrt(distance_x**2 + distance_y**2)
    #calcular metade da diagonal do quadrado
    half_diagonal = l_square * math.sqrt(2) / 2
    # verificar se as formas se intersetam
    if distance > half_diagonal + r_circle:
        return True
    else:
        return False
    
#calcular a area aproximada de interseção
def calculate_approximate_intersection_area(x_square, y_square, l_square, x_circle, y_circle, r_circle):
    l = 0.01
    area = 0

    #se quadrado e circulo nao se intersetam devolve area 0
    if square_and_circle_not_intersect(x_square, y_square, l_square, x_circle, y_circle, r_circle):
        return 0
    
    #se quadrado esta totalmente contido no circulo, devolve a area do quadrado
    if is_square_inside_circle(x_square, y_square, l_square, x_circle, y_circle, r_circle):
        return l_square**2
    
    #se o circulo esta totalmente dentro do quadrado, devolve a area do circulo
    if is_full_circle_inside_square(x_square, y_square, l_square, x_circle, y_circle, r_circle):
        return math.pi * r_circle**2

    if l_square <= l:
        return 0

    #calcula a area de interseção
    area += calculate_approximate_intersection_area(x_square, y_square, l_square / 2, x_circle, y_circle, r_circle)
    area += calculate_approximate_intersection_area(x_square, y_square + l_square / 2, l_square / 2, x_circle, y_circle, r_circle)
    area += calculate_approximate_intersection_area(x_square + l_square / 2, y_square, l_square / 2, x_circle, y_circle, r_circle)
    area += calculate_approximate_intersection_area(x_square + l_square / 2, y_square + l_square / 2, l_square / 2, x_circle, y_circle, r_circle)
    return area

#calcular a area de interseção entre o quadrado e circulo
def calculate_intersection_area_square_circle(shapes_data):
    #converter informacao do quadrado para float
    x_square = float(shapes_data[0])
    y_square = float(shapes_data[1])
    l_square = float(shapes_data[2])
    #converter informacao do circulo para float
    x_circle = float(shapes_data[3])
    y_circle = float(shapes_data[4])
    r_circle = float(shapes_data[5])
    #calcula a area da intersecao das formas    
    return calculate_approximate_intersection_area(x_square, y_square, l_square, x_circle, y_circle, r_circle)

#função principal/orquestração 
def main():
    input_data = read_input("2023-03-25/input_ex2.txt")
    areas = []
    for i in range(len(input_data)):
        areas.append(calculate_intersection_area_square_circle(input_data[i]))
    print(areas)
    write_output("2023-03-25/output_ex2.txt", areas)

if __name__ == "__main__":
    main()