import random
import time

def flip_a_coin(option_a="Чай", option_b="Кофе"):
    print(f"Выбираю между: '{option_a}' и '{option_b}'...")
    time.sleep(1)
    result = random.choice([option_a, option_b])
    print("🪙 Монетка говорит:", result.upper() + "!")
    return result

# Пример:
# flip_a_coin("Пицца", "Суши")
