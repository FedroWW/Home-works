
# к чему приводит ссылочная модель данных
a = [[0]*5]*5
a[0][0] = 5
print(a)


# list comprehensions
a = [[1 for i in range(5)] for j in range(5)]
a[0][0] = 5
print(a)


# изменяемые типы
# list, dict, set
# неизменяемые
#string, int, float, tuple, bool
# литералы типов:
# string - ''/"", tuple - (), list - [], dict - {}, set - {}

# d = {1:3, 3:[2,3], 'a':2} #только неизменяемые типы могут быть ключами!
# d = {key1:value1, key2:value2}
# d[key1] -> value1
#d = {1:3} - словарь
#s = {3} - множество


#s = {3}
#print(s)
#s.add(3)
#print(s)
#s.add(5)
#print(s)


#a = list(map(int, input().split()))
#map:
# map(int, ['1','2','3']) -> [int('1'),int('2'),int('3')]
#print(list(map(float, input().split())))



f = open('input.txt','r')
print(f.readlines())
f.close()

f = open('input.txt','w')
f.write('abacaba')
f.close()

f = open('input.txt','a')
f.write('\n5555')
f.close()

#print('3\n5')


a = [i for i in range(50)]

print(a[1:12:2])
b = [1,2,3,4,5]
print(b[::-2])
