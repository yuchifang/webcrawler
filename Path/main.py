from pathlib import Path
p = Path('.')
# for x in p.iterdir():
#     print("sss", x)
"https://docs.python.org/3/library/pathlib.html"

# print(list(p.glob('**/*.py')))

p = Path('/etc')
q = p / 'init.d'/'reboot'
print(q.resolve())
