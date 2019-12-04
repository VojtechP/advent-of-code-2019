def has_two_adjacent_digits__same(n):
  if n < 10:
    return False

  last_digit = n % 10
  n //= 10

  if n % 10 == last_digit:
    return True

  return has_two_adjacent_digits__same(n)

def has_not_decreased_digits(n):
  if n < 10:
    return True

  last_digit = n % 10
  n //= 10
  penultimate_digit = n % 10

  if penultimate_digit > last_digit:
    return False

  return has_not_decreased_digits(n)

def has_two_same_digits(n):
  last_digit = -1
  count = 0

  while n > 0:
    if last_digit == n % 10:
      count += 1
    elif count == 2:
      return True
    else:
      last_digit = n % 10
      count = 1

    n //= 10

  return count == 2

def main():
  part_1_count = 0
  part_2_count = 0
  for n in range(307_237, 769_058 + 1):
    if has_two_adjacent_digits__same(n) and has_not_decreased_digits(n):
      part_1_count += 1

      if has_two_same_digits(n):
        part_2_count += 1

  print("Part 1: " + str(part_1_count)) # 889
  print("Part 2: " + str(part_2_count)) # 589


if __name__ == "__main__":
  main()
