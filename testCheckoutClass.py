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

def scan_and_total(checkout, item):
    checkout.scan(item)
    return checkout.total()

my_checkout = ch.Checkout({'A': 25, 'B': 40, 'P': 30})

#scan an apple 
tests = [lambda: scan_and_total(my_checkout, 'A') == 25]

#and another apple 
tests.append(lambda: scan_and_total(my_checkout, 'A') == 50)

#and the deal! 
tests.append(lambda: scan_and_total(my_checkout, 'A') == 50)

#another one for good measure
tests.append(lambda: scan_and_total(my_checkout, 'A') == 75)

#scan a banana
tests.append(lambda: scan_and_total(my_checkout, 'B') == 115)

#and another banana 
tests.append(lambda: scan_and_total(my_checkout, 'B') == 155)

#and the deal! 
tests.append(lambda: scan_and_total(my_checkout, 'B') == 175)

#another one for good measure
tests.append(lambda: scan_and_total(my_checkout, 'B') == 215)

#scan a pear
tests.append(lambda: scan_and_total(my_checkout, 'P') == 245)

#and another pear 
tests.append(lambda: scan_and_total(my_checkout, 'P') == 275)

#and no deal! 
tests.append(lambda: scan_and_total(my_checkout, 'P') == 305)

#check for exception with unexpected item
def unexpected_item_check(checkout, item):
    try:
        checkout.scan(item)
    except Exception as exc:
        print(exc)
        return True;
    return False
tests.append(lambda: unexpected_item_check(my_checkout, 'Q'))

#Add another apple (total 5) after the unexpected item
tests.append(lambda: scan_and_total(my_checkout, 'A') == 330)

#Try again with new price list, we'll scan some items then calc a total after all of them
# 3 x A + 1 x O + 2 x D + 3 x B = 60 + 55 + 40 + 100 = 255
my_new_checkout = ch.Checkout({'A': 30, 'B': 45, 'D': 20, 'O': 55})
def add_many_items(checkout, items):
    for i in items:
        checkout.scan(i)
    return checkout.total()
tests.append(lambda: add_many_items(my_new_checkout,['A','B','D','A','O','B','B','A','D']) == 255)

#Check negative pricing (and for warning when entering negative price)
def negative_pricing():
    my_negative_checkout = ch.Checkout({'A':20, 'P':12, 'V':-10})
    return add_many_items(my_negative_checkout, ['A','P','A','A','V','P','V']) == 44
tests.append(negative_pricing)

print("Running tests on checkout function:")
(num_tests, num_passed) = run_tests(tests)
print("Passed ", num_passed, " tests out of ", num_tests)

