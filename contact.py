class contact:

    def __init__(self, Name, PhoneNumber, Gender, EmailAdress, PostalAdress ):
        self.Name = Name
        self.PhoneNumber = PhoneNumber
        self.Gender = Gender
        self.EmailAdress = EmailAdress

        self.PostalAdress = PostalAdress

    def viewcontact(self):
        print "\nName= " + self.Name + " | Phone Number= " + self.PhoneNumber + " | Gender= " + self.Gender+" | Email= " + self.EmailAdress

boucle = 0
while boucle ==0:
    name = raw_input('User name:')
    phone = raw_input('User phone:')
    gender = raw_input('User gender: ')
    email = raw_input('User mail: ')
    postal = raw_input('User Postal Adress: ')
    me = contact(name, phone, gender, email, postal)
    me.viewcontact()

    answer = raw_input("\nWould you want to had one contact ? Yes || No\n")
    if answer != 'Yes':
        boucle = 1


