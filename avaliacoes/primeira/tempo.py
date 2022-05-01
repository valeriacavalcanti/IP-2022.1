h, m, s = input().split(":")
h, m, s = int(h), int(m), int(s)

tempo = h * 3600 + m * 60 + s

h = (tempo * 2) // 3600
m = (tempo * 2) % 3600 // 60
s = (tempo * 2) % 3600 % 60
print("{}:{}:{}".format(h, m, s))

h = (tempo * 3) // 3600
m = (tempo * 3) % 3600 // 60
s = (tempo * 3) % 3600 % 60
print("{}:{}:{}".format(h, m, s))
