class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, plant_name):
        super().__init__(f"Caught PlantError: The {plant_name} plant is wilting!")

class WaterError(GardenError):
    def __init__(self, plant_name):
        super().__init__(f"Caught WaterError: Not enough water in the tank!")

class plant:
    def __init__(self, plant_name, water_level, sunlight_hours):
        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours

class GardenManager:
    def __init__(self, plant):
        self.plants = []

    def add_plants(self):
        try:
            if self.plant == None or self.plant == "":
                raise Exception("Error adding plant: Plant name cannot be empty!")
            self.plants.append(self.plant)
            print(f"Added {self.plant.plant_name} successfully")
        except Exception as e:
            print(e)
    

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant.plant_name is None or plant.plant_name == "":
                    raise ValueError("Cannot water None - invalid plant!")
                print(f"Watering {plant.plant_name} - success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")


    def check_plant_health(self):
        for plant in self.plants:
            try:
                if plant == None or plant == "":
                    raise ValueError("Error: Plant name cannot be empty!")
                if plant.water_level>10:
                    raise ValueError(f"Error: Water level {plant.water_level} is too high (max 10)")
                elif plant.water_level<1:
                    raise ValueError(f"Error: Water level {plant.water_level} is too low (min 1)")
                if plant.sunlight_hours<2:
                    raise ValueError(f"Error: Sunlight hours {plant.sunlight_hours} is too low (min 2)")
                elif plant.sunlight_hours>12:
                    raise ValueError(f"Error: Sunlight hours {plant.sunlight_hours} is too high (max 12)")
                print(f"Plant '{plant.plant_name}' is healthy!")
            except ValueError as e:
                print(e)
