import tkinter as tk
from tkinter import ttk, messagebox

def classificar_urgencia(sintomas):
    sintomas_graves = ["dor no peito", "falta de ar", "sangramento", "desmaio", "convulsão", 
                       "dificuldade para falar", "pressão alta", "pressão baixa"]
    sintomas_moderados = ["febre alta", "vômito persistente", "dor abdominal intensa", 
                          "dificuldade para respirar", "tontura"]
    sintomas_leves = ["dor de cabeça fraca", "nariz entupido"]

    if any(sintoma in sintomas_graves for sintoma in sintomas):
        return "vermelho"  # Muito urgente
    elif any(sintoma in sintomas_moderados for sintoma in sintomas):
        return "amarelo"  # Urgente
    else:
        return "verde"  # Pouco urgente

def coletar_e_classificar():
    nome = nome_entry.get().strip()
    data_nascimento = nascimento_entry.get().strip()
    sexo = sexo_combobox.get().strip()
    cpf = cpf_entry.get().strip()
    
    # Verifica se os campos estão preenchidos
    if not nome or not data_nascimento or not sexo or not cpf:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    # Coleta os sintomas selecionados
    sintomas_selecionados = [sintomas_listbox.get(i) for i in sintomas_listbox.curselection()]
    if not sintomas_selecionados:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos um sintoma!")
        return

    # Classifica a urgência
    urgencia = classificar_urgencia(sintomas_selecionados)

    # Exibe o resultado
    resultado_label.config(
        text=f"Paciente: {nome}\nClassificação de Urgência: {urgencia.upper()}",
        fg="red" if urgencia == "vermelho" else "orange" if urgencia == "amarelo" else "green"
    )

# Criação da janela principal
janela = tk.Tk()
janela.title("Classificação de Sintomas")
janela.geometry("500x600")

# Título
titulo_label = tk.Label(janela, text="Sistema de Classificação de Urgência", font=("Arial", 16, "bold"))
titulo_label.pack(pady=10)
subtitulo = tk.Label(janela, text="ATENDIMENTO RÁPIDO", font=("Arial", 16, "bold"))
subtitulo.pack(pady=11)

# Nome
nome_label = tk.Label(janela, text="Nome Completo:")
nome_label.pack()
nome_entry = tk.Entry(janela, width=40)
nome_entry.pack(pady=5)

# Data de Nascimento
nascimento_label = tk.Label(janela, text="Data de Nascimento (dd/mm/aaaa):")
nascimento_label.pack()
nascimento_entry = tk.Entry(janela, width=40)
nascimento_entry.pack(pady=5)

# Sexo
sexo_label = tk.Label(janela, text="Sexo:")
sexo_label.pack()
sexo_combobox = ttk.Combobox(janela, values=["Masculino", "Feminino", "Outro"], state="readonly", width=37)
sexo_combobox.pack(pady=5)
sexo_combobox.set("Selecione o sexo")

# CPF
cpf_label = tk.Label(janela, text="CPF:")
cpf_label.pack()
cpf_entry = tk.Entry(janela, width=40)
cpf_entry.pack(pady=5)

# Sintomas
sintomas_label = tk.Label(janela, text="Selecione seus sintomas (múltiplos):")
sintomas_label.pack()
sintomas_listbox = tk.Listbox(janela, selectmode="multiple", height=10, width=50)
sintomas_listbox.pack(pady=5)

# Adiciona os sintomas à lista
sintomas_opcoes = [
    "dor no peito", "falta de ar", "sangramento", "desmaio", "convulsão", 
    "dificuldade para falar", "pressão alta", "pressão baixa", "febre alta", 
    "vômito persistente", "dor abdominal intensa", "dificuldade para respirar", 
    "tontura", "dor de cabeça fraca", "nariz entupido"
]
for sintoma in sintomas_opcoes:
    sintomas_listbox.insert(tk.END, sintoma)

# Botão para classificar
classificar_botao = tk.Button(janela, text="Classificar", command=coletar_e_classificar, bg="blue", fg="white")
classificar_botao.pack(pady=20)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12, "bold"))
resultado_label.pack(pady=20)

# Inicia a interface
janela.mainloop()
