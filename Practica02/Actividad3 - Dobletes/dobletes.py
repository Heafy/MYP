s = "ROSA - ROMA - COMA - COME"

#Usar s.trip() para eliminar espacios
arr = s.split(" - ")

def comparaLetra(string1, string2):
	a = list(arr)
	b = list(arr)
	return a + b

c = comparaLetra("sentimiento", "sofocar")


print arr
print c