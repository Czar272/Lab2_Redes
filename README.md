# Laboratorio # 2 - Parte 1: Esquemas de detección y corrección de errores

## Redes

#### Cesar Lopez # 22535

#### **_Reporte_**: [Link al reporte](https://uvggt-my.sharepoint.com/:w:/r/personal/lop22535_uvg_edu_gt/Documents/Lab2.1%20-%20Esquemas%20de%20deteccio%CC%81n%20y%20correccio%CC%81n%20de%20errores.docx?d=w8e60467a9aa54320acfac1c27e24475e&csf=1&web=1&e=NWTpG2)

# Algoritmos de Corrección de errores

## Emisor Viterbi (Codificador convolucional tipo (2,1,3))

### Descripcion

- Por cada bit de entrada, genera 2 bits de salida con redundancia.

- Utiliza 3 registros de desplazamiento (memoria de 2 bits).

- Polinomios generadores:

  - G1 = 111 → XOR de los 3 registros

  - G2 = 101 → XOR del primero y el tercero

### Ejemplo 1011:

1. Entrada: 1

   - Registros: [1,0,0]
   - G1 = 1-0-0 = 1
   - G2 = 1-0 = 1 → salida: 11

2. Entrada: 0

   - Registros: [0,1,0]
   - G1 = 0-1-0 = 1
   - G2 = 0-0 = 0 → salida: 10

3. Entrada: 1

   - Registros: [1,0,1]
   - G1 = 1-0-1 = 0
   - G2 = 1-1 = 0 → salida: 00

4. Entrada: 1
   - Registros: [1,1,0]
   - G1 = 1-1-0 = 0
   - G2 = 1-0 = 1 → salida: 01

```
Entrada original: 1011
Salida codificada: 11100001
```

## Receptor Viterbi (Decodificador con corrección)

### Descripcion

- Reconstruye la secuencia original aunque existan errores.

- Usa una tabla de transiciones basada en los estados posibles de los registros.

- Aplica el algoritmo de Viterbi para encontrar el camino de menor costo (distancia de Hamming) entre todos los caminos posibles.

### Funcionamiento

- Cada estado se representa como los 2 bits de memoria.

- Por cada entrada posible (0 y 1), se genera un estado siguiente y una salida esperada.

- Se construye un árbol de caminos y se calcula el costo de desviación (errores).

- Al final, se elige el camino con menor número de errores detectados.

```
Entrada (salida del emisor):  11110001 <- un bit cambiado
Salida: 1011
```
