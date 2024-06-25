# from PIL import Image, ImageDraw, ImageFont

# def create_meme(image_path, text, output_path='meme.jpg'):
#     try:
#         # Open the image file
#         img = Image.open(image_path)
        
#         # Initialize drawing context
#         draw = ImageDraw.Draw(img)
        
#         # Load a font
#         font = ImageFont.truetype("arial.ttf", 40)
        
#         # Calculate text size
#         textwidth, textheight = draw.textbbox((0, 0), text, font=font)[2:]
        
#         # Calculate text position
#         width, height = img.size
#         x = (width - textwidth) / 2
#         y = height - textheight - 10
        
#         # Add text to image
#         draw.text((x, y), text, font=font, fill=(255, 255, 255))
        
#         # Save and show the final meme
#         img.save(output_path)
#         img.show()
    
#     except FileNotFoundError:
#         print(f"Error: Image file '{image_path}' not found.")
    
#     except Exception as e:
#         print(f"Error: An unexpected error occurred - {e}")

# # Example usage
# create_meme(r'C:\Users\dcl\OneDrive\Desktop\web projec\MemeProject\my_image.jpg', "When you finally understand NumPy")

 







# import os
# import random
# from PIL import Image, ImageDraw, ImageFont

# class MemeGenerator:
#     def __init__(self, font_path, font_size=40):
#         self.font_path = font_path
#         self.font_size = font_size
#         self.font = ImageFont.truetype(font_path, font_size)

#     def generate_meme(self, image_path, top_text, bottom_text, output_path):
#         try:
#             # Open the image file
#             img = Image.open(image_path)

#             # Initialize drawing context
#             draw = ImageDraw.Draw(img)

#             # Calculate text sizes
#             top_text_width, top_text_height = draw.textbbox((0, 0), top_text, font=self.font)[2:]
#             bottom_text_width, bottom_text_height = draw.textbbox((0, 0), bottom_text, font=self.font)[2:]

#             # Calculate text positions
#             width, height = img.size
#             top_x = (width - top_text_width) / 2
#             bottom_x = (width - bottom_text_width) / 2

#             # Optionally vary vertical positions randomly for fun
#             top_y = 10
#             bottom_y = height - bottom_text_height - 10

#             # Add text to image with shadow effect
#             shadow_offset = 2
#             shadow_color = "black"
#             draw.text((top_x - shadow_offset, top_y - shadow_offset), top_text, font=self.font, fill=shadow_color)
#             draw.text((bottom_x - shadow_offset, bottom_y - shadow_offset), bottom_text, font=self.font, fill=shadow_color)
            
#             # Generate random text color (bright colors)
#             text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#             draw.text((top_x, top_y), top_text, font=self.font, fill=text_color)
#             draw.text((bottom_x, bottom_y), bottom_text, font=self.font, fill=text_color)

#             # Save the meme
#             img.save(output_path)

#             print(f"Meme generated successfully! Saved to {output_path}")

#         except FileNotFoundError:
#             print(f"Error: Image file '{image_path}' not found.")

#         except Exception as e:
#             print(f"Error: An unexpected error occurred - {e}")

# if __name__ == "__main__":
#     # Set font path and size
#     font_path = "arial.ttf"
#     font_size = 40

#     # Create a MemeGenerator instance
#     meme_generator = MemeGenerator(font_path, font_size)

#     # Generate a meme
#     image_path = "my_image.jpg"
#     top_text = "When you finally understand NumPy"
#     bottom_text = "But then you realize you still don't understand NumPy"
#     output_path = "meme.jpg"
#     meme_generator.generate_meme(image_path, top_text, bottom_text, output_path)


import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class MemeGenerator:
    def __init__(self, font_path, font_size=40):
        self.font_path = font_path
        self.font_size = font_size
        self.font = ImageFont.truetype(font_path, font_size)
        self.face_emojis = self.load_face_emojis()  # Load face expression images

    def load_face_emojis(self):
        # Load face emojis from a directory
        face_emojis_dir = "face_emojis"
        face_emojis = []
        if not os.path.exists(face_emojis_dir):
            os.makedirs(face_emojis_dir)
        for filename in os.listdir(face_emojis_dir):
            if filename.endswith(".png"):
                emoji_path = os.path.join(face_emojis_dir, filename)
                emoji_img = Image.open(emoji_path)
                face_emojis.append(emoji_img)
        return face_emojis

    def overlay_face_emoji(self, img, emoji_img, position):
        # Resize emoji image proportionally to fit 1/4th of the main image
        emoji_width = min(img.width // 4, emoji_img.width)
        emoji_height = emoji_img.height * emoji_width // emoji_img.width
        emoji_img = emoji_img.resize((emoji_width, emoji_height), Image.LANCZOS)

        # Calculate position based on provided position tuple (x, y)
        x, y = position
        img.paste(emoji_img, (x, y), emoji_img)

    def generate_meme(self, image_path, top_text, bottom_text, output_path):
        try:
            # Open the image file
            img = Image.open(image_path)

            # Initialize drawing context
            draw = ImageDraw.Draw(img)

            # Apply blur effect to the image
            img = self.apply_blur_effect(img)

            # Calculate text sizes
            top_text_width, top_text_height = draw.textbbox((0, 0), top_text, font=self.font)[2:]
            bottom_text_width, bottom_text_height = draw.textbbox((0, 0), bottom_text, font=self.font)[2:]

            # Calculate text positions
            width, height = img.size
            top_x = (width - top_text_width) / 2
            bottom_x = (width - bottom_text_width) / 2

            # Optionally vary vertical positions randomly for fun
            top_y = 10
            bottom_y = height - bottom_text_height - 10

            # Add text to image with shadow effect
            shadow_offset = 2
            shadow_color = "black"
            draw.text((top_x - shadow_offset, top_y - shadow_offset), top_text, font=self.font, fill=shadow_color)
            draw.text((bottom_x - shadow_offset, bottom_y - shadow_offset), bottom_text, font=self.font, fill=shadow_color)
            
            # Generate random text color (bright colors)
            text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.text((top_x, top_y), top_text, font=self.font, fill=text_color)
            draw.text((bottom_x, bottom_y), bottom_text, font=self.font, fill=text_color)

            # Overlay a random face emoji
            if self.face_emojis:
                emoji_img = random.choice(self.face_emojis)
                emoji_position = (random.randint(0, width - emoji_img.width), random.randint(0, height - emoji_img.height))
                self.overlay_face_emoji(img, emoji_img, emoji_position)

            # Save the meme
            img.save(output_path)

            print(f"Meme generated successfully! Saved to {output_path}")

        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

    def apply_blur_effect(self, img):
        # Apply a blur effect to the image
        blurred_img = img.filter(ImageFilter.BLUR)
        return blurred_img

    def generate_batch_memes(self, image_paths, text_list, output_folder):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for i, image_path in enumerate(image_paths):
            if os.path.isfile(image_path):
                output_path = os.path.join(output_folder, f"meme_{i}.jpg")
                top_text = text_list[i % len(text_list)]  # Cycling through a list of texts
                bottom_text = "Your custom bottom text here"
                self.generate_meme(image_path, top_text, bottom_text, output_path)
            else:
                print(f"Error: Image file '{image_path}' not found.")

if __name__ == "__main__":
    # Set font path and size
    font_path = "arial.ttf"
    font_size = 40

    # Create a MemeGenerator instance
    meme_generator = MemeGenerator(font_path, font_size)

    # Generate a meme
    image_path = "my_image.jpg"
    top_text = "marr me"
    bottom_text = "NumPy"
    output_path = "meme.jpg"
    meme_generator.generate_meme(image_path, top_text, bottom_text, output_path)

    # Example of batch meme generation
    image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]
    text_list = ["Text for image 1", "Text for image 2", "Text for image 3"]
    output_folder = "batch_memes"
    meme_generator.generate_batch_memes(image_paths, text_list, output_folder)
