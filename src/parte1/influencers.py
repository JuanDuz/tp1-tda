class Influencer:
    def __init__(self, id, nombre, penetracion, pares_no_compatibles):
        self.id = id
        self.nombre = nombre
        self.penetracion = penetracion
        self.pares_no_compatibles = set(pares_no_compatibles)

    def puede_trabajar_con(self, pares):
        return not any(influencer.id in self.pares_no_compatibles for influencer in pares)

    def __str__(self):
        return f"{self.nombre} ({self.id})"


# Representación del nodo
def print_nodo(nodo):
    if not nodo:
        return "{}"
    else:
        return "{" + ", ".join(str(influencer) for influencer in nodo) + "}"

def leer_archivo_influencers(archivo):
    influencers = []
    n = 0
    with open(archivo, 'r') as f:
        for line in f:
            n += 1
            splited_line = line.strip().split(',')
            influencer = Influencer(
                int(splited_line[0]),
                splited_line[1],
                int(splited_line[2]),
                [int(i) for i in splited_line[3:]]
            )
            influencers.append(influencer)
    return influencers, n


def branch_and_bound(influencers, mayor_penetracion_de_mercado, mejor_combinacion, combinacion_actual, n, index):
    print("\n-------- Altura del arbol:", index, "--------\n")
    print("- nodo ->", print_nodo(combinacion_actual))
    influencer = influencers[index]

    combinacion_actual_ampliada = combinacion_actual + [influencer]
    penetracion_actual = sum(influ.penetracion for influ in combinacion_actual)
    penetracion_actual_ampliada = penetracion_actual + influencer.penetracion

    if penetracion_actual > mayor_penetracion_de_mercado:
        mayor_penetracion_de_mercado = penetracion_actual
        mejor_combinacion[:] = combinacion_actual[:]
        print("Nuevo mejor valor", mayor_penetracion_de_mercado, "del nodo ->", print_nodo(mejor_combinacion))
    if penetracion_actual_ampliada > mayor_penetracion_de_mercado and influencer.puede_trabajar_con(
            combinacion_actual):
        mayor_penetracion_de_mercado = penetracion_actual_ampliada
        mejor_combinacion[:] = combinacion_actual_ampliada[:]
        print("Nuevo mejor valor", mayor_penetracion_de_mercado, "del nodo ->", print_nodo(mejor_combinacion))
    if index == n - 1:
        print("Ya evalue mis 2 nodos descendientes y ambos son hojas, asi que vuelvo")
        return mejor_combinacion, mayor_penetracion_de_mercado

    influencer_sig = influencers[index + 1]
    penetracion_sig = influencer_sig.penetracion
    cota_actual = penetracion_actual + (n - index - 1) * penetracion_sig
    cota_ampliada = penetracion_actual_ampliada + (n - index - 1) * penetracion_sig

    print("|-- nodo desc ->", print_nodo(combinacion_actual_ampliada), "v:", penetracion_actual_ampliada, "l:", cota_ampliada)
    print("|-- nodo desc ->", print_nodo(combinacion_actual), "v:", penetracion_actual, "l:", cota_actual)


    # Nota: cota_ampliada siempre sera >= a cota_actual, debido a esto puedo ir siempre primero por el nodo descendiente que si agrega al influencer
    # Agregar al influencer actual
    if cota_ampliada > mayor_penetracion_de_mercado and influencer.puede_trabajar_con(combinacion_actual):
        combinacion_actual.append(influencer)
        print("Recorro hacia nodo", print_nodo(combinacion_actual_ampliada))
        mejor_combinacion, mayor_penetracion_de_mercado = (
            branch_and_bound(influencers, mayor_penetracion_de_mercado, mejor_combinacion, combinacion_actual, n,
                             index + 1))
        combinacion_actual.pop()
        print("\n-------- Altura del arbol:", index, "--------\n")
        print("Vovli a nodo ->", print_nodo(combinacion_actual))
    else:
        print("Podo nodo desc:", print_nodo(combinacion_actual_ampliada))

    # No agregar al influencer actual
    if cota_actual > mayor_penetracion_de_mercado:
        print("Recorro hacia nodo", print_nodo(combinacion_actual))
        mejor_combinacion, mayor_penetracion_de_mercado = (
            branch_and_bound(influencers, mayor_penetracion_de_mercado, mejor_combinacion, combinacion_actual, n,
                             index + 1))
    else:
        print("Podo nodo desc:", print_nodo(combinacion_actual))
    return mejor_combinacion, mayor_penetracion_de_mercado


def main(file):
    influencers, n = leer_archivo_influencers(file)
    influencers.sort(key=lambda x: x.penetracion, reverse=True)
    combinacion_actual = []
    mejor_combinacion = []
    mayor_penetracion_de_mercado = 0
    contador_pasos = 0 # Para hacer print de la cantidad de pasos, luego borrar
    print("Comienza branch and bound con influencers ordenados:", ", ".join(map(str, combinacion_actual)))

    mejor_combinacion, mayor_penetracion_de_mercado = branch_and_bound(influencers, mayor_penetracion_de_mercado,
                                                                       mejor_combinacion, combinacion_actual, n, 0)

    print("Valor conseguido:", mayor_penetracion_de_mercado)
    for influencer in mejor_combinacion:
        print(influencer)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python influencers.py example_influencers.csv")
    else:
        file = sys.argv[1]
        main(file)
