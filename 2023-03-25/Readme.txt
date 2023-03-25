------------------------------------------------------------------------------------------------------
Autor     : José Casimiro
Nr. Aluno : A51115
Data      : 2023-03-25
------------------------------------------------------------------------------------------------------

Exercício 1, alínea a:
------------------------------------------------------------------------------------------------------
A complexidade de tempo da função recursiva é O(n), onde 'n' é o comprimento da sequência de entrada,
e a complexidade de tempo da função principal depende do número de pares ordenados e do comprimento 
das subsequências, mas no limite será O(n^2), onde 'n' é o comprimento da sequência de entrada.

Exercício 1, alínea b:
------------------------------------------------------------------------------------------------------
A modificação de código apenas um único ciclo para iterar sobre os pares ordenados.
A complexidade do ciclo é O(m), onde m é o número de pares ordenados, e a função 'sum' (soma) de cada
sequência é O(k), onde k é o comprimento da sub-sequência.
Assim, a complexidade total do algoritmo é O(n+m*k), que se reduz para O(n+m) se assumirmos que o 
comprimento de cada sub-sequência é proporcional ao comprimento da sequência principal.

Exercício 3, alínea b:
------------------------------------------------------------------------------------------------------
A complexidade de tempo é O(n), onde 'n' é o tamanho da sequência.