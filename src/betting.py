class Player:
    """Gerencia o saldo do jogador e apostas."""
    
    def __init__(self, balance=100):
        self.balance = balance
    
    def place_bet(self, amount):
        """Realiza uma aposta."""
        if amount > self.balance:
            return "❌ Saldo insuficiente!"
        self.balance -= amount
        return f"✅ Aposta realizada: {amount}. Saldo restante: {self.balance}"

    def add_winnings(self, multiplier, amount):
        """Adiciona os ganhos ao saldo do jogador."""
        winnings = amount * multiplier
        self.balance += winnings
        return f"💰 Você ganhou {winnings}! Novo saldo: {self.balance}"

