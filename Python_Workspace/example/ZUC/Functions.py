import ZUC.ConstParameters as cp

def Int2Bin(a, k):
    res = list(bin(a)[2:])
    for i in range(k - len(res)):
        res.insert(0, '0')
    return ''.join(res)

def LoopLeftShift(a, k):
    res = list(Int2Bin(a, 32))
    for i in range(k):
        temp = res.pop(0)
        res.append(temp)
    return int(''.join(res), 2)

def KeyLoading(Key, iv):
    Key_Str = Int2Bin(Key, 128)
    iv_Str = Int2Bin(iv, 128)
    res = []
    for i in range(16):
        temp = Key_Str[i * 8:(i + 1) * 8]
        temp += cp.D[i]
        temp += iv_Str[i * 8:(i + 1) * 8]
        res.append(int(temp, 2))

    return res


def BitRec(LFSR):
    X0 = Int2Bin(LFSR[15], 31)[:16] + Int2Bin(LFSR[14], 31)[15:]
    X1 = Int2Bin(LFSR[11], 31)[15:] + Int2Bin(LFSR[9], 31)[:16]
    X2 = Int2Bin(LFSR[7], 31)[15:] + Int2Bin(LFSR[5], 31)[:16]
    X3 = Int2Bin(LFSR[2], 31)[15:] + Int2Bin(LFSR[0], 31)[:16]
    return [int(X0, 2), int(X1, 2), int(X2, 2), int(X3, 2)]

def S(a):
    a = Int2Bin(a, 32)
    index = []
    for i in range(8):
        index.append(int(a[4 * i:4 * (i + 1)], 2))
    return SBox(index[0], index[1], 1) + SBox(index[2], index[3], 2) + \
           SBox(index[4], index[5], 1) + SBox(index[6], index[7], 2)


def SBox(a1, a2, k):
    if k == 1:
        return Int2Bin(cp.S1[a1][a2], 8)
    else:
        return Int2Bin(cp.S2[a1][a2], 8)

def LFSRMode(u, LFSR, k):
    s16 = 2 ** 15 * LFSR[15] + 2 ** 17 * LFSR[13] + 2 ** 21 * LFSR[10] + 2 ** 20 * LFSR[4] + \
          (1 + 2 ** 8) * LFSR[0]
    if k == 1:
        s16 = (u + s16) % (2 ** 31 - 1)
    else:
        s16 = s16 % (2 ** 31 - 1)
    if s16 == 0:
        s16 = 2 ** 31 - 1
    LFSR.pop(0)
    LFSR.append(s16)
    return LFSR

def F(X, R1, R2):
    modulus = 2 ** 32
    W = ((X[0] ^ R1) + R2) % (modulus)
    W1 = (R1 + X[1]) % (modulus)
    W2 = R2 ^ X[2]
    temp1 = Int2Bin(W1, 32)[16:32] + Int2Bin(W2, 32)[:16]
    temp2 = Int2Bin(W2, 32)[16:32] + Int2Bin(W1, 32)[:16]
    temp1 = int(temp1, 2)
    temp2 = int(temp2, 2)
    temp1 = temp1 ^ (LoopLeftShift(temp1, 2)) ^ (LoopLeftShift(temp1, 10)) ^ \
            (LoopLeftShift(temp1, 18)) ^ (LoopLeftShift(temp1, 24))
    temp2 = temp2 ^ (LoopLeftShift(temp2, 8)) ^ (LoopLeftShift(temp2, 14)) ^ \
            (LoopLeftShift(temp2, 22)) ^ (LoopLeftShift(temp2, 30))
    R1 = S(temp1)
    R2 = S(temp2)
    return W, int(R1, 2), int(R2, 2)

def init(Key, iv):
    LFSR = KeyLoading(Key, iv)
    R1, R2 = 0, 0
    for i in range(32):
        X = BitRec(LFSR)
        W, R1, R2 = F(X, R1, R2)
        LFSR = LFSRMode(W >> 1, LFSR, 1)
    X = BitRec(LFSR)
    W, R1, R2 = F(X, R1, R2)
    LFSR = LFSRMode(W >> 1, LFSR, 2)
    return LFSR, R1, R2

def work(LFSR, R1, R2):
    X = BitRec(LFSR)
    W, R1, R2 = F(X, R1, R2)
    Z = W ^ X[3]
    LFSR = LFSRMode(W >> 1, LFSR, 2)
    return LFSR, R1, R2, Z

key = input("请输入初始密钥：")
iv = input("请输入初始向量：")
n = input("请输入密钥个数：")
LFSR, R1, R2, = init(int(key), int(iv))
for i in range(int(n)):
    LFSR, R1, R2, ZA = work(LFSR, R1, R2)
    print("第" + str(i) + "个密钥为：" + hex(ZA))