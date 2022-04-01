from dateutil.relativedelta import relativedelta

def separate_rut(rut):
    v_rut = limpiar_rut(str(rut))

    valores_a = v_rut[0:len(v_rut)-1]
    valores_b = v_rut[len(v_rut)-1:len(v_rut)]

    return int(valores_a), valores_b

def limpiar_rut(valor):
    posibles = ["0","1","2","3","4","5","6","7","8","9","K","k"]
    resultado = valor
    for x in valor:
        if x not in posibles:
            resultado = resultado.replace(x,"")
    return resultado.upper()

def limpiar_fono(valor):
    posibles = ["0","1","2","3","4","5","6","7","8","9"]
    resultado = valor
    for x in valor:
        if x not in posibles:
            resultado = resultado.replace(x,"")
    return resultado.upper()
