class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = { 'small': small, 'medium': medium, 'big': big }

    def update_slot(self, type):
        if not self.slots[type]:
            return False
        self.slots[type] -= 1
        return True

    def addCar(self, car_type: int) -> bool:
        match car_type:
            case 1: return self.update_slot('big')
            case 2: return self.update_slot('medium')
            case 3: return self.update_slot('small')
