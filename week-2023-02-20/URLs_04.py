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
def format_string(access_token, enviornment_list, endpoint_list):
    sf_list=[]

    for envi in enviornment_list:
       for endpoint in endpoint_list:
           sf_list.append('https://{envi}.happyapi.com/{endpoint}?access_token={access_token}'.format(envi=envi, endpoint=endpoint, access_token=access_token))
    
    return sf_list



def f_string_method(access_token, enviornment_list, endpoint_list):
    s_list=[]

    for envi in enviornment_list:
        for endpoint in endpoint_list:
            s_list.append(f'https://{envi}.happyapi.com/{endpoint}?access_token={access_token}')
    
    return s_list


def main():
    
    enviornment_list=["production", "staging", "development", "sandbox"]
    endpoint_list=["orders", "transactions", "balance", "store"]
    access_token= input("give access_token: ")
        
    print ("OUTPUT from f-string mode")

    for elem in f_string_method(access_token, enviornment_list, endpoint_list):
        print (elem)

    print ("OUTPUT from format")

    for elem in format_string(access_token, enviornment_list, endpoint_list):
        print (elem)
  

if __name__=="__main__":
    main()