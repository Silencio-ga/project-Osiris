# funcion para aparece el texto gradualmente 
def efect_text_gradual(texto, tmp):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(tmp)