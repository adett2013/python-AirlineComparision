print("Welcome to the Airline Chooser 🛫")
print("In the moment you can compare Lufthansa VS Eurowings")
print("The system will ask you questions. You can answer with yes (or y) and no (or n)")
lufthansa = 0
eurowings = 0
question1 = input("Is an included snack and drink on board important to you? ")
if (question1 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question2 = input("Do you have a high budget for your ticket? ")
if (question2 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question3 = input("Do you need checked bags? ")
if (question3 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question4 = input("Is flexibility important to you for rebooking? ")
if (question4 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question5 = input("Are you travelling with kids (family)? ")
if (question5 == "yes"):
  eurowings += 1
else:
  lufthansa += 1
question6 = input("Are you travelling to holiday-places like mallorca? ")
if (question6 == "yes"):
  eurowings += 1
else:
  lufthansa += 1
question7 = input("Do you want to fly from Hamburg Airport directly? ")
if (question7 == "yes"):
  eurowings += 1
else:
  lufthansa += 1
question8 = input("Do you need priority-services like included airport-checkin? ")
if (question8 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question9 = input("Are you flying long-haul? ")
if (question9 == "yes"):
  lufthansa += 1
else:
  eurowings += 1
question10 = input("Is seat-comfort and legroom important to you? ")
if (question10 == "yes"):
  lufthansa += 1
else:
  eurowings += 1

if (eurowings > lufthansa):
  print("-YOUR RESULTS-")
  print("Based on your answers, Eurowings is a better choice for you.")
elif (lufthansa > eurowings):
  print("-YOUR RESULTS-")
  print("Based on your answers, Lufthansa is a better choice for you.")
elif (lufthansa == eurowings):
  extraquestion = input("Is this trip for business? ")
  if (extraquestion == "yes"):
    lufthansa += 1
  else:
    eurowings += 1
  if (eurowings > lufthansa):
    print("-YOUR RESULTS-")
    print("Based on your answers, Eurowings is a better choice for you.")
  elif (lufthansa > eurowings):
    print("-YOUR RESULTS-")
    print("Based on your answers, Lufthansa is a better choice for you.")
