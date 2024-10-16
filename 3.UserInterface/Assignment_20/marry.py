
import random

girls = ["mahtab" , "hane" , "harir" ,"fateme" , "kiana" , "faezeh" , "minoo" , "mina" , "soghra"]
boys = ["mohammad","sobhan","abdollah", "kiya" , "mahdi" , "sajjad" , "homan" , "arman"]

results = []

for i in range(len(boys)):
    girl_index = random.randint(0, (len(girls)-1))
    boy_index = random.randint(0,(len(boys)-1))
    random_girl = girls[girl_index]
    random_boy = boys[boy_index]
    results.append((random_boy , random_girl))
    girls.pop(girl_index)
    boys.pop(boy_index)

print(results)