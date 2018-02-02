def fac(dest):
    print("function called, currently processing number : ", dest)
    if dest == 1:
        return 1

    return dest * fac(dest - 1)

print(fac(13))