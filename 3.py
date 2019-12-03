import math
import re

path_re = re.compile("(?P<direction>[URDL])(?P<length>\d+)")

def map_path(path):
  direction, length = path_re.search(path).groups()
  return (direction, int(length))

def get_paths(line):
  return [ map_path(path) for path in line.split(',') ]

def is_vertical(direction):
  return direction == 'U' or direction == 'D'

def get_relative_length(length, direction):
  return -length if direction == 'D' or direction == 'L' else length

def calculate_distance(x , y):
  return abs(x) + abs(y)

def part_1():
  with open("3.txt") as input:
    wire_1 = get_paths(input.readline())
    wire_2 = get_paths(input.readline())

    point = (0, 0)
    verticals = {}
    horizontals = {}

    for path in wire_1:
      x, y = point
      direction, length = path
      relative_length = get_relative_length(length, direction)

      if is_vertical(direction):
        ys = (y, y + relative_length)

        if x not in verticals:
          verticals[x] = []
        verticals[x].append((min(ys), max(ys)))

        point = (x, y + relative_length)
      else:
        xs = (x, x + relative_length)

        if y not in horizontals:
          horizontals[y] = []
        horizontals[y].append((min(xs), max(xs)))

        point = (x + relative_length, y)

    shortest_dist = math.inf

    point = (0, 0)

    for path in wire_2:
      x, y = point
      direction, length = path
      relative_length = get_relative_length(length, direction)

      if is_vertical(direction):
        ys = (y, y + relative_length)

        for y_i in range(min(ys), max(ys) + 1):
          if y_i in horizontals and any(True for x_1, x_2 in horizontals[y_i] if x >= x_1 and x <= x_2):
            distance = calculate_distance(x, y_i)
            if distance > 0 and distance < shortest_dist:
              shortest_dist = distance

        point = (x, y + relative_length)
      else:
        xs = (x, x + relative_length)

        for x_i in range(min(xs), max(xs) + 1):
          if x_i in verticals and any(True for y_1, y_2 in verticals[x_i] if y >= y_1 and y <= y_2):
            distance = calculate_distance(x_i, y)
            if distance > 0 and distance < shortest_dist:
              shortest_dist = distance

        point = (x + relative_length, y)
    print("Part 1:" + str(shortest_dist)) # 260

def part_2():
  with open("3.txt") as input:
    wire_1 = get_paths(input.readline())
    wire_2 = get_paths(input.readline())

    point = (0, 0)
    total_distance = 0
    verticals = {}
    horizontals = {}

    for path in wire_1:
      x, y = point
      direction, length = path
      relative_length = get_relative_length(length, direction)
      relative_position = total_distance if relative_length > 0 else -(total_distance + length)
      total_distance += length

      if is_vertical(direction):
        ys = (y, y + relative_length)

        if x not in verticals:
          verticals[x] = []
        verticals[x].append((min(ys), max(ys), relative_position))

        point = (x, y + relative_length)
      else:
        xs = (x, x + relative_length)

        if y not in horizontals:
          horizontals[y] = []
        horizontals[y].append((min(xs), max(xs), relative_position))

        point = (x + relative_length, y)

    shortest_dist = math.inf

    point = (0, 0)
    total_distance = 0

    for path in wire_2:
      x, y = point
      direction, length = path
      relative_length = get_relative_length(length, direction)
      relative_position = total_distance if relative_length > 0 else -(total_distance + length)
      total_distance += length

      if is_vertical(direction):
        ys = (y, y + relative_length)

        for y_i in range(min(ys), max(ys) + 1):
          if calculate_distance(x, y_i) > 0 and y_i in horizontals:
            dists = [ abs(relative_position + x - x_1) for x_1, x_2, relative_position in horizontals[y_i] if x >= x_1 and x <= x_2 ]
            if len(dists) and min(dists) + abs(relative_position + y_i - min(ys)) < shortest_dist:
              shortest_dist = min(dists) + abs(relative_position + y_i - min(ys))

        point = (x, y + relative_length)
      else:
        xs = (x, x + relative_length)

        for x_i in range(min(xs), max(xs) + 1):
          if calculate_distance(x_i, y) > 0 and x_i in verticals:
            dists = [ abs(relative_position + y - y_1) for y_1, y_2, relative_position in verticals[x_i] if y >= y_1 and y <= y_2 ]
            if len(dists) and min(dists) + abs(relative_position + x_i - min(xs)) < shortest_dist:
              shortest_dist = min(dists) + abs(relative_position + x_i - min(xs))

        point = (x + relative_length, y)
    print("Part 2:" + str(shortest_dist)) # 15612

def main():
  part_1()
  part_2()

if __name__ == "__main__":
  main()
