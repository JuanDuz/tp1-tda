class Influencer:
    def __init__(self, id, name, market_value, not_compatible_peers):
        self.id = id
        self.name = name
        self.market_value = market_value
        self.not_compatible_peers = set(not_compatible_peers)

    def can_work_with(self, peers):
        return not any(influencer.id in self.not_compatible_peers for influencer in peers)

    def __str__(self):
        return f"{self.name} ({self.id})"


def reed_influencers_file(archivo):
    influencers = []
    n = 0
    with open(archivo, 'r') as f:
        for line in f:
            n += 1
            splited_line = line.strip().split(',')
            not_compatible_peers = [int(i) for i in splited_line[3:] if i]
            influencer = Influencer(
                int(splited_line[0]),
                splited_line[1],
                int(splited_line[2]),
                not_compatible_peers
            )
            influencers.append(influencer)
    return influencers, n


def branch_and_bound(influencers, max_market_value, best_combination, current_combination, current_market_value, n,
                     index,
                     cost_function):
    influencer = influencers[index]

    current_combination_extended = current_combination + [influencer]
    current_market_value_extended = current_market_value + influencer.market_value

    if current_market_value > max_market_value:
        max_market_value = current_market_value
        best_combination = current_combination
    if current_market_value_extended > max_market_value and influencer.can_work_with(
            current_combination):
        max_market_value = current_market_value_extended
        best_combination = current_combination_extended
    if index == n - 1:
        return best_combination, max_market_value

    current_cost_function = cost_function - influencer.market_value
    cost_function_extended = cost_function

    # Nota: cota_ampliada siempre sera >= a cota_actual, debido a esto puedo ir siempre primero por el nodo descendiente que si agrega al influencer
    # Agregar al influencer actual
    if cost_function_extended > max_market_value and influencer.can_work_with(current_combination):
        current_combination.append(influencer)
        current_market_value += influencer.market_value
        best_combination, max_market_value = (
            branch_and_bound(influencers, max_market_value, best_combination, current_combination, current_market_value,
                             n,
                             index + 1, cost_function_extended))
        current_market_value -= influencer.market_value
        current_combination.pop()

    # No agregar al influencer actual
    if current_cost_function > max_market_value:
        best_combination, max_market_value = (
            branch_and_bound(influencers, max_market_value, best_combination, current_combination, current_market_value,
                             n,
                             index + 1, current_cost_function))
    return best_combination, max_market_value


def main(file):
    influencers, n = reed_influencers_file(file)
    influencers.sort(key=lambda x: x.market_value, reverse=True)
    cost_function = sum(influencer.market_value for influencer in influencers)
    current_combination = []
    current_market_value = 0
    best_combination = []
    max_market_value = 0
    best_combination, max_market_value = branch_and_bound(influencers, max_market_value,
                                                          best_combination, current_combination, current_market_value,
                                                          n, 0, cost_function)

    print("Valor conseguido:", max_market_value)
    for influencer in best_combination:
        print(influencer)

    with open('resultado.txt', 'w') as f:
        f.write(f"Valor conseguido: {max_market_value}\n\n")
        for influencer in best_combination:
            f.write(f"{influencer.name}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Uso: python promocion.py example_influencers.csv")
    else:
        file = sys.argv[1]
        main(file)
