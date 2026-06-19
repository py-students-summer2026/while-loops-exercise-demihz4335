def starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall?")
        if bottles.isdigit() and int(bottles) >= 1:
            return int(bottles)
def song(starting_bottles):
    bottles = starting_bottles
    keep_singing = True
    while keep_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("take it downm, pass it around, no more bottles of beer on the wall.")
            keep_singing = False
        else:
            next_bottles = bottles - 1
            if next_bottles == 1:
                next_bottles_text = "1 bottle"
            else:
                next_bottles_text = f"{next_bottles} bottles"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"take one down, pass it around, {next_bottles_text} of beer on the wall.")
            print()
            bottles -= 1
            