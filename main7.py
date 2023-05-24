def knapsack(capacity, weights, values):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]


# Metin dosyasını okuma

# filename = "ks_10000_0.txt"  
filename = "ks_200_0.txt"
# filename = "ks_19_0.txt"


with open(filename, "r") as file:
    lines = file.readlines()

capacity = int(lines[0])  # Çantanın kapasitesini dosyadan çekme

values = []
weights = []

for line in lines[1:]:
    value, weight = map(int, line.strip().split())
    values.append(value)
    weights.append(weight)

# Knapsack problemini çözme
max_value, selected_items = knapsack(capacity, weights, values)

# Verileri yazdırma
print("Çanta Kapasitesi:", capacity)

print("En Yüksek Değer:", max_value)
print("Seçilen Nesnelerin İndeksleri:", selected_items)
