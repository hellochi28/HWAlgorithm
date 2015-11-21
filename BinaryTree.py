operator_precedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

def postfix_convert(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        if char not in operator_precedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[len(stack) - 1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operator_precedence[char] > operator_precedence[stack[len(stack) - 1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
     
    while len(stack) != 0:
        postfix.append(stack.pop())
 
    return postfix
 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class ExressionTree(object):
    def __init__(self, root = None):
        self.__root = root 
     
    def inorder(self):
        self.__inorder_helper(self.__root)
         
    def __inorder_helper(self, node):
        if node:
            self.__inorder_helper(node.left)
            print node.value,
            self.__inorder_helper(node.right)
 
    def preorder(self):
        self.__preorder_helper(self.__root)
         
    def __preorder_helper(self, node):
        if node:
            print node.value,
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)
 
    def postorder(self):
        self.__postorder_helper(self.__root)
         
    def __postorder_helper(self, node):
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            print node.value,

    def print_tree(self):
        self.__print_tree(self.__root)

    def __print_tree(self, node, name='root', lv=1):
        if node:
            print name,"\tlv %s: "%(lv),node.value
            self.__print_tree(node.left,'left',lv+1)
            self.__print_tree(node.right,'right',lv+1)

    def result(self):
        return self.__result(self.__root)

    def __result(self, node):
        if node:
            if node.value in operator_precedence:
                left=self.__result(node.left)
                right=self.__result(node.right)
                result=eval('%s%s%s'%(left,node.value,right))
                return result
            else:
                return node.value
 
def create_expression_tree(infix):
    global stack,postfix
    postfix = postfix_convert(infix)
 
    stack = []
 
    for char in postfix:
        if char not in operator_precedence:
            node = Node(char)   
            stack.append(node)
        else:
            node = Node(char)
            right = stack.pop()
            left = stack.pop()
            node.right = right
            node.left = left
            stack.append(node)
    return ExressionTree(stack.pop())


## x = create_expression_tree( รับค่าได้ 3 แบบ(infix,postfix,prefix))
## x.inorder()      show infix          แสดงแบบ infix
## x.postorder()    show postfix        แสดงแบบ postfix
## x.preorder()     show prefix         แสดงแบบ prefix
## x.print_tree()   show binary tree    แสดงเป็น BinaryTree
## x.result()       return result       คืนค่าผลลัพธ์

x1="(2(51-)*)(32*)+"    # รับแบบ postfix **/โจทย์ตัวอย่าง/**
x2="(6-2)*3"            # รับแบบ infix value **/สมมติขึ้นมาเพื่อทดสอบโปรแกรม/**

print "\nx1 = %s"%(x1)
y1=create_expression_tree(x1)
print "Infix: ",
y1.inorder()
print "\nPostfix: ",
y1.postorder()
#print "\nPrefix: ",
y1.preorder()
print "\n\nx1 print binary tree:"
y1.print_tree()
print "\nresult of x1 = %s"%(y1.result())


print "\nx2 = %s"%(x2)
y2=create_expression_tree(x2)
print "Infix: ",
y2.inorder()
print "\nPostfix: ",
y2.postorder()
#print "\nPrefix: ",
y2.preorder()

print "\n\nx2 print binary tree:"
y2.print_tree()

print "\nresult of x2 = %s"%(y2.result())

