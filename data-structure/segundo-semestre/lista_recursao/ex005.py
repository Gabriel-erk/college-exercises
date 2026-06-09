def contar_arquivos(estrutura):
    total = 0

    for item in estrutura:
        if isinstance(item, list): # depois de muita pesquisa só consegui resolver o problema usando isinstance, não sei se tem outra forma (mais simples) de fazer isso
            total += contar_arquivos(item)

        else:
            total += 1

    return total


estrutura = [
    "foto.png",
    "documento.pdf",
    [
        "video.mp4",
        [
            "planilha.xlsx"
        ]
    ]
]

print(contar_arquivos(estrutura), "arquivos encontrados")