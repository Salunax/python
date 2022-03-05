Al
class Table():
    def __init__(self, header_items):
        self.headers = header_items
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def__str__(self):
       out ='\n----------------\n'
       for h in self.headers:
           out += h + ''
       out += '\n----------------\n'
       for tr in self.rows:
           out += 'I?'
           for td in tr:
               out += str(td) + 'I'
       out+= '-----------------\n'
    for tr in self.rows:
        for td in tr:
            out += \'n
         out += '----------------\n'
         return out
                             b vg



table = Table(["animal" , "ferocity]"
# table.header(["animal", "ferocity"])

table.row(["woverine", 100])
table.row(["grizzly", 87])
table.row(["cat", -1])
table.add_row(["dolphin", 63])

print(table.__dict__)
print(table)






