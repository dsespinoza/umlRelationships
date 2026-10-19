from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass


class CreditCardProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using Credit Card."


class PayPalProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> str:
        return f"Paid ${amount:.2f} using PayPal."


def make_checkout(gateway: PaymentGateway, amount: float):
    print(gateway.process_payment(amount))


cc = CreditCardProcessor()
pp = PayPalProcessor()

make_checkout(cc, 49.99) 
make_checkout(pp, 120.00) 