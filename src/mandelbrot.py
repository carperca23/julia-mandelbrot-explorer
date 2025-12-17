import matplotlib.pyplot as plt
from config import *

def calcular_mandelbrot(h, w, x_min, x_max, y_min, y_max, max_iter, xp):
    y, x = xp.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    
    c = x + y*1j
    z = xp.zeros(c.shape, dtype=xp.complex128)
    div_time = xp.full(c.shape, max_iter, dtype=int)
    
    for i in range(max_iter):
        mask = xp.abs(z) <= 2
        z[mask] = z[mask]**2 + c[mask]
        escaped_now = (xp.abs(z) > 2) & (div_time == max_iter)
        div_time[escaped_now] = i

    return div_time


def run(xp, gpu_available):
    print(f"Calculando Mandelbrot con {'GPU (CuPy)' if gpu_available else 'CPU (NumPy)'}...")
    
    mandelbrot_set = calcular_mandelbrot(
        MANDELBROT_ALTO, MANDELBROT_ANCHO, 
        MANDELBROT_X_MIN, MANDELBROT_X_MAX, 
        MANDELBROT_Y_MIN, MANDELBROT_Y_MAX, 
        MANDELBROT_ITERACIONES, xp
    )
    
    if gpu_available:
        mandelbrot_set = mandelbrot_set.get()
    
    if MANDELBROT_PHOTO_MODE:
        plt.imsave(
            "out/mandelbrot/mandelbrot_zoom.png",
            mandelbrot_set,
            cmap=COLORMAP,
            origin="lower"
        )
    else:
        plt.figure(figsize=(10, 10))
        plt.imshow(mandelbrot_set, cmap=COLORMAP, 
                   extent=[MANDELBROT_X_MIN, MANDELBROT_X_MAX, MANDELBROT_Y_MIN, MANDELBROT_Y_MAX], 
                   origin='lower') 
        plt.title(f"Zoom de Mandelbrot (Iteraciones: {MANDELBROT_ITERACIONES})")
        plt.xlabel("Parte Real")
        plt.ylabel("Parte Imaginaria")
        plt.colorbar(label="Iteraciones hasta escapar")
        plt.savefig("out/mandelbrot/mandelbrot_zoom.png", dpi=DPI)
        plt.show()
    
    print("Mandelbrot generado correctamente en out/mandelbrot/mandelbrot_zoom.png")