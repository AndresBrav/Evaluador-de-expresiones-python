import tkinter as tk
from sympy import symbols, simplify, pprint


def resolver_expresion():
    expresion_usuario = entrada_expresion.get()

    # Limpiar el área de resultados
    area_resultados.config(state=tk.NORMAL)
    area_resultados.delete(1.0, tk.END)

    # Definir símbolos para las variables
    x, y, z = symbols("x y z")

    # Crear la expresión simbólica
    expresion_simbolica = simplify(expresion_usuario)

    # Mostrar los pasos intermedios
    area_resultados.insert(tk.END, "Expresión original:\n")
    area_resultados.insert(tk.END, str(expresion_simbolica) + "\n\n")

    for paso in range(1, 6):  # Limitamos a 5 pasos por simplicidad
        expresion_simplificada = simplify(expresion_simbolica)

        # Mostrar el paso actual
        area_resultados.insert(tk.END, f"Paso {paso}:\n")
        area_resultados.insert(tk.END, str(expresion_simplificada) + "\n\n")

        # Intentar resolver la expresión
        try:
            solucion = expresion_simplificada.evalf()
            # Mostrar la solución si se encuentra
            area_resultados.insert(tk.END, f"Solución: {solucion}\n")
            break
        except Exception:
            pass

        expresion_simbolica = expresion_simplificada

    # Desactivar la edición en el área de resultados
    area_resultados.config(state=tk.DISABLED)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Resolver Expresión Matemática")

# Etiqueta y entrada para ingresar la expresión
etiqueta_expresion = tk.Label(ventana, text="Expresión Matemática:")
etiqueta_expresion.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entrada_expresion = tk.Entry(ventana, width=40)
entrada_expresion.grid(row=0, column=1, padx=10, pady=10)

# Botón para resolver la expresión
boton_resolver = tk.Button(ventana, text="Resolver", command=resolver_expresion)
boton_resolver.grid(row=0, column=2, padx=10, pady=10)

# Área de resultados
area_resultados = tk.Text(ventana, height=20, width=60, state=tk.DISABLED)
area_resultados.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Iniciar el bucle principal
ventana.mainloop()
