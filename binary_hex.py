"""
    Midterm next week - we'll release a practice exam.
        Wednesday
        No Lab during exam week
    But there will be homework.
    
    Binary-Hexadecimal-Decimal
    
    Most computers operate in binary.
        Except quantum computers - we're not going to worry about that.
        
    Two "digits" 0 or 1
    Octal - Base 8
    Hexadecimal - Base 16
    Decimal - Base 10
    
    What is decimal?
        10 digits - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            each place is a power of 10
        72 = 7(10^1) + 2(10^0)
        32768 = 3(10^4) + 2(10^3) + 7(10^2) + 6(10) + 8
        
        5 = (1)2^2 + 0(2^1) + (1)2^0 = 101b
        8 = 2^3 + 0(2^2) + 0(2^1) + 0(2^0) = 1000b
        
        1101b = 1 + 0(2) + 1(4) + 1(8) = 13
        
        
        26 for example and we want to convert it into binary
        is it even?
            if it is then we put a zero
            if it's odd we put a 1
        divide by 2 (integer divide)
        keep doing it until you get down to zero
        
        26 even => 13 odd => 6 even => 3 odd => 1 odd => 0 done
        11010b
        <--- direction
        2 + 8 + 16 = 26 yes
        171d into binary
        171 odd => 85 odd => 42 even => 21 odd => 10 even => 5 odd =>
            2 even => 1 odd => 0(done)
        1010 1011
        1 + 2 + 8 + 32 + 128 = 171 yes we did it.
        4 bits makes a nibble
        
        234 into binary
            116/2 = (100 + 16)/2 = 50 + 8
            (50 + 8) /2= 25 + 4 or (60 - 2)/2 = 30 - 1
        234 even => 117 odd => 58 even => 29 odd => 14 even => 7 odd
            => 3 odd => 1
        1110 1010
        2 + 8 + 32 + 64 + 128 = 234
        
        __    ___  ___
        100s  10s  1s
        
        ___  ___ ___ ___ ___ ___ ___ ___ ___ ___ ___
        1024 512 256 128 64s 32s 16s 8's 4's 2's 1's
        2^10 2^9 2^8 2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0
        binary <-> decimal
        
        base 16 => hexadecimal [reduce the number of digits/bits that
                                    we have to write]
        slight problem about 16
        we need 16 digits, but we have 10
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                a = 10, b = 11, c = 12
                d = 13, e = 14, f = 15
        
        10h = 16 in decimal
        binary  decimal hex     binary  decimal hex
        0000    0       0       1000    8       8
        0001    1       1       1001    9       9
        0010    2       2       1010    10      a or A
        0011    3       3       1011    11      b or B
        0100    4       4       1100    12      c or C
        0101    5       5       1101    13      d or D
        0110    6       6       1110    14      e or E
        0111    7       7       1111    15      f or F
        
        whole purpose of the hex usage:
            very very easy to go from binary <-> hex
    1001 1011 1100 1010 0101 1000
    9bca58
    
    1000 1010 0011 1111
    8a3f
    
    0101 = 101 NOT 1010 [this is 10]
    5
    
    fc35 convert it into binary [just use the table again]
    1111 1100 0011 0101
    
    64 bit number = big
    1000 1010 0011 1111 1000 1010 0011 1111 1000 1010 0011 1111 1000 1010 0011 1111
    
    e76a2 into binary
    1110 0111 0110 1010 0010
    
    0110 = 110 = 6 dec
    
    dec <-> hex
    [hard]
    
    secret: actually essentially the same as the conversion from
        binary <-> dec
        
    d = 13 dec [use the table
    d3 ??
    13 * 16 + 3 = 208 + 3 = 211 (dec)
    
    3f2 = 3(16^2) + f * (16) + 2
        = 3(256) + 15 * 16 + 2
        = 768 + 240 + 2 = 1010 (dec)
        
    0x791 (hex) = 7(16^2) + 9(16) + 1 = 1937
    
    0x33a = 3(256) + 3(16) + 10
            768 + 48 + 10 = 826
            
    dec -> hex
    
    283 into hex
        mod the number by 16
            that's the hex digit
        divide by 16 (integer divide)
        keep doing it until you get down to zero
    11 => b
        17 mod 16 = 1
    17 // 16 = 1
    
    0x11b <----- direction
    
    8391 dec into hex => 524
    524 mod 16 = 12 => c
    32 mod 16 = 0
    32//16 = 2
    0x20c7
    
    Testable:
    73
    73 mod 16?
        73 - 64 = 9 that's it
            subtract off 16s until you're in range
    73//16 = 4
    0x49
    49 (hex)
"""

x = 0b1011
print(x)
# print always gives you the decimal representation
y = 0xaf4521
print(y)

z = 32749824987
print(bin(y))
print(hex(z), type(hex(z)))

"""
    in python you can write
    0b0101010 for binary
    0xabcd for hex
        0xbad = this is hex to python
        bad
"""
def number_to_hex(number):
    number_map = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5",
                  6: "6", 7: "7", 8: "8", 9: "9", 10: 'a', 11: 'b',
                  12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    result = ''
    if number == 0:
        return '0x0'
    
    while number > 0:
        next_digit = number_map[number % 16]
        result = next_digit + result
        number //= 16
    
    return '0x' + result



x = int(input('>> '))
while x != -2:
    print(number_to_hex(x), hex(x))
    x = int(input('>> '))

