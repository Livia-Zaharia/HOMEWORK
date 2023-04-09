class Container:
    pass

class PlasticContainer(Container):
    pass

class MetalContainer(Container):
    pass

class CustomContainer():
    pass

class TemperatureControlledContainer(Container):
    pass

class RefrigeratedContainer(TemperatureControlledContainer):
    pass


print(issubclass(PlasticContainer,Container))
print(issubclass(MetalContainer,Container))
print(issubclass(CustomContainer,Container))


class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        print(f"brand->{self.brand}")
        print(f"color->{self.color}")
        print(f"year->{self.year}")



class Car(Vehicle):
    def __init__(self,brand,color,year,horsepower):
        super().__init__(brand,color,year)
        self.horsepower=horsepower

    def display_attrs(self):
        super().display_attrs()
        print(f"horsepower->{self.horsepower}")
        

vehicle=Vehicle("Tesla","red",2020)
car=Car("Tesla","red",2020,300)

vehicle.display_attrs()
car.display_attrs()

print(issubclass(TemperatureControlledContainer,Container))
print(issubclass(RefrigeratedContainer,TemperatureControlledContainer))
print(issubclass(RefrigeratedContainer,Container))

