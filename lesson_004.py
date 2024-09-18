# """ Объектно ориентированное програмирование """
# """ Полиморфизм """













































class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по кредитной карте"
    
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по PayPal"
    
class BankTransfer(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по банковскому переводу"
    
payments = [CreditCard(), PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(input("Введите сумму: ")))