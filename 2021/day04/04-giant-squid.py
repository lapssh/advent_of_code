class Desk:
    def __init__(self, desk_number, values):
        self.desk_number = desk_number
        self.values = values
        self.horizon_win = self.values
        self.vertical_win = []
        tmp_vert_win_one = []
        tmp_vert_win_two = []
        tmp_vert_win_three = []
        tmp_vert_win_four = []
        tmp_vert_win_five = []
        for i in self.values:
            tmp_vert_win_one.append(i[0])
            tmp_vert_win_two.append(i[1])
            tmp_vert_win_three.append(i[2])
            tmp_vert_win_four.append(i[3])
            tmp_vert_win_five.append(i[4])
            # self.vertical_win.append(i[1])
        self.vertical_win.append(tmp_vert_win_one)
        self.vertical_win.append(tmp_vert_win_two)
        self.vertical_win.append(tmp_vert_win_three)
        self.vertical_win.append(tmp_vert_win_four)
        self.vertical_win.append(tmp_vert_win_five)
        self.win_combinations = self.vertical_win + self.horizon_win

    def new_number(self, number):
        
        for combination in self.win_combinations:
            if number in combination:



    def __str__(self):
        print(f'Desk number # {self.desk_number}')
        for i in self.values:
            print(i)
        print(f'Win Combinations:  ')
        print(self.vertical_win)
        print(self.horizon_win)
        # for i in self.vertical_win:
        #     print(i)
        return 'ok'


def import_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        nums = lines.pop(0)
        lines.pop(0)  # пропускаем первый перенос строки
        print(nums)
        print(lines)
        desks = []
        desk_line = []
        desk_number = 0
        for line in lines:
            if line == '\n':
                desk_number += 1
                desks.append(Desk(desk_number, desk_line))
                desk_line = []
            else:
                line = line.strip()
                line = line.split()
                line = [int(num) for num in line]
                desk_line.append(line)
        print(f'{desk_number=}, {desk_line=}')
        desk_number += 1
        desks.append(Desk(desk_number, desk_line))
        # print(desks[0])
        print(desks[0].win_combinations)
        # data = [number.strip() for number in f]
        # f.readlines()


if __name__ == '__main__':
    # file = 'input.txt'
    file = 'test-input.txt'
    import_data(file)
