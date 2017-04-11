days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

STATE_DAY = 0
STATE_DATE = 1
STATE_MONEY = 2


if __name__ == '__main__':
    state = STATE_DAY
    currentDate = None
    currentTotal = 0
    with open('input.txt', 'r') as f:
        for line in f:
            items = line.split()
            if state == STATE_DAY and len(items) == 2:
                if items[1] in days:
                    state = STATE_DATE
            elif state == STATE_DATE and len(items) == 1:
                if currentDate != items:
                    if currentDate is not None:
                        print (currentDate[0], round(currentTotal,2))
                    currentDate = items                    
                    currentTotal = 0.0
                state = STATE_MONEY
            elif state == STATE_MONEY:
                if "top up" in line.lower():
                    state = STATE_DAY
                elif len(items) >= 3:
                    try:
                        cost = float(items[-1])
                        discount = float(items[-2])
                        raw_price = float(items[-3])
                        currentTotal += cost
                        state = STATE_DAY
                    except:
                        pass
                    