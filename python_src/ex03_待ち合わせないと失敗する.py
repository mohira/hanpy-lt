import time
from pathlib import Path
from threading import Thread


def preprocess():
    """処理を再現するために、生成されるtxtを削除するヘルパー関数"""
    file_paths = sorted(Path(__file__).parent.glob('*.txt'))

    for file_path in file_paths:
        if file_path.exists():
            file_path.unlink(missing_ok=True)


def fetch_data(n: int) -> None:
    """WebAPIのレスポンスを取得して、どこかに永続化するイメージ"""
    time.sleep(n)

    with open(f'file{n}.txt', 'w') as f:
        f.write(f'hello from #{n}')

    print(f'task{n} done')


def main():
    preprocess()

    thread1 = Thread(target=fetch_data, args=[1], name='Thread1')
    thread2 = Thread(target=fetch_data, args=[2], name='Thread2')
    thread3 = Thread(target=fetch_data, args=[3], name='Thread3')

    thread1.start()
    thread2.start()
    thread3.start()

    file1 = Path('file1.txt')
    file2 = Path('file2.txt')
    file3 = Path('file3.txt')

    print(file1.read_text())
    print(file2.read_text())
    print(file3.read_text())

    print('Main done')


if __name__ == '__main__':
    main()
