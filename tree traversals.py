#!/usr/bin/env python
#
# key takeaways:
# * traversals divided in three types:
#   - depth-first or stack
#   - breadth-first or queue
#   - other
# * the stack techniques are preorder, inorder, postorder
# * the stack techniques are identical, simply positioning the [v]isitor: vLR, LvR, LRv
# * the stack techniques correspond to operator order (prefix, infix, postfix) when traversing expression trees
# * the queue is needed for breadth-first
# * other techniques include boundary traversal and diagonal traversal
# 
# techniques:
#   depth-first traversal (DFS) required stack (explicit or implicit via call/ret)
#     preorder
#     inorder
#     postorder
#   breadth-first traversal (BFS) (requires queue)
# 
# The three DFS techniques are correspond to the operator orders, when the traversal is used on an expression tree:
# 
# traversal  visit order      operator
# ---------  ---------------  -------------------
# preorder   CURR left right  prefix (eg: "+AB")
# inorder    left CURR right  infix  (eg: "A+B")
# postorder  left right CURR  postfix (eg: "AB+")
# 
#    +
#   / \
#  3   *
#     / \
#    2   5
# 
# ('+', 3, ('*', 2, 5))
# 
# preorder: +3*25
# inorder: 3+2*5
# postorder: 325*+
# 
# This is the example tree from the geeksforgeeks.org articles:
#   
#     1
#    / \
#   2   3
#  / \   \
# 4   5   6
# 
# preorder: 124536
# inorder: 425136
# postorder: 452631

def visit_preorder(node):
    if node is None: return
    this, left, right = node
    print(this, end='')
    visit_preorder(left)
    visit_preorder(right)

def visit_inorder(node):
    if node is None: return
    this, left, right = node
    visit_inorder(left)
    print(this, end='')
    visit_inorder(right)

def visit_postorder(node):
    if node is None: return
    this, left, right = node
    visit_postorder(left)
    visit_postorder(right)
    print(this, end='')

def visit_level(node):
    queue = [node]
    while queue:
        this, left, right = queue.pop(0)
        print(this, end='')
        if left: queue.append(left)
        if right: queue.append(right)

tree = ('+', (3, None, None), ('*', (2, None, None), (5, None, None)))

print('preorder: ', end='')
visit_preorder(tree)
print('')
print('inorder: ', end='')
visit_inorder(tree)
print('')
print('postorder: ', end='')
visit_postorder(tree)
print('')

tree = ('1', ('2', ('4', None, None), ('5', None, None)), (3, None, (6, None, None)))

print('preorder: ', end='')
visit_preorder(tree)
print('')
print('inorder: ', end='')
visit_inorder(tree)
print('')
print('postorder: ', end='')
visit_postorder(tree)
print('')
print('level: ', end='')
visit_level(tree)
print('')
