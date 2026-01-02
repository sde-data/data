if __name__ == '__main__':
    try:
        n = int(input().strip())
    except KeyboardInterrupt:
        print("\nExecution interrupted by user")
        sys.exit(0)

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Weird")
    elif 6 <= n <= 20:
        print("Not Weird")
    else:
        print("Weird")
