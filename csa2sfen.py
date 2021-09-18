import argparse
import urllib.request

import shogi
import shogi.CSA


class CSA2SFEN:
    def __init__(self, moves: list[str]):
        self.moves = moves

    def __repr__(self):
        return self.moves.__repr__()

    def __len__(self):
        return len(self.moves)

    def to_sfen(self, index: int) -> str:
        board = shogi.Board()
        for i in range(index):
            board.push_usi(self.moves[i])
        return board.sfen()

    @staticmethod
    def from_csa(csa_str: str):
        csa = shogi.CSA.Parser.parse_str(csa_str)[0]
        return CSA2SFEN(csa["moves"])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='将棋のCSA形式の棋譜をSFENのリストに変換するツールです。')
    parser.add_argument('source', type=str, nargs=1,
                    help='CSA形式のファイル名か棋譜')

    args = parser.parse_args()
    assert(len(args.source) == 1)

    source = args.source[0]
    if (source.startswith("http")):
        with urllib.request.urlopen(source) as r:
           csa_str = r.read().decode()
    else:
        with open(source) as f:
            csa_str = f.read()

    cv = CSA2SFEN.from_csa(csa_str)
    for i in range(len(cv)):
        print(cv.to_sfen(i))
