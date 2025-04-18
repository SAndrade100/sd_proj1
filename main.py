import sys, os
sys.path.append(os.path.abspath('./map_reduce'))
from map_reduce import utils, mapper, shuffle, reducer
import multiprocessing

def main(path):
    chunks = list(utils.split_file(path, num_chunks=10))
    with multiprocessing.Pool(processes=len(chunks)) as pool:
        pool.map(mapper.mapper, chunks)
    shuffle.shuffle()
    reducer.reducer()
    print("MapReduce completo")

if __name__ == "__main__":
    path = './data/arquivo.txt'
    if not os.path.exists(path):
        print(f"Arquivo {path} não encontrado.")
        sys.exit(1)
    main(path)