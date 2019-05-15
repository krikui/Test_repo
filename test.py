#!/usr/bin/python
import sys
print('Number of arguments:', len(sys.argv), 'arguments')
type(sys.argv)
print(str(sys.argv))

print("Help\n")
raw_input("\n\nPress the enter key to exit.")
x = 'foo'; sys.stdout.write(x+'\n')
sys.exit(0)