
def wash_hands(X,Y):
    minutes = 0
    seconds = 0
    minutes = X * 21 * Y * 30 // 60
    seconds = X * 21 * Y * 30 % 60
    return f"{minutes} minutes and {seconds} seconds"

print(wash_hands(8, 7))
print(wash_hands(0, 0))
print(wash_hands(7, 9))