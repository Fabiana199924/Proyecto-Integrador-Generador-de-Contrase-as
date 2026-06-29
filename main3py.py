import random

print("==================================================")
print("  BIENVENIDO AL GENERADOR DE CONTRASEÑAS SEGURAS  ")
print("==================================================")

# Listas básicas de caracteres para armar la contraseña
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
especiales = ".*-+#@$"

# Unimos todo en una sola lista de opciones
todos_los_caracteres = letras + numeros + especiales

# Pedir al usuario el largo de la contraseña
largo = int(input("¿De cuántos caracteres quieres tu contraseña?: "))

# --- ESTRUCTURA REPETITIVA (Bucle para armar la clave) ---
contrasena_final = ""
contador = 0

while contador < largo:
    # Elegimos un caracter al azar y lo sumamos a la contraseña
    caracter_alazar = random.choice(todos_los_caracteres)
    contrasena_final = contrasena_final + caracter_alazar
    contador = contador + 1

print(f"\nTu nueva contraseña es: {contrasena_final}")

# --- ESTRUCTURA CONDICIONAL (Evaluar si es segura por su largo) ---
print("\n--- DIAGNÓSTICO DE SEGURIDAD ---")
if largo < 8:
    print("Resultado: DÉBIL ❌ (Es muy corta, te pueden hackear fácil)")
elif largo >= 8 and largo < 12:
    print("Resultado: REGULAR ⚠️ (Sirve para cosas poco importantes)")
else:
    print("Resultado: FUERTE ✅ (Excelente longitud para proteger tus datos)")

print("==================================================")