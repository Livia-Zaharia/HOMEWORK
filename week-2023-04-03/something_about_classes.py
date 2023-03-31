"""
1. Restaurant: Faceți o clasă numită Restaurant. Metoda __init__() pentru Restaurant ar trebui să stocheze două atribute: un nume de restaurant și un tip de bucătărie. Faceți o metodă numită describe_restaurant() care tipărește aceste două informații și o metodă numită open_restaurant() care tipărește un mesaj care indică faptul că restaurantul este deschis.

Creați o instanță numită restaurant din clasa dvs. Imprimați cele două atribute individual, apoi apelați ambele metode.

2. Trei restaurante: începeți cu clasa dvs. de la exercițiul 1. Creați trei instanțe diferite din clasă și apelați describe_restaurant() pentru fiecare instanță.

3. Utilizatori: Faceți o clasă numită User. Creați două atribute numite first_name și last_name, apoi creați alte câteva atribute care sunt de obicei stocate într-un profil de utilizator. Realizați o metodă numită describe_user() care imprimă un rezumat al informațiilor utilizatorului. Realizați o altă metodă numită greet_user() care imprimă utilizatorului o felicitare personalizată.

Creați mai multe instanțe care reprezintă utilizatori diferiți și apelați ambele metode pentru fiecare utilizator.


"""
class Restaurant:
    def __init__(self,name:str,cusine:str):
        self.name=name
        self.cusine=cusine
    def describe_restaurant(self):
        print(f"this is a {self.cusine} restaurant called {self.name}")
    def open_restaurant(self):
        print("the restaurnat is now open")


OneAdress=Restaurant("Blue Moon", "Thai")
print(OneAdress.name)
print(OneAdress.cusine)
OneAdress.describe_restaurant()
OneAdress.open_restaurant()


TwoAdress=("Buongiorno","Italian cusine")
ThreeAdress=("Mc","fastfood")
FourAdress=("Japanos","Japanese")

TwoAdress.describe_restaurant()
ThreeAdress.describe_restaurant()
FourAdress.describe_restaurant()


class User:
    def __init__(self, last_name:str, first_name:str, ID:int, password:str):
        self.last_name=last_name
        self.first_name=first_name
        self.ID=ID
        self.password=password
    def describe_user(self):
        print(f"User is named {self.last_name} {self.first_name} and uses ID {self.ID} with a secret password")
    def greet_user(self):
        print(f"Hi there, {self.first_name}")