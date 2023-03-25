#ler o ficheiro
def read_input(filename):
    sequence = []
    try:
        file = open(filename, encoding="utf-8")
        file.readline()
        line = file.readline().replace("\n", "").split(" ")
        for i in range(len(line)):
            sequence.append(int(line[i]))
    except IOError:
        print("Erro a ler o ficheiro. Confirme nome e caminho para o ficheiro.")
        return None
    finally:
        if file != None:
            file.close()
    return sequence

#escrever o ficheiro de output
def write_output(filename, max_sum, subsequence):
    file = open(filename, "w")
    file.write(str(max_sum) + "\n")
    for n in subsequence:
        file.write(str(n) + " ")
    file.close()

#calcula a sub-sequencia cuja soma dos elementos e a maior
#devolve a soma e sequencia
def max_subsequence_sum(seq):
    max_sum = seq[0]
    current_max_sum = seq[0]
    start = 0
    end = 0
    current_start = 0

    for i in range(1, len(seq)):
        if seq[i] > current_max_sum + seq[i]:
            current_start = i

        current_max_sum = max(seq[i], current_max_sum + seq[i])

        if current_max_sum > max_sum:
            max_sum = current_max_sum
            start = current_start
            end = i

    return max_sum, seq[start:end+1]

#função principal / orquestração 
def main():
    sequence = read_input("2023-03-25/input_ex3.txt")
    max_sum, subsequence = max_subsequence_sum(sequence)
    print(max_sum)
    print(subsequence)
    write_output("2023-03-25/output_ex3.txt", max_sum, subsequence)

if __name__ == "__main__":
    main()