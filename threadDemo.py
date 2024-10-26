import threading, time
print('Начало программы.')

def takeANap():
    time.sleep(5)
    print('Просыпайтесь!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('Конец программы.')
