
# Fungsi membaca data dari file teks
def read_assignment_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = list(map(int, line.split()))
            data.append(row)
    return data

# Menghitung total cost dari suatu penugasan
def calculate_total_cost(assignment, data):
    total_cost = 0
    for i in range(len(assignment)):
        total_cost += data[i][assignment[i]]
    return total_cost

# Mencari penugasan yang optimal dengan biaya minimum
def find_optimal_assignment(data):
    num_workers = len(data)
    num_jobs = len(data[0])

    assignment = list(range(num_jobs))
    min_cost = calculate_total_cost(assignment, data)
    optimal_assignment = assignment[:]

    # List untuk menyimpan kemungkinan setiap iterasi
    iteration_possibilities = []
    iteration_costs = []

    # Cari penugasan yang memiliki biaya minimum
    for i in range(num_jobs):
        for j in range(i+1, num_jobs):
            # Swap pekerjaan pada posisi i dan j
            assignment[i], assignment[j] = assignment[j], assignment[i]
            cost = calculate_total_cost(assignment, data)
            iteration_possibilities.append(assignment[:])
            iteration_costs.append(cost)
            if cost < min_cost:
                min_cost = cost
                optimal_assignment = assignment[:]
            else:
                # Jika biaya lebih besar atau sama, kembalikan ke penugasan semula
                assignment[i], assignment[j] = assignment[j], assignment[i]

    return optimal_assignment, min_cost, iteration_possibilities, iteration_costs

# Mencari file yang akan dibaca dan diolah dalam fungsi read_assignment_data
filename = 'C:/Users/JORDAN/Downloads/TUBES SA/data 5x5.txt'
data = read_assignment_data(filename)

# Menampilkan iterasi dengan solusi paling optimal
optimal_assignment, min_cost, iteration_possibilities, iteration_costs = find_optimal_assignment(data)
for i in range(len(optimal_assignment)):
    optimal_assignment[i] += 1

print("Assignment Optimal:", optimal_assignment)
print("Cost paling sedikit:", min_cost)

# Menampilkan semua hasil iterasi beserta dengan total biaya (cost) masing-masing
print("Permutasi:")
for i in range(len(iteration_possibilities)):
    for j in range(len(iteration_possibilities[i])):
        iteration_possibilities[i][j] += 1
    print("Iterasi ke-", i+1, "=> Assignment", iteration_possibilities[i], "Dengan Biaya:", iteration_costs[i])
