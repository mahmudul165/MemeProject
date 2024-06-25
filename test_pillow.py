from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
img = Image.new('RGB', (200, 100), color='white')

# Initialize ImageDraw object
draw = ImageDraw.Draw(img)

# Draw text on the image
text = "Hello, Pillow!"
font = ImageFont.truetype("arial.ttf", size=20)
draw.text((10, 10), text, font=font, fill='black')

# Save and display the image
img.save('test_image.png')
img.show()
