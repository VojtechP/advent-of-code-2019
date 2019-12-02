def calculate(original_codes, noun, verb):
  index = 0
  codes = original_codes.copy()
  codes[1] = noun
  codes[2] = verb

  while index + 3 < len(codes) and codes[index] != 99:
    opcode, index_a, index_b, result_index = codes[index:index + 4]
    a = codes[index_a]
    b = codes[index_b]

    if opcode == 1:
      codes[result_index] = a + b
    elif opcode == 2:
      codes[result_index] = a * b
    else:
      raise ValueError("Invalid combination of noun and verb")

    index += 4

  return codes[0]


def main():
  with open("2.txt") as input:
    index = 0
    line = input.readline()
    codes = [ int(code) for code in line.split(",") ]

    for noun in range(0, 100):
      for verb in range(0, 100):
        try:
          result = calculate(codes, noun, verb)

          if result == 19690720:
            part1 = calculate(codes, 12, 2)
            part2 = 100 * noun + verb

            print("Part 1: " + str(part1))
            print("Part 2: " + str(part2))
            return
        except ValueError:
          pass

if __name__ == "__main__":
  main()
