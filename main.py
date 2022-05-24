def c_string(s):
    s = s[s.rfind("(") + 1:s.rfind(")")]
    s = s.split(",")
    return s


def calc(base, exponent, mod):
    return pow(base, exponent) % mod


def valid_string(string, val):
    if len(string) == val:
        for n in range(0, len(string)):
            if not string[n].isnumeric():
                print("Nur Zahlen erlaubt!")
                return False
        return True

    else:
        print("Funktionsargumente falsch!")
        return False


def main():
    print("")
    in_str = input("Rechne: ")
    out_str = ""

    if in_str == "":
        print("Keine valide Eingabe")
        return

    if in_str.find("help") != -1:
        print("")
        print("Funktionen dieses Rechners: \n")
        print("Addition (a + b):                                add(a,b)")
        print("Subtraktion (a - b):                             sub(a,b)")
        print("Multiplikation (a * b):                          mul(a,b)")
        print("Division (a / b):                                div(a,b)")
        print("Wurzel (b√ a):                                   sqrt(a[,b)])")
        print("Modulo (a % b):                                  mod(a,b)\n")
        print("Diffie–Hellman key exchange (b^key mod N):       dhe(N,b,key_a,key_b)")
        print("Square and multiply (b^e mod N):                 sam(b,e,N)")
        print("Polynomreduktion (relation, polynom):            poly_red(relation,polynom)\n")
        print("Rechner beenden:                                 exit")
        return

    if in_str.find("add") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            print(len(num))
            out_str = int(num[0]) + int(num[1])
            print(f"{num[0]} + {num[1]} = {out_str}")
        return

    if in_str.find("sub") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            out_str = int(num[0]) - int(num[1])
            print(f"{num[0]} - {num[1]} = {out_str}")
        return

    if in_str.find("mul") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            out_str = int(num[0]) * int(num[1])
            print(f"{num[0]} * {num[1]} = {out_str}")
        return

    if in_str.find("div") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            out_str = int(num[0]) / int(num[1])
            print(f"{num[0]} / {num[1]} = {out_str}")
        return

    if in_str.find("sqrt") != -1:
        num = c_string(in_str)
        if valid_string(num, 1):
            if len(num) == 1:
                out_str = pow(int(num[0]), 0.5)
                print(f"√{num[0]} = {out_str}")
            else:
                out_str = pow(int(num[0]), (1 / int(num[1])))
                print(f"{num[1]}√{num[0]} = {out_str}")
        return

    if in_str.find("mod") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            out_str = int(num[0]) % int(num[1])
            print(f"{num[0]} mod {num[1]} = {out_str}")
        return

    if in_str.find("sam") != -1:
        num = c_string(in_str)
        if valid_string(num, 3):
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
        return

    if in_str.find("dhe") != -1:
        num = c_string(in_str)
        if valid_string(num, 4):
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
        return

    if in_str.find("poly_red") != -1:
        num = c_string(in_str)
        if valid_string(num, 2):
            relation = int(num[0], 16)
            rel_bin = bin(relation)

            poly = int(num[1], 16)
            poly_bin = bin(poly)

            out = ""

            dist = len(poly_bin) - len(rel_bin)
            while dist >= 0:
                t = (relation << dist)
                poly = t ^ poly
                print(f"{hex(t)} xor {hex(poly)}")
                dist = len(bin(poly)) - len(rel_bin)

            l_str = len(bin(poly)[2:])
            for n in range(0, l_str):
                p_str = str(bin(poly)[2:])
                if p_str[l_str - (n + 1)] == '1':
                    out = f"x^{n} + " + out
                    if out.rfind("x^0") != -1:
                        out.replace("x^0", "1")

            print(out)
        return

    if in_str.find("exit") != -1:
        print("Beende Rechner...")
        print(quit())

    else:
        print("Keine passende Funktion gefunden.")
        return


while 1:
    main()
