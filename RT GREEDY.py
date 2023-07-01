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

def find_optimal_assignment(data):
    num_workers = len(data)
    num_jobs = len(data[0])

    # Inisialisasi penugasan awal dengan indeks jobs berurutan
    assignment = list(range(num_jobs))
    min_cost = calculate_total_cost(assignment, data)

    # Cari penugasan yang memiliki biaya minimum
    for i in range(num_jobs):
        for j in range(i+1, num_jobs):
            # Swap pekerjaan pada posisi i dan j
            assignment[i], assignment[j] = assignment[j], assignment[i]
            cost = calculate_total_cost(assignment, data)
            if cost < min_cost:
                min_cost = cost
            else:
                # Jika biaya lebih besar atau sama, kembalikan ke penugasan semula
                assignment[i], assignment[j] = assignment[j], assignment[i]

    return assignment, min_cost

def calculate_total_cost(assignment, data):
    total_cost = 0
    for i in range(len(assignment)):
        total_cost += data[i][assignment[i]]
    return total_cost

# Main code
filename = 'C:/Users/JORDAN/Downloads/TUBES SA/data 5x5.txt'
data = read_assignment_data(filename)

optimal_assignment, min_cost = find_optimal_assignment(data)
print("Optimal Assignment:", optimal_assignment)
print("Minimum Cost:", min_cost)
print("Running time : %.6f" % (time.time() - start_time))
