from Korpora import Korpora
import os
from tokenizers.implementations import BertWordPieceTokenizer

class HanberTest:
    def __init__(self):
        self.nsmc = Korpora.load("nsmc", force_download=True)


    def write_lines(self, path, lines):
        with open(path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(f'{line}\n')
    def exec(self):
        nsmc = self.nsmc
        self.write_lines("data/hanbert/train.txt", nsmc.train.get_all_texts())
        self.write_lines("data/hanbert/test.txt", nsmc.test.get_all_texts())
        wordpiece_tokenizer = BertWordPieceTokenizer(lowercase=False)
        wordpiece_tokenizer.train(
            files=["./data/hanbert/train.txt", "./data/hanbert/test.txt"],
            vocab_size=10000,
        )
        # wordpiece_tokenizer.save_model("/gdrive/My Drive/nlpbook/wordpiece")
        wordpiece_tokenizer.save_model("./save/wordpiece")


if __name__ == '__main__':
    HanberTest().exec()