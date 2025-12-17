import sys

try:
    import cupy as xp
    GPU_AVAILABLE = True
    print("GPU detectada - Usando CuPy")
except ImportError:
    import numpy as xp
    GPU_AVAILABLE = False
    print("GPU no disponible - Usando NumPy")

def main():
    print("\nSelecciona el fractal a generar:")
    print("1. Mandelbrot")
    print("2. Julia")
    print("0. Salir")
    
    opcion = input("\nOpción: ").strip()
    
    if opcion == "1":
        import mandelbrot
        mandelbrot.run(xp, GPU_AVAILABLE)
    elif opcion == "2":
        import julia
        julia.run(xp, GPU_AVAILABLE)
    elif opcion == "0":
        print("Saliendo...")
        sys.exit(0)
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()