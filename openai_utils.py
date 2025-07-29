import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from image_utils import encode_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def describe_image(image_path, sku_info_text=""):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente que genera títulos y descripciones para productos de joyería basados en el diseño de las imagenes que recibes, tu proposito es generar contenido que incite a la persona a comprar el producto "
                    "Tu estilo es elegante, persuasivo y refinado."
                    "Solo debes de usar los recursos que te doy, no debes de inventar nada, si no tienes información suficiente para generar un título o descripción, simplemente déjalo en blanco."
                    "De momento todos los productos contienen piedras de circonia, por lo que no debes de mencionar ninguna piedra preciosa como diamantes, esmeraldas o similares."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            f"Basado en el diseño de la imagen y detalles del producto:\n"
                            f"{sku_info_text}\n\n"
                            "Devuélveme lo siguiente:\n"
                            "- Un título atractivo basado unicamente en el diseño que se ve en la imagen (máx 15 palabras)\n"
                            "- Una descripción corta (1-2 frases vendedoras)\n"
                            "- Una descripción larga (3–4 frases)\n\n"
                            "Responde en el siguiente formato (sin etiquetas):\n"
                            "Título:\n<texto>\n\nDescripción corta:\n<texto>\n\nDescripción larga:\n<texto>"
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    }
                ]
            }
        ],
        max_tokens=1000,
    )
    return response.choices[0].message.content