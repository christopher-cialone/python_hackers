

'''
    The Official Python Documentation defines 'namespace' as
    mapping from names to objects, and 'scope' is the textual
    region of a Python program where the namespace is directly
    accessible
'''

# # Built In Scope (def)
# def outer():

#     # Enclosed Scope
#     b = 2
#     def inner():

#         # Local Scope
#         c = 3

greek = "alpha"
    # Print(:Global decalration: "+Greek, id(Greek))
      
def b():
    Greek = "beta"
    print("Inside local: : + greek, id(greek)")
def c():
    greek =  "gamma"
    print("Enclosed: " + greek, id(greek))
c()
print("Inside local: End of local scope: " + greek, id(greek))

b()
print("Global after local execution: " + greek, id(greek))