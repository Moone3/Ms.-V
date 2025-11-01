import time

# MS. V :>
#zirehT
print("\033c")

lyrics = [
    ("Pagkat ikaw lang ang nais makatabi", 1.0, 0.10),
    ("Malamig man o mainit ang gabi", 2.5, 0.11),
    ("Nais ko sanang iparating", 2.0, 0.17),
    ("Na ikaw lamang ang s'yang aking", 2.0, 0.11),
    ("Iibigin", 5.0, 0.11),
    (".........", 9.0, 5.0),
    
]
print("Alipin - Michael Pangilinan Lyrics\n")
for text, delay_before, delay_char in lyrics:
    time.sleep(delay_before)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay_char)
        
    print()
