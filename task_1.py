import queue
import random
import time

requests_queue = queue.Queue()
request_id = 1


def generate_request():
    global request_id
    request = f"Заявка #{request_id}"
    print(f"[+]{request} створена")
    requests_queue.put(request)
    request_id += 1


def process_request():
    if not requests_queue.empty():
        request = requests_queue.get()
        print(f"[✓]{request} оброблена")
    else:
        print("[!] Черга пуста, немає заявок для обробки")


if __name__ == "__main__":
    for _ in range(5):
        generate_request()
        time.sleep(random.uniform(0.5, 1.0))
        process_request()
        time.sleep(random.uniform(0.5, 1.0))
