# Generador de Fractales de Mandelbrot y Julia

Visualización de conjuntos fractales utilizando Python, NumPy y Matplotlib.

## Descripción

Este proyecto genera imágenes de alta resolución de dos de los fractales más famosos:

- **Conjunto de Mandelbrot**: Fractal definido por la iteración `z = z² + c`, donde `z` comienza en 0
- **Conjunto de Julia**: Fractal definido por la misma fórmula, pero con `c` constante y `z` variando según la posición

## Requisitos

```bash
pip install numpy matplotlib
```

## Uso

### Generar el Conjunto de Mandelbrot

```bash
python mandelbrot.py
```

Este script genera una imagen con zoom extremo del conjunto de Mandelbrot en la región:
- Parte real: -0.74575 a -0.74570
- Parte imaginaria: 0.10510 a 0.10515
- Resolución: 1500x1500 píxeles
- Iteraciones: 350

### Generar el Conjunto de Julia

```bash
python julia.py
```

Genera el conjunto de Julia con parámetro `c = -0.2 + 0.75i`:
- Región: -1.5 a 1.5 (ambos ejes)
- Resolución: 1000x1000 píxeles
- Iteraciones: 50

## Estructura de Salida

Las imágenes se guardan en:
```
out/
├── mandelbrot/
│   └── mandelbrot_zoom.png
└── julia/
    └── Julia.png
```

## Personalización

### Cambiar la región de visualización

Modifica las variables en cada script:

```python
x_min = -2.0  # Límite izquierdo
x_max = 0.8   # Límite derecho
y_min = -1.4  # Límite inferior
y_max = 1.4   # Límite superior
```

### Ajustar la calidad

```python
alto, ancho = 1500, 1500  # Resolución en píxeles
iteraciones = 350          # Más iteraciones = más detalle
```

### Cambiar el parámetro de Julia

```python
c = complex(-0.2, 0.75)  # Prueba diferentes valores
```

### Modificar el esquema de colores

```python
plt.imshow(mandelbrot_set, cmap='magma')  
# Otras opciones: 'viridis', 'plasma', 'inferno', 'hot', 'cool'
```

## Cómo funcionan

Ambos fractales se basan en determinar si un punto en el plano complejo "escapa" al infinito bajo iteración:

1. Para cada píxel, se crea un número complejo correspondiente a esa coordenada
2. Se aplica repetidamente la fórmula `z = z² + c`
3. Se cuenta cuántas iteraciones tarda en escapar (|z| > 2)
4. El color representa el número de iteraciones

**Diferencia clave**:
- **Mandelbrot**: `c` varía (es la posición), `z` empieza en 0
- **Julia**: `c` es constante, `z` varía (es la posición)

## Ejemplos de resultados

El proyecto genera visualizaciones de alta calidad con:
- Paleta de colores "magma" para resaltar detalles
- Alta resolución (300 DPI)
- Etiquetas de ejes y barra de colores informativa
