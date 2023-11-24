#Izveidojiet Pythonprogrammu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kvadrāts ir lielāks par 1000.
skaitlis=[1,2,3,4,5,6,7,8,9,10]
kvadrati=list(filter(lambda x: x%2==0 or x%3, skaitlis))
print(kvadrati)