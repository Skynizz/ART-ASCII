from PIL import Image, ImageDraw, ImageFont
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def map_pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = np.array(image)
    pixels = (pixels / 255.0) * (len(ascii_chars) - 1)
    ascii_art = np.array([ascii_chars[int(pixel)] for pixel in pixels.flatten()])
    return "\n".join("".join(row) for row in ascii_art.reshape(pixels.shape))

def save_ascii_art_to_image(ascii_art, output_path, font_path="cour.ttf", font_size=10):
    lines = ascii_art.split("\n")
    width, height = max(len(line) for line in lines), len(lines)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    bbox = font.getbbox("A")
    char_width, char_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    image_width, image_height = width * char_width, height * char_height

    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    y = 0
    for line in lines:
        draw.text((0, y), line, font=font, fill="black")
        y += char_height

    image.save(output_path)

def save_ascii_art_to_text(ascii_art, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ascii_art)

image_path = input("Enter the image path :")
output_format = input("Save as (JPG/TXT)?").strip().lower()

ascii_art = map_pixels_to_ascii(grayscale_image(resize_image(Image.open(image_path))))

if output_format == "jpg":
    output_path = input("Enter the output file name (e.g., output.jpg) :  ")
    save_ascii_art_to_image(ascii_art, output_path)
    print(f"ASCII art saved as {output_path}")
elif output_format == "txt":
    output_path = input("Enter the output file name (e.g., output.txt):  ")
    save_ascii_art_to_text(ascii_art, output_path)
    print(f"ASCII art saved as {output_path}")
else:
    print("Invalid format. Please choose JPG or TXT.")
