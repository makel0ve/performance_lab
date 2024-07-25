def main():
    print("Введите путь к файлу с данными:")
    a = input()
    f1 = open(a, 'r')
    nums = [int(i.strip()) for i in f1]
    f1.close()
    mid = (max(nums) + min(nums)) // 2
    s = 0
    
    for i in range(len(nums)):
        s += abs(nums[i] - mid)
    
    
    return s


if __name__ == "__main__":
    print(main())