"""
입력받은 리스트의 각 원소를 출력한다
원소가 리스트인 경우엔 재귀호출을 통해 indent 를 적용 후 원소를 출력한다
"""
def print_lol(the_list, indent=False, level=0):
    if level < 0:
        level = 0
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1)
        else:
            if indent:
                for tab_stab in range(level):
                    print("\t", end='')
            print(each_item)
