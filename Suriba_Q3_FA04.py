names = ["My", "Lia's", "Jake's"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

total_steps = []

for person_steps in steps:
    total_steps.append(sum(person_steps))

max_steps = max(total_steps)
min_steps = min(total_steps)

max_index = total_steps.index(max_steps)
top_person = names[max_index]

for i in range(len(names)):
    print(f"{names[i]}'s total steps: {total_steps[i]}")

print(f"Highest total steps: {top_person} with {max_steps} steps")
print(f"Difference between highest and lowest total: {max_steps - min_steps}")
