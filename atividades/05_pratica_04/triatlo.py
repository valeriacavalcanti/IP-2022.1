h,m,s = input().split(":")
h,m,s = int(h),int(m),int(s)
total = h*60**2 + m*60 + s

h,m,s = input().split(":")
h,m,s = int(h),int(m),int(s)
total += h*60**2 + m*60 + s

h,m,s = input().split(":")
h,m,s = int(h),int(m),int(s)
total += h*60**2 + m*60 + s

h = total // 60**2
m = total % 60**2 // 60
s = total % 60**2 % 60

print(h,m,s,sep=":")
