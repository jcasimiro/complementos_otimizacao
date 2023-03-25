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

#calcular a area aproximada de intersecao
def calculate_approximate_intersection_area(x_square, y_square, l_square, x_circle, y_circle, r_circle):
    x = x_square
    y = y_square
    l = 0.01
    area = 0
    while x < x_square + l_square:
        while y < y_square + l_square:
            dist_begin, dist_end = calculate_distance_square_2_circle(x, y, l, x_circle, y_circle)
            if dist_begin <= r_circle and dist_end <= r_circle:
                    area += l**2
            y += l
        y = y_square
        x += l
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
    if is_square_inside_circle(x_square, y_square, l_square, x_circle, y_circle, r_circle):
        return l_square**2
    if is_full_circle_inside_square(x_square, y_square, l_square, x_circle, y_circle, r_circle):
        return math.pi * r_circle**2
    
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