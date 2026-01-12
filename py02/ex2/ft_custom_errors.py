class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, plant_name):
        super().__init__(f"Caught PlantError: The {plant_name} plant is wilting!")

class WaterError(GardenError):
    def __init__(self, plant_name):
        super().__init__(f"Caught WaterError: Not enough water in the tank!")

def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print(f"\nTesting PlantError...")
    try:
        raise PlantError("Tomato")
    except PlantError as e:
        print(e)
    print(f"\nTesting WaterError...")
    try:
        raise WaterError("Tomato")
    except WaterError as e:
        print(e)

    print(f"\nTesting catching all garden errors...")
    try:
        raise (PlantError("Tomato"))
    except GardenError as e:
        print(e)
    try:
        raise (WaterError("Tomato"))
    except GardenError as e:
        print(e)


test_errors()