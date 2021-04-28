# zigzag animation
import time, sys
indent = 0
indent_increase = True

try:
    while True:
        if (indent_increase):
            print(" " * indent + "*" * 8)
            time.sleep(0.1)
            indent += 1
            if (indent == 20):
                indent_increase = False

        else:
            print(" " * indent + "*" * 8)
            time.sleep(0.1)
            indent -= 1
            if (indent == 0):
                indent_increase = True
except KeyboardInterrupt:
    sys.exit()
