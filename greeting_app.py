# -----------------------------
#   My First Python Project
# -----------------------------

# User details (change these values if you want)
name = "Yasmin"
age = 18
s = 5   # how many times to print Hello World

# Title
print("===================================")
print("   🌟 Welcome to the Greeting App 🌟")
print("===================================\n")

# Greeting section
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Motivational message
if age < 18:
    print("✨ You are still young and have a bright future ahead! 🚀")
else:
    print("💪 You are an adult, keep working hard on your goals!")

print("\n--- Printing Hello World ---")
for i in range(s):
    print("Hello World " + str(i + 1))

print("\n===================================")
print("        🎉 End of the App 🎉       ")
print("===================================")