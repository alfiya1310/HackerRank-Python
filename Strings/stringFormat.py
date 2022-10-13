def print_formatted(number):
    # your code goes here
    d = len(bin(number)[2:])
        
    for i in range(1,number+1):
        h = hex(i).upper()
        o = oct(i)
        b = bin(i)
        print(str(i).rjust(d), o[2:].rjust(d), h[2:].rjust(d), b[2:].rjust(d))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)