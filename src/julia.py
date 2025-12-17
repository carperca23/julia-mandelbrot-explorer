import matplotlib.pyplot as plt
from config import *

def calcular_julia(h, w, c, x_min, x_max, y_min, y_max, max_iter, xp):
    y, x = xp.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    
    z = x + y*1j
    div_time = xp.full(z.shape, max_iter, dtype=int)
    
    for i in range(max_iter):
        mask = xp.abs(z) <= 2
        z[mask] = z[mask]**2 + c
        escaped_now = (xp.abs(z) > 2) & (div_time == max_iter)
        div_time[escaped_now] = i

    return div_time


def run(xp, gpu_available):
    c = complex(JULIA_C_REAL, JULIA_C_IMAG)
    
    print(f"Calculando Julia con {'GPU (CuPy)' if gpu_available else 'CPU (NumPy)'}...")
    
    julia_set = calcular_julia(
        JULIA_ALTO, JULIA_ANCHO, c, 
        JULIA_X_MIN, JULIA_X_MAX, 
        JULIA_Y_MIN, JULIA_Y_MAX, 
        JULIA_ITERACIONES, xp
    )
    
    if gpu_available:
        julia_set = julia_set.get()
    
    if JULIA_PHOTO_MODE:
        plt.imsave(
            "out/julia/Julia.png",
            julia_set,
            cmap=COLORMAP,
            origin="lower"
        )
    else:
        plt.figure(figsize=(10, 10))
        plt.imshow(julia_set, cmap=COLORMAP, 
                   extent=[JULIA_X_MIN, JULIA_X_MAX, JULIA_Y_MIN, JULIA_Y_MAX], 
                   origin='lower') 
        plt.title(f"Julia (Iteraciones: {JULIA_ITERACIONES})")
        plt.xlabel("Parte Real")
        plt.ylabel("Parte Imaginaria")
        plt.colorbar(label="Iteraciones hasta escapar")
        plt.savefig("out/julia/Julia.png", dpi=DPI)
        plt.show()
    
    print("Julia generado correctamente en out/julia/Julia.png")