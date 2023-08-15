
import random

class Utils:
    def xor(a, b):
        p = 1
        c = 0
        while a > 0 and b > 0:
            ra = a % 2
            rb = b % 2
            if ra != rb:
                c = c + p
            a = (a - ra) / 2
            b = (b - rb) / 2
            p = p * 2

        if a < b:
            a = b

        while a > 0:
            ra = a % 2
            if ra > 0:
                c = c + p
            a = (a - ra) / 2
            p = p * 2
        return c

    def ShuffleArray(array, SHUFFLE = True):
        if SHUFFLE == False: return array
        for i in range(len(array)):
            j = random.randint(0, len(array) - 1)
            array[i], array[j] = array[j], array[i]
        return array

    def AssignBits(Arr):
        Ret = {}
        Len = 0
        for Idx in range(len(Arr)):
            v = Arr[Idx]
            Ret[v["Name"]] = [Len, Len + v["Length"] - 1]
            Len += v["Length"]
        return Ret

    def WriteBits(Arr, Vals):
        Int32 = 0
        for K in Arr:
            aaa = Vals.__getitem__(K)
            if aaa != None:
                Int32 |= (aaa << Arr[K][0])

        return Int32
        