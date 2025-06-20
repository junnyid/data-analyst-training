import random

# Danh sách gồm 10 số và 5 chữ cái
lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]

# Chọn ngẫu nhiên 4 phần tử
win_ticket = random.sample(lottery_numbers, 4)

# In ra kết quả
print("Winning ticket:", win_ticket)
print("Any ticket matching these 4 numbers or letters wins a prize!")
