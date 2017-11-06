#First makes a list
def lista(inicio, final):
	a=list(range(inicio,final+1))
	return a
    
#Then it sums the elements of that list and checks if odd or not
def oddornot(a,b):
    if sum(lista(a,b))%2==0:
        return "not odd"
    else:
        return "odd"
