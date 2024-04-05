from redis_db import connect_db
from get_add_quote import post_quote, get_slump_quote

def main():

    while True:
        print("1.Find a quote")
        print("2.Add your quote")


        your_choice = input("Your choice is: ")

        if your_choice == '1':
            print(get_slump_quote())
        elif your_choice == '2':
            your_quote = input("write quote here: ")
            r = connect_db()
            post_quote()
            r.push('new_quotes', your_quote)
        else:
            print("try again")

if __name__ == "__main__":
    main()
