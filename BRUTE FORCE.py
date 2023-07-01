#fungsi membaca data dari text data
def read_assignment_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            row = list(map(int, line.split()))
            data.append(row)
    return data

#menghitung total cost dari iterasi
def calculate_total_cost(assignment, data):
    total_cost = 0
    for i in range(len(assignment)):
        total_cost += data[i][assignment[i]]
    return total_cost

#fungsi menghitung permutasi dari kemungkinan yang terjadi
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

#fungsi mencari hasil minimum yang paling optimal
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


#mencari file yang akan dibaca, dan diolah dalam fungsi read data
filename = 'C:/Users/JORDAN/Downloads/TUBES SA/data 6x6.txt'
data = read_assignment_data(filename)

#mengambil nilai hasil data dengan paling optimal yang didapatkan
optimal_assignment, min_cost = find_optimal_assignment(data)

#menampilkan setiap permutasi beserta costnya
print("Permutasi: ")
permutations = []
used = [False] * len(data[0])
generate_permutations(len(data[0]), [], used, permutations, data)
i = 1
for assignment, cost in permutations:
    for j in range(len(assignment)):
        assignment[j] += 1
    print("Iterasi ke -", i, "=> Assignment:", assignment, "dengan Cost:", cost)
    i += 1

#membuat agar data job yang dipilih lebih jelas
for i in range(len(optimal_assignment)):
    optimal_assignment[i] += 1
print("Assignment Teroptimal:", optimal_assignment)
print("Cost paling sedikit:", min_cost)
