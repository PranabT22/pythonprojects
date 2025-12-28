import time

target_text= "Python is the best language"
print("Type thid fast:")
print(target_text)

input("Enter to start...")
start_time = time.time()

user_input = input("\nStart Typing:")
end_time = time.time()

if user_input == target_text:
  time_taken = end_time - start_time
  print(f"{time_taken=:.2f}seconds")
else:
  print("Try again")
