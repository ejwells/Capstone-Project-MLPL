from Tree import Tree
# please write your first name ethan, tu, lakshay, jiandi
my_name = 'titouan'
names = ['ethan', 'tu', 'lakshay', 'jiandi', 'titouan']
root_list = []
size = 275


input_file = open('invalidation_data.txt', 'r')
content = input_file.readlines()
length = len(content)

window = {}
for i in range(len(names)):
    start = i*len(content)/5
    stop = (i+1)*len(content)/5
    window[names[i]] = (start, stop)

(start, stop) = window[my_name]
for i in range(start, stop):
    line = content[i].split(',')
    root_list.append(int(line[0]))

tree = Tree(root_list, 'all_patent_nums_in_db.txt')
tree.build_tree(size)
tree.txt_output()
