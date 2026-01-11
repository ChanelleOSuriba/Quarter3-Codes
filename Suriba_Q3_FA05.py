names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],  
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]   
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

daily_totals = []

for day in range(len(steps[0])):
    day_total = 0
    for person in range(len(steps)):
        day_total += steps[person][day]
    daily_totals.append(day_total)
    print(f"Total steps on {days[day]}: {day_total}")

max_steps = max(daily_totals)
max_day_index = daily_totals.index(max_steps)

print(f"\nMost active day: {days[max_day_index]} with {max_steps} steps")
