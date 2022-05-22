in_str = input("Rechne: ")
out_str = ""


def n_c_string(s):
    s = s[s.rfind("(") + 1:s.rfind(")")]
    s = s.split(",")
    return s


def calc(base, exponent, mod):
    return pow(base, exponent) % mod


if in_str.find("add") != -1:
    num = n_c_string(in_str)
    out_str = num[0] + num[1]
    print(f"{num[0]} + {num[1]} = {out_str}")

if in_str.find("sub") != -1:
    num = n_c_string(in_str)
    out_str = num[0] - num[1]
    print(f"{num[0]} - {num[1]} = {out_str}")

if in_str.find("mul") != -1:
    num = n_c_string(in_str)
    out_str = num[0] * num[1]
    print(f"{num[0]} * {num[1]} = {out_str}")

if in_str.find("div") != -1:
    num = n_c_string(in_str)
    out_str = num[0] / num[1]
    print(f"{num[0]} / {num[1]} = {out_str}")

if in_str.find("sam") != -1:
    num = n_c_string(in_str)
    y = int(num[0])
    b = bin(int(num[1]))[2:]
    N = int(num[2])
    x = 1
    c = 0
    for i in range(len(b) - 1, -1, -1):
        print(f"{c + 1}. Durchlauf:")
        if b[c] == "0":
            print(" b ist 0")
            y = (x * y) % N
            x = (x * x) % N
        else:
            print(" b ist 1")
            x = (x * y) % N
            y = (y * y) % N
        print(f"    x{i} = {x}")
        print(f"    y{i} = {y}\n")
        c += 1
    if x == 1:
        print(f"Für {num[0]}^{num[1]} mod {num[2]} = {x} gilt: x ist ein Quadrat")
    else:
        print(f"Für {num[0]}^{num[1]} mod {num[2]} = {x} gilt: x ist kein Quadrat")

if in_str.find("dhe") != -1:
    num = n_c_string(in_str)
    prime_p = int(num[0])
    base_g = int(num[1])
    priv_key_a = int(num[2])
    priv_key_b = int(num[3])

    A = calc(base_g, priv_key_a, prime_p)
    B = calc(base_g, priv_key_b, prime_p)

    session_a = calc(A, priv_key_b, prime_p)
    session_b = calc(B, priv_key_a, prime_p)

    print("")
    print("Key A: " + str(A))
    print("Key B: " + str(B))
    print("Session Key: " + str(session_a) + "|" + str(session_b))
