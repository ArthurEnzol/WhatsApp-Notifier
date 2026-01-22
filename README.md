# Envio Automático de Mensagens no WhatsApp

Projeto em Python para envio automático de mensagens personalizadas via **WhatsApp Web**, utilizando uma planilha do Excel como base de dados.

Indicado para:
- Avisos de vencimento
- Lembretes
- Mensagens em massa personalizadas

---

## Tecnologias Utilizadas

- Python 3
- Selenium (automação do navegador)
- PyAutoGUI (automação de cliques)
- OpenPyXL (leitura de arquivos Excel)
- WhatsApp Web

---

## Estrutura do Projeto

projeto/
├── main.py
├── clientes.xlsx
├── requirements.txt
├── README.md
└── errors.txt


---

## Instalação

### 1. Clonar ou baixar o projeto

git clone <url-do-repositorio>
cd projeto

2. Instalar as dependências
pip install -r requirements.txt

3. Requisitos

Python 3 instalado

Google Chrome instalado

Conta ativa no WhatsApp

Conexão com a internet

Formato do Arquivo Excel (clientes.xlsx)

A planilha deve conter a aba Sheet1 com a seguinte estrutura:

Nome	Telefone	Data de Vencimento
João	5511999999999	2026-01-25
Maria	5511988888888	2026-02-10

Observações:

O telefone deve conter código do país + DDD

A data deve estar no formato de data do Excel

Como Usar

Execute o script:

python main.py


O navegador será aberto no WhatsApp Web

Aguarde o tempo indicado para escanear o QR Code

As mensagens serão enviadas automaticamente para os contatos da planilha

Mensagem padrão enviada:

Olá João seu boleto vence dia: 25/01/2026.

Tratamento de Erros

Caso uma mensagem não seja enviada:

O número será registrado no arquivo errors.txt

O programa continuará a execução normalmente

Observações Importantes

O PyAutoGUI depende da resolução da tela

As coordenadas de clique podem precisar de ajuste

Não minimize o navegador durante a execução

O WhatsApp pode limitar envios em massa

Possíveis Melhorias

Remover dependência do PyAutoGUI

Adicionar envio de anexos

Criar interface gráfica

Melhorar sistema de logs

Aviso Legal

Este projeto tem finalidade educacional.
O uso inadequado pode violar os termos de uso do WhatsApp.