import os

path_ = os.path.join('adithya/kadi/adi' , 'project.csv')

print(os.path.dirname(path_))
print(path_)

# os.makedirs(path_ , exist_ok=True)
os.makedirs(os.path.dirname(path_) , exist_ok=True)
