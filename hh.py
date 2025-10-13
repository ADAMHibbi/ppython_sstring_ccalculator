import random
import time
import statistics

def r_s(tab, v):
    c = 0
    for x in tab:
        c += 1
        if x == v:
            return True, c
    return False, c

def r_s_o(tab, v):
    c = 0
    for x in tab:
        c += 1
        if x == v:
            return True, c
        if x > v:
            return False, c
    return False, c

def r_b_i(tab, v):
    g, d = 0, len(tab) - 1
    c = 0
    while g <= d:
        c += 1
        m = (g + d) // 2
        if tab[m] == v:
            return True, c
        elif tab[m] < v:
            g = m + 1
        else:
            d = m - 1
    return False, c

def r_b_r(tab, v, g, d, c=0):
    if g > d:
        return False, c
    c += 1
    m = (g + d) // 2
    if tab[m] == v:
        return True, c
    elif tab[m] < v:
        return r_b_r(tab, v, m + 1, d, c)
    else:
        return r_b_r(tab, v, g, m - 1, c)

def test(f, tab, v):
    t0 = time.perf_counter_ns()
    _, c = f(tab, v)
    t1 = time.perf_counter_ns()
    return c, (t1 - t0) / 1e6

tailles = [10000, 100000, 1000000]
for n in tailles:
    print(f"\n========== {n} ")
    res = {"r.s": [], "r.s.o": [], "r.b.i": [], "r.b.r": []}
    for _ in range(30):
        tab = sorted(random.sample(range(n * 4), n))
        v = random.choice(tab)
        res["r.s"].append(test(r_s, tab, v))
        res["r.s.o"].append(test(r_s_o, tab, v))
        res["r.b.i"].append(test(r_b_i, tab, v))
        res["r.b.r"].append(test(lambda t, val: r_b_r(t, val, 0, len(t)-1), tab, v))
    for k in res:
        comps = [x[0] for x in res[k]]
        times = [x[1] for x in res[k]]
        print(f"{k}: moy={statistics.mean(times):.3f}ms  | o={statistics.stdev(times):.3f} | cmp={int(statistics.mean(comps))}")

