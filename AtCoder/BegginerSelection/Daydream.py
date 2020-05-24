s = input()
s = s[::-1]
# print(s)
key = 0
#print(s[:5])
while len(s) > 0:
    if s[:5] in ['maerd', 'esare']:
        s = s[5:]
        #print(s)
    elif s[:6] == 'resare':
        s = s[6:]
        #print(s)
    elif s[:7] == 'remaerd':
        s = s[7:]
        #print(s)
    else:
        key = 1
        break
if key == 0:
    print('YES')
else:
    print('NO')