def hamming_distance(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))

# Tabla de transiciones: (current_state, input_bit) → (next_state, output_bits)
def generate_transitions():
    transitions = {}
    for reg1 in [0, 1]:
        for reg2 in [0, 1]:
            state = f"{reg1}{reg2}"
            transitions[state] = {}
            for input_bit in [0, 1]:
                reg = [input_bit, reg1, reg2]
                out1 = reg[0] ^ reg[1] ^ reg[2]  # G1 = 111
                out2 = reg[0] ^ reg[2]          # G2 = 101
                next_state = f"{reg[0]}{reg[1]}"
                output_bits = f"{out1}{out2}"
                transitions[state][str(input_bit)] = (next_state, output_bits)
    return transitions

transitions = generate_transitions()



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
