
#1
import time
import random

def create_file_with_random_number(i):
    time.sleep(1)
    random_number = random.randint(1, 100)  
    with open(f"file_{i}.txt", "w") as file:
        file.write(str(random_number))  


#2
start_time = time.time()


for i in range(1, 1001):
    create_file_with_random_number(i)

end_time = time.time()
elapsed_time = end_time - start_time




#3
import threading

start_time = time.time()


threads = []
for i in range(1, 1001):
    thread = threading.Thread(target=create_file_with_random_number, args=(i,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


end_time = time.time()


elapsed_time = end_time - start_time
print(f"{elapsed_time:.2f} секунд")







