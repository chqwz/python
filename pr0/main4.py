
def search(count):
    searchedCount = 0
    a = 1
    b = 1

    while True:
        while True:
            if a < b:
                pifagorNumbers = [(b ** 2) - (a ** 2), 2 * a * b, (b ** 2) + (a ** 2)]
                pifagorNumbers.sort()
                
                print(pifagorNumbers)
                
                if searchedCount < count:
                    
                    searchedCount += 1
                    if searchedCount >= count:
                        return
                    
                    break
                    
            b += 1
        a += 1
        b = a + 1
                    
        
search(10)

