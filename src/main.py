from src.game import spin, check_win  # Importação ajustada
from src.betting import Player

# Criando jogador
player = Player(balance=200)

print("🎰 Bem-vindo ao Jogo do Tigrinho! 🎰")
while player.balance > 0:
    try:
        bet = int(input("Quanto deseja apostar? (Digite 0 para sair) "))
    except ValueError:
        print("❌ Entrada inválida! Digite um número.")
        continue

    if bet == 0:
        break
    
    result = player.place_bet(bet)
    print(result)
    
    if "Saldo insuficiente" in result:
        continue
    
    spin_result = spin()
    outcome = check_win(spin_result)
    print(outcome)

    if "Jackpot" in outcome or "Bônus" in outcome:
        multiplier = int(outcome.split()[-1].replace("x", ""))
        print(player.add_winnings(multiplier, bet))

print("🚀 Jogo encerrado! Obrigado por jogar.")
