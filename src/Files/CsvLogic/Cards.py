import csv

class Cards:
    def get_spg_id():
        CardSkillsID = []
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[6].lower() == '4' or row[6].lower() == '5':
                        CardSkillsID.append(line_count - 2)
                    line_count += 1

            return CardSkillsID



    def check_spg_id(self, id):
        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if line_count-2 == id:
                        return row[6].lower()

                    line_count += 1


    def get_spg_by_brawler_id(self, brawler_id, type):
        char_file =  open('GameAssets/csv_logic/characters.csv')
        csv_reader = csv.reader(char_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                line_count += 1
            else:
                line_count += 1
                if line_count == brawler_id + 3:
                    name = row[0]
                    line_count += 1

                    cards_file = open('GameAssets/csv_logic/cards.csv')
                    csv_reader = csv.reader(cards_file, delimiter=',')
                    line_count = 0

                    for row in csv_reader:
                        if line_count == 0 or line_count == 1:
                            line_count += 1
                        else:
                            line_count += 1
                            if type == 4:
                                if row[6].lower() == '4' and row[3] == name:
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id

                            elif type == 5:
                                if row[3] == name and row[6].lower() == '5':
                                    id = line_count - 3
                                    char_file.close()
                                    cards_file.close()
                                    return id




    def get_brawler_unlock():
        CardUnlockID = []

        with open('GameAssets/csv_logic/cards.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:

                if line_count == 0 or line_count == 1:
                    line_count += 1
                else:
                    if row[6].lower() == '0':
                        CardUnlockID.append(line_count - 2)
                    line_count += 1


            return CardUnlockID