# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# main.py : wordle倒すマン
from asyncio.windows_events import NULL
import re
import sys


class BeatWordle:
    NUM_OF_LETTERS = 0
    WORD_LIST_FILE = 'allowed.txt'
    possible_word_set = set()
    total_word_set = set()
    dictionary = dict()

    def __init__(self, arg=""):
        print(arg)
        if arg != "":
            self.WORD_LIST_FILE = str(arg)
        with open(self.WORD_LIST_FILE) as word_list_file:
            for data in word_list_file:
                if self.NUM_OF_LETTERS == 0:
                    self.NUM_OF_LETTERS = len(data) - 1
                if data != "":
                    self.possible_word_set.add(data[0: self.NUM_OF_LETTERS])
                    self.total_word_set.add(data[0: self.NUM_OF_LETTERS])
        # self.make_dictionary()

    """ メモリ消費量えげつないのでコメントアウト
    def make_dictionary(self):
        for word in self.total_word_set:
            for answer in self.total_word_set:
                self.dictionary[word+"_"+answer] = self.judge_word(word, answer)
        print("word: judge, answer:cubeb" + self.dictionary['judge_cubeb'])
        print("word: gombo, answer:godso" + self.dictionary['gombo_godso'])
        print("word: judge, answer:judge" + self.dictionary['judge_judge'])"""

    def judge_word(self, word, answer):
        letter_state = ""
        for i in range(self.NUM_OF_LETTERS):
            if word[i] == answer[i]:
                letter_state = letter_state + 'B'
            elif word[i] in answer:
                letter_state = letter_state + 'H'
            else:
                letter_state = letter_state + 'N'
        return letter_state

    def main_logic(self):
        while True:
            next_word = self.decide_next_word()
            print("The next word is " + next_word)
            result = self.recieve_result(next_word)
            if result == "B"*self.NUM_OF_LETTERS:
                print("The answer is " + next_word)
                break
            self.squeeze_possible_word_set(next_word, result)

    def decide_next_word(self):
        if(len(self.possible_word_set)) == 0:
            print("No possible word. Please check wordlist")
            return ""
        if(len(self.possible_word_set)) == 1:
            for word in self.possible_word_set:
                return word
        min_max_candidate = len(self.possible_word_set) + 1
        candidate = ""
        num_of_candidates = dict()
        tmp = 0
        for total_word in self.total_word_set:
            if tmp % 1000 == 0:
                print(str(tmp)+"words in "+str(len(self.total_word_set))+" words.")
            tmp += 1
            num_of_candidates.clear()
            for possible_word in self.possible_word_set:
                result = self.judge_word(total_word, possible_word)
                if result not in num_of_candidates.keys():
                    num_of_candidates[result] = 0
                num_of_candidates[result] += 1
            if min_max_candidate > max(num_of_candidates.values()):
                candidate = total_word
                min_max_candidate = max(num_of_candidates.values())
            elif min_max_candidate == max(num_of_candidates.values()) and total_word in self.possible_word_set:
                candidate = total_word
        return candidate

    def recieve_result(self, next_word):
        print("please input result. the format is 'BBHNN'\n (B:bite, H:hit, N:nothing)\nIf there isn't the suggested word, send 'NO'")
        while True:
            result = input()
            if result == "NO":
                self.possible_word_set.remove(next_word)
                self.total_word_set.remove(next_word)
                break
            print(result+str(len(result))+str(re.match(r'[BNH]+', result)))
            if len(result) != self.NUM_OF_LETTERS or not re.match(r'[BNH]+', result):
                print("please write with the format. the format is 'BBHNN'\n (B:bite, H:hit, N:nothing)\n")
            else:
                break
        return result
    
    def squeeze_possible_word_set(self, next_word, result):
        if result == "NO":
            return
        removing_set = set()
        for word in self.possible_word_set:
            if self.judge_word(next_word, word) != result:
                removing_set.add(word)
        self.possible_word_set -= removing_set


if __name__ == '__main__':
    if len(sys.argv) == 1:
        beatWordle = BeatWordle()
    else:
        beatWordle = BeatWordle(sys.argv[1])
    beatWordle.main_logic()