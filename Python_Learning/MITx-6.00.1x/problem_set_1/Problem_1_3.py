from doctest import REPORT_CDIFF
def item_order(order):
    salad = 0
    hamburger = 0
    water = 0
    startplace = 0
    space = 0
    while space > -1:
        space = order.find(' ', startplace)
        if space == -1:
            item = order[startplace:]
        else:
            item = order[startplace:space]
        if item == 'salad':
            salad += 1
        if item == 'hamburger':
            hamburger += 1
        if item == 'water':
            water += 1
        startplace = space + 1
    report = str(salad) + str(hamburger) + str(water)
    return report

print item_order("salad water hamburger salad hamburger")
        