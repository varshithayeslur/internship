from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:
    contact_list =[]
    @classmethod
    def addcontact(cls):
        name =  input("enter the name")
        email =  input("enter the email")
        mobile = input("enter the mobile")
        address =  input("enter the address")
        cls.contact_list.append(Contact(name,email,mobile,address))
        print("contact is added successfully with name : {name}")


    @classmethod
    def deletecontact(cls):
        name= input("enter the name to be deleted:")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_list.remove(contact)
            print(f"contact {name} is deleted successfully")
            InMemoryImpl._paint(cls.contact_list)
        else:
            print(f"contact {name} not found")

    @classmethod
    def viewcontact(cls):
        InMemoryImpl._paint(cls.contact_list)

    @classmethod
    def search(cls):
        if len(cls.contact_list)>0:
            name = input("enter the name to be searched")
            s_list= list(filter(lambda x: name.lower() in x.get__name().lower(),cls.contact_list))
            if len(s_list)>0:
                InMemoryImpl._paint(s_list)
            else:
                print("there is no data with given string ")
        else:
            print("contact book is empty......!you can't search")
    @classmethod
    def updatecontact(cls):
        name= input("enter the name to update:")
        contact=cls.get_contact_by_name(name)
        if contact:
            print("1.name 2.email 3.mobile 4.address")
            ch= int(input("enter your choice"))
            if ch==1:
                print(f"oldname:{contact.get__name()}")
                name=input("enter the new name:")
                if name:
                    contact.set__name(name)
            if ch==2:
                print(f"oldemail:{contact.get__email()}")
                email=input("enter the new email:")
                if email:
                    contact.set__email(email)
            if ch==3:
                print(f"oldmobile:{contact.get__mobile()}")
                mobile=input("enter the new mobile:")
                if mobile:
                    contact.set__mobile(mobile)
            if ch==4:
                print(f"oldaddress:{contact.get__address()}")
                address=input("enter the new address:")
                if address:
                    contact.set__address(address)        
        
        else:
            print(f"contact is not found")


    @staticmethod
    def _paint(lst):
        if len(lst) !=0:
            table = BeautifulTable()
            table.column_headers = ["name","email","mobile","address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"contact book is empty")

    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contact_list)>0:
            contact=list(filter(lambda x:x.get__name().lower()==name.lower(),cls.contact_list))
            return contact[0] if contact else None
