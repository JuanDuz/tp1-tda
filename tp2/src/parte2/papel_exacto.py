import pulp
import sys


def read_data(filepath):
    actors = {}
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            actor = parts[0]
            i = 1
            while i < len(parts):
                role = int(parts[i])
                potential = int(parts[i + 1])
                if actor not in actors:
                    actors[actor] = []
                actors[actor].append((role, potential))
                i += 2
    return actors


def solve_casting_problem(actors):
    model = pulp.LpProblem("Maximize_Audience_Potential", pulp.LpMaximize)

    # Variables
    x = {}
    for actor, roles in actors.items():
        for role, potential in roles:
            x[(actor, role)] = pulp.LpVariable(f'x_{actor}_{role}', cat='Binary')

    # Objective Function
    model += pulp.lpSum(x[(actor, role)] * potential for actor, roles in actors.items() for role, potential in roles)

    # Constraints
    # Each actor can be assigned to at most one role
    for actor in actors:
        model += pulp.lpSum(x[(actor, role)] for role, potential in actors[actor]) <= 1, f"One_role_per_actor_{actor}"

    # Each role can be filled by at most one actor
    all_roles = set(role for roles in actors.values() for role, _ in roles)
    for role in all_roles:
        model += pulp.lpSum(x[(actor, r)] for actor, roles in actors.items() for r, p in roles if
                            r == role) <= 1, f"One_actor_per_role_{role}"

    # Solve the problem
    model.solve()

    # Output results
    total_potential = 0
    print("Assigned Actors and Roles:")
    for actor, roles in actors.items():
        for role, potential in roles:
            if x[(actor, role)].value() == 1:
                print(f"Actor {actor} is assigned to Role {role} with potential {potential}")
                total_potential += potential
    print(f"Total potential of audience: {total_potential}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_data_file")
    else:
        filepath = sys.argv[1]
        actors = read_data(filepath)
        solve_casting_problem(actors)