import time

def keep_alive():
    print("Keeping the process alive...")
    while True:
        time.sleep(60)  # Sleep for 60 seconds

if __name__ == "__main__":
    keep_alive()
