import tkinter as tk
from jogo import verificar_vitoria, empate, jogada_maquina
from som import (
    som_clique, som_vitoria, som_derrota, som_empate,
    musica_fundo, toggle_musica, toggle_som
)

BG = "#0f172a"
BTN = "#1e293b"
PLAYER = "#38bdf8"
AI = "#f43f5e"

tabuleiro = [""] * 9
botoes = []

vitorias = 0
derrotas = 0
empates = 0


def atualizar_placar():
    placar_label.config(
        text=f"Você: {vitorias}   IA: {derrotas}   Empates: {empates}"
    )


def alternar_musica(botao):
    toggle_musica()
    if "ON" in botao["text"]:
        botao["text"] = "🎵 Música: OFF"
    else:
        botao["text"] = "🎵 Música: ON"


def alternar_som(botao):
    toggle_som()
    if "ON" in botao["text"]:
        botao["text"] = "🔊 Som: OFF"
    else:
        botao["text"] = "🔊 Som: ON"


def clique(i):
    global vitorias, empates

    if tabuleiro[i] == "":
        tabuleiro[i] = "X"
        botoes[i].config(text="X", fg=PLAYER)
        som_clique()

        if verificar_vitoria(tabuleiro, "X"):
            som_vitoria()
            vitorias += 1
            atualizar_placar()
            status.config(text="Você venceu!")
            desabilitar()
            return

        if empate(tabuleiro):
            som_empate()  # 🔥 NOVO
            empates += 1
            atualizar_placar()
            status.config(text="Empate!")
            return

        jogada_pc()


def jogada_pc():
    global derrotas, empates

    pos = jogada_maquina(tabuleiro)
    tabuleiro[pos] = "O"
    botoes[pos].config(text="O", fg=AI)

    if verificar_vitoria(tabuleiro, "O"):
        som_derrota()
        derrotas += 1
        atualizar_placar()
        status.config(text="Você perdeu!")
        desabilitar()
        return

    if empate(tabuleiro):
        som_empate()  # 🔥 NOVO
        empates += 1
        atualizar_placar()
        status.config(text="Empate!")


def desabilitar():
    for b in botoes:
        b.config(state="disabled")


def resetar():
    global tabuleiro
    tabuleiro = [""] * 9
    for b in botoes:
        b.config(text="", state="normal")
    status.config(text="Sua vez!")


def iniciar_jogo():
    global botoes, status, placar_label

    janela = tk.Tk()
    janela.title("Jogo da Velha")
    janela.configure(bg=BG)

    musica_fundo()

    placar_label = tk.Label(
        janela,
        text="Você: 0   IA: 0   Empates: 0",
        font=("Arial", 14, "bold"),
        bg=BG,
        fg="white"
    )
    placar_label.pack(pady=10)

    frame_dificuldade = tk.Frame(janela, bg=BG)
    frame_dificuldade.pack(pady=5)

    tk.Label(frame_dificuldade, text="Dificuldade:", bg=BG, fg="white").pack(side="left")

    nivel = tk.StringVar(value="dificil")

    def atualizar_dificuldade(*args):
        import jogo
        jogo.dificuldade = nivel.get()

    nivel.trace("w", atualizar_dificuldade)

    tk.OptionMenu(frame_dificuldade, nivel, "facil", "medio", "dificil").pack(side="left")

    frame = tk.Frame(janela, bg=BG)
    frame.pack()

    botoes = []
    for i in range(9):
        b = tk.Button(
            frame,
            text="",
            font=("Arial", 24),
            width=5,
            height=2,
            bg=BTN,
            fg="white",
            command=lambda i=i: clique(i)
        )
        b.grid(row=i//3, column=i%3, padx=5, pady=5)
        botoes.append(b)

    status = tk.Label(
        janela,
        text="Sua vez!",
        font=("Arial", 14),
        bg=BG,
        fg="white"
    )
    status.pack(pady=10)

    frame_controles = tk.Frame(janela, bg=BG)
    frame_controles.pack()

    btn_musica = tk.Button(
        frame_controles,
        text="🎵 Música: ON",
        command=lambda: alternar_musica(btn_musica)
    )
    btn_musica.grid(row=0, column=0, padx=5)

    btn_som = tk.Button(
        frame_controles,
        text="🔊 Som: ON",
        command=lambda: alternar_som(btn_som)
    )
    btn_som.grid(row=0, column=1, padx=5)

    tk.Button(janela, text="Reiniciar", command=resetar).pack(pady=10)

    janela.mainloop()