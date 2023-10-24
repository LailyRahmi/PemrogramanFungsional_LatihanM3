random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

def map1(num):
    satuan = num % 10
    puluhan = (num // 10) % 10
    ratusan = (num // 100) % 10
    return [ratusan, puluhan, satuan]

int_values_mapped = list(map(map1, int_values))

print("Data Float:")
print(float_values)
print("Data Int:")
print(int_values_mapped)
print("Data String:")
print(string_values)
