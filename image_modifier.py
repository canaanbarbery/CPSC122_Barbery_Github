#Canaan Barbery
#1/28/2026
#CPSC 122 - Assignment 1
#This program takes an image file and can perform alterations to it, like flipping, rotating, and changing color.

def pretty_print(data):
    for row in data:
        print(row)

def load_image_data(image: str):
    row = []
    data = []
    x = 0
    with open(image, "r") as infile:
        for line in infile:
            line = line.strip()
            x += 1
            if x < 4:
                continue
            vals = line.split(" ")
            for i in range(len(vals)):
                vals[i] = int(vals[i])
            
            for i in range(0,len(vals), 3):
                red = vals[i]
                green = vals[i +1]
                blue = vals[i+2]
                pixel = [red,green,blue]
                row.append(pixel)
            data.append(row)
            row = []
        pretty_print(data)
    
    return data
            
def vertical_flip():

def start_menu():
    
    output_file = "new_image.ppm"
    # input_file = input("What image would you like to use? ")    
    input_file = "test.ppm"

    image_data = load_image_data(input_file)
    
    
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
    if user_input == "a":
       image_data = vertical_flip(image_data)
    
start_menu()