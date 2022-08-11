def rule_substitution(seq):
    new_seq = []
    while seq:
        match seq:
            case [x, y, z, *tail] if x == y == z:
                new_seq.extend(["3", x])
            case [x, y, *tail] if x == y:
                new_seq.extend(["2", x])
            case [x, *tail]:
                new_seq.extend(["1", x])
        seq = tail
    return new_seq

seq = [input()] #работает только с 1 цифрой, более-значные числа просто копируются в хвост
for _ in range(10):
    seq = rule_substitution(seq)
    print("".join(seq))