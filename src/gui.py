import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from src.game import spin, check_win
from src.betting import Player

class SlotMachineGUI:
    """Interface gráfica do Jogo do Tigrinho."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo do Tigrinho 🎰")
        self.root.geometry("500x400")
        self.root.configure(bg="#2B2B2B")
        
        # Criando jogador
        self.player = Player(balance=200)

        # Criar rótulo de saldo
        self.balance_label = Label(root, text=f"Saldo: R$ {self.player.balance}", fg="white", bg="#2B2B2B", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Criar área dos símbolos
        self.symbol_label = Label(root, text="🎰 🎰 🎰", fg="white", bg="#2B2B2B", font=("Arial", 24))
        self.symbol_label.pack(pady=20)

        # Botão de jogar
        self.spin_button = Button(root, text="🎲 Girar", command=self.play, font=("Arial", 14), bg="gold", fg="black")
        self.spin_button.pack(pady=10)

        # Exibir resultados
        self.result_label = Label(root, text="", fg="white", bg="#2B2B2B", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def play(self):
        """Executa uma rodada do jogo."""
        spin_result = spin()
        self.symbol_label.config(text=" ".join(spin_result))

        outcome = check_win(spin_result)
        self.result_label.config(text=outcome)

        # Atualizar saldo
        if "Jackpot" in outcome or "Bônus" in outcome:
            multiplier = int(outcome.split()[-1].replace("x", ""))
            self.player.add_winnings(multiplier, 10)
        else:
            self.player.place_bet(10)

        self.balance_label.config(text=f"Saldo: R$ {self.player.balance}")

# Executar interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    gui = SlotMachineGUI(root)
    root.mainloop()
