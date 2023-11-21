#Definition de la variable
i=0

#Ouverture de la boucle while : tant que i est inférieur ou égal à 100 tu réalises les tâches suivantes :
while i <=100:
#Si le modulo de i est égal à zéro quand on le divise par 3 et 5 alors on imprime "FizzBuzz" 
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
#Sinon si le modulo de i est égal à zéro quand on le divise par 3 alors on imprime "Fizz"
    elif i%3 == 0:
        print("Fizz")
#Sinon si le modulo de i est égal à zéro quand on le divise par 3 alors on imprime "Buzz"
    elif i%5 == 0:
        print("Buzz")
#Sinon imprime i
    else:       
        print(i)
    i=i+1