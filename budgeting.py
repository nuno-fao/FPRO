def budgeting(budget, products, wishlist):
    out = {}
    for key in sorted(wishlist, key=lambda x: products[x], reverse=True):
        while  wishlist[key]!=0:
            print(key,wishlist[key],products[key],budget)
            budget -= products[key]
            if budget < 0:
                return out
            wishlist[key] -= 1
            if key not in out:
                out[key]=1
            else:
                out[key]+=1
    return out        