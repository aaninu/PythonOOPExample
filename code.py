#python 


class Cuprins:
    def __init__(self):
        print ("Welcome Cuprins")


class Autor:
    def __init__(self, nume):
        self.sNume = nume
        print ("Welcome Autor!")

    def nume(self):
        return self.sNume

class Carte:
    def __init__(self, titlu):
        self.sTitlu = titlu
        self.cAutor = None
        self.capitol = Capitol()
        self.subcapitol = Subcapitol()
        self.text = None
        self.imagine = None
        self.tabel = None
        print("Welcome Carte!")
    
    def titlu(self):
        return self.sTitlu

    def addAutor(self, autor):
        self.cAutor = autor
        return 0

    def getAutor(self):
        return self.cAutor.nume

    def createCapitol(self, capitol):
        self.capitol.setTitlu(capitol)
        return 0

    def createSubCapitol(self, subcapitol, lista):
        self.subcapitol = Subcapitol()
        self.subcapitol.setTitlu(subcapitol)
        self.subcapitol.addElement(lista)
        return 0

    def printt (self, lista):
        for i in range(0,len(lista)):
            print (lista[i].titlu + " " + lista[i].getAutor())

    def printSubCapitol(self):
        return self.subcapitol.printt()

class Capitol:
    def __init__(self):
        self.sTitlu = None
        print ("Welcome Capitol!")

    def titlu(self):
        return self.sTitlu
    
    def setTitlu(self, titlu):
        self.sTitlu = titlu
        return 0

class Subcapitol:
    def __init__(self):
        self.sName = None
        self.aLista = None
        print ("Welcome Subcapitol!")

    def titlu(self):
        return self.sName
    
    def setTitlu(self, titlu):
        self.sName = titlu
        return 0
    
    def addElement(self, el):
        self.aLista = el
        return 0
    
    def printt(self):
        print ()
        print ("Afiseaza subcapitolul: ")
        print (self.titlu())
        self.aLista.printt()
        return 0

class Text:
    def __init__(self):
        self.sText = None
        print ("Welcome Text!")

    def text(self):
        return self.sText
    
    def setText(self, text):
        self.sText = text
        return 0
        
class Imagine:
    def __init__(self):
        self.uImg = None
        print ("Welcome Imagine!")

    def numeImagine(self):
        return self.uImg
    
    def setImagine(self, img):
        self.uImg = img
        return 0

class Tabel:
    def __init__(self):
        self.tTable = None
        print ("Welcome Tabel!")

    def numeTabel(self):
        return self.tTable
    
    def setTabel(self, table):
        self.tTable = table
        return 0

class Element(Text, Imagine, Tabel):
    def __init__(self):
        self.lista = []
    
    def Imagine(self, img):
        elem = Imagine()
        elem.setImagine(img)
        self.lista.append(["imagine", elem])
        return 0
    
    def Tabel(self, tabel):
        elem = Tabel()
        elem.setTabel(tabel)
        self.lista.append(["tabel", elem])
        return 0
    
    def Text(self, text):
        elem = Text()
        elem.setText(text)
        self.lista.append(["text", elem])
        return 0

    def len(self):
        return len(self.lista)
    
    def printt(self):
        for i in range(0, len(self.lista)):
            if self.lista[i][0] == "imagine":
                print("Imagine: ", self.lista[i][1].numeImagine())
            elif self.lista[i][0] == "tabel":
                print("Tabel: ", self.lista[i][1].numeTabel())
            elif self.lista[i][0] == "text":
                print("Text: ", self.lista[i][1].text())
            else:
                print ("Unknown!")
        return 0


c = Carte("Disco Titanic")
c.addAutor(Autor("Gelu Cristian"))

c.createCapitol("Mancare")

lista = Element()
lista.Tabel("Something table")
lista.Imagine("http://example.com/image.png")
lista.Text("Welcome the user!")
lista.Tabel("Tabel1")
lista.Tabel("table 24")
lista.Imagine("http://example.com/im2.jpg")
lista.Text("Write text")

c.createSubCapitol(" Cirese de vara ", lista)

c.printSubCapitol()

