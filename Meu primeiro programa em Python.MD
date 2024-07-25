# Meu primeiro programa em Python



- Escreva uma função que receba uma lista como entrada e remova todos os elementos duplicados, mantendo apenas a primeira ocorrência de cada elemento. Programa deve pedir 10 inputs ao usuário:

  

  Como estou iniciando os estudos de Python agora e ainda não sei trabalhar com funções, resolvi fazer o código com o conhecimento básico que tenho. Para conseguir acompanhar a funcionalidade da lógica montada e entender os erros que ocorriam durante o desenvolvimento e testes, coloquei vários prints mostrando o resultado de cada etapa do processo, dessa forma consegui solucionar o problema. Abaixo segue o código e a execução:

  

  #### Código:

`\# numero duplicado`

`lista=[]`

`lista_pos=[]`

`for i in range(10):`

 `num=int(input("Montar lista:"))`

 `if num in lista:`

  `lista_pos.append(i)`

  `lista.append(num)`

 `else:`

  `lista.append(num)`

`print(lista)`

`print(lista_pos)`

`x=len(lista_pos)`

`print(x)`

`pos=0`

`i=0`

`v=0`

`for i in range(x):`

 `if i==0:`

  `pos=lista_pos[v]`

  `lista.pop(pos)`

  `print(pos)`

  `print(i)`

  `print(v)`

  `print(lista)`

 `else:`

  `v=v+1`

  `pos=lista_pos[v]`

  `lista.pop(pos-i)`

  `print(pos)`

  `print(i)`

  `print(v)`

  `print(lista)`



#### Execução:

Montar lista:1
Montar lista:3
Montar lista:5
Montar lista:1
Montar lista:7
Montar lista:9
Montar lista:3
Montar lista:11
Montar lista:5
Montar lista:13
[1, 3, 5, 1, 7, 9, 3, 11, 5, 13]
[3, 6, 8]
3
3
0
0
[1, 3, 5, 7, 9, 3, 11, 5, 13]
6
1
1
[1, 3, 5, 7, 9, 11, 5, 13]
8
2
2
[1, 3, 5, 7, 9, 11, 13]



