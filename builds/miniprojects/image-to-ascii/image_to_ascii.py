from PIL import Image

# ASCII characters used to represent pixel brightness
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # 0.55 adjusts for font height
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def image_to_ascii(image_path, new_width=100, output_file=None):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    pixel_count = len(ascii_str)
    ascii_image = "\n".join([ascii_str[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
    
    if output_file:
        with open(output_file, "w") as f:
            f.write(ascii_image)
        print(f"ASCII art saved to {output_file}")
    else:
        print(ascii_image)

# Example usage:
image_path = r"C:\Users\Hp\Desktop\workspace\projects\image-to-ascii\white-bear.png"
image_to_ascii(image_path, new_width=120, output_file="ascii_art.txt")
