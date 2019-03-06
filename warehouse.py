class Warehouse(object):
    """Represents a warehouse unit of the company. Warehouse name should be the
       first three letters of its home town, capitalised."""

    def __init__(self, name, address = None):
        """Warehouse name should be the first three letters of its home town,
           capitalised.
        """
        assert type(name) == str, 'Name should be a string'
        assert len(name) == 3, 'Name must consist of first three letters of home town.'
        assert name.isupper(), 'Name must have all capital letters.'           
        self.name = name
        self.address = address
        self.levelnr = 3 #Number of levels for inventory in the building.
        self.levels = {}

    def __str__(self):
        return 'Warehouse ' + self.name

    def add_address(self, address):
        """Changes the address of the warehouse."""
        assert type(address) == str, 'Address should be a string.'
        self.address = address

    def change_level_number(self, levelNr):
        """Changes the number of levels for inventory in the building."""
        assert type(levelNr) == int, 'LevelNr must be an integer.'
        self.levelnr = levelNr

    def get_name(self):
        """Returns the name of the warehouse."""
        return self.name

    def get_address(self):
        """Returns the address of the warehouse."""
        return self.address

    def get_levelnr(self):
        """Returns the number of levels of the warehouse."""
        return self.levelnr
    
    def get_levels(self):
        """Returns the number of levels for inventory in the building."""
        return self.levels

    def add_level(self, level):
        """Adds one level to the warehouse."""
        self.levels.setdefault(level, {})



