---
title: "Documentação do Fluxo: Filtro e Processamento de Mensagens"
flow_id: rjTbb1sbdqKYfyxr
flow_name: "Filtro de mensagens - Completo"
version: 1.0
created: 2025-07-26
modified: 2025-07-26
author: "[Seu Nome/Sua Equipe]"
status: "Versão Inicial"
abstract: "Detalha o fluxo n8n para receber, validar, classificar e processar mensagens. O fluxo trata diferentes tipos de mídia, integra-se com APIs externas (Google Gemini, Redis) e padroniza a saída para consumo por sistemas subsequentes."
tags:
  - n8n
  - automacao
  - workflow
  - chatbot
  - api
  - gemini
  - redis
audience:
  - "Desenvolvedores"
  - "Analistas de Automação"
  - "Equipe de TI"
related_systems:
  - "Plataforma n8n"
  - "Evolution API"
  - "Google Gemini API"
  - "Redis"
---

# Documentação do Fluxo: Filtro e Processamento de Mensagens

## Objetivo Geral

O objetivo principal deste fluxo é atuar como um gateway inteligente para todas as mensagens recebidas. Ele identifica o tipo de cada mensagem (texto, áudio, imagem, vídeo, documento), extrai o conteúdo relevante, o converte para um formato padronizado e o enriquece quando necessário (por exemplo, transcrevendo áudios ou fazendo upload de mídias).

## Componentes e Serviços Externos

O fluxo integra-se com os seguintes serviços:

- **Plataforma de Mensagens (via Webhook):** O ponto de entrada que envia os dados das mensagens recebidas.
- **API da Plataforma de Mensagens:** Utilizada para buscar o conteúdo de mídias (áudios, imagens, etc.).
- **[[Google Gemini API]]:** Usada para transcrever mensagens de áudio e para fazer o upload de arquivos de mídia.
- **[[Redis]]:** Um banco de dados em memória utilizado para armazenar temporariamente referências a arquivos de mídia associados a um usuário.

---

## Estrutura e Etapas do Fluxo

O fluxo pode ser dividido nas seguintes etapas lógicas:

### 1. Gatilho: Recebimento da Mensagem

- **Nó:** `Webhook EVO`
- **Descrição:** Este é o ponto de partida. O nó do tipo Webhook aguarda uma requisição `POST` em um endpoint específico (ex: `/odontosan`). Quando a plataforma de mensagens envia uma nova mensagem, ela dispara o início do fluxo.

### 2. Configuração Inicial e Verificação

- **Nó:** `Credenciais`
- **Descrição:** Este nó do tipo "Set" é responsável por configurar variáveis essenciais que serão usadas ao longo do fluxo, como credenciais de APIs, informações do contato e parâmetros gerais.

- **Nó:** `Verificar mensagem IA`
- **Descrição:** Um nó "IF" crucial para evitar loops. Ele verifica se a mensagem foi enviada pelo próprio sistema (`fromMe` é verdadeiro). Se sim, o fluxo é interrompido.

### 3. Roteamento por Tipo de Mensagem

- **Nó:** `Verifica o tipo da mensagem enviada1`
- **Descrição:** Este é o principal roteador do fluxo. Usando um nó "Switch", ele analisa o campo `messageType` e direciona a execução para um caminho específico dependendo do conteúdo.

### 4. Processamento Específico por Rota

#### a) Mensagens de Texto (`conversation`, `extendedTextMessage`, etc.)

- **Nós:** `Tratamento de dados` (múltiplos)
- **Descrição:** Para mensagens de texto, o fluxo extrai o conteúdo e o padroniza em um formato comum, contendo `remoteJid`, `textMessage`, `id` e `timestamp`.

#### b) Mensagens de Áudio (`audioMessage`)

- **Descrição:** Esta rota converte a fala em texto.
	1. **`Pega base64 do audio1`:** Faz uma chamada à API para obter o arquivo de áudio em formato base64.
	2. **`Transcrever audio Gemini`:** Envia o áudio para a API do Google Gemini para transcrição.
	3. **`Tratamento de dados8`:** Pega o texto transcrito e o formata no campo `textMessage`, padronizando a saída.

#### c) Mensagens de Mídia (`imageMessage`, `videoMessage`, `documentMessage`)

- **Descrição:** Esta rota processa arquivos, fazendo o upload para um serviço de nuvem e armazenando a referência.
	1. **`Pega base64 da imagem/documento`:** Obtém o arquivo de mídia em base64.
	2. **`Verifica se o arquivo tem mais de 20MB`:** Condição para o limite de upload do Gemini.
	3. **`Solicita link de upload midia` e `Faz Upload Arquivo`:** Executa o processo de upload para a API do Google Gemini.
	4. **`Verifica se arquivo tem legenda`:** Se a mídia tiver uma legenda (caption), ela é extraída como `textMessage`.
	5. **`Prepara body para input1`:** Prepara um objeto com as informações do arquivo após o upload.
	6. **`coloca arquivo na lista`:** Armazena a referência do arquivo no Redis, usando uma chave vinculada ao contato (ex: `img:55119...`).

### 5. Consolidação Final

- **Nó:** `Recebe mensagem e numero das rotas1`
- **Descrição:** Um nó "Merge" que serve como ponto de convergência para todas as rotas. Independentemente do tipo de mensagem original, a saída deste nó é um item padronizado.

---

## Saída do Fluxo

Ao final, temos um objeto de dados limpo e padronizado, pronto para ser enviado ao próximo sistema.

**Exemplo de Objeto de Saída:**
```json
{
  "remoteJid": "5511987654321@s.whatsapp.net",
  "textMessage": "Este é o conteúdo da mensagem (original ou transcrito).",
  "id": "3A1B2C3D4E5F6G7H",
  "timestamp": "1753546833"
}
```
---

### **Configurações e Variáveis a Preencher**

| Nó | Parâmetro / Variável | Descrição | Exemplo de Valor |
| :--- | :--- | :--- | :--- |
| **Credenciais** | `openai_token` | Sua chave de API da OpenAI (ou outro serviço de IA). | `sk-xxxxxxxxxxxx` |
| **Credenciais** | `Gemini_API_key` | Sua chave de API do Google Gemini. | `AIzaSyxxxxxxxxxxxx` |
| **Credenciais** | `evo_url` | A URL base da sua instância da Evolution API. | `https://api.suaempresa.com` |
| **Credenciais** | `evo_instace` | O nome da sua instância na Evolution API. | `minha-instancia` |
| **Credenciais** | `evo_apikey` | A chave de API da sua instância da Evolution API. | `809EEAFF8F28-xxxx-xxxx` |
| **coloca arquivo na lista** | Credencial Redis | A configuração de conexão com seu servidor Redis. | (Configurado na interface do n8n) |
| **Webhook EVO** | `path` | O caminho do endpoint do webhook. | `odontosan` |
