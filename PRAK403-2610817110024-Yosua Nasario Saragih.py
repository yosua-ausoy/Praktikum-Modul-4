angka = input().split()
a = int(angka[0])
b = int(angka[1])

if a > b:
  total_langkah = a - b + 1
  for i in range(total_langkah):
    print(f"{a} {b}", end="")
    if i < total_langkah - 1:
      print(" - ", end="")
  a = a - 1
  b = b + 1
else:
  total_langkah = b - a + 1
  for i in range(total_langkah):
    print(f"{a} {b}", end="")
    if i < total_langkah - 1:
      print(" - ", end="")
    a = a + 1
    b = b - 1