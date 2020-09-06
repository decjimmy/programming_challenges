
def decomposeAddress(STRaddress):
    address = STRaddress.split(", ")
    separator = ' '
    
    full = [address[0].split(" ")[0]] #Address Number
    full.append(separator.join(address[0].split(" ")[1:])) #address street
    full.append(address[1]) #city
    full.append(address[2].split(" ")[0]) #state
    full.append(address[2].split(" ")[1]) #zip code
    return full




print (decomposeAddress("3315 Vanity St, Beverly Hills, CA 90210"))

print (decomposeAddress("557 Farmer Rd, Corner, MT 59105"))
