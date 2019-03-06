from level import *

class Shelf(Level):
    """Represents a shelf on a level of a warehouse. A level can accomodate
       500 shelves.
       """

    shelfID = 1
    
    def __init__(self, level):
        assert isinstance(level, Level), 'Please supply an existing Level.'
        self.shelfID = 'S' + str(Shelf.shelfID).zfill(3)
        Shelf.shelfID += 1
        self.home = level.get_levelID()
        self.depth = 0
        self.locations = {}
        level.shelves[self] = self.locations

    def __str__(self):
        return 'Shelf ' + self.ShelfID

    def get_shelfID(self):
        """Returns the ID of shelf."""
        return self.shelfID

    def get_home(self):
        """Returns the home level of the shelf."""
        return self.home

    def get_depth(self):
        """Returns the physical depth of shelf."""
        return self.depth

    def get_locations(self):
        """Returns a copy of the list of locations on shelf."""
        return self.locations.copy()

    def show_home(self):
        """Prints home level of shelf."""
        print(self.home)

    def list_locations(self):
        """Returns a list of locations on shelf."""
        locationList = []
        for i in self.get_locations():
            locationList.append(i)
        return locationList

    def add_location(self, location):
        """Adds one location to list of locations."""
        self.locations.setdefault(location, [])

ltn = Warehouse('LTN')
p1 = Level(ltn)
p2 = Level(ltn)
s001 = Shelf(p1)
s002 = Shelf(p1)
for i in range(1, 21):
    s001.add_location('loc')
print(ltn.levels)
print(p1.shelves)
print(s001.locations)
s002.show_home()
