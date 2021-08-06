from seed import Seed

if(__name__ == "__main__"):
    #User input for the number of rows and columns.
    no_of_rows = int(input("Enter the number of rows: "))
    no_of_columns = int(input("Enter the number of columns: "))

    # create seed:
    seed = Seed(no_of_rows,no_of_columns)

    #run the first iteration of the seed:
    seed.draw_seed()
    
    user_action = ''
    while user_action != 'q':
        user_action = input('Press enter to add generation or q to quit:')

        if user_action == '':
            seed.update_seed()
            seed.draw_seed()
