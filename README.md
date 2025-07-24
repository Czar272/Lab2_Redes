# Laboratorio # 2 - Parte 1: Esquemas de detección y corrección de errores

## Redes

#### Cesar Lopez # 22535

## Ejemplo de funcionamiento del emisor Fletcher-16

Este ejemplo muestra paso a paso cómo se genera el checksum para una trama binaria utilizando el algoritmo Fletcher-16, incluyendo el padding, el cálculo de s1 y s2, y el resultado final.

---

### Trama de entrada

```
110100111011
```

- Longitud: 12 bits (faltan 4 bits entonces se le agregan padding como 0's)

```
110100111011 -> 11010011 10110000
```

- Byte 1: 11010011 = 211 (decimal)
- Byte 2: 10110000 = 176 (decimal)

### Calculo de checksum

```plaiantext
Inicial: s1 = 0, s2 = 0

Paso 1:
s1 = (0 + 211) % 255 = 211
s2 = (0 + 211) % 255 = 211

Paso 2:
s1 = (211 + 176) % 255 = 132
s2 = (211 + 132) % 255 = 88

```

- Resultado:
  - s1 = 132 -> 10000100 (binario)
  - s2 = 88 -> 01011000 (binario)

### Trama Final

- Trama original: 110100111011

- Checksum: 1000010001011000

```
1101001110111000010001011000
```
