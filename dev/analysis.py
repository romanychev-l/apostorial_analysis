import math


def get_graph():
    f = open('uploads/file.txt')

    Q = []
    FQ = []
    AL = []
    BE = []
    X = []
    flag = 0
    for line in f:
        if flag == 0:
            n, kol = line.split()
            n = int(n)
            flag += 1
            continue
        flag = 0
        data = list(map(int, line.split()))
        print("n ", n)
        print("data ", data[:10])

        data = data[:5000]

        m = len(data)

        print(data[:10])

        FMI = min(data)
        FMA = max(data)
        fmi = 1
        fma = n

        t = []
        for d in data:
            t.append((d - fmi)/(fma - fmi))

        z = fma - fmi
        fmi /= z
        fma /= z

        print(t[:10])

        k = int(m ** 0.5)
        print("len data ", len(data))
        print("k ", k)

        import matplotlib.pyplot as plt

        #plt.hist(t, bins=k, range=(0, 1), density=True)
        #plt.show()


        f_t = sum(t) / m
        print(f_t)

        t_ = (f_t - fmi) / (fma - fmi)

        s_2 = 0
        for fi in t:
            s_2 += (fi - f_t) ** 2 / (fma - fmi) ** 2
        s_2 /= m - 1

        al = t_ * (t_ - t_ ** 2 - s_2) / s_2
        be = (1 - t_) * (t_ - t_ ** 2 - s_2) / s_2
        AL.append(al)
        BE.append(be)

        print(al, be)
        from scipy.stats import beta
        from scipy import integrate, stats

        import numpy as np

        q = beta.ppf(0.5 + 0.95 / 2, al, be) - beta.ppf(0.5 - 0.95 / 2, al, be)

        #fq = FMI + q * (fma - fmi)
        fq = FMI + q * (FMA - FMI)

        Q.append(n)
        FQ.append(fq)
        X.append(n)
        print(q, fq)

    #print("q ", Q)
    #print("fq ", FQ)
    #print("alpha ", AL)
    #print("beta ", BE)

    fig, ax = plt.subplots()

    ax.plot(Q, FQ, label = r'$V_{\gamma}(n)$')
    ax.plot(Q, X, label = 'Теоретический максимум')
    ax.legend()

    plt.xlabel("Размер входа, n")
    plt.ylabel("Объем памяти")

    #plt.plot(Q, FQ, label = 'Vy(n)')
    #plt.plot(Q, X, label = 'Теоретический максимум')
    #plt.show()

    plt.savefig('images/img2.jpg', dpi=300, bbox_inches='tight')

