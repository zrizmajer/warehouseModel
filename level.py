from warehouse import *

class Level(Warehouse):
    """Represents a level of inventory in a warehouse."""

    levelID = 1
    
    def __init__(self, warehouse):
        """warehouse should be an instance of Warehouse object. Level will be added to this warehouse, and named
           with a level ID (Level P1, Level P2 etc.)
           """
        assert isinstance(warehouse, Warehouse), 'Please supply existing warehouse.'
        assert Level.levelID <= warehouse.get_levelnr()
        self.levelID = 'P' + str(Level.levelID)
        Level.levelID += 1
        self.home = warehouse
        self.shelves = {}
        warehouse.levels[self] = self.shelves

    def __str__(self):
        return 'Level ' + self.level

    def get_levelID(self):
        """Returns the ID of level"""
        return self.levelID

    def get_home(self):
        """Returns the home warehouse of the level."""
        return self.home

    def get_shelves(self):
        """Returns a copy of shelves present on level."""
        return self.shelves.copy()

    def show_home(self):
        """Prints home warehouse of level"""
        print(self.home.name)

    def list_shelves(self):
        """Returns a list of shelves on the level."""
        shelflist = []
        for i in self.get_shelves():
            shelflist.append(i)
        return shelflist

    def add_shelf(self, shelf):
        """Adds one shelf to list of shelves."""
        self.shelves.setdefault(shelf, {})
        



                
