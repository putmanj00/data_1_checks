# print hello world
print("Hello World!\n")

# a list populated with several values. They can be strings / integers / floats etc. Then, print() one of those values either to the prompt or in a cell (if using Jupyter Notebook)
ediblePlants = [
    {
        "Nr": 9.0,
        "Name": "Alfalfa",
        "# pics": 50.0,
        "scientific name": "Medicago sativa",
        "description": "A flowering plant in the pea family, Alfalfa is nutritious and may be used for a variety of benefits including; treatment for alcoholism and drug dependency.\nIt has deep roots and can grow quite tall making it very resilient. The leaves and young shoots are the only parts that you can eat raw."
    },
    {
        "Nr": 5.0,
        "Name": "Asparagus",
        "# pics": 100.0,
        "scientific name": "Asparagus",
        "description": "Asparagus, easily identified by its fleshy green spears which are luscious and delicate, can be eaten raw as opposed to boiled. It is a good source of vitamin C and potassium.\n\nBe mindful of wild Asparagus which has a thinner stalk than those usually found in grocery-stores.\n\nHarvest length of these plants are usually 6-8 inches."
    }
]
plantDescription = ediblePlants[0]["description"]
print(f"Printing description of the edible plant Alfalfa: {plantDescription}\n")

# a dictionary populated with two keys and two values. Print one of the values just like you did above.
pineappleWeed = {
    "Nr": 23.0,
    "Name": "Pineapple Weed",
    "# pics": 50.0,
    "scientific name": "Matricaria discoidea",
    "description": "Judging by its name, I would definitely have high hopes for this plant's taste. Pineapple weed's flowers and leaves are, in fact, appetizing finger foods for hikers.\nThe plant is commonly mistaken for chamomile. It does resemble chamomile with the exception of the flower petals. It grows up to 30cm tall.Judging by its name, I would definitely have high hopes for this plant's taste. Pineapple weed's flowers and leaves are, in fact, appetizing finger foods for hikers.\nThe plant is commonly mistaken for chamomile. It does resemble chamomile with the exception of the flower petals. It grows up to 30cm tall."
}
plantScientificName = pineappleWeed["scientific name"]
print(f"The scientific name for pineapple weed is: {plantScientificName}\n")

# a tuple with 4 values. Print one of them.
tuple1 = ("One", 2, {"three": 3.4, "four": 4}, ['five', 6, 'seven'])
print(f"The fourth value of the tuple is: {tuple1[3]} and the third value of that list is: {tuple1[3][2]}")
