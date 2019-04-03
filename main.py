from mytree import MyTree, insert, in_order_print, pre_order_print, create_tree

with open("words_42.txt") as file:
    data = file.readlines()

words = []

for i in range(len(data)-1):
    data[i] = data[i][:len(data[i]) - 1]
    words.append(data[i])

print(words)
b = MyTree(words)
insert(b, words)
tree = create_tree(words)
in_order_print(tree)
# pre_order_print(words)