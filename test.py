import random

# Secret number between 1 and 50
secret = random.randint(1, 50)
attempts = 5
won = False

print("Welcome to the Number Guessing Game!")
print("I have picked a secret number between 1 and 50.")
print(f"You have {attempts} attempts to guess it. Good luck!\n")

while attempts > 0:
  # 1. Read the player's guess using int(input())
  try:
    guess = int(input("Enter your guess (1-50): "))
  except ValueError:
    print("Please enter a valid integer!")
    continue

  # Check if the player won
  if guess == secret:
    print(f"🎉 Congratulations! You guessed the secret number {secret}!")
    won = True
    break
  else:
    attempts -= 1

    # 3. Hint system (ice cold, cold, warm, hot) based on distance
    diff = abs(secret - guess)
    if diff >= 20:
      hint = "🧊 Ice cold!"
    elif diff >= 10:
      hint = "🥶 Cold!"
    elif diff >= 5:
      hint = "🌡️ Warm!"
    else:
      hint = "🔥 Hot!"

    print(f"Wrong guess! Hint: {hint}")

    # 4. For loop to show remaining ❤️ hearts after each wrong guess
    print("Remaining lives: ", end="")
    for _ in range(attempts):
      print("❤️ ", end="")
    print("\n")

# 6. Win/loss message and revealing secret number if attempts run out
if not won:
  print(
      f"❌ You ran out of attempts! The secret number was {secret}. Better luck"
      " next time!")