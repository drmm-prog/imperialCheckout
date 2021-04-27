import checkout as ch

def run_tests(testFuncs):
    num_tests = 0
    num_passed = 0
    for T in testFuncs:
        if (T() == True):
            print("Passed test ", num_tests+1)
            num_passed += 1
        else:
            print("Failed test ", num_tests+1)
        num_tests += 1
    return (num_tests, num_passed)

#Canonical example = 155 (one deal applies to bananas -> 100 + 25 + 30)
tests = [lambda: ch.checkout(['B', 'A', 'B', 'P', 'B'], {'A': 25, 'B': 40, 'P': 30}) == 155]

#Check that an empty cart costs nothing
tests.append(lambda: ch.checkout([], {'A': 25, 'B': 40, 'P': 30}) == 0)

#Check that one apple is 1 x apple price
tests.append(lambda: ch.checkout(['A'], {'A': 25, 'B': 40, 'P': 30}) == 25)

#Check that one banana is 1 x banana price
tests.append(lambda: ch.checkout(['B'], {'A': 25, 'B': 40, 'P': 30}) == 40)

#Change the price list to exclude bananas 
tests.append(lambda: ch.checkout(['A'], {'A': 25, 'P': 30}) == 25)

#Check exception raised for missing item (not on price list)
def test_unexpected_item_exception():
    try:
        ch.checkout(['B'], {'A': 25, 'P': 30})
    except Exception as exc: 
        print(exc)
        return True
    return False

tests.append(test_unexpected_item_exception)

#Check that one pear is 1 x pear price
tests.append(lambda: ch.checkout(['P'], {'A': 25, 'B': 40, 'P': 30}) == 30)

#Check that two apples are 2 x apple price
tests.append(lambda: ch.checkout(['A','A'], {'A': 25, 'B': 40, 'P': 30}) == 50)

#Check that three apples are 2 x apple price
tests.append(lambda: ch.checkout(['A','A','A'], {'A': 25, 'B': 40, 'P': 30}) == 50)

#Check response to apple price change 
tests.append(lambda: ch.checkout(['A','A','A'], {'A': 30, 'B': 40, 'P': 30}) == 60)

#Check surplus apples added correctly  
tests.append(lambda: ch.checkout(['A','A','A','A'], {'A': 25, 'B': 40, 'P': 30}) == 75)

#Check multiple of deal: six apples are 4 x apple price
tests.append(lambda: ch.checkout(['A','A','A','A','A','A'], {'A': 25, 'B': 40, 'P': 30}) == 100)

#Check surplus apples added correctly (including multiples of deal)
tests.append(lambda: ch.checkout(['A','A','A','A','A','A','A'], {'A': 25, 'B': 40, 'P': 30}) == 125)

#Check that two bananas are 2 x banana price
tests.append(lambda: ch.checkout(['B','B'], {'A': 25, 'B': 40, 'P': 30}) == 80)

#Check that three bananas are 100
tests.append(lambda: ch.checkout(['B','B','B'], {'A': 25, 'B': 40, 'P': 30}) == 100)

#Check no response to banana price change for deal with three (deal is fixed)
tests.append(lambda: ch.checkout(['B','B','B'], {'A': 30, 'B': 75, 'P': 30}) == 100)

#Check surplus bananas added on top of deal  correctly  
tests.append(lambda: ch.checkout(['B','B','B','B','B'], {'A': 25, 'B': 40, 'P': 30}) == 180)

#Check multiple of deal: six bananas are 200
tests.append(lambda: ch.checkout(['B','B','B','B','B','B'], {'A': 25, 'B': 40, 'P': 30}) == 200)

#Check surplus bananas added correctly (including multiples of deal)
tests.append(lambda: ch.checkout(['B','B','B','B','B','B','B'], {'A': 25, 'B': 40, 'P': 30}) == 240)

#Check no deal on pears x 3 
tests.append(lambda: ch.checkout(['P']*3, {'A': 25, 'B': 40, 'P': 30}) == 90)

#Check no deal on pears x 5
tests.append(lambda: ch.checkout(['P']*5, {'A': 25, 'B': 40, 'P': 30}) == 150)

#Change price of pears 
tests.append(lambda: ch.checkout(['P']*20, {'A': 25, 'B': 40, 'P': 15}) == 300)

#Multiple deals and new items! Mixed up orders
#(8 apples + 3 bananas + 1 pear + 2 strawberries + 1 orange = 150 + 100 + 30 + 20 + 55 = 355
tests.append(lambda: ch.checkout(['A','A','A','B','A','P','B','S','A','A','S','B','O','A','A'], {'A': 25, 'B': 40, 'P': 30, 'S': 10, 'O': 55}) == 355)

#Negative pricing! Scanning a gift voucher perhaps 
tests.append(lambda: ch.checkout(['A','A','A','B','A','P','B','S','A','A','S','B','O','A','A','V'], {'A': 25, 'B': 40, 'P': 30, 'S': 10, 'O': 55, 'V': -150}) == 205)

print("Running tests on checkout function:")
(num_tests, num_passed) = run_tests(tests)
print("Passed ", num_passed, " tests out of ", num_tests)
