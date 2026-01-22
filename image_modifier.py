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
        filename = ("vflip_"+filename)
        print(filename)
        write_image_data(data, filename)
        
        

    
    return data, filename

def vertical_flip(data: list[list[list[int]]]):
    new_data = []
    rounds = 1
    for i in range(0,len(data)):
        for row in range(0,len(data)):
            if row == (len(data) - rounds):
                new_data.append(data[row])
                rounds += 1
    
    return new_data

def start_menu():
    exit_pgm = False
    # input_file = input("What image would you like to use? ")    
    image_file = "test.ppm"

    image_data = load_image_data(image_file)
    
    while exit_pgm != True:
        user_input = input("How would you like to edit your image?\n"
                        "\n"
                        "a) Flip the image vertically\n"
                        "b) Flip the image horizontally\n"
                        "c) Remove a primary color (red, green, blue)\n"
                        "d) Negate the colors\n"
                        "e) Apply a high contrast\n"
                        "f) Add random noise\n"
                        "g) Apply a gray scale\n"
                        "h) Apply a horizontal blur\n"
                        "i) Save and exit\n"
                        "\n"
                        "> ")
        
        if user_input == "i":
            write_image_data(image_data, image_file)
            print("Image saved.")
            exit_pgm = True
        apply_modification(user_input)
        
        
start_menu()