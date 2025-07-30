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