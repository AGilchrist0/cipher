alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphacurrent = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher = input("Cipher:\n").lower()

for i in range(25):
    plain = ""
    alphacurrent.append(alphacurrent.pop(0))
    for j in cipher:
        if j in alphabet:
            plain += alphacurrent[alphabet.index(j)]
        else:
            plain += j
    print("Shift " + str(i + 1) + ":\n" + plain + "\n")
