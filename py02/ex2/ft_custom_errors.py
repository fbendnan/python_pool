class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant_name):
        super().__init__(f"Caught PlantError: The {plant_name} "
                         f"plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Caught WaterError: Not enough water in the tank!")


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        raise PlantError("Tomato")
    except PlantError as e:
        print(e)
    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(e)

    print("\nTesting catching all garden errors...")
    try:
        raise (PlantError("Tomato"))
    except GardenError as e:
        print(e)
    try:
        raise (WaterError())
    except GardenError as e:
        print(e)


test_errors()
