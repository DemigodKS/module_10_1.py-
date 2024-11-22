from datetime import datetime
from os import write
from time import sleep
#import threading
import time
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
        print(f'Завершилась запись в файл {file_name}')
        time.sleep(0.1)


start_time1 = datetime.now()
print(f'start_time1: {start_time1}')
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
finish_time1 = datetime.now()
print(f'finish_time1: {finish_time1}')
all_time = finish_time1 - start_time1
print(f'Работа потоков {all_time}')

start_time2 = datetime.now()
print(f'start_time2: {start_time2}')
t1 = Thread(target=write_words(10, 'example5.txt'))
t2 = Thread(target=write_words(30, 'example6.txt'))
t3 = Thread(target=write_words(200, 'example7.txt'))
t4 = Thread(target=write_words(100, 'example8.txt'))
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
finish_time2 = datetime.now()
print(f'finish_time2: {finish_time2}')
print(f'Работа потоков {finish_time2 - start_time2}')