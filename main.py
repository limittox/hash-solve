from hashes.md5 import MD5
from timeit import default_timer as timer

with open('../rockyou.txt',encoding='utf-8', errors='ignore') as f:
    start=timer()
    wordlist = f.read().splitlines()
    end=timer()

print(f'File read time: {end-start}')

with open('rulesBasic.rule',encoding='utf-8') as f:
    rules = f.read().splitlines()


# print(wordlist)
# 4229d691b07b13341da53f17ab9f2416
# print(MD5().encrypt("hell")) 

# yathu
# print(MD5().decrypt("caaa325b4a9411820027611af3d90cf3"))

# hell
# print(MD5(wordlist).decrypt("4229d691b07b13341da53f17ab9f2416"))

# f.close()
# timert = d353427dce3b700e92a76a79098f7f8f
# print(MD5().encrypt("timert")) 
# print(MD5(wordlist).decrypt("d353427dce3b700e92a76a79098f7f8f"))

# hello = 5d41402abc4b2a76b9719d911017c592
# print(MD5().encrypt("hello"))
# print(MD5(wordlist, rules).decrypt("5d41402abc4b2a76b9719d911017c592"))

# raprap = de94a2b5bb89232d55e250bc0b87ea0b | 5000th line in rockyou.txt
# print(MD5(wordlist, rules).decrypt("de94a2b5bb89232d55e250bc0b87ea0b"))

# 1mann19906 = bc0a63aef289456481501f41abe1d56c | 13,000,500th line in rockyou.txt
print(MD5(wordlist, rules).decrypt("bc0a63aef289456481501f41abe1d56c"))

# Raprap = c986008b920825bffd0491b444cf50ee | Modification of 5000th line in rockyou.txt (First letter capital)
# print(MD5(wordlist, rules).decrypt("c986008b920825bffd0491b444cf50ee"))

# sagar = ada15bd1a5ddf0b790ae1dcfd05a1e70
# print(MD5(wordlist, rules).decrypt("41ed44e3038dbeee7d2ffaa7f51d8a4b"))