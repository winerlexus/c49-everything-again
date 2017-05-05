#prices dictionary
prices={"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
#stock dictionary
stock={'banana': 6,
    'apple' : 0,
    'orange': 32,
    'pear': 15,
}
##method 1:
'''
for key in prices:
    print(key,':', prices[str(key)])'''

##method 2:
total=0
for a,b in prices.items():
    for c,d in stock.items():
        if a==c:
            print(a,':','price: ',b,'stock:',d)
            mul=b*d
            total=total+mul
print(total)
print(a,':',b)
