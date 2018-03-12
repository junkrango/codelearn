class bot:
    population = 0
    def __init__(self,name):
        self.name = name
        bot.population += 1
    def say_hi(self):
        print ("hello,my name is {}".format(self.name))
    def kill(self):
        print ("my name is {},I will die".format(self.name))
        bot.population -= 1
    @classmethod
    def how_many(cls):
        print ("there is {}".format(cls.population))


a=bot("a")
b=bot("b")
a.say_hi()
b.say_hi()
a.how_many()
a.kill()
bot.how_many()
