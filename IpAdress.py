def check_if_private(ip_address: str) -> bool:

    ip_parts = ip_address.split(".")
    first_number = int(ip_parts[0])

    if first_number == 10 or (first_number == 192 and int(ip_parts[1]) == 168) or \
            (first_number == 172 and 16 <= int(ip_parts[1]) <= 31):
        return True

def check_class(ip_address: str) -> str:
    
    ip_parts = ip_address.split(".")
    first_number = int(ip_parts[0])
   
    if first_number < 128:
        return "A"

    elif first_number < 192:
        return "B"

    elif first_number < 224:
        return "C"

    elif first_number < 240:
        return "D"
    
    elif first_number < 254:
        return "E"



def check_ip(ip_address:str) -> str: 
    is_private = check_if_private(ip_address)
    ip_class = check_class(ip_address)
    

    if ip_class == "A":
        ip_mask = "255.0.0.0"

    elif ip_class == "B":
        ip_mask = "255.255.0.0"

    elif ip_class == "C":
        ip_mask = "255.255.255.0"
    else:
        ip_mask = "No aplica"
    
    if is_private == True:
        str_is_private = "privada"
    else:
        str_is_private = "publica"

    return "La IP %s es %s y es de clase %s \nLa máscara de red es: %s " %(ip_address, str_is_private, ip_class, ip_mask) 
