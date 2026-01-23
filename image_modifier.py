#Canaan Barbery
#1/28/2026
#CPSC 122 - Assignment 1
#This program takes an image file and can perform alterations to it, like flipping, rotating, and changing color.

def pretty_print(data):
    for row in data:
        print(row)

def load_image_data(filename: str):
    row = []
    data = []
    x = 0
    with open(filename, "r") as infile:
        for line in infile:
            line = line.strip()
            x += 1
            if x < 4:
                continue
            vals = line.split(" ")
            
            for i in range(0,len(vals), 3):
                red = int(vals[i])
                green = int(vals[i + 1])
                blue = int(vals[i + 2])
                pixel = [red,green,blue]
                row.append(pixel)
            data.append(row)
            row = []

    return data 

def write_image_data(data: list[list[list[int]]], filename: str):
    
    with open(filename, "w") as outfile:
        for row in data:
            for pixel in row:
                for x in pixel:
                    x = str(x)
                    outfile.write(x+" ")
            outfile.write("\n")


def apply_modification(data: list[list[list[int]]], mod: str):
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
    
    # elif mod == "f":
        
       
    
    # elif mod == "g":
        
        
    
    # elif mod == "h":
        
   
    
    elif mod == "i":
        
        data = bw(data)
    
    # elif mod == "j":
        
        
        

    
    return data 

def vertical_flip(data: list[list[list[int]]]):
    new_data = []
    for row in range(0,len(data)):
        new_data.append(data[len(data)-1-row])
    pretty_print(new_data)
    return new_data

def horizontal_flip(data: list[list[list[int]]]):
    new_data = []
    new_row = []
    for row in range(0,len(data)):
        for pixel in range(0, len(data[row])):
            new_row.append(data[row][len(data[row])-1-pixel])
        new_data.append(new_row)
        new_row = []
    pretty_print(new_data)

    return new_data

def rm_red(data: list[list[list[int]]]):
    
    for row in data:
        for pixel in row:
            pixel[0] = 0
    pretty_print(data)

    return data

def rm_green(data: list[list[list[int]]]):

    for row in data:
        for pixel in row:
            pixel[2] = 0
    pretty_print(data)

    return data

def rm_blue(data: list[list[list[int]]]):

    for row in data:
        for pixel in row:
            pixel[1] = 0
    pretty_print(data)

    return data

def bw(data: list[list[list[int]]]):

    for row in data:
        for pixel in row:
            average = sum(pixel)/len(pixel)
            pixel[0] = int(average)
            pixel[1] = int(average)
            pixel[2] = int(average)

    return data

def start_menu():
    exit_pgm = False
    # input_file = input("What image would you like to use? ")     
    
    input_file = "test.ppm"
    filename = input_file

    image_data = load_image_data(input_file)
    pretty_print(image_data)
    while exit_pgm != True:
        user_input = input("How would you like to edit your image?\n"
                        "\n"
                        "a) Flip the image vertically\n"
                        "b) Flip the image horizontally\n"
                        "c) Remove red\n"
                        "d) Remove green\n"
                        "e) Remove blue\n"
                        "f) Negate the colors\n"
                        "g) Apply a high contrast\n"
                        "h) Add random noise\n"
                        "i) Apply a gray scale\n"
                        "j) Apply a horizontal blur\n"
                        "k) Save and exit\n"
                        "\n"
                        "> ")
        
        if user_input == "a":
            
            image_data = apply_modification(image_data, user_input)
            filename = filename.replace(".ppm","") + "_vflip.ppm"
            write_image_data(image_data, filename)
        
        elif user_input == "b":
            
            filename = filename.replace(".ppm","") + "_hflip.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "c":
            
            filename = filename.replace(".ppm","") + "_rmred.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "d":
            
            filename = filename.replace(".ppm","") + "_rmgreen.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "e":
            
            filename = filename.replace(".ppm","") + "_rmblue.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "f":
            
            filename = filename.replace(".ppm","") + "_neg.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "g":
            
            filename = filename.replace(".ppm","") + "_hicont.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "h":
            
            filename = filename.replace(".ppm","") + "_noise.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "i":
            
            filename = filename.replace(".ppm","") + "_bw.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "j":
            
            filename = filename.replace(".ppm","") + "_blur.ppm"
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "k":
            print("Exiting program...")
            exit_pgm = True
        
        
        
start_menu()