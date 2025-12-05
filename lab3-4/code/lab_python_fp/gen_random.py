from random import randint

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)

if __name__ == "__main__":
    for num in gen_random(10, 3, 20):
        print(num, end=" ")
    print()