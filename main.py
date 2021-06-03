from date import DateTime
from datetime import datetime


class FunctionalityForDateTime:
    file_obj = DateTime().date_file()
    file_name = f"{datetime.now():%Y-%m-%d %H-%m-%d}.txt"

    def writer(self, text):
        with open(self.file_name, "a") as file:
            file.write(text)

    def find_symbol(self, symbol):
        array = []
        with open(self.file_name, "r") as file:
            for each_symbol in file.readline():
                array.append(each_symbol)
        for i in range(len(array) - 1):
            if symbol == array[i]:
                print(f"{symbol} is in file, and index is {i}")
                break
        else:
            print(f"{symbol} is not in file")

    def del_phrase(self, word):
        with open(self.file_name, "r") as f:
            lines = f.readlines()
        with open(self.file_name, "w") as fi:
            for line in lines:
                if word not in line:
                    fi.write(line)
                else:
                    line = line.replace(word, "")
                    fi.write(line)

    def count_symbols(self):
        count = 0
        with open(self.file_name, "r") as file:
            for each_line in file.readlines():
                for each_symbol in each_line:
                    count += 1
        return count

    def is_phrase(self, word):
        word_array = []
        with open(self.file_name, "r") as file:
            for line in file:
                for each_word in line.split():
                    word_array.append(each_word)
        if word in word_array:
            return True
        else:
            return False


f = FunctionalityForDateTime()
f.writer(" Summer is coming")
f.writer("\nThis is second line")
f.writer("\nThis is third line")
# f.find_symbol("3")
# f.find_symbol("W")
# f.find_symbol("S")
# f.del_phrase("coming")
# f.del_phrase("This is second line")
print(f.count_symbols())
print(f.is_phrase("Babken"))
