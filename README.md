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

## 🔍 Advanced Search Features

### Smart Search Categories
Our system automatically categorizes workflows into 12 service categories:

#### Available Categories:
- **messaging**: Telegram, Discord, Slack, WhatsApp, Teams
- **ai_ml**: OpenAI, Anthropic, Hugging Face 
- **database**: PostgreSQL, MySQL, MongoDB, Redis, Airtable
- **email**: Gmail, Mailjet, Outlook, SMTP/IMAP
- **cloud_storage**: Google Drive, Google Docs, Dropbox, OneDrive
- **project_management**: Jira, GitHub, GitLab, Trello, Asana
- **social_media**: LinkedIn, Twitter/X, Facebook, Instagram
- **ecommerce**: Shopify, Stripe, PayPal
- **analytics**: Google Analytics, Mixpanel
- **calendar_tasks**: Google Calendar, Cal.com, Calendly
- **forms**: Typeform, Google Forms, Form Triggers
- **development**: Webhook, HTTP Request, GraphQL, SSE

### API Usage Examples
```bash
# Search workflows by text
curl "http://localhost:8000/api/workflows?q=telegram+automation"

# Filter by trigger type and complexity
curl "http://localhost:8000/api/workflows?trigger=Webhook&complexity=high"

# Find all messaging workflows
curl "http://localhost:8000/api/workflows/category/messaging"

# Get database statistics
curl "http://localhost:8000/api/stats"

# Browse available categories
curl "http://localhost:8000/api/categories"
```

---

## 🏗 Technical Architecture

### Modern Stack
- **SQLite Database** - FTS5 full-text search with 365 indexed integrations
- **FastAPI Backend** - RESTful API with automatic OpenAPI documentation
- **Responsive Frontend** - Modern HTML5 with embedded CSS/JavaScript
- **Smart Analysis** - Automatic workflow categorization and naming

### Key Features
- **Change Detection** - MD5 hashing for efficient re-indexing
- **Background Processing** - Non-blocking workflow analysis
- **Compressed Responses** - Gzip middleware for optimal speed
- **Error Handling** - Graceful degradation and comprehensive logging
- **Mobile Optimization** - Touch-friendly interface design

### Database Performance
```sql
-- Optimized schema for lightning-fast queries
CREATE TABLE workflows (
    id INTEGER PRIMARY KEY,
    filename TEXT UNIQUE,
    name TEXT,
    active BOOLEAN,
    trigger_type TEXT,
    complexity TEXT,
    node_count INTEGER,
    integrations TEXT,  -- JSON array of 365 unique services
    description TEXT,
    file_hash TEXT,     -- MD5 for change detection
    analyzed_at TIMESTAMP
);

-- Full-text search with ranking
CREATE VIRTUAL TABLE workflows_fts USING fts5(
    filename, name, description, integrations, tags,
    content='workflows', content_rowid='id'
);
```

---

## 🔧 Setup & Requirements

### System Requirements
- **Python 3.7+** - For running the documentation system
- **Modern Browser** - Chrome, Firefox, Safari, Edge
- **50MB Storage** - For SQLite database and indexes
- **n8n Instance** - For importing and running workflows

### Installation
```bash
# Clone repository
git clone <repo-url>
cd n8n-workflows

# Install dependencies
pip install -r requirements.txt

# Start documentation server
python run.py

# Access at http://localhost:8000
```

### Development Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run with auto-reload for development
python api_server.py --reload

# Force database reindexing
python workflow_db.py --index --force
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

## 🤝 Contributing

### Adding New Workflows
1. **Export workflow** as JSON from n8n
2. **Name descriptively** following the established pattern
3. **Add to workflows/** directory
4. **Remove sensitive data** (credentials, personal URLs)
5. **Run reindexing** to update the database

### Quality Standards
- ✅ Workflow must be functional and tested
- ✅ Remove all credentials and sensitive data
- ✅ Follow naming convention for consistency
- ✅ Verify compatibility with recent n8n versions
- ✅ Include meaningful description or comments

---

## ⚠️ Important Notes

### Security & Privacy
- **Review before use** - All workflows shared as-is for educational purposes
- **Update credentials** - Replace API keys, tokens, and webhooks
- **Test safely** - Verify in development environment first
- **Check permissions** - Ensure proper access rights for integrations

### Compatibility
- **n8n Version** - Compatible with n8n 1.0+ (most workflows)
- **Community Nodes** - Some workflows may require additional node installations
- **API Changes** - External services may have updated their APIs since creation
- **Dependencies** - Verify required integrations before importing

---

## 📚 Resources & References

### Workflow Sources
This comprehensive collection includes workflows from:
- **Official n8n.io** - Documentation and community examples
- **GitHub repositories** - Open source community contributions  
- **Blog posts & tutorials** - Real-world automation patterns
- **User submissions** - Tested and verified workflows
- **Enterprise use cases** - Business process automations

### Learn More
- [n8n Documentation](https://docs.n8n.io/) - Official documentation
- [n8n Community](https://community.n8n.io/) - Community forum and support
- [Workflow Templates](https://n8n.io/workflows/) - Official template library
- [Integration Docs](https://docs.n8n.io/integrations/) - Service-specific guides

---

## 🏆 Project Achievements

### Repository Transformation
- **2,053 workflows** professionally organized and named
- **365 unique integrations** automatically detected and categorized
- **100% meaningful names** (improved from basic filename patterns)
- **Zero data loss** during intelligent renaming process
- **Advanced search** with 12 service categories

### Performance Revolution
- **Sub-100ms search** with SQLite FTS5 full-text indexing
- **Instant filtering** across 29,445 workflow nodes
- **Mobile-optimized** responsive design for all devices
- **Real-time statistics** with live database queries
- **Professional interface** with modern UX principles

### System Reliability
- **Robust error handling** with graceful degradation
- **Change detection** for efficient database updates
- **Background processing** for non-blocking operations
- **Comprehensive logging** for debugging and monitoring
- **Production-ready** with proper middleware and security

---

*This repository represents the most comprehensive and well-organized collection of n8n workflows available, featuring cutting-edge search technology and professional documentation that makes workflow discovery and usage a delightful experience.*

**🎯 Perfect for**: Developers, automation engineers, business analysts, and anyone looking to streamline their workflows with proven n8n automations.

---

[中文](./README_ZH.md)
