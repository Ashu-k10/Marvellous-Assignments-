import threading

# Shared variable
counter = 0

# Lock object
lock = threading.Lock()

# Function executed by each thread
def Increment():
    global counter

    for i in range(1000):
        lock.acquire()      # Acquire lock
        counter += 1
        lock.release()      # Release lock


def main():

    # Create threads
    t1 = threading.Thread(target=Increment, name="Thread1")
    t2 = threading.Thread(target=Increment, name="Thread2")
    t3 = threading.Thread(target=Increment, name="Thread3")

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value :", counter)


if __name__ == "__main__":
    main()