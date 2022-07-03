st = input()
palavras = []
vogais = [0] * 5
limpa = ''

for s in st.upper():
    if s.isalnum() or s == ' ':
        limpa += s

for p in limpa.split():
    if p not in palavras:
        palavras.append(p)
    for s in p:
        if s in 'AEIOU':
            vogais['AEIOU'.find(s)] += 1

print(len(palavras))
for i in range(5):
    print('AEIOU'[i], vogais[i])
