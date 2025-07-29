import base64 # library for base64 encoding

def encode_image(image_path):
    with open(image_path, "rb") as image_file: # Open the image file in binary mode
        return base64.b64encode(image_file.read()).decode('utf-8') # Encode the image to base64 and decode to string
