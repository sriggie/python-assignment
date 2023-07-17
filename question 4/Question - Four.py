# #  the are the steps i followed to set the data structure 

# Create two empty sets to store the observations for each game park.
# Start a loop to repeatedly ask the user for the name of the animal observed in each park.
# For each park:
# a. Prompt the user to enter the name of the animal observed.
# b. Add the animal name to the respective set for that park.
# c. If the user enters 'q', exit the loop.
# Display the observations for the first game park by printing the elements of the set.
# Display the observations for the second game park by printing the elements of the set.
# Find the common observations in both game parks by using the intersection operation on the two sets.
# Display the observations that were common in both game parks by printing the elements of the common set.
# Find the observations made in the first game park only by using the difference operation on the two sets.
# Display the observations made in the first game park only by printing the elements of the difference set.
# Find the total number of animals observed in the second park only by using the difference operation on the two sets.
# Display the total number of animals observed in the second park only by printing the length of the difference set.



# added an ectra funvtion for better UI experinece 
observations_park1 = set()
observations_park2 = set()

while True:
    animal_park1 = input("Enter the animal observed in the first park (or 'q' to quit): ")
    if animal_park1 == 'q':
        break

    observations_park1.add(animal_park1)

while True:
    animal_park2 = input("Enter the animal observed in the second park (or 'q' to quit): ")
    if animal_park2 == 'q':
        break

    observations_park2.add(animal_park2)

print("Observations for the first game park:")
for animal in observations_park1:
    print(animal)

print("Observations for the second game park:")
for animal in observations_park2:
    print(animal)

common_observations = observations_park1.intersection(observations_park2)
print("Observations common in both game parks:")
for animal in common_observations:
    print(animal)

observations_park1_only = observations_park1.difference(observations_park2)
print("Observations made in the first game park only:")
for animal in observations_park1_only:
    print(animal)

observations_park2_only = observations_park2.difference(observations_park1)
total_animals_park2_only = len(observations_park2_only)
print("Total number of animals observed in the second park only:", total_animals_park2_only)
