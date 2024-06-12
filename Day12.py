#Global vs Local Scope
# Global scope is the scope in which all functions are in, and even the starting code. Any variable created and accessed by all functions and all parts of the program are in the global scope.
#local scope is a scope created by functions and the indents the functions create. Anything within a function is seperate from the global scope, and in that space, it is considered local scope.
# use the keyword 'global' to modify a global variable inside a local space. THIS IS NOT RECOMMENDED, as it is prone to creating bugs
#instead, you would want to return a value changed from a function to the global variable
