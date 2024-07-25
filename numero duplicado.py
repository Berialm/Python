# numero duplicado
lista=[]
lista_pos=[]
for i in range(10):
  num=int(input("Montar lista:"))
  if num in lista:
    lista_pos.append(i)
    lista.append(num)
  else:
    lista.append(num)
print(lista)
print(lista_pos)
x=len(lista_pos)
print(x)
pos=0
i=0
v=0
for i in range(x):
  if i==0:
    pos=lista_pos[v]
    lista.pop(pos)
    print(pos)
    print(i)
    print(v)
    print(lista)
  else:
    v=v+1
    pos=lista_pos[v]
    lista.pop(pos-i)
    print(pos)
    print(i)
    print(v)
    print(lista)