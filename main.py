from openai_utils import describe_image
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
    )
    return file_path

if __name__ == "__main__":
    image_path = choose_file()
    if image_path:
        result = describe_image(image_path)
        print(result)
    else:
        print("No file selected.")
