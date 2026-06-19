def starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall? ")
        if bottles.isdigit() and int(bottles) >= 1:
            return int(bottles)
        
def song(starting_bottles):
    for bottles in range(starting_bottles, 0, -1):
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall {bottles} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall.")
        else:
            next_bottles = bottles - 1
            if next_bottles == 1:
                next_bottles_text = "1 bottle"
            else:
                next_bottles_text = f"{next_bottles} bottles"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {next_bottles_text} of beer on the wall.")
            if bottles > 1:
                print()
            