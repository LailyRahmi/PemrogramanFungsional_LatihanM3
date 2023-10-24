data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def is_integer(s):
    return s.isdigit()

output_data = []

for item in data:
    data_split = item.split()

    integer_values = list(filter(is_integer, data_split))
    
    integer_values = list(map(int, integer_values))
    output_data.append(integer_values)

print("Data = ", data)
print("Output Data (hanya integer) = ", output_data)
