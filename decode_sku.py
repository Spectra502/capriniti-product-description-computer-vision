import re

def decode_sku(sku: str) -> dict:
    parts = sku.split('-')

    # Lookup maps
    material_map = {"AU": "oro", "AG": "plata .925", "CH": "chapa de oro", "AI": "acero inoxidable"}
    origin_map = {"MX": "mexico", "IT": "italia"}
    purity_map = {"10K": "10 quilates", "14K": "14 quilates", "18K": "18 quilates", "925": "plata .925"}
    coating_map = {"NO": "sin baño", "RH": "baño de rodio", "OR": "baño de oro rosa", "YG": "baño de oro amarillo", "WG": "baño de oro blanco"}
    category_map = {"AR": "aretes", "BR": "broqueles", "PU": "pulsera", "AN": "anillo", "DI": "dije", "CO": "collar", "SE": "set"}
    gender_map = {"H": "hombre", "M": "mujer", "U": "unisex", "I": "infantil"}
    usage_map = {"D": "uso diario", "E": "uso elegante", "R": "uso religioso"}
    religious_map = {"CR": "cruz", "VG": "Virgen", "SJ": "San Judas", "OM": "otro motivo religioso"}

    decoded = {}
    for part in parts:
        if part in material_map:
            decoded["material"] = material_map[part]
        elif part in origin_map:
            decoded["origen"] = origin_map[part]
        elif part in purity_map:
            decoded["quilataje"] = purity_map[part]
        elif part in coating_map:
            decoded["baño"] = coating_map[part]
        elif part in category_map:
            decoded["categoría"] = category_map[part]
        elif part in gender_map:
            decoded["género"] = gender_map[part]
        elif part in usage_map:
            decoded["uso"] = usage_map[part]
        elif part in religious_map:
            decoded["motivo_religioso"] = religious_map[part]
        """"
        elif re.fullmatch(r"\d{2}", part):  # ring size
            decoded["talla_anillo"] = part
        elif re.fullmatch(r"L\d{2}", part):  # length
            decoded["longitud"] = f"{part[1:]} cm"
        elif re.fullmatch(r"G\d+(\.\d+)?", part):  # weight
            decoded["peso"] = f"{part[1:]} g"
        elif re.fullmatch(r"PR\d+", part):  # provider
            decoded["proveedor"] = f"Proveedor {part[2:]}"
        elif re.fullmatch(r"\d{3}", part):  # model number
            decoded["modelo"] = part
        else:
            decoded.setdefault("otros", []).append(part)
        """
    return decoded

def main():
    sku = "CH-18K-AR-M-D-AR-010-01"
    result = decode_sku(sku)
    print("Resultado del SKU:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()