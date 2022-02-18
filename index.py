from page1 import page1
from camera1 import camera1
from virtual_mouse import virtual_mouse
from basic import root
from threading import Thread

if __name__ == '__main__':
    Thread(target = camera1).start()
    Thread(target = page1).start()
    root.mainloop()




