def prime(no: int) ->bool:
    i=2
    if no==0:
        return False
    else:
        while i<no:
            if no%i==0:
                return False
            
            return True
        