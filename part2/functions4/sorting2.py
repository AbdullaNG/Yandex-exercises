def sorting_bis(key, reverse):
    if key == "abc":
        data.sort(reverse=reverse)
    elif key == "len":
        data.sort(key=len, reverse=reverse)


data = ["use", "plan", "guy", "case", "view", "way", "government"]
sorting_bis("len", False)
print(data)