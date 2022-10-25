from user import User

user1 = User('Jahmil', 'Stafford', 'jdog@bark.net', 29)
user2 = User('Roy', 'Lee', 'leedog@google.com', 24)

user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
