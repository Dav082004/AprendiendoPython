#creando un conjunto con set

conjunto = set(["dinqidq","dqidiq"])

#metiendo un conjunto dentro de otro conjunto
conjunto1= frozenset({"dato 1", " dato2"})
conjunto2= {conjunto1, "dato4"}

#Teoria de conjuntos
conjunto1 = {1,3,4,5}
conjunto2 = {1,3,4}

#verficando si es un subconjuto
resultado= conjunto1.issubset(conjunto2)
resultado= conjunto1 <= conjunto2

#verficando si es un superconjuto
resultado= conjunto2.issuperset(conjunto1)
resultado= conjunto2 > conjunto1

#verificamos si hay algun numero en comun 
resultado=conjunto2.isdisjoint(conjunto1)