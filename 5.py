def get_instruction_params_length(opcode):
  if opcode in [1, 2, 7, 8]:
    return 3
  elif opcode in [3, 4]:
    return 1
  elif opcode in [5, 6]:
    return 2

def get_params(codes, instruction_index):
  opcode = codes[instruction_index] % 100
  instruction_params_length = get_instruction_params_length(opcode)
  start_index = instruction_index + 1
  end_index = start_index + instruction_params_length

  return codes[start_index:end_index]

def get_modes(instruction):
  modes = []
  instruction //= 100

  for i in range(3):
    modes.append(instruction % 10)
    instruction //= 10

  return modes

def get_param_value(codes, param, mode):
  return param if mode else codes[param]

def run(codes, input_value):
  index = 0
  diagnostic_code = 0

  while codes[index] != 99:
    next_index = -1
    instruction = codes[index]
    opcode = instruction % 100
    params = get_params(codes, index)
    modes = get_modes(instruction)
    param_values = [ get_param_value(codes, params[i], modes[i]) for i in range(len(params)) ]

    if opcode == 1:
      codes[params[2]] = param_values[0] + param_values[1]
    elif opcode == 2:
      codes[params[2]] = param_values[0] * param_values[1]
    elif opcode == 3:
      codes[params[0]] = input_value
    elif opcode == 4:
      diagnostic_code = codes[params[0]]
    elif opcode == 5:
      if param_values[0]:
        next_index = param_values[1]
    elif opcode == 6:
      if not param_values[0]:
        next_index = param_values[1]
    elif opcode == 7:
      codes[params[2]] = 1 if param_values[0] < param_values[1] else 0
    elif opcode == 8:
      codes[params[2]] = 1 if param_values[0] == param_values[1] else 0

    index = index + len(params) + 1 if next_index == -1 else next_index

  return diagnostic_code


def main():
  with open("5.txt") as input:
    line = input.readline()
    codes = [ int(code) for code in line.split(",") ]

    print("Part 1: " + str(run(codes.copy(), 1))) # 4511442
    print("Part 2: " + str(run(codes.copy(), 5))) # 12648139

if __name__ == "__main__":
  main()
