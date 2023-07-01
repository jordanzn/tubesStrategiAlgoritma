import time
start_time = time.time()
def read_assignment_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = list(map(int, line.split()))
            data.append(row)
    return data

def calculate_total_cost(assignment, data):
    total_cost = 0
    for i in range(len(assignment)):
        total_cost += data[i][assignment[i]]
    return total_cost

def generate_permutations(n, current_permutation, used, permutations, data):
    if len(current_permutation) == n:
        total_cost = calculate_total_cost(current_permutation, data)
        permutations.append((current_permutation[:], total_cost))
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            current_permutation.append(i)
            generate_permutations(n, current_permutation, used, permutations, data)
            current_permutation.pop()
            used[i] = False

def find_optimal_assignment(data):
    num_workers = len(data)
    num_jobs = len(data[0])
    min_cost = float('inf')
    optimal_assignment = None

    permutations = []
    used = [False] * num_jobs
    generate_permutations(num_jobs, [], used, permutations, data)

    for assignment, cost in permutations:
        if cost < min_cost:
            min_cost = cost
            optimal_assignment = assignment

    return optimal_assignment, min_cost

# Main code
filename = 'C:/Users/JORDAN/Downloads/TUBES SA/data 6x6.txt'
data = read_assignment_data(filename)

optimal_assignment, min_cost = find_optimal_assignment(data)
print("Optimal Assignment:", optimal_assignment)
print("Minimum Cost:", min_cost)
print("Running time : %.6f" % (time.time() - start_time))
