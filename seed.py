from cell import Cell
from random import randint

class Seed:
    #constructor holds input from user and populates the grid with cells. 
    def __init__(self,rows,columns):
        self.cell_rows = rows
        self.cell_columns = columns   
        self._grid = [[Cell() for column_cells in range(self.cell_columns)] for row_cells in range(self.cell_rows)]

        self.create_seed() #this creates the seed right away

    #method that sets the random state of the cells.
    def create_seed(self):
        for row in self._grid:
            for column in row:
                #there is a 33% chance for the cells to be alive
                chance = randint(0,2) 
                if chance == 1:
                    column.set_alive()

    #method that draws the actual seed in the terminal
    def draw_seed(self):
        print('\n')
        for row in self._grid:
            for column in row:
                print(column.print_character(),end='')
            print() # to create a new line after every row.

    
    #method to check all the neighbours for all the cells
    #returns the list of the valid neighbours so the update method can set the new status
    def check_neighbor(self, check_row , check_column):
        #empty list to append neighbors into.
        neighbor_list = []
        for row in range(-1,2):
            for column in range(-1,2):
                neighbor_row = check_row + row
                neighbor_column = check_column + column 
                
                neighbor = True

                if (neighbor_row) == check_row and (neighbor_column) == check_column:
                    neighbor = False

                if (neighbor_row) < 0 or (neighbor_row) >= self.cell_rows:
                    neighbor = False

                if (neighbor_column) < 0 or (neighbor_column) >= self.cell_columns:
                    neighbor = False

                if neighbor:
                    neighbor_list.append(self._grid[neighbor_row][neighbor_column])
        return neighbor_list 

    #method tp update the seed per generation
    def update_seed(self):
        #cells list for living cells to kill and cells to keep alive
        alive_cells = []
        killed_cells = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbour per square:
                check_neighbour = self.check_neighbor(row,column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                c1 = self._grid[row][column] #cell object
                status_of_cell = c1.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_of_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        killed_cells.append(c1)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        alive_cells.append(c1)

                else:
                    if len(living_neighbours_count) == 3:
                        alive_cells.append(c1)

        #set cell statuses
        for cell in alive_cells:
            cell.set_alive()

        for cell in killed_cells:
            cell.set_dead()

    
    
    

    

