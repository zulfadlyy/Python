# **kwargs = parameter that will pack all arguments into a dictionary using **
#            useful so that a function can accept a varying amount of keyword argument

def hello(**kwargs):
    # print("Hello "+kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Bro",middle="Dude",last="Code")