# BeatWordle
Wordle対策のアルゴリズムです．同じ文字が複数ある場合の，wordle側の仕様を知らないので，その場合はバグります．

# 使いかた
main.pyの入っているフォルダに候補単語のリストを乗せたファイル(hoge.txt)を入れてください．

そのうえで 

```
python main.py hoge.txt
```

としてください．

すべての単語が同じ文字数で，改行区切りであれば問題ありません．

下記のファイルを入れてもらえば問題ないはずですが，著作権不明のためリンクのみ張ります．

https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57


# BeatWordle
it is an algorithm for solving wordle problems.

I don't know what Wordle return when there are same letters in a word, so it may not work in this case.

# How to use
Place a word-list file(hoge.txt) in the same folder with main.py.

Run
```
python main.py hoge.txt
```

The word-list file must satisfy
- all words have same # of letters
- each words are separated by a line feed charactor.
See this format.
https://gist.github.com/cfreshman/dec102adb5e60a8299857cbf78f6cf57
