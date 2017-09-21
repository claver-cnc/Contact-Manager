'''

Mr. Todd has bought Andrew a new weave, so now MEST is on a hiring freeze. We can only afford to pay for 4 fellows at a time.
Use a static field to keep track of how many Fellows have been created
If  a user tries to construct a fifth Fellow, raise an exception

'''

class Fellow:
    numberFellow = 0

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        Fellow.numberFellow += 1

    def show(self):
        print("Fellow('{}','{}')".format(self.name, self.nationality))


while True:
    name = input("Enter one Fellow's name ")
    nation = input("Enter the nationality of this Fellow")
    test = Fellow(name, nation)
    test.show()
    while Fellow.numberFellow >= 5:
        raise Exception("Execption: We cannot afford to hire {}".format(test.name))



