#Desarrolla una concesionaria de vehículos en la cual se puedan gestionar las compras y ventas de vehículos. Un usuario podrá 
# ver los vehículos disponibles, su precio y realizar la compra de uno. Aplica los conceptos de programación orientada a objetos 
# vistos en este ejercicio.

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price
        self.available = True

    def buy(self):
        self.available = True
        
    def sell(self):
        self.available = False

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.bought_car = []

    def buy_car(self, car):
        if car.available:
            car.sell()
            self.bought_car.append(car)
            print(f"El auto {car.make} - {car.model} ha sido vendido por ${car.price} a {self.name}")
        else:
            print(f"El auto {car.make} - {car.model} No esta disponible para la venta")
        

class Dealer:
    def __init__(self):
        self.cars = []
        self.users = []
    
    def buy_car(self, car):
        self.cars.append(car)
        print(f"El auto {car.make} - {car.model} ha sido comprado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_cars(self):
        print("-- Autos disponibles para la venta --")
        for car in self.cars:
            if car.available:
                print(f"{car.make} - {car. model} --> Price: {car.price}")

#Autos
car1 = Car("Audi", "Q2", 10000)
car2 = Car("BMW", "X2", 9000)

#Usuarios
user1 = User("Dalia", "001")

#Crear Consecionario
dealer = Dealer()

# Comprar autos 
dealer.buy_car(car1)
dealer.buy_car(car2)

#Registrar Usuario
dealer.register_user(user1)

#Mostrar autos disponibles a la venta
dealer.show_available_cars()

#Vender auto
user1.buy_car(car1)

#Mostrar autos disponibles a la venta
dealer.show_available_cars()

#Vender auto
user1.buy_car(car1)


