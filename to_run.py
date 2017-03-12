from Tree import Tree

root_list = []
size = 275

input_file = open('invalidation_data.txt', 'r')
content = input_file.readlines()
length = len(content)
start = 4*length/5
for i in range(start, length):
    line = content[i].split(',')
    root_list.append(int(line[0]))

tree = Tree(root_list, 'all_patent_nums_in_db.txt')
tree.build_tree(size)
tree.txt_output()
