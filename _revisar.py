import sys
sys.path.insert(0, r"C:\Users\bruno\.claude\skills\gemini-imagem")
from engine.gemimg import revisar

contexto = (
    "Esta é uma landing page de uma fábrica de chocolate nacional (MPS Alimentos) que vende "
    "'Trufas Ocas' (cascas de chocolate para confeitarias). Público B2B: confeitarias e docerias. "
    "Estilo pretendido: artesanal, quente, elegante — creme, serifada, dourado e marrom chocolate. "
    "Avalie como DIRETOR DE ARTE, em português, de forma honesta e específica: hierarquia visual, "
    "legibilidade, contraste, espaçamento, e o que melhoraria a comunicação. Aponte no máximo os "
    "5 pontos mais importantes, do mais crítico ao menor. Seja direto."
)
print("===== DESKTOP =====")
print(revisar("_shots/desktop.png", contexto))
print("\n===== MOBILE =====")
print(revisar("_shots/mobile2.png", contexto + " Esta é a versão MOBILE (celular)."))
