import random
import time
import sys

def roll_dice():
    print("Get ready to roll the die!")
    animation = ["Rolling.", "Rolling..", "Rolling..."]
    
    for i in range(3):
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.5)

    result = random.randint(1, 6)
    print(f"\n🎲 You rolled a {result}!")

if __name__ == "__main__":
    input("Press Enter to roll the die... ")
    roll_dice()
