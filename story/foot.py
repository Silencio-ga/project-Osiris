import shutil

texto = "Hola mundo"
cols, rows = shutil.get_terminal_size()

# líneas en blanco antes para centrar verticalmente
print("\n" * (rows // 2))
print(texto.center(cols))