import csv

class DictExamples:
    def gradBook(self):
        grade_book = {
        'Muhamad' : [93, 86, 100],
        'Wontae' : [84, 96, 78],
        'Juwon' : [99, 99, 99],
        'Juheok' : [40, 59, 30],
        'Seunghye' : [79, 60, 90],
        }
        all_grades_total = 0
        all_grades_count = 0
        # items(): Returns objects composed of key - value.
        for name, grades in grade_book.items(): # name -> key, grades -> value
            total = sum(grades)
            print(f'Average for {name} is {total/len(grades):.2f}')
            all_grades_count += len(grades)
            all_grades_total += total
        print(f"Class's average is : {all_grades_total/all_grades_count:.2f}")
            
    def getFrequencyOfWords(self):
        cnt = 0
        with open("License.txt", "r") as file:
            for line in file:
                for word in line.split():
                    cnt = cnt + 1
        return cnt
                
    def getFrequencyOfLetters(self):
        cnt = 0
        with open("License.txt", "r") as file:
            file_data = file.read()
            for i in file_data:
                if i.isalpha():
                    cnt = cnt + 1
        return cnt
    
    def getLongestWords(self):
        str_list = []
        with open("License.txt", "r") as file:
            for line in file:
                for word in line.split():
                    str_list.append(word)
                
        # sort by len
        str_list.sort(key = len)
        return str_list[len(str_list) - 1]
                    
    def csvFile(self):
        with open('countrycode.csv') as csv_file:
            codeDic = {} # Initialize with Dictionary
            csv_reader = csv.reader(csv_file)
            count = 0
            for row in csv_reader:
                # key: code(row[1]), value: name(row[0])
                codeDic[row[1]] = row[0]
                count += 1
            for code in codeDic:
                print('{}:{}'.format(code, codeDic[code]))
            print('No of countries = {}'.format(count))
            print('No of Countries = {}'.format(len(codeDic)))