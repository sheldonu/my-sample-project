# Tic-Tac-Toe Assignment -- Sheldon Uchytil

def main():
    x_turn_1()
    o_turn_1()

def x_square_1():
    print("""
    x|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def x_square_2():
    print("""
    1|x|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def x_square_3():
    print("""
    1|2|x
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def x_square_4():
    print("""
    1|2|3
    -+-+-
    x|5|6
    -+-+-
    7|8|9
    """)

def x_square_5():
    print("""
    1|2|3
    -+-+-
    4|x|6
    -+-+-
    7|8|9
    """)

def x_square_6():
    print("""
    1|2|3
    -+-+-
    4|5|x
    -+-+-
    7|8|9
    """)

def x_square_7():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    x|8|9
    """)

def x_square_8():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|x|9
    """)

def x_square_9():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|x
    """)

def o_square_1():
    print("""
    o|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def o_square_2():
    print("""
    1|o|3
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def o_square_3():
    print("""
    1|2|o
    -+-+-
    4|5|6
    -+-+-
    7|8|9
    """)

def o_square_4():
    print("""
    1|2|3
    -+-+-
    o|5|6
    -+-+-
    7|8|9
    """)

def o_square_5():
    print("""
    1|2|3
    -+-+-
    4|o|6
    -+-+-
    7|8|9
    """)

def o_square_6():
    print("""
    1|2|3
    -+-+-
    4|5|o
    -+-+-
    7|8|9
    """)

def o_square_7():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    o|8|9
    """)

def o_square_8():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|o|9
    """)

def o_square_9():
    print("""
    1|2|3
    -+-+-
    4|5|6
    -+-+-
    7|8|o
    """)

def x_turn_1():
    Q1x = int(input("x's turn to choose a sqaure (1-9): "))
    if Q1x == 1:
        x_square_1()
        return Q1x
    elif Q1x == 2:
        x_square_2()
        return Q1x
    elif Q1x == 3:
        x_square_3()
        return Q1x
    elif Q1x == 4:
        x_square_4()
        return Q1x
    elif Q1x == 5:
        x_square_5()
        return Q1x
    elif Q1x == 6:
        x_square_6()
        return Q1x
    elif Q1x == 7:
        x_square_7()
        return Q1x
    elif Q1x == 8:
        x_square_8()
        return Q1x
    elif Q1x == 9:
        x_square_9()
        return Q1x
    else:
        print('oops, try again.')
        x_turn_1()

def o_turn_1():
    Q1o = int(input("o's turn to choose a sqaure (1-9): "))
    if Q1o == 1:
        o_square_1()
        return Q1o
    elif Q1o == 2:
        o_square_2()
        return Q1o
    elif Q1o == 3:
        o_square_3()
        return Q1o
    elif Q1o == 4:
        o_square_4()
        return Q1o
    elif Q1o == 5:
        o_square_5()
        return Q1o
    elif Q1o == 6:
        o_square_6()
        return Q1o
    elif Q1o == 7:
        o_square_7()
        return Q1o
    elif Q1o == 8:
        o_square_8()
        return Q1o
    elif Q1o == 9:
        o_square_9()
        return Q1o
    else:
        print('oops, try again.')
        o_turn_1()




main()