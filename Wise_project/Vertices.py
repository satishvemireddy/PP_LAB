# For Triangle

def Triangle(row,col):
    if row[0] == row[1]:
       dst = col[1] - col[0]
       return dst>0 and col[2] == col[1] and row[2] == row[0]+dst
    else:
        dst = row[1] - row[0]
        return dst > 0 and col[0] == col[1] and row[2] == row[1] and col[2] == col[1]+dst

# For Parallelogram

def Parallelogram(row,col):
     if row[0] == row[1]:
        dst = col[1] - col[0]
        return dst>0 and row[2] == row[3] and col[3]-col[2] == dst and row[2]-row[0] == dst and (col[2] == col[0] or col[2] == col[1])
     else:
        dst = row[1] - row[0]
        return dst>0 and col[0] == col[1] and col[2] == col[3] and row[1] == row[2] and row[3]-row[2] == dst and col[2]-col[1] == dst
   
# For Hexagon

def Hexagon( row,col):
    dst = col[1] - col[0]

    return dst>0 and row[0] == row[1] and col[2] == col[0] and row[2] == row[0]+dst and col[3] == col[1]+dst and row[3] == row[2] and col[4] == col[1] and row[4] == row[2]+dst and col[5] == col[3] and row[5] == row[4]

def RowCol(p):
    row = cnt = 0
    while True:
        row+=1
        for col in range(row):
            cnt+=1
            if cnt == p:
                return row, col+1
def main():
    try:
        while True:
            points = list(map(int, input().strip().split()))
            points = sorted(points)
            n = len(points)
            i = 0
            row = []
            col = []
            while i < n:
                 x,y = RowCol(points[i])
                 row.append(x)
                 col.append(y)
                 i += 1
            # print (row, col)
            if n == 3 and Triangle(row, col):
                print("forms a Triangle")
            elif n == 4 and Parallelogram(row,col):
                print("forms a Parallelogram")
            elif n == 6 and Hexagon(row,col):
                print("forms a Hexagon")
           
    except ValueError:
        exit()
print(main())
