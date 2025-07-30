# ⚡ Coleção de Workflows N8N & Documentação

Uma coleção profissionalmente organizada de **2.053 workflows n8n** com um sistema de documentação ultrarrápido que oferece recursos de busca, análise e navegação instantâneos.

## 🚀 **NOVO: Sistema de Documentação de Alto Desempenho**

**Experimente uma melhoria de desempenho 100x em relação à documentação tradicional!**

### Início Rápido - Sistema de Documentação Rápida
```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor API rápido
python run.py

# Abrir no navegador
http://localhost:8000
```

**Recursos:**
- ⚡ **Tempos de resposta abaixo de 100ms** com busca SQLite FTS5
- 🔍 **Busca em texto completo instantânea** com filtragem avançada
- 📱 **Design responsivo** - funciona perfeitamente em dispositivos móveis
- 🌙 **Temas claro/escuro** com detecção de preferência do sistema
- 📊 **Estatísticas em tempo real** - 365 integrações únicas, 29.445 nós no total
- 🎯 **Categorização inteligente** por tipo de gatilho e complexidade
- 🎯 **Categorização por caso de uso** com mapeamento de nomes de serviços para categorias
- 📄 **Visualização e download de JSON** sob demanda
- 🔗 **Geração de diagramas Mermaid** para visualização de fluxos de trabalho
- 🔄 **Nomeação em tempo real de fluxos de trabalho** com formatação inteligente

### Comparação de Desempenho

| Métrica | Sistema Antigo | Novo Sistema | Melhoria |
|---------|----------------|--------------|-----------|
| **Tamanho do Arquivo** | 71MB HTML | <100KB | **700x menor** |
| **Tempo de Carregamento** | 10+ segundos | <1 segundo | **10x mais rápido** |
| **Busca** | Apenas no cliente | Texto completo com FTS5 | **Instantâneo** |
| **Uso de Memória** | ~2GB RAM | <50MB RAM | **40x menor** |
| **Suporte Móvel** | Ruim | Excelente | **Totalmente responsivo** |

---

## 📂 Organização do Repositório

### Coleção de Workflows
- **2.053 workflows** com nomes significativos e pesquisáveis
- **365 integrações únicas** em várias plataformas populares
- **29.445 nós no total** com categorização profissional
- **Garantia de qualidade** - Todos os workflows foram analisados e categorizados

### Sistema Avançado de Nomenclatura ✨
Nosso sistema inteligente de nomenclatura converte nomes de arquivos técnicos em títulos legíveis:
- **Antes**: `2051_Telegram_Webhook_Automation_Webhook.json`
- **Depois**: `Automação de Webhook do Telegram`
- **Nomes 100% significativos** com capitalização inteligente
- **Detecção automática de integração** a partir da análise de nós

### Categoria de Caso de Uso ✨

A interface de pesquisa inclui um filtro suspenso que permite navegar por mais de 2.000 workflows por categoria.

O sistema inclui um recurso de categorização automática que organiza os workflows por categorias de serviço para facilitar a descoberta e filtragem.

### Como Funciona a Categorização

1. **Execute o script de categorização**
   ```
   python create_categories.py
   ```

2. **Reconhecimento de Nomes de Serviço**
   O script analisa cada nome de arquivo JSON do workflow para identificar nomes de serviços reconhecidos (por exemplo, "Twilio", "Slack", "Gmail", etc.)

3. **Mapeamento de Categorias**
   Cada nome de serviço reconhecido é associado à sua categoria correspondente usando as definições em `context/def_categories.json`. Por exemplo:
   - Twilio → Comunicação e Mensagens
   - Gmail → Comunicação e Mensagens  
   - Airtable → Processamento e Análise de Dados
   - Salesforce → CRM e Vendas

4. **Geração de Categorias de Busca**
   O script gera um arquivo `search_categories.json` que contém os dados de workflow categorizados

5. **Interface de Filtro**
   Os usuários podem filtrar os workflows por categoria na interface de pesquisa, facilitando a localização de workflows para casos de uso específicos

### Categorias Disponíveis

O sistema de categorização inclui as seguintes categorias principais:
- Desenvolvimento de Agentes de IA
- Automação de Processos de Negócios
- Armazenamento em Nuvem e Gerenciamento de Arquivos
- Comunicação e Mensagens
- Conteúdo Criativo e Automação de Vídeo
- Automação de Design Criativo
- CRM e Vendas
- Processamento e Análise de Dados
- Comércio Eletrônico e Varejo
- Finanças e Contabilidade
- Automação de Marketing e Publicidade
- Gerenciamento de Projetos
- Gerenciamento de Mídias Sociais
- Infraestrutura Técnica e DevOps
- Web Scraping e Extração de Dados

### Contribua com Categorias

Você pode ajudar a expandir a categorização adicionando mais mapeamentos de serviço para categoria (por exemplo, Twilio → Comunicação e Mensagens) em context/defs_categories.json.

Muitos arquivos JSON de workflow são convenientemente nomeados com o nome do serviço, geralmente separados por sublinhados (_).


---

## 🛠 Instruções de Uso

### Opção 1: Sistema Rápido Moderno (Recomendado)
```bash
# Clonar o repositório
git clone <repo-url>
cd n8n-workflows

# Instalar dependências do Python
pip install -r requirements.txt

# Iniciar o servidor de documentação
python run.py

# Navegar pelos workflows em http://localhost:8000
# - Busca instantânea em 2.053 workflows
# - Interface profissional responsiva
# - Estatísticas de workflow em tempo real
```

### Opção 2: Modo de Desenvolvimento
```bash
# Iniciar com recarregamento automático para desenvolvimento
python run.py --dev

# Ou especificar host/porta personalizados
python run.py --host 0.0.0.0 --port 3000

# Forçar reindexação do banco de dados
python run.py --reindex
```

### Importar Workflows para o n8n
```bash
# Usar o importador Python (recomendado)
python import_workflows.py

# Ou importar manualmente workflows individuais:
# 1. Abra a interface do Editor n8n
# 2. Clique no menu (☰) → Importar workflow
# 3. Escolha qualquer arquivo .json da pasta workflows/
# 4. Atualize as credenciais/URLs de webhook antes de executar
```

---

## 📊 Estatísticas dos Workflows

### Estatísticas Atuais da Coleção
- **Total de Workflows**: 2.053 workflows de automação
- **Workflows Ativos**: 215 (taxa de ativos de 10,5%)
- **Total de Nós**: 29.445 (média de 14,3 nós por workflow)
- **Integrações Únicas**: 365 serviços e APIs diferentes
- **Banco de Dados**: SQLite com busca de texto completo FTS5

### Distribuição de Gatilhos
- **Complexo**: 831 workflows (40,5%) - Sistemas com múltiplos gatilhos  
- **Webhook**: 519 workflows (25,3%) - Automações acionadas por API  
- **Manual**: 477 workflows (23,2%) - Workflows iniciados pelo usuário
- **Agendado**: 226 workflows (11,0%) - Execuções baseadas em tempo

### Análise de Complexidade
- **Baixa (≤5 nós)**: ~35% - Automações simples
- **Média (6-15 nós)**: ~45% - Workflows padrão
- **Alta (16+ nós)**: ~20% - Sistemas empresariais complexos

### Popular Integrations
Top services by usage frequency:
- **Communication**: Telegram, Discord, Slack, WhatsApp
- **Cloud Storage**: Google Drive, Google Sheets, Dropbox
- **Databases**: PostgreSQL, MySQL, MongoDB, Airtable
- **AI/ML**: OpenAI, Anthropic, Hugging Face
- **Development**: HTTP Request, Webhook, GraphQL

---

## 🔍 Recursos Avançados de Busca

### Categorias de Busca Inteligente
Nosso sistema categoriza automaticamente os workflows em 12 categorias de serviço:

#### Categorias Disponíveis:
- **mensagens**: Telegram, Discord, Slack, WhatsApp, Teams
- **ia_ml**: OpenAI, Anthropic, Hugging Face 
- **banco_dados**: PostgreSQL, MySQL, MongoDB, Redis, Airtable
- **email**: Gmail, Mailjet, Outlook, SMTP/IMAP
- **armazenamento_nuvem**: Google Drive, Google Docs, Dropbox, OneDrive
- **gestao_projetos**: Jira, GitHub, GitLab, Trello, Asana
- **midias_sociais**: LinkedIn, Twitter/X, Facebook, Instagram
- **ecommerce**: Shopify, Stripe, PayPal
- **analytics**: Google Analytics, Mixpanel
- **calendario_tarefas**: Google Agenda, Cal.com, Calendly
- **formularios**: Typeform, Google Forms, Form Triggers
- **desenvolvimento**: Webhook, HTTP Request, GraphQL, SSE

### Exemplos de Uso da API
```bash
# Buscar workflows por texto
curl "http://localhost:8000/api/workflows?q=telegram+automacao"

# Filtrar por tipo de gatilho e complexidade
curl "http://localhost:8000/api/workflows?trigger=Webhook&complexity=alta"

# Encontrar todos os workflows de mensagens
curl "http://localhost:8000/api/workflows/category/mensagens"

# Obter estatísticas do banco de dados
curl "http://localhost:8000/api/stats"

# Navegar pelas categorias disponíveis
curl "http://localhost:8000/api/categories"
```

---

## 🏗 Arquitetura Técnica

### Stack Moderna
- **Banco de Dados SQLite** - Busca de texto completo FTS5 com 365 integrações indexadas
- **Backend FastAPI** - API RESTful com documentação OpenAPI automática
- **Frontend Responsivo** - HTML5 moderno com CSS/JavaScript incorporado
- **Análise Inteligente** - Categorização e nomenclatura automática de workflows

### Principais Recursos
- **Detecção de Mudanças** - Hash MD5 para reindexação eficiente
- **Processamento em Segundo Plano** - Análise de workflows não-bloqueante
- **Respostas Comprimidas** - Middleware Gzip para velocidade ideal
- **Tratamento de Erros** - Degradação graciosa e registro abrangente
- **Otimização para Dispositivos Móveis** - Interface amigável para toque

### Desempenho do Banco de Dados
```sql
-- Esquema otimizado para consultas ultrarrápidas
CREATE TABLE workflows (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE,
    name TEXT,
    active BOOLEAN,
    trigger_type TEXT,
    complexity TEXT,
    node_count INTEGER,
    integrations TEXT,  -- Array JSON de 365 serviços únicos
    description TEXT,
    file_hash TEXT,     -- MD5 para detecção de alterações
    analyzed_at TIMESTAMP
);

-- Busca de texto completo com classificação
CREATE VIRTUAL TABLE workflows_fts USING fts5(
    filename, name, description, integrations, tags,
    content='workflows', content_rowid='id'
);
```

---

## 🔧 Configuração e Requisitos

### Requisitos do Sistema
- **Python 3.7+** - Para executar o sistema de documentação
- **Navegador Moderno** - Chrome, Firefox, Safari, Edge
- **50MB de Armazenamento** - Para o banco de dados SQLite e índices
- **Instância n8n** - Para importar e executar os workflows

### Instalação
```bash
# Clonar o repositório
git clone <repo-url>
cd n8n-workflows

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor de documentação
python run.py

# Acessar em http://localhost:8000
```

### Configuração de Desenvolvimento
```bash
# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows

# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar testes
pytest tests/

# Verificar estilo de código
flake8 src/

# Formatar código
black src/
```

---

## 📋 Naming Convention

### Intelligent Formatting System
Our system automatically converts technical filenames to user-friendly names:

```bash
# Automatic transformations:
2051_Telegram_Webhook_Automation_Webhook.json → "Telegram Webhook Automation"
0250_HTTP_Discord_Import_Scheduled.json → "HTTP Discord Import Scheduled"  
0966_OpenAI_Data_Processing_Manual.json → "OpenAI Data Processing Manual"
```

### Technical Format
```
[ID]_[Service1]_[Service2]_[Purpose]_[Trigger].json
```

### Smart Capitalization Rules
- **HTTP** → HTTP (not Http)
- **API** → API (not Api)  
- **webhook** → Webhook
- **automation** → Automation
- **scheduled** → Scheduled

---

## 🚀 API Documentation

### Core Endpoints
- `GET /` - Main workflow browser interface
- `GET /api/stats` - Database statistics and metrics
- `GET /api/workflows` - Search with filters and pagination
- `GET /api/workflows/{filename}` - Detailed workflow information
- `GET /api/workflows/{filename}/download` - Download workflow JSON
- `GET /api/workflows/{filename}/diagram` - Generate Mermaid diagram

### Advanced Search
- `GET /api/workflows/category/{category}` - Search by service category
- `GET /api/categories` - List all available categories
- `GET /api/integrations` - Get integration statistics
- `POST /api/reindex` - Trigger background reindexing

### Response Examples
```json
// GET /api/stats
{
  "total": 2053,
  "active": 215,
  "inactive": 1838,
  "triggers": {
    "Complex": 831,
    "Webhook": 519,
    "Manual": 477,
    "Scheduled": 226
  },
  "total_nodes": 29445,
  "unique_integrations": 365
}
```

---

## 🤝 Contribuindo

### Adicionando Novos Workflows
1. **Exporte o workflow** como JSON do n8n
2. **Nomeie de forma descritiva** seguindo o padrão estabelecido
3. **Adicione à pasta workflows/**
4. **Remova dados sensíveis** (credenciais, URLs pessoais)
5. **Execute a reindexação** para atualizar o banco de dados

### Padrões de Qualidade
- ✅ O workflow deve ser funcional e testado
- ✅ Remova todas as credenciais e dados sensíveis
- ✅ Siga a convenção de nomenclatura para consistência
- ✅ Verifique a compatibilidade com versões recentes do n8n
- ✅ Inclua uma descrição ou comentários significativos

---

## ⚠️ Notas Importantes

### Segurança e Privacidade
- **Revise antes de usar** - Todos os workflows são compartilhados como estão, para fins educacionais
- **Atualize as credenciais** - Substitua chaves de API, tokens e webhooks
- **Teste com segurança** - Verifique primeiro em um ambiente de desenvolvimento
- **Verifique as permissões** - Garanta os direitos de acesso adequados para as integrações

### Compatibilidade
- **Versão do n8n** - Compatível com n8n 1.0+ (a maioria dos workflows)
- **Nós da Comunidade** - Alguns workflows podem exigir instalações adicionais de nós
- **Mudanças na API** - Serviços externos podem ter atualizado suas APIs desde a criação
- **Dependências** - Verifique as integrações necessárias antes de importar

---

## 📚 Recursos e Referências

### Fontes dos Workflows
Esta coleção abrangente inclui workflows de:
- **n8n.io Oficial** - Documentação e exemplos da comunidade
- **Repositórios do GitHub** - Contribuições da comunidade de código aberto  
- **Posts de blog e tutoriais** - Padrões de automação do mundo real
- **Submissões de usuários** - Workflows testados e verificados
- **Casos de uso empresariais** - Automações de processos de negócios

### Saiba Mais
- [Documentação do n8n](https://docs.n8n.io/) - Documentação oficial
- [Comunidade n8n](https://community.n8n.io/) - Fórum e suporte da comunidade
- [Modelos de Workflow](https://n8n.io/workflows/) - Biblioteca oficial de modelos
- [Documentação de Integrações](https://docs.n8n.io/integrations/) - Guias específicos por serviço

---

## 🏆 Conquistas do Projeto

### Transformação do Repositório
- **2.053 workflows** organizados e nomeados profissionalmente
- **365 integrações únicas** detectadas e categorizadas automaticamente
- **Nomes 100% significativos** (melhorados a partir de padrões básicos de nomeação de arquivos)
- **Nenhuma perda de dados** durante o processo de renomeação inteligente
- **Busca avançada** com 12 categorias de serviço

### Revolução de Desempenho
- **Busca em menos de 100ms** com indexação de texto completo SQLite FTS5
- **Filtragem instantânea** em 29.445 nós de workflow
- **Design responsivo** otimizado para dispositivos móveis
- **Estatísticas em tempo real** com consultas ao banco de dados ao vivo
- **Interface profissional** com princípios modernos de UX

### Confiabilidade do Sistema
- **Tratamento robusto de erros** com degradação graciosa
- **Detecção de alterações** para atualizações eficientes do banco de dados
- **Processamento em segundo plano** para operações não-bloqueantes
- **Registro abrangente** para depuração e monitoramento
- **Pronto para produção** com middleware e segurança adequados

---

*Este repositório representa a coleção mais abrangente e bem organizada de workflows n8n disponíveis, apresentando tecnologia de busca de ponta e documentação profissional que torna a descoberta e o uso de workflows uma experiência agradável.*

**🎯 Perfeito para**: Desenvolvedores, engenheiros de automação, analistas de negócios e qualquer pessoa que deseje simplificar seus fluxos de trabalho com automações n8n comprovadas.

---

[中文](./README_ZH.md) | [Português](./README.md)
