import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
from image_utils import encode_image

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def describe_image(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un asistente que genera títulos y descripciones para productos de una joyería online. "
                    "Esta tienda transmite elegancia y lujo. Todas las piedras son de fantasía de alta calidad. "
                    "Tu estilo debe ser refinado, persuasivo y emocional para atraer a compradores que valoran el diseño exclusivo."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Genera el siguiente contenido a partir de la imagen del producto:\n"
                            "- Un título atractivo (máx 10 palabras)\n"
                            "- Una descripción corta (1 frase vendedora)\n"
                            "- Una descripción larga (3–4 frases, enfatiza lujo, elegancia y materiales de calidad)\n\n"
                            "Materiales: metal dorado, cristales de fantasía."
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