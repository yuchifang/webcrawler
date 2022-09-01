from pathlib import Path
p = Path('.')
[x for x in p.iterdir() if x.is_dir()]

# print("iterdir", p.iterdir())

# print("isDir",)
for x in p.iterdir():
    print("xxxx", x)
