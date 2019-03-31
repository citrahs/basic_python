def tambah(a,b):
	penambahan = a+b
	return penambahan

def kali(a, b):
    perkalian = a * b
    return perkalian
	
def bagi(a, b):
    pembagian = a//b
    return pembagian
	
def pangkat(a,b):
	pangkat = a ** b
	return pangkat
	
def absolut(a):
	if a < 0:
		hasil = (-1)*a
		return hasil
	else:
		return a