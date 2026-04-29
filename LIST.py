###   List methods ####
# 1.basic list methods
# lst = [1, 2]

# lst.append(3)
# print(lst)   # [1, 2, 3]

# lst.extend([4, 5])
# print(lst)   # [1, 2, 3, 4, 5]

# lst.insert(1, 10)
# print(lst)   # [1, 10, 2, 3, 4, 5]

# lst.remove(10)
# print(lst)   # [1, 2, 3, 4, 5]

# lst.pop()
# print(lst)  #[1, 2, 3, 4[]]

# print(lst.pop(1))  # 2
# print(lst)         # [1, 3, 4, 5]

# lst.clear()
# print(lst)   # []

# 2.searching and sorting methods
# lst = [3, 1, 2]

# lst.sort()
# print(lst)   # [1, 2, 3]

# lst.sort(reverse=True)
# print(lst)   # [3, 2, 1]

# print(sorted([3, 1, 2]))  # [1, 2, 3]

# lst = [1, 2, 3]
# lst.reverse()
# print(lst)   # [3, 2, 1]
# 3.Searching and counting methods
# lst = [1, 2, 2, 3]

# print(lst.index(2))   # 1
# print(lst.count(2))   # 2
# print(2 in lst)       # True
# print(5 in lst)       # False

# 5.advanced methods
# lst = [1, 2, 3]

# print(len(lst))   # 3
# print(sum(lst))   # 6
# print(max(lst))   # 3
# print(min(lst))   # 1

# print(any([0, 1, 0]))  # True
# print(all([1, 2, 3])) 
#######################################################
# List slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]

# String slicing
text = "Python"
print(text[1:4])      # yth
print(text[::-1])     # nohtyP (reverse)