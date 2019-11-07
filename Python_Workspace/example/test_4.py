# time:2018/11/30
class T:
    def __init__(self, *args):
        self.value = [x for x in args]  #构造列表
        self.count = {}.fromkeys(range(len(self.value)), 0)  #构造字典
    def __len__(self):
        return len(self.value)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.value[key]

t1 = T(1,3,5,7,9)
t2 = T(2,4,6,8,10)
print(t1[1])
print(t2[2])
print(t1[1] + t2[2])
print(t1.count)
print(t2.count)