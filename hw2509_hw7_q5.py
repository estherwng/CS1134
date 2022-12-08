from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    prefix_exp_lst = prefix_exp_str.split()
    operators = '+-*/'
    for i in range(len(prefix_exp_lst)):
        if prefix_exp_lst[i] in operators:
            pass
        else:
            prefix_exp_lst[i] = int(prefix_exp_lst[i])

    def create_expression_tree_helper(prefix_exp, start_pos):
        if isinstance(prefix_exp[start_pos], int):
            subtree = LinkedBinaryTree.Node(prefix_exp[start_pos])
            return (subtree, 1)
        else:
            left = create_expression_tree_helper(prefix_exp, start_pos + 1)
            right = create_expression_tree_helper(prefix_exp, start_pos + left[1] + 1)
            root = LinkedBinaryTree.Node(prefix_exp[start_pos], left[0], right[0])
            return (root, left[1] + right[1] + 1)

    return LinkedBinaryTree(create_expression_tree_helper(prefix_exp_lst, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    prefix_tree = create_expression_tree(prefix_exp_str)

    def prefix_to_postfix_helper(root):
        if root.left is None and root.right is None:
            return str(root.data)
        else:
            left = prefix_to_postfix_helper(root.left)
            right = prefix_to_postfix_helper(root.right)
            root_data = root.data
            return str(left + " " + right + " " + root_data)

    return prefix_to_postfix_helper(prefix_tree.root)

