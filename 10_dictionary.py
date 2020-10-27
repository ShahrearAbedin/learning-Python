# Dictionary is nothing but key value pairs
dic = {}
dic = {
    "Shadhin": {"M": "Rooti",
                "L": "Rice",
                "E": "Tea",
                "N": "Rice"
                },
    "Shahrear": "Fish",
    "Abedin": "Meat",
    "Bhuiyan": "Roast"
}
dic2 = dic.copy()
del dic2["Shadhin"]
dic.update({"Ishmam": "Noodles"})
print(dic.items())