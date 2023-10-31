import time, sys
indent = 0 
changeDirection = True 

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if changeDirection:
            indent = indent + 1
            if indent == 20:
                changeDirection = False
        else:
            indent = indent - 1
            if indent == 0:
                changeDirection = True
except KeyboardInterrupt:
    sys.exit()