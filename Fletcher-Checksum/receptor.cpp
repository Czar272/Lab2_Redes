#include <iostream>
#include <vector>
#include <string>
#include <bitset>

using namespace std;

// Convierte una cadena binaria en vector de bytes (8 bits)
vector<int> binStringToBytes(string bits) {
    while (bits.length() % 8 != 0)
        bits += "0";

    vector<int> bytes;
    for (size_t i = 0; i < bits.length(); i += 8) {
        string byteStr = bits.substr(i, 8);
        int byteVal = stoi(byteStr, nullptr, 2);
        bytes.push_back(byteVal);
    }
    return bytes;
}

// Calcula el checksum Fletcher-16
pair<int, int> fletcher16(const vector<int>& data) {
    int s1 = 0, s2 = 0;
    for (int byte : data) {
        s1 = (s1 + byte) % 255;
        s2 = (s2 + s1) % 255;
    }
    return {s1, s2};
}

// Extrae los últimos 16 bits como s1 y s2
pair<int, int> extractChecksum(string bits) {
    string s1_str = bits.substr(bits.length() - 16, 8);
    string s2_str = bits.substr(bits.length() - 8, 8);
    int s1 = stoi(s1_str, nullptr, 2);
    int s2 = stoi(s2_str, nullptr, 2);
    return {s1, s2};
}

int main() {
    string received;
    cout << "Ingrese la trama recibida (datos + checksum): ";
    cin >> received;

    if (received.length() < 16) {
        cout << "Error: Trama demasiado corta para contener un checksum válido." << endl;
        return 1;
    }

    string dataBits = received.substr(0, received.length() - 16);
    pair<int, int> expected = extractChecksum(received);
    vector<int> dataBytes = binStringToBytes(dataBits);
    pair<int, int> computed = fletcher16(dataBytes);

    if (expected == computed) {
        cout << "Trama valida. No se detectaron errores." << endl;
        cout << "Trama original: " << dataBits << endl;
    } else {
        cout << "Error detectado. La trama se descarta." << endl;
        cout << "Checksum esperado: s1 = " << expected.first << ", s2 = " << expected.second << endl;
        cout << "Checksum calculado: s1 = " << computed.first << ", s2 = " << computed.second << endl;
    }

    return 0;
}
