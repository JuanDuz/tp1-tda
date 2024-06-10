class Person:
    def __init__(self, person_id, name, project_weight, project_profit):
        self.id = person_id
        self.name = name
        self.project_weight = project_weight
        self.project_profit = project_profit

    def __str__(self):
        return f"({self.id}) {self.name} {self.project_weight} {self.project_profit}"


def read_transport_file(archivo):
    persons = []
    n = 0
    with open(archivo, 'r') as f:
        for line in f:
            n += 1
            split_line = line.strip().split(',')
            person = Person(
                n,
                split_line[0],
                int(split_line[1]),
                int(split_line[2])
            )
            persons.append(person)
    return persons


def max_profit(persons, max_capacity, max_weight):
    opt = [[[0 for m in range(max_capacity + 1)] for j in range(max_weight + 1)] for i in range(len(persons) + 1)]
    selected_persons_indexes = [[[-1 for m in range(max_capacity + 1)] for j in range(max_weight + 1)] for i in range(len(persons) + 1)]

    for i in range(1, len(persons) + 1):
        for j in range(1, max_weight + 1):
            for m in range(1, max_capacity + 1):
                not_in_opt = opt[i - 1][j][m]

                if j >= persons[i - 1].project_weight and m >= 1:
                    in_opt = opt[i - 1][j - persons[i - 1].project_weight][m - 1] + persons[i - 1].project_profit
                    if in_opt > not_in_opt:
                        opt[i][j][m] = in_opt
                        selected_persons_indexes[i][j][m] = i
                    else:
                        opt[i][j][m] = not_in_opt
                        selected_persons_indexes[i][j][m] = selected_persons_indexes[i - 1][j][m]
                else:
                    opt[i][j][m] = not_in_opt
                    selected_persons_indexes[i][j][m] = selected_persons_indexes[i - 1][j][m]

    selected_persons = []
    cur_weight = max_weight
    cur_capacity = max_capacity
    for i in range(len(persons), 0, -1):
        if selected_persons_indexes[i][cur_weight][cur_capacity] != -1:
            selected_persons.append(selected_persons_indexes[i][cur_weight][cur_capacity])
            cur_weight -= persons[selected_persons_indexes[i][cur_weight][cur_capacity] - 1].project_weight
            cur_capacity -= 1

    total_selected_persons_weight = sum(persons[idx - 1].project_weight for idx in selected_persons)
    profit_result = opt[len(persons)][max_weight][max_capacity]

    return selected_persons, total_selected_persons_weight, profit_result


def compute_weight_and_profit(persons_file, transport_capacity, transport_weight):
    persons = read_transport_file(persons_file)
    selected_persons, total_weight, profit_result = max_profit(persons, transport_capacity, transport_weight)

    print("Pasajeros:", end=" ")
    for i, idx in enumerate(selected_persons):
        person = persons[idx - 1]
        print(person.name, end="")
        if i < len(selected_persons) - 1:
            print(", ", end="")

    print("\nPeso total:", end=" ")
    for i, idx in enumerate(selected_persons):
        person = persons[idx - 1]
        print(f"{person.project_weight}", end="")
        if i < len(selected_persons) - 1:
            print(" + ", end="")
        else:
            print(end=" ")
    print(f"= {total_weight}")

    print("Ganancia:", end=" ")
    for i, idx in enumerate(selected_persons):
        person = persons[idx - 1]
        print(f"{person.project_profit}", end="")
        if i < len(selected_persons) - 1:
            print(" + ", end="")
        else:
            print(end=" ")
    print(f"= {profit_result}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python mision.py personas.txt transport_capacity transport_maximum_weight")
        sys.exit()

    persons_text_file = sys.argv[1]
    transport_max_capacity = int(sys.argv[2])
    transport_max_weight = int(sys.argv[3])

    compute_weight_and_profit(persons_text_file, transport_max_capacity, transport_max_weight)
