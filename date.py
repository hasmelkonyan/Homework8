from datetime import datetime


class DateTime:
    def date_file(self):
        file_name = f"{datetime.now():%Y-%m-%d %H-%m-%d}"
        print(file_name)
        file = open(file_name + ".txt", "w")
        file.write(file_name)
