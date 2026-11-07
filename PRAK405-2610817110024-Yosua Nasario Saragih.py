data = input().split()
n = int(data[0])
kelipatan = int(data[1])

total_akhir = 0

for i in range(1, n + 1):
  baris_sum = 0

  for j in range(i, 0, -1):
    print(f"({j}*{kelipatan})", end="")
    baris_sum = baris_sum + (j * kelipatan)

    if j > 1:
      print(" + ", end="")

  print(f" = {baris_sum}")
  total_akhir = total_akhir + baris_sum

print(total_akhir)