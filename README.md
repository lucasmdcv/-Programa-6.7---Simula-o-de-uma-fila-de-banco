# -Programa-6.7---Simula-o-de-uma-fila-de-banco
Usando listas como filas
Uma lista pode ser utilizada como  fila se obedecermos a certas regras de inclusão e eliminnação de elementos.
Em uma fila , a inclusão é sempre realizada no fim, e as remoções são feitas no início. Dizemos que o primeiro a chegar é o 
primeiro a sair (FIFO - First In First Out).

É mais simples de entender se imaginarmos uma fila de banco. Quando a agência abre pela manhã, a fila está vazia.Quando os clientes 
começam a chegar, eles vão diretamente para o fim da fila. Os caixas então começam a atender esses clientes por ordem de chegada, ou seja,
o cliente que chegou primeiro será atendido primeiro. Uma vez que ocliente é atendido, ele sai da fila. Então, um novo cliente passa a ser 
o primeiro da fila e o próximo a ser atendido.

Para escrevermos algo similiar em Python, imaginaremmos uma lista de clientes, representando a fila, em que o valor de cada 
elemento é igual à ordem de chegada  do cliente. Vamos imaginar uma lista inicial com 10 clientes. Se outro cliente chegar, realizaremos um append
para que ele seja inserido no fim da fila (fila.append(último)). Para retirarmos um cliente da  fila e atendê-lo, poderíamos fazer *del* fila.
Se quisermos retirá-lo da fila e, ao mesmo tempo, obter o elemento retirado, podemos utilizar o método pop fila.pop(0).
O método pop retorna o valor do elemento e o exclui da fila. Passamos 0 como parâmetro para indicar que queremos excluir o primeiro elemento.
