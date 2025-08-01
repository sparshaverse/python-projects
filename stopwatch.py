import time

print("Press Enter to start the stopwatch")
print("Press Enter again to stop it")
start_time = time.time()

input()
end_time = time.time()


elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")