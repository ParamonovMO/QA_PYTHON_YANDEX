types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}


tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def remove_duplicates(dict_1):
    for i in range(2, 6):
        for v in dict_1[1]:
            if v in dict_1[i]:
                tickets[i].remove(v)

        if i == 3 and 'E2E_45' in dict_1[i]:
            dict_1[i].remove('E2E_45')

        if i == 5 and 'E2E_2' in dict_1[i]:
            dict_1[i].remove('E2E_2')   
    
    return dict_1


def merge_dicts(dict_1, dict_2):
    new_dict = {}
    
    for i in range(1, 6):
        new_dict[dict_1[i]] = dict_2[i]
    
    return new_dict


remove_duplicates(tickets)
merge_dicts(types, tickets)