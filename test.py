from bitcoin import *

private_key = random_key()
print(private_key)

public_key = privtopub(private_key)
print(public_key)

address = pubtoaddr(public_key)
print("My Address id : " + address)