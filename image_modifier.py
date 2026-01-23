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
        
    # elif mod == "c":
     

    # elif mod == "d":
        
    

    # elif mod == "e":
        
   
    
    # elif mod == "f":
        
       
    
    # elif mod == "g":
        
        
    
    # elif mod == "h":
        
   
    
    # elif mod == "i":
        
     
    
    # elif mod == "j":
        
        
        

    
    return data 

def vertical_flip(data: list[list[list[int]]]):
    new_data = []
    for i in range(0,len(data)):
        new_data.append(data[len(data)-1-i])
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
            filename = "vflip_" + filename
            write_image_data(image_data, filename)
        
        elif user_input == "b":
            
            filename = ("hflip_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "c":
            
            filename = ("rmred_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "d":
            
            filename = ("rmgreen_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)

        elif user_input == "e":
            
            filename = ("rmblue_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "f":
            
            filename = ("neg_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "g":
            
            filename = ("hcont_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "h":
            
            filename = ("noise_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "i":
            
            filename = ("bw_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "j":
            
            filename = ("blur_"+filename)
            image_data = apply_modification(image_data, user_input)
            write_image_data(image_data, filename)
        
        elif user_input == "k":
            print("Exiting program...")
            exit_pgm = True
        
        
        
start_menu()