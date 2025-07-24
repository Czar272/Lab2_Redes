def hamming_distance(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))

# Tabla de transiciones: (current_state, input_bit) → (next_state, output_bits)
transitions = {
    '00': {'0': ('00', '00'), '1': ('10', '11')},
    '01': {'0': ('00', '10'), '1': ('10', '01')},
    '10': {'0': ('01', '11'), '1': ('11', '00')},
    '11': {'0': ('01', '01'), '1': ('11', '10')}
}

def viterbi_decode(encoded_bits: str) -> str:
    # Inicializar caminos: {estado: (cost, path)}
    paths = {'00': (0, '')}

    for i in range(0, len(encoded_bits), 2):
        segment = encoded_bits[i:i+2]
        new_paths = {}

        for state, (cost, path) in paths.items():
            for bit_in in ['0', '1']:
                next_state, expected_out = transitions[state][bit_in]
                distance = hamming_distance(segment, expected_out)
                total_cost = cost + distance

                if next_state not in new_paths or total_cost < new_paths[next_state][0]:
                    new_paths[next_state] = (total_cost, path + bit_in)

        paths = new_paths

    # Buscar el camino con menor costo
    best_state = min(paths, key=lambda s: paths[s][0])
    best_cost, best_path = paths[best_state]

    print(f"Mejor estado final: {best_state}")
    print(f"Costo total (errores corregidos): {best_cost}")
    return best_path

if __name__ == "__main__":
    encoded = input("Ingrese la trama codificada de 2 bits por símbolo: ")
    decoded = viterbi_decode(encoded)
    print(f"Bits originales decodificados: {decoded}")
