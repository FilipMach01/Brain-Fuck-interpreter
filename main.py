import sys
import getch

def execute(filename):
  f = open(filename, "r")
  evaluate(f.read())
  f.close()

def evaluate(code):
  cells, codeptr, cellptr = [0], 0, 0
  bracemap = get_bracemap(code)

  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells):
        cells.append(0)

    if command == "<":
      if cellptr == 0:
        cellptr = 0
      else:
        cellptr -= 1

    if command == "+":
      if cells[cellptr] < 255:
        cells[cellptr] += 1
      else:
        cells[cellptr] = 0

    if command == "-":
      if cells[cellptr] > 0:
        cells[cellptr] -= 1
      else:
        cells[cellptr] = 0

    if command == "[" and cells[cellptr] == 0:
      codeptr = bracemap[codeptr]

    if command == "]" and cells[cellptr] != 0:
      codeptr = bracemap[codeptr]

    if command == ".":
      sys.stdout.write(chr(cells[cellptr]))

    if command == ",":
      cells[cellptr] = ord(getch.getch())

    codeptr += 1


def celan_up(code):
  return ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code))

def get_bracemap(code):
  brace_map = {}
  temp_bracestack = []

  for position, cmd in enumerate(code):
    if cmd == "[":
      temp_bracestack.append(position)
    if cmd == "]":
      start = temp_bracestack.pop()
      brace_map[start] = position
      brace_map[position] = start

  return brace_map

def main():
  if len(sys.argv) == 2:
    execute(sys.argv[1])
  else:
    print("Usage:", sys.argv[0], "filename")

if __name__ == "__main__": main()
