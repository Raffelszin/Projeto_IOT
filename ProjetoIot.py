import tkinter as tk
from tkinter import ttk

# --- Lógica de controle ---
def atualizar_status(event=None):
    """
    Função que é chamada sempre que o controle deslizante muda.
    Ela atualiza o status do ventilador e a cor do LED.
    """
    # Pega o valor atual do controle deslizante de temperatura
    temperatura = slider_temp.get()

    # Define o limite para ligar o ventilador (28ºC)
    limite_ventilador = 28

    # Lógica do ventilador: se a temperatura for maior que o limite, ele liga
    if temperatura > limite_ventilador:
        status_ventilador = "Ligado"
        cor_ventilador = "red" # Cor vermelha para indicar que está quente
    else:
        status_ventilador = "Desligado"
        cor_ventilador = "green" # Cor verde para indicar que está normal

    # Lógica do LED: muda a cor dependendo da temperatura
    if temperatura > 30:
        cor_led = "red"    # Muito quente
    elif temperatura > 25:
        cor_led = "yellow" # Atenção
    else:
        cor_led = "green"  # Normal

    # Atualiza o texto na tela com a temperatura e o status
    label_temperatura.config(text=f"Temperatura: {temperatura:.1f} °C")
    label_ventilador.config(text=f"Ventilador: {status_ventilador}", foreground=cor_ventilador)
    
    # Atualiza a cor do círculo (LED)
    canvas_led.itemconfig(led, fill=cor_led)


# --- Criação da interface gráfica (Janela) ---
janela = tk.Tk()
janela.title("Simulação Simples de IoT")
janela.geometry("350x300")
janela.configure(bg="#f0f0f0")

# --- Widgets ---
# Título
label_titulo = ttk.Label(janela, text="Monitor de Ambiente (Simulação)", font=("Arial", 14, "bold"), background="#f0f0f0")
label_titulo.pack(pady=10)

# Controle deslizante para simular a temperatura
label_slider = ttk.Label(janela, text="Simular Temperatura (°C):", background="#f0f0f0")
label_slider.pack()
slider_temp = ttk.Scale(janela, from_=10, to=40, orient="horizontal", command=atualizar_status)
slider_temp.set(25) # Valor inicial
slider_temp.pack(pady=5, padx=20, fill="x")

# Texto para mostrar a temperatura
label_temperatura = ttk.Label(janela, text="Temperatura: 25.0 °C", font=("Arial", 12), background="#f0f0f0")
label_temperatura.pack(pady=10)

# Texto para mostrar o status do ventilador
label_ventilador = ttk.Label(janela, text="Ventilador: Desligado", font=("Arial", 12, "bold"), background="#f0f0f0", foreground="green")
label_ventilador.pack(pady=5)

# Canvas para simular o LED
canvas_led = tk.Canvas(janela, width=50, height=50, highlightthickness=0, bg="#f0f0f0")
canvas_led.pack(pady=10)
# Desenha um círculo no canvas
led = canvas_led.create_oval(10, 10, 40, 40, fill="green", outline="gray")

# Chama a função uma vez para configurar o estado inicial
atualizar_status()

# Inicia o programa
janela.mainloop()