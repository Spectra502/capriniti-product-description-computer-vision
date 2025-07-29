import os
import csv
from tkinter import Tk, filedialog
from openai_utils import describe_image
from decode_sku import decode_sku  

def parse_description_response(response: str):
    try:
        parts = response.strip().split("Descripción corta:")
        title = parts[0].replace("Título:", "").strip()
        short, long = parts[1].split("Descripción larga:")
        return title, short.strip(), long.strip()
    except:
        return "", "", ""

def choose_folder():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select a folder with product images")

def generate_csv(rows, output_path):
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["SKU", "Nombre", "Descripción corta", "Descripción"])
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def main():
    folder_path = choose_folder()
    if not folder_path:
        print("No folder selected.")
        return

    results = []
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue

        sku = os.path.splitext(filename)[0]
        image_path = os.path.join(folder_path, filename)
        sku_info = decode_sku(sku)

        # Compose custom prompt
        prompt_info = ", ".join(f"{k}: {v}" for k, v in sku_info.items())
        result = describe_image(image_path, prompt_info)  # <- we'll modify describe_image

        # Expecting a structured response
        title, short, long = parse_description_response(result)
        base_sku = "-".join(sku.split("-")[:-1])
        results.append({
            "SKU": base_sku,
            "Nombre": title,
            "Descripción corta": short,
            "Descripción": long
        })

    output_csv = os.path.join(folder_path, "descriptions.csv")
    generate_csv(results, output_csv)
    print(f"CSV saved at: {output_csv}")

if __name__ == "__main__":
    main()