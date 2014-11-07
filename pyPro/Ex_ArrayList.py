
test_data = [
    ["2014-06-01", "APPL", 100.11],
    ["2014-06-02", "APPL", 110.61],
    ["2014-06-03", "APPL", 120.22],
    ["2014-06-04", "APPL", 100.54],
    ["2014-06-01", "MSFT", 20.46],
    ["2014-06-02", "MSFT", 21.25],
    ["2014-06-03", "MSFT", 32.53],
    ["2014-06-04", "MSFT", 40.71],
    ["2014-06-04", "MSF", 40.71]
]

appl = {}
mstf = {}
for a in test_data[]:
    if a[1] == "APPL":
        print [0, 2]
    elif a[1] == "MSFT":
        mstf.append(a)
    else:
        print "ERROR"

print appl
print mstf





#ONCE THAT WORKS THEN what would need to change to copy with an unknown number of stock ticker symbols?