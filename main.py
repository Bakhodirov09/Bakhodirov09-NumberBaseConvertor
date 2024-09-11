num = int(input('Enter num: '))

def find_operator(number: int):
    def intToBin(n):
        bits = ""
        while n > 0:
            bits += str(0 if n % 2 == 0 else 1)
            n = n // 2
        return bits[::-1]

    def intToDec(n):
        return n

    def intToOct(n):
        octs = ""
        while n > 0:
            octs += str(n % 8)
            n = n // 8
        return octs[::-1]

    def intToHex(n):
        hexes = ""
        hex_values = "0123456789ABCDEF"
        while n > 0:
            remind = n % 16
            hexes += hex_values[remind]
            n = n // 16
        return hexes[::-1]

    print(f"Sonning 2 lik sanoq sistemasidagi ko'rinishi: {intToBin(number)}")
    print(f"Sonning 8 lik sanoq sistemasidagi ko'rinishi: {intToOct(number)}")
    print(f"Sonning 10 lik sanoq sistemasidagi ko'rinishi: {intToDec(number)}")
    print(f"Sonning 16 lik sanoq sistemasidagi ko'rinishi: {intToHex(number)}")

find_operator(num)