

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