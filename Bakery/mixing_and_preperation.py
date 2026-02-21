# Combine ingredients and prepare batters and doughs before they go into the oven

#Whisks: blend thoroughly and incorporate air. Used for whisking eggs, combining dry ingredients evenly, or beating cream.
class Whisk:
    pass

class Balloon_Whisk(Whisk):
    # general mixing
    pass

class French_Whisk(Whisk):
    #heavy mixing
    pass


class Spoon:
    def stirring(self):
        pass

    def mixing(self):
        pass

    def scraping(self):
        pass

class Wooden_Spoon(Spoon):
    pass

class Spatula:
    def __init__(self, material):
        self.material = material #silicone or wooden

class Rubber_Scrapers:
    # smaller and more flexible
    # for scraping every last bit of batter from bowl sides and corners.
    def scrape():
        pass
    pass

class Electric_Mixer:
    #automate the mixing process
    pass