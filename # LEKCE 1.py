# LEKCE 1
print("helo, this is the first ever print of this course")

print(type(5)) #int
print(type("text")) #str
print(type(5.5)) #float

print(10 / 3) #dělení na desetinná
print(10 // 3) #dělení (zahodím zbytek)
print(10 // 4)
print(10 % 3) #fce modulo (vrátí zbytek --> dobré na cyklování)
print (11 % 3)
print(2 ** 2) #umocňování
print(2 ** 3)

print(type("ahoj"))
print("he said \"helo\"!") #zpětné lomítko před uvozovkami ve stringu, aby printnul uvzovky
print("\n helo \t helo") #příklad special znaků pro odskakování apod.

print(2+2) #4
print("2"+"2") #22
print(2.0+2) #4.0

print(type(float(2))) #float
print(float(2)) #2.0
print(type(int(2.0))) #int
print(int(2.0)) #2
print(2 + float("2")) #4.0

print("nakoupil jsem " + str(10) + " kusu")
#práce se stringem
print("Michal " + "Titl")
print("Michal" + " " + "TITL") #spojí dohromady
print(10 * "X") #je to fajn na vizuální oddělování
print("Miata " * 3) #napíše xkrát
print(10 * "X")
print("Michal"[0]) #indexování (první prvek 0, poslední = počet písmen -1)
print("michal"[-1]) #lze i od konce, ale tam se začíná od nuly
print("michal"[-2])
print("michal"[-3])
print("michal"[-4])
print("michal"[-5])
print("michal"[-6])
print("michal titl"[0:6]) #slicing --> michal
print("michal titl"[5:]) #když neuvedu druhý parametr --> bere jako do konce
print("X" * 10)
print("0123456789"[0::2]) #striding - když chci třeba každé druhé číslo
print("0123456789"[10::-2]) #minusové znaménko --> jde od konce
print("\n XXX XXX XXX" * 3)

################
jmeno = "Michal"
vek = "23"
print(jmeno, vek)