#!/usr/bin/env python3
<<<<<<< HEAD

proto = ["ssh", "http", "https"] 
print(proto)
print(proto[1],proto[2])
=======
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

>>>>>>> 5f9b86fa5fe9dbe0253077d6f87d7662cab794a9
