#length unit = inches

class Pan:
    def __init__(self, material, shape, size, non_stick, handle_type = "heat_resistant" side_height = "2"):
        #metal = aluminium / steel / cast iron
        # shape = round / rectangular
        # size
        # side_height
        pass

class Cake_Pan(Pan):
    # oven cooking
    pass

class frying_pan(Pan):
    # flat bottom + sloped sides
    # cook - eggs, vegetables, meat on stovetop
    pass

class SaucePan(Pan):
    # deeper with higher sides
    # simmering sauces or boiling liquids
    pass

class Wok(Pan):
    pass

class Griddle(Pan):
    pass

class Dutch_Oven(Pan):
    pass

if __name__ == "__main__":
     #this will run only when pan is run directly
    print("Defined are the the types of pans")