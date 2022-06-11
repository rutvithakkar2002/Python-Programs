stack=[1,2,3,4,5,6]
print("Original stack is: ",stack)
stack.append(7)
print("stack after push operation: ",stack)
stack.pop()
print("stack after pop operation: ",stack)
last_element_index=len(stack)-1
print(stack[last_element_index])

