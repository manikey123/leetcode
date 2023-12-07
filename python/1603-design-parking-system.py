class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        
        # [total_occupied, max_capacity]
        self.parking = {
            1: [0 ,big],
            2: [0, medium],
            3: [0, small]
        }

    def addCar(self, carType: int) -> bool:
        new_total = self.parking[carType][0] + 1
        if new_total <= self.parking[carType][1]:
            self.parking[carType][0] += 1
            return True
        return False

park= ParkingSystem(0,0,0)

#Input
keyOps = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
valueOps = [[1, 1, 0], [1], [2], [3], [1]]
#Output
#[null, true, true, false, false]

output =[]
for index,value in enumerate(keyOps):
    if value == "ParkingSystem":
        park = ParkingSystem(valueOps[index][0], valueOps[index][1], valueOps[index][2])
        output.append(None)
    elif value == "addCar":
        o1 = park.addCar(valueOps[index][0])
        output.append(o1)
print(output)