phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# plist.pop(0)
# for w in range(4):
#     plist.pop()
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))

plist = plist[1:8]
print(plist)
plist.remove("'")
plist.extend([plist.pop(3), plist.pop(2)])
plist.extend(plist[3:1:-1])
plist.pop(1)
plist.pop(2)

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
