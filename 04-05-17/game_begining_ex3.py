groceries={
    "banana",
    "orange",
    "apple"
    }
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
b=set(stock)
c=set(prices)
a=b.intersection(c)
##for i in a:
##    print(stock[str(i)]*prices[str(i)]) test only
def compute_bill(food):
##    food=list(food)
    total=0
    for i in food:
        if i in a and stock[str(i)]>0:
            total=total+prices[str(i)]
            stock[str(i)]-=1
    print(stock)
x=['banana','apple','banana','apple','orange']       
compute_bill(x)
