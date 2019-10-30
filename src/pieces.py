
class Coordinate:

    def __init__(self, coord, label, piece):

        self.coord = coord
        self.label = label
        self.piece = piece
        self.nextPos = self.nextPos()
        # a list of coordinates that the next piece can travel if the player decides to do so.
    
    def nextPos(self):
        
        return []
        # Calculate the next pos

