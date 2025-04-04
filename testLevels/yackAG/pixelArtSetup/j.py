from PIL import Image

def clamp(num, min, max):
    if num >= max:
        return max
    elif num <= min:
        return min
    else:
        return num

def image_to_ascii(image_path, width=80):
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * width)
    image = image.resize((width, new_height))

    pixels = image.getdata()
    chars = ['x','.']  # ASCII characters for different brightness levels
    ascii_image_str = ''
    ascii_image = []

    for pixel in pixels:
        brightness = pixel // 85
        ascii_image_str += chars[clamp(brightness, 0,1)]

    ascii_image_str = ('\n'.join(ascii_image_str[i:(i + width)] for i in range(0, len(ascii_image_str), width)))

    temp = ''
    for str in ascii_image_str:
        if str == '\n':
            ascii_image.append(temp)
            temp = ''
        else:
            temp += str

    ascii_image.append(temp)
    return ascii_image

print(image_to_ascii('troll.png'))