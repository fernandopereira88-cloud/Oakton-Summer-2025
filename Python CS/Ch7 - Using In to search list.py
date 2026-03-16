def main():
    prod_nums = ['A','B','C']

    search = input('Enter product ID:')

    if search in produ_nums:
        print(f'{search} was found!')
    else:
        print(f'{search} was NOT found!')

if __name__ == '__main__':
    main()
