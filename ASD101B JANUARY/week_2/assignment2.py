lst1 = ['salamander','triceratops','cheetah','puma']

lst2 = ['banana','banana','banana','banana','orange you glad I didn\'t say banana?']



if len(lst1) < len(lst2):
    print(lst1)
elif len(lst1) > len(lst2):
    print(lst2[-1])
else:
    print(lst1)[-1], lst2[-2]