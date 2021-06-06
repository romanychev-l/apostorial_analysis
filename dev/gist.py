import math

def get_plt():
    #f = open('uploads/dfs_10000_200.txt')
    f = open('uploads/file.txt')

    data = []
    flag = 0
    for line in f:
        if flag == 0:
            flag = 1
            continue
        else:
            flag = 0
            d = list(map(int, line.split()))
            if len(d):
                data = d
            break
            #data.append(int(line))

    print(data[:10])
    #data = data[:7000]

    m = len(data)

    fmi = 1
    fma = 200

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
    import numpy as np

    x = np.linspace(0, 1, k)

    plt.hist(t, bins=k, range=(0, 1), density=True)
    plt.title("Гистограмма относительных частот")
    plt.xlabel("Значение ресурсоемкости")
    plt.ylabel("Частота")
    #plt.show()


    f_t = sum(t) / m
    print('f_t', f_t)

    t_ = (f_t - fmi) / (fma - fmi)

    s_2 = 0
    for fi in t:
        s_2 += (fi - f_t) ** 2 / (fma - fmi) ** 2
    s_2 /= m - 1

    al = t_ * (t_ - t_ ** 2 - s_2) / s_2
    be = (1 - t_) * (t_ - t_ ** 2 - s_2) / s_2

    print(al, be)
    from scipy.stats import beta
    from scipy import integrate, stats

    '''
    q = beta.ppf(0.5 + 0.95 / 2, al, be) - beta.ppf(0.5 - 0.95 / 2, al, be)

    fq = fmi + q * (fma - fmi)

    Q.append(q)

    x = np.linspace(beta.ppf(0, al, be), beta.ppf(1, al, be), k)
    '''
    print(x)

    p = beta.pdf(x, al, be)
    plt.plot(x, p, 'r-', lw=2, alpha=0.6, label='beta pdf')

    #plt.plot(t, y)
    #plt.show()
    plt.savefig('images/img.jpg', dpi=300, bbox_inches='tight')

    p = [integrate.quad(lambda _x : beta.pdf(_x, al, be), x[i], x[i+1])[0] for i in range(len(x)-1)]

    print(len(p))
    print(sum(p))

    w = []
    su = 0
    for i in range(len(x)-1):
        s = 0
        for j in t:
            if x[i] <= j and j < x[i+1]:
                s += 1
        su += s
        w.append(s / len(t))
    print("sum ", su)
    print("p ", p)

    print("w ", w)
    print(sum(w))

    x_2 = 0
    for i in range(len(w)):
        if p[i]:
            x_2 += (w[i] - p[i]) ** 2 / p[i]

    x_2 *= m

    print(x_2)
    return x_2
