t = int(input( ))
for i in range(t):
    rating = int(input())
    if 1900 <= rating:
        x = 1
        print("Division",x)
    if 1600 <= rating and rating <= 1899:
        x = 2
        print("Division",x)
    if 1400 <= rating and rating <= 1599:
        x = 3
        print("Division",x)
    if rating <= 1399:
        x = 4
        print("Division",x)
