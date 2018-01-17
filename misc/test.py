def confirmer(code):
    def confirm1(d, t):
        def result(digit):
            if d == digit:
                return t
            else:
                return False
        return result

    def extend(prefix, rest):
        left, last = prefix // 10, prefix % 10
        if prefix == 0:
            return rest
        else:
            return extend(left, confirm1(last, rest))

    return extend(code // 10, confirm1(code % 10, True))
