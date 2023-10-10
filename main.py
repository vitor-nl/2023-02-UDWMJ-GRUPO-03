from client import *
from client_socialnetwork import *
from order import *
from orderitem import *
from product import *
from socialnetwork import *
from category import *

gustavo = Client("Gustavo", "Cabral", "Rua Não te interessa, 10", "9xxx-xxx", "naoteinteressa@seila.com", "M")
socialnetwork1 = SocialNetwork("Facebook","é o facebook feito pelo markinho")
gustavo_socialnetwork1 = Client_Socialnetwork(gustavo, socialnetwork1)

perucas = Category(1, "Perucas", "Tudo de perucas")
peruca_do_gabriel = Product("Peruca do Gabriel", "Para ficar mais lindo e desfarçar a careca", "09/10/2023", True, perucas)
order1 = Order(0, "em processo", gustavo)
orderitem1= OrderItem(1,0,order1, peruca_do_gabriel)

print("Nome do cliente", orderitem1.get_obj_order().get_obj_client().get_first_name())
print("Nome do produto", orderitem1.get_obj_product().get_name())

