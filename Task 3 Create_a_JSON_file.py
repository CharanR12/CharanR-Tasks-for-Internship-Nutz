import json

user_data ={
    'users' : 
        [
        {
            'name' : 'Charan',
            'age' : '19',
            'address' : '200b msk street,Erode-638004'
        },
        {
            'name' : 'Swetha',
            'age' : '19',
            'address' : '45/b,kk street,Erode-638002'
        },
        {
            'name' : 'Cibi',
            'age' : '18',
            'address' : '70/v pkp street,Erode-638009'
        },
        {
            'name' : 'Saran',
            'age' : '23',
            'address' : '88/v zby street,salem-538015'
        },
           {
            'name' : 'Darshan',
            'age' : '21',
            'address' : '125m xyz street,Erode-638044'
        }
    ]
}

with open("user detail json.json", 'w') as user:
    json.dump(user_data, user)
    
print("json file created")