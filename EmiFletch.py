# s1 = sum(bytes) % 255
# s2 = sum acumulativa de s1 % 255


def pad_to_bytes(bits: str) -> list[int]:
    # Rellena a múltiplos de 8
    while len(bits) % 8 != 0:
        bits += '0'
    return [int(bits[i:i+8], 2) for i in range(0, len(bits), 8)]

def fletcher16(data: list[int]) -> tuple[int, int]:
    s1 = 0
    s2 = 0
    for byte in data:
        s1 = (s1 + byte) % 255
        s2 = (s2 + s1) % 255
    return s1, s2

def emisor_fletcher(bits: str) -> str:
    data_bytes = pad_to_bytes(bits)
    s1, s2 = fletcher16(data_bytes)
    # Añadir s1 y s2 como 8 bits cada uno al final
    checksum = f'{s1:08b}{s2:08b}'
    return bits + checksum

if __name__ == "__main__":
    bits = input("Ingrese la trama en binario: ")
    trama_final = emisor_fletcher(bits)
    print(f"Trama emitida con checksum: {trama_final}")


# Ejemplo: 
# Ingresamos 110100111011 (Le faltan 4 bits para completar 2 bytes 16 bits)
# Se le agregará padding con ceros al final para formar 16 bits:
# 110100111011 -> 11010011 10110000
# Byte 1: 11010011 = 211 (decimal)
# Byte 2: 10110000 = 176 (decimal)
# s1 = (0 + 211) % 255 = 211
# s2 = (0 + 211) % 255 = 211

# s1 = (211 + 176) % 255 = 132
# s2 = (211 + 132) % 255 = 88

# s1 = 132 -> 10000100 (binario)
# s2 = 88-> 01011000 (binario)

# Trama original: 110100111011
# Checksum: 1000010001011000

# Final:
# 1101001110111000010001011000
