from PIL import Image

# Load image
image = Image.open("./Simpson holding Bible.jpg")

# Resize
image = image.resize((180, 150))

# Convert to grayscale
image = image.convert("L")

# ASCII characters
chars = "@%#*+=-:. "
#chars = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Convert pixels to ASCII
pixels = image.get_flattened_data()
ascii_str = ""

for pixel in pixels:
    index = pixel * len(chars) // 256
    ascii_str += chars[index]

# Format output
width = image.width
ascii_img = ""

for i in range(0, len(ascii_str), width):
    ascii_img += ascii_str[i:i+width] + "\n"

# Print result
print(ascii_img)

# Save to file
with open("ascii.txt", "w") as f:
    f.write(ascii_img)