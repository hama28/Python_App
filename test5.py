import MeCab

str = "となりの隣がとなりのトトロ"
tagger = MeCab.Tagger()
print(tagger.parse(str))