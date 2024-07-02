import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont
from pathlib import Path

def generate_random_string(length):
    random_string = ""
    for i in range(0,length):
        random_string = random_string + random.choice('123456789ABCDEFGHIJKLMNOPQRSTUVWQXYZ')
    return random_string

def draw_random_ellipse(draw):
    # A random circle on the image
    a = random.randrange(10, 300, 1)
    b = random.randrange(10, 275, 1)
    c = a + random.randrange(10, 90, 1)
    d = b + random.randrange(10, 90, 1)
    draw.ellipse((a,b,c,d), fill=(default_color_red + random.randrange(-100,100,1), 
                                  default_color_green + random.randrange(-100,100,1), 
                                  default_color_blue + random.randrange(-100,100,1), 255), 
                                  outline = "black")

def generate_captcha(path_font, width=180, height=40, bg_color="white"):
    
    captcha_string = generate_random_string(6)
    # print(">" + captcha_string + "<")
    captcha_image = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(captcha_image, "RGBA")
    # for i in range(1,20):
    #     draw_random_ellipse(draw)
    draw_random_lines(draw, width, height)
    fontStyle = ImageFont.truetype(path_font, 25) # font must be in the same folder as the .py file. 

    # Arbitrary starting co-ordinates for the text we will write
    x = 12 + random.randrange(0, 5, 1)
    y = 4
    multiplicador = 1
    for letter in captcha_string:
        #print(letter)
        draw.text((x, y), letter, (0,0,0), font=fontStyle)    # Write in black
        x = x + 28
        y = 6 + random.randrange(1, 7, 1) * multiplicador
        multiplicador = multiplicador * (-1)
    return captcha_image, captcha_string  # return a heterogeneous tuple

def draw_random_lines(draw, width, height, color="black", line_count=1):
    for _ in range(line_count):
        # definir coordenadas de lineas
        off_width = random.randint(-9, 9)
        off_height = 10 + random.randint(5, 10)
        width_line = width - off_width if off_width > 0 else -(off_width)
        off_width = random.randint(-9, 9)
        off_height = 10 + random.randint(5, 10)
        height_line = height - off_height if off_width > 0 else off_height
        
        start_point = (width_line, height_line)
        end_point = (width-width_line, height-height_line)
        draw.line([start_point, end_point], fill=color, width=1)

def save_generated(image_dir, array_font, cantidad=10000):
    j = 0
    for i in range(1, cantidad+1, 1):
        if (i % 40000) == 0:
            j = j + 1
        image, label = generate_captcha(array_font[j])
        image_path = image_dir + f"{label}_{i+1}.png"
        image.save(image_path)

# Parámetros
total_images = 80000
output_directory = "DataGenerated/"
font_path = "Complementos/TNR Extra Bold.ttf" # Reemplaza esto con la ruta a tu archivo de fuente
font_array = ["Complementos/TNR Extra Bold.ttf", "Complementos/Sabon Bold.ttf", "Complementos/Cambria Bold.ttf"]
# Colores de objetos que dificultan la imagen
default_color_red = 228
default_color_green = 150
default_color_blue = 150

# Genera las imágenes CAPTCHA
save_generated(output_directory, font_array, total_images)