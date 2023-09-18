home1 = [int(i) for i in input().split()]
away1 = [int(i) for i in input().split()]
home2 = [int(i) for i in input().split()]
away2 = [int(i) for i in input().split()]
game1 = None
game2 = None
if sum(home1) > sum(away1):
    game1 = True
else:
    game1 = False
if sum(home2) > sum(away2):
    game2 = True
else:
    game2 = False
print(f"{sum(home1)}:{sum(away1)}")
print(f"{sum(home2)}:{sum(away2)}")
if game1 != game2:
    print("Tie")
elif game1 == True:
    print("Win")
else:
    print("Lose")
