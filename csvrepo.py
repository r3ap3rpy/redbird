from redbird.repos import CSVFileRepo

repo = CSVFileRepo(filename="test.csv",fieldnames=["name","age","height"])

repo.add({'name':"Daniel",'age':"31",'height':"187"})
repo.add({'name':"Florian",'age':"30",'height':"183"})
repo.add({'name':"Naomi",'age':"29",'height':"180"})

for item in list(repo):
    print(item)

repo.filter_by(name='Naomi').update(age=22)

for item in list(repo):
    print(item)

repo.filter_by(name='Naomi').delete()