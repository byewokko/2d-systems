import numpy as np
import sys

from time import sleep

def print_bin_matrix(m, true="O", false=" "):
    for row in m:
        for cell in row:
            if cell:
                print(true, end="")
            else:
                print(false, end="")
        print()
    print("\u001b[" + str(m.shape[0]+1) + "A")


def conway_step(field):
    neighbors = np.roll(field, 1, 0) \
                + np.roll(field, 1, 1) \
                + np.roll(field, -1, 0) \
                + np.roll(field, -1, 1) \
                + np.roll(np.roll(field, 1, 0), 1, 1) \
                + np.roll(np.roll(field, 1, 0), -1, 1) \
                + np.roll(np.roll(field, -1, 0), 1, 1) \
                + np.roll(np.roll(field, -1, 0), -1, 1)

    #print(neighbors)
    field_new = np.zeros_like(field)
    field_new[neighbors == 3] = 1
    field_new[(neighbors == 2) * (field == 1)] = 1

    return field_new


def main():
    if len(sys.argv) > 2:
        h = int(sys.argv[1])
        w = int(sys.argv[2])
    else:
        h, w = 20, 35

    if len(sys.argv) > 3:
        tick = 1/float(sys.argv[3])
    else:
        tick = 1/20

    field = np.random.choice(a=[0, 1], size=(h, w))
    try:
        while True:
            field = conway_step(field)
            print_bin_matrix(field)
            sleep(tick)
    except KeyboardInterrupt:
        print_bin_matrix(np.zeros_like(field))
        quit()

if __name__ == "__main__":
    main()