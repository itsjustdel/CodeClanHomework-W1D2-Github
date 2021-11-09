users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
twitter_handle_jonathon = users["Jonathan"]["twitter"]

# 2. Get Erik's hometown
hometown_erik = users["Erik"]["home_town"]

# 3. Get the array of Erik's lottery numbers
lottery_numbers_erik = users["Erik"]["lottery_numbers"]

# 4. Get the species of Avril's pet Monty
species_of_avrils_pet = users["Avril"]["pets"][0]["species"]

# 5. Get the smallest of Erik's lottery numbers
lottery_numbers_erik.sort()
smallest = lottery_numbers_erik[0]

# 6. Return an array of Avril's lottery numbers that are even

#create a list to populate with even numbers
lottery_numbers_avril_even = [] 
#use a for loop to iterate through list
for lottery_number in users["Avril"]["lottery_numbers"]:
  #use modulo operator to determine if number is even (if no fraction left over afer division, then we have an even number)
    if lottery_number %2 == 0:
      lottery_numbers_avril_even.append(lottery_number)

#lottery_numbers_avril_even will now have only even numbers in it

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "Fluffy"
users["Erik"]["pets"].append({"name" : "fluffy", "species" : "dog"})

# 10. Add another person to the users dictionary
users["Jimmy"] = {
    "twitter": "weeJimmyBimmy",
    "lottery_numbers": [1, 2, 3, 4, 123 ,12],
    "home_town": "Paris",
    "pets": [
    {
      "name": "razza",
      "species": "fish"
    },
    {
      "name": "mataz",
      "species": "cat"
    },
    {
      "name": "dingwall",
      "species": "lizard"
    }
  ]
}
