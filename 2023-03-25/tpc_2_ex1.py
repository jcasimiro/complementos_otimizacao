
#ler o ficheiro
def read_input(filename):
    ordered_pairs = []
    try:
        file = open(filename, encoding="utf-8")
        sequence_len = int(file.readline())
        sequence = file.readline().replace("\n", "").split(" ")
        if len(sequence) != sequence_len:
            raise ValueError()
        ordered_pairs_len = int(file.readline())
        for i in range(ordered_pairs_len):
            ordered_pairs.append(file.readline().replace("\n", "").split(" "))
    except IOError:
        print("Erro a ler o ficheiro. Confirme nome e caminho para o ficheiro.")
        return None
    finally:
        if file != None:
            file.close()
    return sequence, ordered_pairs

#escrever o ficheiro de output
def write_output(filename, results):
    file = open(filename, "w")
    for result in results:
        file.write(str(result) + "\n")
    file.close()

#exercicio 1 | alínea a
def ex1_a(sequence):
    if not sequence:
        return 0
    else:
        return int(sequence[0]) + ex1_a(sequence[1:])

#função principal / orquestração 
def main():
    sequence, ordered_pairs = read_input("2023-03-25/input_ex1.txt")
    
    #exercicio 1 | alínea a
    ex1_a_out = []
    for i in range(len(ordered_pairs)):
        upper_bound = int(max(ordered_pairs[i]))-1
        lower_bound = int(min(ordered_pairs[i]))-1
        subsequence = sequence[lower_bound:upper_bound+1]
        total = ex1_a(subsequence)
        ex1_a_out.append(total)
    write_output("2023-03-25/output_ex1_a.txt", ex1_a_out)

    #exercicio 1 | alínea b
    ex1_b_out = []
    for i in range(len(ordered_pairs)):
        upper_bound = int(max(ordered_pairs[i]))-1
        lower_bound = int(min(ordered_pairs[i]))-1
        subsequence = list(map(int, sequence[lower_bound:upper_bound+1]))
        total = sum(subsequence)
        ex1_b_out.append(total)  
    write_output("2023-03-25/output_ex1_b.txt", ex1_b_out)

if __name__ == "__main__":
    main()