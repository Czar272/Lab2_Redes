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

# Algoritmos de Deteccion de errores

## Emisor Fletcher-Checksum (Fletcher-16 sobre bloques de 8 bits)

### Descripcion

- Toma una trama de bits y la divide en bytes (bloques de 8 bits).

- Calcula dos valores de suma:

  - s1: suma acumulativa de los bytes

  - s2: suma acumulativa de los s1

- Ambas sumas se hacen módulo 255.

- El resultado (s1 y s2) se codifica como 16 bits adicionales que se agregan al final de la trama.

### Ejemplo 10110011:

1. Entrada: 10110011

   - Byte: 179
   - s1 = 179
   - s2 = 179

2. Checksum generado:

   - s1 = 179 → 10110011

   - s2 = 179 → 10110011

```
Trama original: 10110011
Trama con checksum: 101100111011001110110011
```

## Receptor Fletcher-Checksum (Verificación con s1 y s2)

### Descripcion

- Extrae los últimos 16 bits como s1 y s2 recibidos.

- Vuelve a calcular s1 y s2 con los bits de datos recibidos (excluyendo el checksum).

- Si ambos valores coinciden exactamente, la trama se acepta como válida.

- Si hay una diferencia, se detecta un error y la trama se descarta.

### Funcionamiento

- Verifica si los valores de suma acumulada (s1, s2) coinciden con los esperados.

- Si se cambia 1 bit, normalmente s1 o s2 no coinciden → se detecta el error.

- Sin embargo, si se cambian múltiples bits con un efecto "balanceado", puede que el error no se detecte.

```
Trama recibida (válida):     101100111011001110110011
Trama recibida (con error):  101100111111001110110011
Resultado: Error detectado

```
