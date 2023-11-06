"""
    Midterm not next week, but the week after that.
    
    Binary Decimal and Hex
    
    since we only have on-off switches we need something that we can encode
    as either 0 or 1
    
    binary = base 2
    decimal = base 10
    hexadecimal = base 16
    
    decimal means base 10:
        - 10 digits (0, 1,2, 3,4,5,6,7,8,9)
        - each slot increases by a power of 10
    
    582 (dec) = 5(10^2) + 8(10^1) + 2(10^0)
    
    binary
        - 2 binary digits [bit]
            they can only have 0 or 1 as bits
        - each slot increases by a power of 2
     
    bin --> dec
    
    1011 = 1(2^0) + 1(2^1) + 0(2^2) + 1(2^3) = 8 + 2 + 1 = 11
    11001 = 1(2^0) + 0(2^1) + 0(2^2) + 1(2^3) + 1(2^4) = 16 + 8 + 1 = 25
    Space between every four bits:
        4 bits makes a nibble
        2 nibbles, 8 bits makes a byte
    0110 1110 = 0(2^0) + 1(2^1) + 1(2^2) + 1(2^3)
                + 0(2^4) + 1(2^5) + 1(2^6) + 0(2^7)
                = 2 + 4 + 8 + 32 + 64 = 110
    
    bin <-- dec
    start with a number to convert
    repeat while number > 0
        is the number odd?
            if it is, add a 1
            else add a 0
        int-divide number by 2
    
    13 into binary
    13 odd => 6 even => 3 odd => 1 odd => 0 (done)
    <-----
    1101
    72 into binary
    72 (even) => 36 (even) => 18 (even) => 9 (odd) => 4 (even)
        => 2 (even) => 1 (odd) => 0 (done)
    0100 1000
    8 + 64 = 72
    072 vs 72
    
    193 into binary
    193 (odd) => 96 (even) => 48 (even) => 24 (even) => 12 (even)
        => 6 (even) => 3 (odd) => 1(odd)
    1100 0001
    1 + 64 + 128 = 193
    
    Hexadecimal - Base 16
        put binary numbers in a more readable format
        
        slight problem with base 16
        16 digits
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            A=10, B=11, C=12, D=13, E=14, F=15
        What about 16?
            10 (hex)
            
            ____ ___  ___ ____
            4096 256s 16s 1's
            
    convert from hex <-> bin
    
    binary  dec hex     binary  dec hex
    0000    0   0       1000    8   8
    0001    1   1       1001    9   9
    0010    2   2       1010    10  a or A
    0011    3   3       1011    11  b or B
    0100    4   4       1100    12  c or C
    0101    5   5       1101    13  d or D
    0110    6   6       1110    14  e or E
    0111    7   7       1111    15  f or F
    
    
    0110 1110 1101 1111 1001 1011
    0x6edf9b
    
    1110 0011 1001 1000 0111 0001 0000
    0xe398710
    
    0x123 (hex)
    1 * 256 + 2 * 16 + 3 = 291
    
    ff34
    1111 1111 0011 0100
    
    abcdef
    1010 1011 1100 1101 1110 1111
    
    6a3d4c
    0110 1010 0011 1101 0100 1100
    
    bin <-> dec
    bin <-> hex
    to do:
    hex <-> dec
    
    2ad to decimal
    2(256) + 10(16) + 13
    512 + 160 + 13 = 685
    
    a3c into decimal
    10(256) + 3(16) + 12 = 2560 + 48 + 12 = 2620
    
    3de into decimal
    3(256) + 13(16) + 14
    
    (10 + 3)(16) = 160 + 48 = 208
    768 + 208 + 14 = 990
    
    c3 = 12(16) + 3 = (160 + 32) + 3 = 195
    examable
    
    not examable
    6a3d
    6(4096) + 10(256) + 3(16) + 13
    6(4000 + 100 - 4) = 24000 + 600 - 24 = 24576
                                            2560
                                              48
                                              13
                                           27197
    dec into hex
    
    start with a number to convert
    repeat while number > 0
        mod it by 16
            that's the digit
        int-divide number by 16
        
    73 into hex
    73 mod 16
    73 - 4(16) = 73 - 64 = 9
    73 // 16 =4
    
    0x49 = 4 * 16 + 9 = 64 + 9 = 73
    
    188 into hex
    188 mod 16 =
    188 - 176 = 188 - 11(16) = 12
    188//16 = 11
    
    0xbc
"""

x = 589321678
print(bin(x))

x = 0x123
print(x)

x = 21
print(x)

x = 0b10010010101010
print(bin(x), type(bin(x)))


def num_to_hex(number):
    hex_map = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
        8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
    }
    result = ''
    if number == 0:
        return '0x0'
    while number > 0:
        result = hex_map[number % 16] + result
        number //= 16
    return '0x' + result

print(num_to_hex(x), hex(x))

print(num_to_hex(0), hex(0))