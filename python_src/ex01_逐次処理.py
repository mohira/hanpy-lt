import time
from pathlib import Path


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

    fetch_data(1)
    fetch_data(2)
    fetch_data(3)

    file1 = Path('file1.txt')
    file2 = Path('file2.txt')
    file3 = Path('file3.txt')

    print(file1.read_text())
    print(file2.read_text())
    print(file3.read_text())

    print('Main done')


if __name__ == '__main__':
    main()
