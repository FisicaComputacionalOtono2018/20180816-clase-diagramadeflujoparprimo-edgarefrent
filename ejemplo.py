

def isPrimeFor(num):
	flag=True
	if num==1:
		flag=False

	for i in range (2, (num-1)):
		if num%i==0:
			flag=False
			break
	return flag

p = input("Dame un numero: ")

if isPrimeFor(p)==True:

	print("Es primo")
else :
	print("No es primo")

