#Canaan Barbery
#CPSC 122-01, Spring 2026
#Programming Assignment #1
#1/25/26
#I attempted the bonus
#This program takes an image file and can perform alterations to it, like flipping, rotating, and changing color.


import random 

# def pretty_print(data):
#     for row in data:
#         print(row)

def load_image_data(filename: str) -> list[list[list[int]]]:
    """Loads the file according to its filename, and creates a 3D list from its numerical data, 
with every three numbers being a pixel, every line being a row, and finally the both lists being one large list.

    Args: 
        input_file (str): Name of the file whose data is being appended into lists.

    Returns:
        data (list): 3D list of pixels and rows.
    """    
    row = [] #empty list to be filled with pixel lists
    data = [] #empty list to be filled with row lists
    
    x = 0
    
    #opens input_file to read
    with open(filename, "r") as infile:
        
        #loops through lines in the file to add integers to lists
        for line in infile:            
            line = line.strip()
            
            #skips first 3 lines
            if x < 3:
                x += 1
                continue
            
            #adds commas between integers
            vals = line.split(" ")
            
            #loops through every 3 integers and pockets them in a list, then appends lists to row
            for i in range(0,len(vals), 3):               
                red = int(vals[i])
                green = int(vals[i + 1])
                blue = int(vals[i + 2])
                pixel = [red, green, blue]                
                row.append(pixel)
            
            #appends new_row lists to data list, and resets row list for every iteration of the loop.
            data.append(row)
            row = []
    
    return data 

def write_image_data(data: list[list[list[int]]], filename: str):
    """Takes the 3D list of pixels and rows, and writes it to a file as just numerical data, preceeded by P3, 
the width and length of the image, and 255.

    Args:
        image_data (list): 3D list of pixels and rows.
        
        filename (str): name of the file being written
    """
    
    length = str(len(data)) #length of the data
    width = str(len(data[0])) #width of the daa        
    
    #opens filename to write image_data
    with open(filename, "w") as outfile:
        
        #adds back in the first 3 lines, using width and length.
        outfile.write("P3\n"
                      + width + " " + length + "\n"
                      + "255\n")
        
        #loops through each pixel in image_data and converts to str, then writes to filename.
        for row in data:
            for pixel in row:
                for x in pixel:
                    x = str(x)
                    outfile.write(x + " ")
            
            outfile.write("\n")


def apply_modification(data: list[list[list[int]]], mod: str) -> list[list[list[int]]]:
    """Calls a modification function based on user input.
    
    Args:
        
        image_data (list): 3D list of pixels and rows.
        
        user_input (str): letter that corresponds to a mod function.
         
    Returns:
        
        data (list): Updated 3D list of pixels and rows that replaces 'image_data'.
    """
    
    if mod == "a":
        
        data = vertical_flip(data)

    elif mod == "b":
            
        data = horizontal_flip(data)
        
    elif mod == "c":

        data = rm_red(data)
    
    elif mod == "d":

        data = rm_green(data)

    elif mod == "e":
        
        data = rm_blue(data)
    
    elif mod == "f":

        data = neg(data)
    
    elif mod == "g":

        data = hicont(data)
        
    elif mod == "h":

        data = noise(data)
    
    elif mod == "i":
        
        data = bw(data)
    
    elif mod == "j":

        data = blur(data)
        
        
    return data 

def vertical_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Flips the data upside down by creaing a new list, where the rows in the 'data' 
list are in their opposite position relative to the center of 'data'.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        new_data (list): Updated 3D list of pixels and rows that replaces 'data'.
    """
    new_data = [] #empty list to be appended with new row lists
    
    #loops through data list and appends new_data with new row lists
    for row in range(0, len(data)):
        new_data.append(data[len(data) - 1 - row]) #subtracts one to account for the fact that index starts at 0.
    
    return new_data

def horizontal_flip(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Flips the image horizontally by creating a new list, where every pixel in a row in the 'data'
list are in their opposite position relative to the center of the row.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        new_data (list): Updated 3D list of pixels and rows that replaces 'data'.
    """
    new_data = [] #empty list to be filled with new_row lists
    new_row = [] #empty list to be filled with new pixel lists
    
    #loops through row lists and appends new_row with new pixel lists
    for row in data:
        for pixel in range(0, len(row)):
            new_row.append(row[len(row) - 1 - pixel]) #subtracts one to account for the fact that index starts at 0.
        
        #appends new_row to new_data, and resets new_row list for each iteration of the loop.
        new_data.append(new_row)
        new_row = []

    return new_data

def rm_red(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Removes all red from the image by updating every pixel in 'data' so
the first integer in every pixel is 0.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through row lists and sets red pixel integers to 0.
    for row in data:
        for pixel in row:
            pixel[0] = 0

    return data

def rm_green(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Removes all green from the image by updating every pixel in 'data' so
the second integer in every pixel is 0.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through row lists and sets green pixel integers to 0.
    for row in data:
        for pixel in row:
            pixel[1] = 0

    return data

def rm_blue(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Removes all blue from the image by updating every pixel in 'data' so
the third integer in every pixel is 0.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through row lists and sets blue pixel integers to 0.
    for row in data:
        for pixel in row:
            pixel[2] = 0

    return data

def neg(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Negates the colors in the image by updating every pixel in 'data' so 
each integer is equal to 255 minus itself.
    
    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through pixel lists and sets all pixel integers to 255 minus themselves.
    for row in data:
        for pixel in row:
            for x in range(0, len(pixel)):
                pixel[x] = 255 - pixel[x]

    return data

def hicont(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Applies a high contrast to the iage by updating every pixel in 'data' so 
each integer is either 255, or 0, based on if it is greater than or less than 127.

    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through pixel lists and updates integer values
    for row in data:
        for pixel in row:
            for x in range(0, len(pixel)):
                
                #checks if integer value is greater than 127, and updates value appropriately.
                if pixel[x] > 127:
                    
                    pixel[x] = 255
                
                else: 
                    
                    pixel[x] = 0

    return data

def noise(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Adds radom noise to the image by updating every pixel in 'data' so 
each integer has a random number between -50 and 50 added to it.

    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through pixel lists and adds a random amount to integer values
    for row in data:
        for pixel in row:
            for x in range(0, len(pixel)):
                noise = random.randint(-50, 50)
                pixel[x] += noise #adds noise value to integer
                
                #prevents new integer values from being above 255 or below 0.
                if pixel[x] > 255:
                    
                    pixel[x] = 255
                
                elif pixel[x] < 0:
                    
                    pixel[x] = 0

    return data

def bw(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Applies a gray scale to the iage by updating every pixel in 'data' so 
each integer is the average of the three integers in a given pixel.

    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    #loops through row lists, and changes every integer in a pixel to be the average of its integers.
    for row in data:
        for pixel in row:
            average = sum(pixel) // len(pixel)
            pixel[0] = int(average)
            pixel[1] = int(average)
            pixel[2] = int(average)

    return data

def blur(data: list[list[list[int]]]) -> list[list[list[int]]]:
    """Applies a horizontal blur to the iage by updating every pixel in 'data' so
each red, green, and blue integers are the average of itself, and the integer values 
of the two pixels to its left, and the two pixels to its right (for edge cases, it takes the
average of either itself and the pixel to its left or right, or the average of itself 
and the one pixel to its left and right).

    Args: 
        
        data (list): 3D list of pixels and rows.
        
    Returns:
    
        data (list): Updated 3D list of pixels and rows.
    """
    sum_red, sum_green, sum_blue = 0, 0, 0 #starter sum values for computing averages
    
    #loops through pixel lists and changes every RGB integer to the average of itself and the surrounding 4 RGB integers.
    for row in range(0, len(data)):
        for pixel in range(2, len(data[row]) - 2):           
            for x in range(-2, 3): #loops through the previous two pixels and the two subsequent pixels   
                #sums integer values
                sum_red += data[row][pixel + x][0]
                sum_green += data[row][pixel + x][1]
                sum_blue += data[row][pixel + x][2]
            
            #appends each RGB integer with the averages
            data[row][pixel][0] = sum_red // 5
            data[row][pixel][1] = sum_green // 5
            data[row][pixel][2] = sum_blue // 5
            
            sum_red, sum_green, sum_blue = 0, 0, 0 #resets the RGB sums for each iteration of the loop.

        #edge case 0, loops through the subsequent pixel
        for pixel in range(0, 2):
            sum_red += data[row][pixel][0]
            sum_green += data[row][pixel][1]
            sum_blue += data[row][pixel][2]
        
        data[row][0][0] = sum_red // 2
        data[row][0][1] = sum_green // 2
        data[row][0][2] = sum_blue // 2

        sum_red, sum_green, sum_blue = 0, 0, 0 

        #edge case 1, loops through the previous and subsequent pixel.
        for pixel in range(0, 3):
            sum_red += data[row][pixel][0]
            sum_green += data[row][pixel][1]
            sum_blue += data[row][pixel][2]

        data[row][1][0] = sum_red // 3
        data[row][1][1] = sum_green // 3
        data[row][1][2] = sum_blue // 3

        sum_red, sum_green, sum_blue = 0, 0, 0


        #edge case -1, loops through the previous and subsequent pixel
        for pixel in range(len(data[row]) - 3, len(data[row])):
            sum_red += data[row][pixel][0]
            sum_green += data[row][pixel][1]
            sum_blue += data[row][pixel][2]

        data[row][len(data[row]) - 2][0] = sum_red // 3
        data[row][len(data[row]) - 2][1] = sum_green // 3
        data[row][len(data[row]) - 2][2] = sum_blue // 3

        sum_red, sum_green, sum_blue = 0, 0, 0


        #edge case -0, loops through the subsequent pixel.
        for pixel in range(len(data[row]) - 2, len(data[row])):

            sum_red += data[row][pixel][0]
            sum_green += data[row][pixel][1]
            sum_blue += data[row][pixel][2]

        data[row][len(data[row]) - 1][0] = sum_red // 2
        data[row][len(data[row]) - 1][1] = sum_green // 2
        data[row][len(data[row]) - 1][2] = sum_blue // 2

        sum_red, sum_green, sum_blue = 0, 0, 0
        
        # for pixel in range(len(data)-remainder, len(data), remainder):
        #     for x in range(0,remainder):
                
        #         sum_red += data[row][pixel+x][0]
        #         sum_green += data[row][pixel+x][1]
        #         sum_blue += data[row][pixel+x][2]

        #     for x in range(0,remainder):
                
        #         data[row][pixel+x][0] = sum_red//remainder
        #         data[row][pixel+x][1] = sum_green//remainder
        #         data[row][pixel+x][2] = sum_blue//remainder

            
    return data
            

def start_menu():
    """Starts the program, giving the user an option to input a filename, 
apply modifications to that file, or exit the program.
    """
    
    
    input_file = input("What image would you like to use? ") #accepts user input for filename.
    filename = input_file
    
    image_data = load_image_data(input_file) #converts file data to 3D list.
    
    #pints menu
    print("How would you like to edit your image?\n"
                        "\n"
                        "a) Flip the image vertically\n"
                        "b) Flip the image horizontally\n"
                        "c) Remove red\n"
                        "d) Remove green\n"
                        "e) Remove blue\n"
                        "f) Invert the colors\n"
                        "g) Apply a high contrast\n"
                        "h) Add random noise\n"
                        "i) Apply a gray scale\n"
                        "j) Apply a horizontal blur\n"
                        "k) Save and exit")
    
    exit_pgm = False #prevents program from closing.
    while exit_pgm == False:
        
        user_input = input("> ")
        
        #accepts user input and appropriately prints progress message, applies modifications, changes filename, and writes data to new file.
        if user_input == "a":
            print("Flipping vertically...")
            image_data = apply_modification(image_data, user_input)
            filename = filename.replace(".ppm", "") + "_vflip.ppm"
            write_image_data(image_data, filename)
        
        elif user_input == "b":
            print("Flipping horizontally...")
            filename = filename.replace(".ppm", "") + "_hflip.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "c":
            print("Removing red...")
            filename = filename.replace(".ppm", "") + "_rmred.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "d":
            print("Removing green...")
            filename = filename.replace(".ppm", "") + "_rmgreen.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "e":
            print("Removing blue...")
            filename = filename.replace(".ppm", "") + "_rmblue.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "f":
            print("Inverting colors...")
            filename = filename.replace(".ppm", "") + "_neg.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "g":
            print("Applying high contrast...")
            filename = filename.replace(".ppm", "") + "_hicont.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "h":
            print("Adding noise...")
            filename = filename.replace(".ppm", "") + "_noise.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "i":
            print("Applying gray scale...")
            filename = filename.replace(".ppm", "") + "_bw.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "j":
            print("Applying blur...")
            filename = filename.replace(".ppm", "") + "_blur.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        #exits program
        elif user_input == "k":
            print("Exiting program...")
            exit_pgm = True
        
        
        
start_menu()