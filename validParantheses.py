class Solution:
  # Time: O(n)
  # Space: O(n)
  def isValid(self, s : str) -> bool:
    # create a stack, purpose of serve is to store the valid paratheses
    stack = []
    # this hashMap helps us to check and get the closing parantheses's opening one.
    closeToOpen = { "}" : "{", "]" : "[", ")" : "("}
    # using for loop, iterate the given string, s with char c
    for c in s:
      # if c in closeToOpen, we found the  c is closingPair
      if c in closeToOpen:
        # if the stack is not empty and top of the stack equals the c in closeToOpen hashMap, then pop the parentheses
        if (stack and stack[-1] == closeToOpen[c]):
          stack.pop()
        else:
          return False
      else: # if c is an opening bracket, push it to stack as it's waiting for its match
        stack.append(c)
    # This line basically checks if the stack is empty print true, not false. 
    # Reason is that we have to have an empty stack, so we can be sure we solved the problem & found pairs to each and every paratheses.
    return True if not stack else False
