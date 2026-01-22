# WhatsApp Automation System

Sistema em Python para envio automatizado de mensagens via WhatsApp Web, utilizando dados de planilhas Excel.

## 📋 Sobre o Projeto

O sistema automatiza a comunicação de avisos e lembretes. Ele lê o nome, o telefone e a data de vencimento diretamente de um arquivo `.xlsx` e realiza o envio personalizado.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Selenium:** Automação do navegador.
* **PyAutoGUI:** Automação de cliques e interface.
* **OpenPyXL:** Leitura de arquivos Excel.

---

## 📂 Estrutura do Projeto

```text
projeto/
├── main.py
├── clientes.xlsx
├── requirements.txt
├── README.md
└── errors.txt
```
🚀 Instalação e Requisitos
Pré-requisitos
Python 3 instalado.

Google Chrome instalado.

Passo a Passo
Instale as dependências:

Bash
pip install -r requirements.txt
📊 Formato da Planilha (clientes.xlsx)
A planilha deve ter as colunas: Nome, Telefone (ex: 5511999999999) e Data de Vencimento.

⚙️ Como Usar
Execute o script: python main.py

O navegador abrirá no WhatsApp Web.

Você terá 90 segundos para escanear o QR Code.

O sistema iniciará o envio automaticamente após esse tempo.

⚠️ Observações Importantes
Não minimize o navegador durante a execução, pois o PyAutoGUI usa a tela.

Falhas de envio serão registradas no arquivo errors.txt.

Este projeto tem fins educacionais. Use com moderação.