counts = dict()
names = ["csev", "cwen", "csev", "zquan", "cwen"]
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

# countss = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(countss.get('kris', 0))
# print(countss)