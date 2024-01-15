from os import listdir


def generator_directory(path: str) -> None:
    directory: list = listdir(path)
    for file in directory:
        if file.endswith('.txt'):
            yield file


def read_content(file: str, genset: set = set(), counter=[0,0]) -> set:
    with open('./baza/' + file, mode='r', encoding='KOI8-U') as f:
        start = 0
        game = '<раздатка>'
        prev_row = '\n'
        for row in f:
            if game in row:
                start = 1
            if row == '\n':
                start = 0
            if start:
                print(row,end='')
        else:
            counter[0] += 1

        # flag = 0
        # question = ''
        # max_question = ''
        # for row in f:
        #     if flag:
        #         if row == '\n':
        #             max_len = len(question)
        #             if counter[0] < max_len:
        #                 max_question = question
        #                 counter[0] = max_len
        #             flag = 0
        #             question = ''
        #         else:
        #             row = row.split()
        #             question += ' '.join(row)
        #             continue
        #     if row.startswith(game):
        #         flag = 1
    return [genset, counter] # counter[0], max_question
        # if counter[0] != _counter:
        #     genset.add(f)
        # return genset
        # flag = False
        # for row in f:
        #     if flag:
        #         # temp = row.strip()
        #         temp = row
        #         if temp.startswith('   (') and temp[7] == ':':
        #             genset.add(row)
        #         flag = False
        #     if row.startswith('Вопрос'):
        #         flag = True
        # prev_row = '\n'
        # for row in f:
        #     if prev_row == '\n' and row.endswith(':\n') and not row.startswith('Воп'):
        #         genset.add(row)
        #     prev_row = row
        # return genset


def counter_field():
    filename_max_length = 0
    for file in generator_directory('./baza/'):
        filename_length = len(file)
        if filename_max_length < filename_length:
            filename_max_length = filename_length
    return filename_max_length


def main():
    # read_content('1vs1200.txt')
    for file in generator_directory('./baza/'):
        t = read_content(file)
    
    # k = sorted(t)
    print(t)


if __name__ == '__main__':
    # print(counter_field())
    main()
