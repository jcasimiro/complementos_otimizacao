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
    if len(seq) == 1:
        return seq[0], [seq[0]]
    else:
        mid = len(seq) // 2
        left_max, left_seq = max_subsequence_sum(seq[:mid])
        right_max, right_seq = max_subsequence_sum(seq[mid:])
        
        #encontrar a soma maxima da subsequencia incluindo o elemento do meio
        max_left = seq[mid-1]
        left_idx = mid - 1
        for i in range(mid-1, -1, -1):
            if seq[i] > max_left:
                max_left = seq[i]
                left_idx = i
        
        max_right = seq[mid]
        right_idx = mid
        for i in range(mid, len(seq)):
            if seq[i] > max_right:
                max_right = seq[i]
                right_idx = i
        
        mid_seq = seq[left_idx:right_idx+1]
        mid_max = sum(mid_seq) if mid_seq else 0
        
        return max(left_max, right_max, mid_max), max(left_seq, mid_seq, right_seq, key=sum)

#função principal / orquestração 
def main():
    sequence = read_input("2023-03-25/input_ex3.txt")
    max_sum, subsequence = max_subsequence_sum(sequence)
    write_output("2023-03-25/output_ex3.txt", max_sum, subsequence)

if __name__ == "__main__":
    main()