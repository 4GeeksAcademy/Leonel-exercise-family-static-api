
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
    
        # example list of members
        self._members = [{
            "id":self._generateId(),
            "first_name":"Leonel",
            "last_name":last_name,
            "age":23,
            "lucky_numbers":[2,4,1,9,4]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"]=self._generateId()
        self._members.append(member)

        return self._members
        

    def delete_member(self, id):
        count=0
        for member in self._members:
            if member["id"]==id:
                count+=1
                self._members.remove(member)
        
        length_of_members=len(self._members)

        if (count>=1):
            return None
        
        return self._members

    def update_member(self, id, member):
        self._members=[update_member if member["id"]==id else member for member in self._members ]
        return self._members

    def get_member(self, id):  
        member_needed=next((member for member in self._members if member["id"]==id),None)
        return member_needed

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
