import numpy as np
import matplotlib.pyplot as plt

def calcular_julia(h, w, c, x_min, x_max, y_min, y_max, max_iter=100):
    y, x = np.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    
    z = x + y*1j
    div_time = np.full(z.shape, max_iter, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask]**2 + c
        escaped_now = (np.abs(z) > 2) & (div_time == max_iter)
        div_time[escaped_now] = i

    return div_time


x_min = -1.5
x_max = 1.5
y_min = -1.5
y_max = 1.5
c = complex(-0.2, 0.75)

alto, ancho = 1000, 1000  
iteraciones = 50 

print("Calculando...")

mandelbrot_set = calcular_julia(alto, ancho, c, x_min, x_max, y_min, y_max, iteraciones)

plt.figure(figsize=(10, 10))

plt.imshow(mandelbrot_set, cmap='magma', 
           extent=[x_min, x_max, y_min, y_max], 
           origin='lower') 

plt.title(f"Julia (Iteraciones: {iteraciones})")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginaria")
plt.colorbar(label="Iteraciones hasta escapar")

plt.savefig("out/julia/Julia.png", dpi=300)
plt.show()