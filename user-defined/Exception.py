def parse_int(s):
    try:
        return int(s)
    except ValueError:
        print(f"Cannot convert {s!r} to int")
        return None
    else:
        print("Conversion succeeded")

# demo
print(parse_int("10"))  
print(parse_int("abc"))  
print(parse_int("20.5"))
print(parse_int("30"))

