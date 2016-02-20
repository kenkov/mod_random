#! /usr/bin/env python
# coding:utf-8


from mod import Mod
import random
import os


class ModRandom(Mod):
    def __init__(
            self,
            filename: str=None,
            train: bool=False,
            logger=None
    ):
        Mod.__init__(self, logger)
        self.dict_path = filename or os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "random_dict.txt"
        )
        self.is_train = train
        self.random_texts = self.load_dict()

    def train(self, message):
        with open(self.dict_path, "a") as f:
            f.write("{}\n".format(message["text"]))

        # reload dict
        self.random_texts = self.load_dict()

    def load_dict(self):
        with open(self.dict_path) as f:
            random_texts = [line.strip() for line in f]
        return random_texts

    def can_utter(self, message, master):
        if self.is_train:
            self.train(message)
            print("Learn new sentence: {}".format(
                message["text"]
            ))
        return True

    def utter(self, message, master):
        return [
            (random.uniform(0, 0.2),
             text, "random", dict())
            for text in self.random_texts
        ]
