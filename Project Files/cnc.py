"""
def x_axis(grid):
    a_g = str(grid * " ")
    for x in a_g:
        print("[ ]", end=" ")
    return

def raster_grid(grid):
    a_g = str(grid * " ")
    for y in a_g:
        print(x_axis(grid))
    return
"""


def raster_grid(grid):
    grid += 1
    val = 0
    for x in range(1, grid):  # --> out here, this iterates 'grid' times
        for y in range(1, grid):  # --> in here, this iterates 'grid'**2 times
            val += 1
            print("[ " " ]", end=" ")  # --> count number insterted here, within the box
        print()  # --> prints the horizontal row 'grid' amount of times
    return


raster_grid(int(input("What is the length of the square grid?: \n")))
