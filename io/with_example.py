class Proces:
    def __enter__(self):
        print('Start procesu...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Koniec procesu!')


with Proces():
    print('test...')
