import pandas as pd


# X = Ingresos (dólares), Y = Metros cuadrados
x_intervals = ["50-100", "100-150", "150-200", "200-250", "250-300"]
x_midpoints = [75, 125, 175, 225, 275]  # marcas de clase de X

y_intervals = ["0-60", "60-80", "80-100", "100-150", "150-200"]
y_midpoints = [30, 70, 90, 125, 175]  # marcas de clase de Y

# Frecuencias (matriz CORREGIDA: filas = X, columnas = Y)
frequencies = [
    [20, 18, 2, 1, 0],    # X=50-100
    [25, 40, 16, 2, 1],    # X=100-150
    [4, 10, 15, 22, 3],    # X=150-200
    [1, 5, 15, 20, 8],     # X=200-250
    [2, 1, 2, 7, 10]       # X=250-300
]


rows = []
for i, x in enumerate(x_midpoints):
    for j, y in enumerate(y_midpoints):
        f = frequencies[i][j]
        rows.append({
            'x': x,
            'y': y,
            'f': f,
            'f*x': f * x,
            'f*y': f * y,
            'f*xy': f * x * y
        })

df = pd.DataFrame(rows)


N = df['f'].sum()
fx = df['f*x'].sum()
fy = df['f*y'].sum()
fxy = df['f*xy'].sum()

x_mean = fx / N
y_mean = fy / N
cov_xy = (fxy / N) - (x_mean * y_mean)



print(f"Número de familias (N): {N}")
print(f"Media de X (Ingresos): {x_mean:.2f}")
print(f"Media de Y (Metros cuadrados): {y_mean:.2f}")
print(f"\nCovarianza (σ_xy): {cov_xy:.2f}")
