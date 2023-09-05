input_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
filtered_list = []
for s in input_list:
    if s:
        filtered_list.append(s)

print(filtered_list)