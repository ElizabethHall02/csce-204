class Ice_Cream:
    def __init__(self, fl, top, con, ser):
        self.flavor = fl
        self.topping = top
        self.cone = con 
        self.serve = ser
         
class Books:
     def __init__(self, title, author, pages, genre):
         self.title = title 
         self.author = author
         self.pages = pages 
         self.genre = genre 
          
class Pets:
     def __init__(self, species, name, age, color,breed):
         self.species = species 
         self.name = name
         self.age = age 
         self.color = color
         self.breed = breed
                    

new_icecream = Ice_Cream("Mint","Sprinkles","Waffle Cone","Soft serve") 
text_material = Books("If you give a mouse a cookie","Laura Numeroff","40","Children")
vet_clinic = Pets("Dog","Rex","3","Black with white spots","Great Dane")
 
print("Flavor:", new_icecream.flavor)
print("Toppings:", new_icecream.topping)
print("Cone:", new_icecream.cone)
print("Serve Type:", new_icecream.serve)
 
print("Title:", text_material.title)
print("Author:", text_material.author)
print("Pages:", text_material.pages)
print("Genre:", text_material.genre )

print("Species:", vet_clinic.species)
print("Name:", vet_clinic.name)
print("Age:", vet_clinic.age)
print("Color:", vet_clinic.color)
print("Breed:", vet_clinic.breed)
 


