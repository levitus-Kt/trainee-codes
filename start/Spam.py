import textwrap
import time
import hashlib
import math
import libs

comment1 = input()
print(comment1)

while True:
    tic = time.perf_counter()
    comment2 = input()
    tac = time.perf_counter()

    if (tac - tic) >= 4:
        print(comment2)
        #print(round(tac-tic, 2))

    else:
        print(f"Вы слишком часто отправляете сообщения")
        break