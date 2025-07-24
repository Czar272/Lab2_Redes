#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<int> encode_convolutional(const string& input) {
    vector<int> output;
    int reg[3] = {0, 0, 0}; // shift register initialized to 0

    for (char bit : input) {
        int in_bit = bit - '0';

        // Shift register: reg[2] <- reg[1], reg[1] <- reg[0], reg[0] <- in_bit
        reg[2] = reg[1];
        reg[1] = reg[0];
        reg[0] = in_bit;

        // G1 = 111 → XOR(reg[0], reg[1], reg[2])
        int out1 = reg[0] ^ reg[1] ^ reg[2];

        // G2 = 101 → XOR(reg[0], reg[2])
        int out2 = reg[0] ^ reg[2];

        output.push_back(out1);
        output.push_back(out2);
    }

    return output;
}

int main() {
    string input_bits;
    cout << "Ingrese la trama binaria a codificar: ";
    cin >> input_bits;

    vector<int> encoded = encode_convolutional(input_bits);

    cout << "Trama codificada: ";
    for (int bit : encoded) {
        cout << bit;
    }
    cout << endl;

    return 0;
}