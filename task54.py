cost1 = [0, 0, 0]
cost2 = [0, 0, 0]
counter_fh_wins = 0


def check_string(inp_str):
    first_hand = inp_str[:14]
    print(first_hand)
    second_hand = inp_str[15:]
    print(second_hand)
    print()
    print('first_hand:')
    global counter_fh_wins
    cost_1 = check_compairing(first_hand)
    print()
    print('second_hand:')
    cost_2 = check_compairing(second_hand)
    print()
    if cost_1 > cost_2:
        print('first hand won')
        counter_fh_wins += 1
    elif cost_1 < cost_2:
        print('second hand won')
    elif cost_1 == cost_2:
        print('draw')
    print()


def get_sorted_list_of_values(inp_hand):
    cards = inp_hand.split()
    vals = []
    for card in cards:
        val = card[0]
        if val == 'T':
            val = 10
        elif val == 'J':
            val = 11
        elif val == 'Q':
            val = 12
        elif val == 'K':
            val = 13
        elif val == 'A':
            val = 14
        vals.append(int(val))
        # print(val)
    return sorted(vals)


def check_compairing(inp_hand):
    print(inp_hand)
    vals = get_sorted_list_of_values(inp_hand)
    unique_elements = list(set(vals))
    count_of_pairs = 0
    first_pair = None
    three_cards = None
    if len(unique_elements) < 5:
        # global result
        result = 0
        for element in unique_elements:
            if vals.count(element) == 4:
                # result = 'four of a kind with ' + str(element)
                return [8, element, 0]
            if vals.count(element) == 3:
                if first_pair is not None:
                    # result = 'fullhouse with three ' + str(element) + ' and two ' + str(first_pair)
                    return [7, element, first_pair]
                else:
                    result = 'three of a kind with ' + str(element)
                    three_cards = element
            if vals.count(element) == 2:
                count_of_pairs += 1
                if count_of_pairs == 1:
                    if three_cards is not None:
                        result = 'full-house with three' + str(three_cards) + 'and two' + str(element)
                    first_pair = element
                    result = 'pair of ' + str(element)
                if count_of_pairs == 2:
                    print(f'2 pairs:', max(first_pair, element), min(first_pair, element))
                    return [3, max(first_pair, element), min(first_pair, element)]
        print(result)
        if 'pair of' in result:
            return [2, first_pair, 0]
        elif 'three' in result:
            return [4, three_cards, 0]
    else:
        res = check_on_straight(inp_hand)
        if res is not None:
            return res
        else:
            print('one card', max(vals))
            return [1, max(vals), 0]


def check_on_flash(inp_hand):
    cards = inp_hand.split()
    suits = []
    for card in cards:
        suit = card[1]
        suits.append(suit)
        # print(suit)
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        print('flash')
        return [6, 0, 0]


def check_on_straight(inp_hand):
    vals = get_sorted_list_of_values(inp_hand)
    if vals[0] + 1 == vals[1] and vals[1] + 1 == vals[2] and vals[2] + 1 == vals[3] and vals[3] + 1 == vals[4]:
        if check_on_flash(inp_hand):
            if max(vals) == 14:
                print('royal flash')
                return [10, 0, 0]
            else:
                print('straight flash', max(vals))
                return [9, max(vals), 0]
        else:
            print('straight', max(vals))
            return [5, max(vals), 0]
    else:
        check_on_flash(inp_hand)


with open('poker.txt', 'r') as file:
    content = file.readlines()
    counter = 0
    for line in content:
        counter += 1
        print('line №', counter)
        check_string(line.split('\n')[0])
    print("Total wins of 1st hand = ", counter_fh_wins)
