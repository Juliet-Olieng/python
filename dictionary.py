capital_city={"Nepal":"kathmandu","Italy":"rome","England":"London"}
print(capital_city)

capital_city["Japan"]="Tokyo"
print("Updated Dictionary:", capital_city)
del capital_city["England"]
print("Updated Dictionary:", capital_city)
capital_city["Japan"]="newland"
print("Updated Dictionary:", capital_city)
print("kenya" in capital_city)
print(capital_city.keys())
print(capital_city.__len__())
print(capital_city.values())

squares={1:1,3:9,5:25,7:49,9:81}
for i in squares:
    print(squares[i])