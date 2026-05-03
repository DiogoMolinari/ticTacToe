import winsound

musica_ativa = True
som_ativo = True


def som_clique():
    if som_ativo:
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)


def som_vitoria():
    if som_ativo:
        winsound.PlaySound("win.wav", winsound.SND_ASYNC)


def som_derrota():
    if som_ativo:
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)


# 🔥 NOVO
def som_empate():
    if som_ativo:
        winsound.PlaySound("draw.wav", winsound.SND_ASYNC)


def musica_fundo():
    if musica_ativa:
        winsound.PlaySound("bg.wav", winsound.SND_ASYNC | winsound.SND_LOOP)


def parar_musica():
    winsound.PlaySound(None, winsound.SND_PURGE)


def toggle_musica():
    global musica_ativa
    musica_ativa = not musica_ativa

    if musica_ativa:
        musica_fundo()
    else:
        parar_musica()


def toggle_som():
    global som_ativo
    som_ativo = not som_ativo