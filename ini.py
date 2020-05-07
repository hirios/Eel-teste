import eel 


eel.init('web')


@eel.expose
def mostrar():
    print("Teste realizado com sucesso")
    return "Teste realizado com sucesso"

eel.start('index.html', size=(1000, 600))