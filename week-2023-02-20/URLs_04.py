"""

4. Generating URLs: You are given the following base URL as a string: BASE_URL = 'https://{environment}.happyapi.com/{endpoint}?access_token={access_token}' .
Given that the environment can be any of the [production, staging, development, sandbox] , endpoint can be any of the [orders, transactions, balance, store] and the
access_token is something specific to a user, create all combinations of URLs by using the
supplied environment and endpoint values. Read the access token from the user in the
beginning. The access token can be any random string that is supplied by the user. Use both
the " string.format() " method and the "f-string" methods to build the strings.
Hint: Store the supplied values for environments and endpoints as lists and use a "for in for"
to iterate all combinations. Don't forget to read from user's input for the access token value.

"""

def main():
    read()
    global no_elements
    no_elements=int(input("How many outliners to be removed: "))
    if check_and_eliminate():
        for element in no_list_copy:
            print(element)
        print("+++++++++++++++")
        for element in no_list:
            print(element)
    else:
        print("List was too short")

if __name__=="__main__":
    main()