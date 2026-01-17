selfish = '01234567'
#          01234567 

# [start:stop:stepover]
print(selfish[7])
print(selfish[0:7])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::2])
print(selfish[-1])
print(selfish[::-1])

# immutability
# string cannot be changeable
selfish[0] = '8' # cannot you need to reassign the entire value
selfish = '8' # it works