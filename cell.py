class Cell:
    #Class which holds initial status of cell (dead).
    def __init__(self):
        self.cell_status = 'Dead'

    #method to set the cell status to DEAD
    def set_dead(self):
        self.cell_status = 'Dead'

    #method to set the cell status to ALIVE
    def set_alive(self):
        self.cell_status= 'Alive'

    #method to check if the cell is ALIVE and returns True if it is alive, False if not.
    def is_alive(self):
        if self.cell_status == 'Alive':
            return True
        return False

    #method to return a charcter for the cell status to print on the seed
    def print_character(self):
        if self.is_alive():
            return '0'
        return '*'