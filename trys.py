batch1 = [1, 0, 0, 0, 1]
batch2 = [1, 1, 0, 0, 1]
variable = 0
variable += 1 if any(x in batch2 for x in batch1) else 0
print(variable)