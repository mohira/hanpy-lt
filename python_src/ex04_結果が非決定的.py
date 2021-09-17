from threading import Thread
from time import sleep


def task(number: int) -> None:
    sleep(0.1)
    print(f'{number},', end='')


def main():
    threads = []

    for i in range(1, 10):
        thread = Thread(target=task, args=(i,), name=f'Thread{i}')
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print('\n=====')
    print('Main done')


if __name__ == '__main__':
    main()
