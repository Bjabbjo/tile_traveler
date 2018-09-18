def check_print (x,y):
    valid_directions = ""
    valid_print = ""

    if x == 1 and y >= 1 and y <= 2:
        valid_directions += "n"
        north_print = " (N)orth "
        valid_print += north_print
    
    if x == 3 and y >= 1 and y <= 2:
        valid_directions += "n"
        north_print = " (N)orth "
        valid_print += north_print
    
    if x == 2 and y == 1:
        valid_directions += "n"
        north_print = " (N)orth "
        valid_print += north_print
    
    if y == 2 and x == 1:
        valid_directions += "e"
        east_print = "(E)ast"
        if len(valid_directions) >= 2:
            east_print = " or (E)ast"
        valid_print += east_print 

    if y == 3 and x >= 1 and x <= 2:
        valid_directions += "e"
        east_print = "(E)ast"
        if len(valid_directions) >= 2:
            east_print = " or (E)ast"
        valid_print += east_print 
    
    if y == 2 and x == 2:
        valid_directions += "s"
        south_print = "(S)outh"
        if len(valid_directions) >= 2:
            south_print = " or (S)outh"
        valid_print += south_print
    
    if y >= 2 and y <= 3 and x == 3:
        valid_directions += "s"
        south_print = "(S)outh"
        if len(valid_directions) >= 2:
            south_print = " or (S)outh"
        valid_print += south_print

    if y >= 2 and y <= 3 and x == 1:
        valid_directions += "s"
        south_print = "(S)outh"
        if len(valid_directions) >= 2:
            south_print = " or (S)outh"
        valid_print += south_print
    
    if y == 3 and x <= 3 and x >= 2:
        valid_directions += "w"
        west_print = "(W)est"
        if len(valid_directions) >= 2:
            west_print = " or (W)est"
        valid_print += west_print
    
    if y ==2 and x == 2:
        valid_directions += "w"
        west_print = "(W)est"
        if len(valid_directions) >= 2:
            west_print = " or (W)est"
        valid_print += west_print
    
    return valid_print, valid_directions

def change_value(direction,x,y):
    if direction == "n":
        y += 1
    if direction == "e":
        x += 1
    if direction == "s":
        y -= 1
    if direction == "w":
        x -= 1
    
    return x,y


victory = False
x = 1
y = 1


while not victory:
    valid_directions = ""
    valid_print = ""
    number = len(valid_directions)

    valid_print,valid_directions = check_print(x,y)
    
    
    options = ""
    options_print = "You can travel: "
    print(options_print + valid_print)
    direction = input("Direction: ")


    if not direction in valid_directions:
        print("Not a valid direction!")
    
    else:
        x,y = change_value(direction,x,y)


    if x == 3 and y == 1:
        victory = True

print("Victory!")