"""
Factories
Builds images on demand
good for building many of a similar thing
Has one public access point
__init__ request tree.png
asks Factory for a tree. makes a basic tree
"""

"""
Flyweight 
REduced # of objects created
Objects with the same image use the same memory
__init__ request tree.png
creates it, if requested again, give the same tree

good to add to factories, keeping all loaded images in a dictionary, keeping stamps for duplicate objects
"""
def __init__(_loadFull):
    self._loadFull = _loadFull
    pass
def getSprite():
    pass
def _loadImage():
    pass
def _loadFull(filename):
    fullImage = self._loadFull(filename)
def applyTramsparency():
    pass
def applyColorKey():
    pass

"""
Color Key & Transparency
factory keeps a list of what objects need to be transparent and color keys for other objects

"""
