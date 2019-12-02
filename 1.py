def calculate_required_fuel(mass):
  return mass // 3 - 2

calculate_part_1_required_fuel = calculate_required_fuel

def calculate_part_2_required_fuel(mass):
  total = 0
  fuel = calculate_required_fuel(mass)

  while fuel > 0:
    total += fuel
    fuel = calculate_required_fuel(fuel)

  return total

def main():
  with open("1.txt") as input:
    part1 = 0
    part2 = 0

    line = input.readline()
    while line:
      mass = int(line)
      part1 += calculate_part_1_required_fuel(mass)
      part2 += calculate_part_2_required_fuel(mass)

      line = input.readline()

    print("Part 1: " + str(part1))
    print("Part 2: " + str(part2))

if __name__ == "__main__":
  main()
