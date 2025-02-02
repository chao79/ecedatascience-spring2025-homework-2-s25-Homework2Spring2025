from typing import List, Tuple, Dict

def histogram(d: dict) -> list:
    a, b, c, e = d['data'], d['n'], d['min_val'], d['max_val']

    if c == e:
        print("Error: min_val and max_val are the same value")
        return []

    if b <= 0:
        return []

    if c > e:
        c, e = e, c

    f = [0] * b
    g = (e - c) / b

    for i in a:
        if c <= i < e:
            j = min(b - 1, int((i - c) / g))
            f[j] += 1

    return f

def combine_birthday_data(a: List[Tuple[str, int]], 
                          b: List[Tuple[str, int]], 
                          c: List[Tuple[str, int]]) -> Dict[int, Tuple]:
    y, d = 2025, {}

    for i, j in a:
        d[i] = {'d': j}
    
    for i, j in b:
        if i in d:
            d[i]['m'] = j
    
    for i, j in c:
        if i in d:
            d[i]['y'] = j
            d[i]['a'] = y - j
    
    r = {}

    for i, j in d.items():
        m = j.get('m')
        if m is not None:
            t = (i, j['d'], j['y'], j['a'])
            if m in r:
                if isinstance(r[m], list):
                    r[m].append(t)
                else:
                    r[m] = [r[m], t]
            else:
                r[m] = t

    return r
