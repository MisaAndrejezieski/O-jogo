import random
from src.symbols import SYMBOLS, PAYOUTS  # Importação corrigida

def spin():
    """Simula um giro da máquina de caça-níquel."""
    return [random.choice(SYMBOLS) for _ in range(3)]

def check_win(result):
    """Verifica se a rodada resultou em uma vitória."""
    if result[0] == result[1] == result[2]:  # Jackpot!
        return f"🎉 Jackpot! Você ganhou com {result}. Prêmio: {PAYOUTS[result[0]]}x"
    elif result.count("🐯") == 2:  # Bônus com dois tigres
        return f"✨ Bônus! Dois tigres: {result}. Prêmio: {PAYOUTS['🐯']//2}x"
    else:
        return f"❌ Nada dessa vez: {result}"

# Teste de 5 rodadas
if __name__ == "__main__":
    for _ in range(5):
        resultado = spin()
        print(check_win(resultado))
