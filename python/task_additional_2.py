"""
Draw a Christmas tree from triangles using the # (hash) sign in such a way that each level of the Christmas tree is 1 line longer than the previous one. At first, the script should ask about the height of the Christmas tree (number of triangles) and then draw it.
"""

level=int(input("Enter the level of the Christmas tree to generate: "))
height=3
for i in range(0, level):
    for x in range(1, height):
        print(x * "#")
    height+=1
