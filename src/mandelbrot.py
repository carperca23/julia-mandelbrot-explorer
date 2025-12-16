import numpy as np
import matplotlib.pyplot as plt

def calcular_mandelbrot(h, w, x_min, x_max, y_min, y_max, max_iter=100):
    y, x = np.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    
    c = x + y*1j
    z = np.zeros(c.shape, dtype=np.complex128)
    div_time = np.full(c.shape, max_iter, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask]**2 + c[mask]
        escaped_now = (np.abs(z) > 2) & (div_time == max_iter)
        div_time[escaped_now] = i

    return div_time


# x_min, x_max = -2.0, 0.8
# y_min, y_max = -1.4, 1.4


x_min = -0.74570
x_max = -0.74575
y_min = 0.10510
y_max = 0.10515

alto, ancho = 1500, 1500  
iteraciones = 350 

print("Calculando...")

mandelbrot_set = calcular_mandelbrot(alto, ancho, x_min, x_max, y_min, y_max, iteraciones)

plt.figure(figsize=(10, 10))

plt.imshow(mandelbrot_set, cmap='magma', 
           extent=[x_min, x_max, y_min, y_max], 
           origin='lower') 

plt.title(f"Zoom de Mandelbrot (Iteraciones: {iteraciones})")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.colorbar(label="Iteraciones hasta escapar")

plt.savefig("out/mandelbrot/mandelbrot_zoom.png", dpi=300)
plt.show()