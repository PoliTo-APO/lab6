class Vehicle:
    def __init__(self, model: str, fuel_eff: float, euro_class: int) -> None:
        self._model = model
        self._fuel_eff = fuel_eff
        self._euro_class = euro_class
        self._entrance_count = 0

    def get_model(self) -> str:
        return self._model

    def get_fuel_eff(self) -> float:
        return self._fuel_eff

    def get_euro_class(self) -> float:
        return self._euro_class

    def get_travel_cost(self, kms: float, fuel_cost: float) -> float:
        return kms / self._fuel_eff * fuel_cost

    def enter_ztl(self) -> bool:
        self._entrance_count += 1
        if self._entrance_count > 3 and self._euro_class < 4:
            return False
        return True


class Car(Vehicle):
    def __init__(self, model: str, fuel_eff: float, euro_class: int) -> None:
        super().__init__(model, fuel_eff, euro_class)
        self._passengers = 1

    def set_passengers(self, passengers: int) -> None:
        self._passengers = passengers

    def get_passengers(self) -> int:
        return self._passengers

    def get_travel_cost(self, kms: float, fuel_cost: float) -> float:
        return super().get_travel_cost(kms, fuel_cost) / self._passengers


class Truck(Vehicle):
    def __init__(self, model: str, fuel_eff: float, euro_class: int, weight: int) -> None:
        super().__init__(model, fuel_eff, euro_class)
        self._weight = weight
        self._cargo = 0

    def get_weight(self):
        return self._weight

    def set_cargo(self, cargo: float) -> None:
        self._cargo = cargo

    def get_cargo(self) -> float:
        return self._cargo

    def get_travel_cost(self, kms: float, fuel_cost: float) -> float:
        return super().get_travel_cost(kms, fuel_cost) * (self._weight + self._cargo) / self._weight

    def enter_ztl(self) -> bool:
        return True


# The following code is for testing
def vehicle_info(vehicle: Vehicle):
    print("-----------------------")
    print("Model: {}".format(vehicle.get_model()))
    print("Fuel efficiency (km/L): {:.1f}".format(vehicle.get_fuel_eff()))
    print("Euro class: {}".format(vehicle.get_euro_class()))
    print("Trip cost: {:.2f} €".format(vehicle.get_travel_cost(100, 1.7)))
    for i in range(4):
        print("Enter ztl {}: {}".format(i + 1, vehicle.enter_ztl()))


def main():
    sport_bike = Vehicle("Yamaha R1", fuel_eff=17, euro_class=1)
    vehicle_info(sport_bike)

    scooter = Vehicle("Tmax", fuel_eff=22, euro_class=4)
    vehicle_info(scooter)

    city_car = Car("Fiat panda", fuel_eff=14, euro_class=3)
    vehicle_info(city_car)
    print("Num passengers: {}".format(city_car.get_passengers()))
    city_car.set_passengers(3)
    print("Trip cost ({} passengers): {:.2f} €".format(city_car.get_passengers(), city_car.get_travel_cost(100, 2.2)))

    lorry = Truck("Fiat Ducato", fuel_eff=20.1, euro_class=1, weight=1700)
    vehicle_info(lorry)
    lorry.set_cargo(850)
    print("Trip cost ({} kg of cargo): {:.2f} €".format(lorry.get_cargo(), lorry.get_travel_cost(100, 2.2)))


if __name__ == "__main__":
    main()
