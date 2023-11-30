
def chekered_board (row: int , column: int):
    for j in range (row):
        for i in range (column):
            if ((i%2==0 and j%2==0) or (i%2==1 and j%2==1)):
                print("#",end="")
            else:
                print("*",end="")
        print( )

n = int(input("Please enter the rows: "))
m = int(input("Please enter the columns: "))

chekered_board(n, m)