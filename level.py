from warehouse import *

class Level(Warehouse):
    """Represents a level of inventory in a warehouse."""

    levelID = 1
    
    def __init__(self, warehouse):
        assert isinstance(warehouse, Warehouse), 'Please supply existing warehouse.'
        assert Level.levelID <= warehouse.get_levels()
        self.level = 'P' + str(Level.levelID)
        self.home = warehouse
        Level.levelID += 1
        warehouse.levels.append(self)

    def __str__(self):
        return 'Level ' + self.level


                
