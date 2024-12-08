# Define a custom class that extends Thread
import threading
import time
class MyThread2(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.num = 5
        self.finish = False

    def run(self):
        for i in range(5, 0, -1):
            print(f"{self.name}: Count {i}")
            time.sleep(1)
        
        self.finish = True
        print(f"Finish attribute set to {self.finish}")

# Create two instances of the MyThread class
thread1 = MyThread2("Thread 1")
thread2 = MyThread2("Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish before continuing
thread1.join()
thread2.join()







# Print a message to indicate that the program has finished
print("Program finished.")


 