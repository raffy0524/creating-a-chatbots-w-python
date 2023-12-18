# Step 1: Create some lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Step 2: Create a two-dimensional list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Print gradebook
print("Initial Gradebook:")
print(gradebook)

# Step 3: Add more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Step 4: Modify the gradebook
# Increase the grade for visual arts by 5 points
gradebook[4][1] += 5

# Remove the numerical grade for poetry and add "Pass"
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Step 5: One Big Gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook

# Print the final gradebook
print("\nFinal Gradebook:")
print(full_gradebook)
