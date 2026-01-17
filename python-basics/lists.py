# Lists
li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a',True]

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0:2])
print(amazon_cart[0::2])
amazon_cart[0] = 'laptop'
#if you try this one (new_cart = amazon_cart) they both be the same since they point to the same value in memory
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(amazon_cart[1:3])
print(amazon_cart)
