import time

'''
Append [1,1,1] 10000 times to a list: 0.004019
Append (1,1,1) 10000 times to a list: 0.001852
'''

n = 10000

start = time.time()
res = []
for i in range(n):
    res.append([1,1,1])
end = time.time()

print 'Append [1,1,1] %d times to a list: %f' % (n, end - start)

start = time.time()
res = []
for i in range(n):
    res.append((1,1,1))
end = time.time()

print 'Append (1,1,1) %d times to a list: %f' % (n, end - start)
