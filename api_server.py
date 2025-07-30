#!/usr/bin/env python3
"""
Servidor FastAPI para Documentação de Workflows N8N - GG.AI Labs
API de alta performance com respostas abaixo de 100ms.
"""

from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import BaseModel, field_validator
from typing import Optional, List, Dict, Any
import json
import os
import asyncio
from pathlib import Path
import uvicorn

from workflow_db import WorkflowDatabase

app = FastAPI(
    title="GG.AI Labs - API de Documentação de Workflows N8N",
    description="API rápida para navegação e busca de documentação de workflows",
    version="2.0.0"
)

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = WorkflowDatabase()

@app.on_event("startup")
async def startup_event():
    """Verifica a conectividade com o banco de dados ao iniciar."""
    try:
        stats = db.get_stats()
        if stats['total'] == 0:
            print("⚠️  Aviso: Nenhum workflow encontrado no banco. Execute o indexador primeiro.")
        else:
            print(f"✅ Banco de dados conectado: {stats['total']} workflows indexados")
    except Exception as e:
        print(f"❌ Falha ao conectar no banco de dados: {e}")
        raise

class WorkflowSummary(BaseModel):
    id: Optional[int] = None
    filename: str
    name: str
    active: bool
    description: str = ""
    trigger_type: str = "Manual"
    complexity: str = "low"
    node_count: int = 0
    integrations: List[str] = []
    tags: List[str] = []
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        validate_assignment = True

    @field_validator('active', mode='before')
    @classmethod
    def convert_active(cls, v):
        if isinstance(v, int):
            return bool(v)
        return v

class SearchResponse(BaseModel):
    workflows: List[WorkflowSummary]
    total: int
    page: int
    per_page: int
    pages: int
    query: str
    filters: Dict[str, Any]

class StatsResponse(BaseModel):
    total: int
    active: int
    inactive: int
    triggers: Dict[str, int]
    complexity: Dict[str, int]
    total_nodes: int
    unique_integrations: int
    last_indexed: str

@app.get("/")
async def root():
    """Exibe a página principal de documentação."""
    static_dir = Path("static")
    index_file = static_dir / "index.html"
    if not index_file.exists():
        return HTMLResponse("""
        <html><body>
        <h1>Configuração necessária</h1>
        <p>Arquivos estáticos não encontrados. Certifique-se de que a pasta static existe com index.html</p>
        <p>Diretório atual: """ + str(Path.cwd()) + """</p>
        </body></html>
        """)
    return FileResponse(str(index_file))

@app.get("/health")
async def health_check():
    """Endpoint de saúde."""
    return {"status": "ok", "version": "2.0.0", "mensagem": "API de Workflows N8N rodando"}

@app.get("/api/version")
async def get_version():
    """Obtém a versão da API."""
    return {"version": "2.0.0"}

@app.get("/api/stats", response_model=StatsResponse)
async def get_stats():
    """Obtém estatísticas do banco de dados de workflows."""
    try:
        stats = db.get_stats()
        return StatsResponse(**stats)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar estatísticas: {str(e)}")

@app.get("/api/workflows", response_model=SearchResponse)
async def search_workflows(
    q: str = Query("", description="Consulta de busca"),
    trigger: str = Query("all", description="Filtrar por tipo de disparo"),
    complexity: str = Query("all", description="Filtrar por complexidade"),
    active_only: bool = Query(False, description="Apenas workflows ativos"),
    page: int = Query(1, ge=1, description="Página"),
    per_page: int = Query(20, ge=1, le=100, description="Itens por página")
):
    """Busca e filtra workflows com paginação."""
    try:
        offset = (page - 1) * per_page

        workflows, total = db.search_workflows(
            query=q,
            trigger_filter=trigger,
            complexity_filter=complexity,
            active_only=active_only,
            limit=per_page,
            offset=offset
        )

        workflow_summaries = []
        for workflow in workflows:
            try:
                clean_workflow = {
                    'id': workflow.get('id'),
                    'filename': workflow.get('filename', ''),
                    'name': workflow.get('name', ''),
                    'active': workflow.get('active', False),
                    'description': workflow.get('description', ''),
                    'trigger_type': workflow.get('trigger_type', 'Manual'),
                    'complexity': workflow.get('complexity', 'low'),
                    'node_count': workflow.get('node_count', 0),
                    'integrations': workflow.get('integrations', []),
                    'tags': workflow.get('tags', []),
                    'created_at': workflow.get('created_at'),
                    'updated_at': workflow.get('updated_at')
                }
                workflow_summaries.append(WorkflowSummary(**clean_workflow))
            except Exception as e:
                print(f"Erro ao converter workflow {workflow.get('filename', 'desconhecido')}: {e}")
                continue

        pages = (total + per_page - 1) // per_page

        return SearchResponse(
            workflows=workflow_summaries,
            total=total,
            page=page,
            per_page=per_page,
            pages=pages,
            query=q,
            filters={
                "trigger": trigger,
                "complexity": complexity,
                "active_only": active_only
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar workflows: {str(e)}")

@app.get("/api/workflows/{filename}")
async def get_workflow_detail(filename: str):
    """Obtém detalhes completos do workflow, incluindo JSON bruto."""
    try:
        workflows, _ = db.search_workflows(f'filename:"{filename}"', limit=1)
        if not workflows:
            raise HTTPException(status_code=404, detail="Workflow não encontrado no banco")
        workflow_meta = workflows[0]
        file_path = os.path.join("workflows", filename)
        if not os.path.exists(file_path):
            print(f"Aviso: Arquivo {file_path} não encontrado no sistema, mas está no banco")
            raise HTTPException(status_code=404, detail=f"Arquivo '{filename}' não encontrado")
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_json = json.load(f)
        return {
            "metadata": workflow_meta,
            "raw_json": raw_json
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao carregar workflow: {str(e)}")

@app.get("/api/workflows/{filename}/download")
async def download_workflow(filename: str):
    """Baixa o arquivo JSON do workflow."""
    try:
        file_path = os.path.join("workflows", filename)
        if not os.path.exists(file_path):
            print(f"Aviso: Download solicitado para arquivo ausente: {file_path}")
            raise HTTPException(status_code=404, detail=f"Arquivo '{filename}' não encontrado")
        return FileResponse(
            file_path,
            media_type="application/json",
            filename=filename
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Arquivo '{filename}' não encontrado")
    except Exception as e:
        print(f"Erro ao baixar workflow {filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao baixar workflow: {str(e)}")

@app.get("/api/workflows/{filename}/diagram")
async def get_workflow_diagram(filename: str):
    """Obtém o diagrama Mermaid para visualização do workflow."""
    try:
        file_path = os.path.join("workflows", filename)
        if not os.path.exists(file_path):
            print(f"Aviso: Diagrama solicitado para arquivo ausente: {file_path}")
            raise HTTPException(status_code=404, detail=f"Arquivo '{filename}' não encontrado")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        nodes = data.get('nodes', [])
        connections = data.get('connections', {})
        diagram = generate_mermaid_diagram(nodes, connections)
        return {"diagram": diagram}
    except HTTPException:
        raise
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Arquivo '{filename}' não encontrado")
    except json.JSONDecodeError as e:
        print(f"Erro ao ler JSON em {filename}: {str(e)}")
        raise HTTPException(status_code=400, detail=f"JSON inválido no workflow: {str(e)}")
    except Exception as e:
        print(f"Erro ao gerar diagrama para {filename}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao gerar diagrama: {str(e)}")

def generate_mermaid_diagram(nodes: List[Dict], connections: Dict) -> str:
    """Gera código Mermaid.js a partir dos nós e conexões do workflow."""
    if not nodes:
        return "graph TD\n  EmptyWorkflow[Sem nós encontrados no workflow]"
    mermaid_ids = {}
    for i, node in enumerate(nodes):
        node_id = f"node{i}"
        node_name = node.get('name', f'Node {i}')
        mermaid_ids[node_name] = node_id
    mermaid_code = ["graph TD"]
    for node in nodes:
        node_name = node.get('name', 'Sem nome')
        node_id = mermaid_ids[node_name]
        node_type = node.get('type', '').replace('n8n-nodes-base.', '')
        style = ""
        if any(x in node_type.lower() for x in ['trigger', 'webhook', 'cron']):
            style = "fill:#b3e0ff,stroke:#0066cc"
        elif any(x in node_type.lower() for x in ['if', 'switch']):
            style = "fill:#ffffb3,stroke:#e6e600"
        elif any(x in node_type.lower() for x in ['function', 'code']):
            style = "fill:#d9b3ff,stroke:#6600cc"
        elif 'error' in node_type.lower():
            style = "fill:#ffb3b3,stroke:#cc0000"
        else:
            style = "fill:#d9d9d9,stroke:#666666"
        clean_name = node_name.replace('"', "'")
        clean_type = node_type.replace('"', "'")
        label = f"{clean_name}<br>({clean_type})"
        mermaid_code.append(f"  {node_id}[\"{label}\"]")
        mermaid_code.append(f"  style {node_id} {style}")
    for source_name, source_connections in connections.items():
        if source_name not in mermaid_ids:
            continue
        if isinstance(source_connections, dict) and 'main' in source_connections:
            main_connections = source_connections['main']
            for i, output_connections in enumerate(main_connections):
                if not isinstance(output_connections, list):
                    continue
                for connection in output_connections:
                    if not isinstance(connection, dict) or 'node' not in connection:
                        continue
                    target_name = connection['node']
                    if target_name not in mermaid_ids:
                        continue
                    label = f" -->|{i}| " if len(main_connections) > 1 else " --> "
                    mermaid_code.append(f"  {mermaid_ids[source_name]}{label}{mermaid_ids[target_name]}")
    return "\n".join(mermaid_code)

@app.post("/api/reindex")
async def reindex_workflows(background_tasks: BackgroundTasks, force: bool = False):
    """Reindexa workflows em segundo plano."""
    def run_indexing():
        db.index_all_workflows(force_reindex=force)
    background_tasks.add_task(run_indexing)
    return {"mensagem": "Reindexação iniciada em segundo plano"}

@app.get("/api/integrations")
async def get_integrations():
    """Obtém lista de todas as integrações únicas."""
    try:
        stats = db.get_stats()
        return {"integrations": [], "count": stats['unique_integrations']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar integrações: {str(e)}")

@app.get("/api/categories")
async def get_categories():
    """Obtém categorias disponíveis para filtragem."""
    try:
        categories_file = Path("context/unique_categories.json")
        if categories_file.exists():
            with open(categories_file, 'r', encoding='utf-8') as f:
                categories = json.load(f)
            return {"categories": categories}
        else:
            search_categories_file = Path("context/search_categories.json")
            if search_categories_file.exists():
                with open(search_categories_file, 'r', encoding='utf-8') as f:
                    search_data = json.load(f)
                unique_categories = set()
                for item in search_data:
                    if item.get('category'):
                        unique_categories.add(item['category'])
                    else:
                        unique_categories.add('Sem categoria')
                categories = sorted(list(unique_categories))
                return {"categories": categories}
            else:
                return {"categories": ["Sem categoria"]}
    except Exception as e:
        print(f"Erro ao carregar categorias: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao buscar categorias: {str(e)}")

@app.get("/api/category-mappings")
async def get_category_mappings():
    """Obtém mapeamento de arquivo para categoria."""
    try:
        search_categories_file = Path("context/search_categories.json")
        if not search_categories_file.exists():
            return {"mappings": {}}
        with open(search_categories_file, 'r', encoding='utf-8') as f:
            search_data = json.load(f)
        mappings = {}
        for item in search_data:
            filename = item.get('filename')
            category = item.get('category') or 'Sem categoria'
            if filename:
                mappings[filename] = category
        return {"mappings": mappings}
    except Exception as e:
        print(f"Erro ao carregar mapeamentos de categoria: {e}")
        raise HTTPException(status_code=500, detail=f"Erro ao buscar mapeamentos de categoria: {str(e)}")

@app.get("/api/workflows/category/{category}", response_model=SearchResponse)
async def search_workflows_by_category(
    category: str,
    page: int = Query(1, ge=1, description="Página"),
    per_page: int = Query(20, ge=1, le=100, description="Itens por página")
):
    """Busca workflows por categoria de serviço."""
    try:
        offset = (page - 1) * per_page
        workflows, total = db.search_by_category(
            category=category,
            limit=per_page,
            offset=offset
        )
        workflow_summaries = []
        for workflow in workflows:
            try:
                clean_workflow = {
                    'id': workflow.get('id'),
                    'filename': workflow.get('filename', ''),
                    'name': workflow.get('name', ''),
                    'active': workflow.get('active', False),
                    'description': workflow.get('description', ''),
                    'trigger_type': workflow.get('trigger_type', 'Manual'),
                    'complexity': workflow.get('complexity', 'low'),
                    'node_count': workflow.get('node_count', 0),
                    'integrations': workflow.get('integrations', []),
                    'tags': workflow.get('tags', []),
                    'created_at': workflow.get('created_at'),
                    'updated_at': workflow.get('updated_at')
                }
                workflow_summaries.append(WorkflowSummary(**clean_workflow))
            except Exception as e:
                print(f"Erro ao converter workflow {workflow.get('filename', 'desconhecido')}: {e}")
                continue
        pages = (total + per_page - 1) // per_page
        return SearchResponse(
            workflows=workflow_summaries,
            total=total,
            page=page,
            per_page=per_page,
            pages=pages,
            query=f"category:{category}",
            filters={"category": category}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar por categoria: {str(e)}")

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": f"Erro interno no servidor: {str(exc)}"}
    )

static_dir = Path("static")
if static_dir.exists():
    app.mount("/static", StaticFiles(directory="static"), name="static")
    print(f"✅ Arquivos estáticos carregados de {static_dir.absolute()}")
else:
    print(f"❌ Atenção: Diretório static não encontrado em {static_dir.absolute()}")

def create_static_directory():
    static_dir = Path("static")
    static_dir.mkdir(exist_ok=True)
    return static_dir

def run_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    create_static_directory()
    try:
        stats = db.get_stats()
        print(f"✅ Banco de dados conectado: {stats['total']} workflows encontrados")
        if stats['total'] == 0:
            print("🔄 Banco vazio. Indexando workflows...")
            db.index_all_workflows()
            stats = db.get_stats()
    except Exception as e:
        print(f"❌ Erro no banco de dados: {e}")
        print("🔄 Tentando criar e indexar banco de dados...")
        try:
            db.index_all_workflows()
            stats = db.get_stats()
            print(f"✅ Banco criado: {stats['total']} workflows indexados")
        except Exception as e2:
            print(f"❌ Falha ao criar banco: {e2}")
            stats = {'total': 0}
    static_path = Path("static")
    if static_path.exists():
        files = list(static_path.glob("*"))
        print(f"✅ Arquivos estáticos encontrados: {[f.name for f in files]}")
    else:
        print(f"❌ Diretório static não encontrado: {static_path.absolute()}")
    print(f"🚀 Iniciando GG.AI Labs - API de Documentação de Workflows N8N")
    print(f"📊 Banco contém {stats['total']} workflows")
    print(f"🌐 Servidor disponível em: http://{host}:{port}")
    print(f"📁 Arquivos estáticos em: http://{host}:{port}/static/")
    uvicorn.run(
        "api_server:app",
        host=host,
        port=port,
        reload=reload,
        access_log=True,
        log_level="info"
    )

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Servidor GG.AI Labs - API de Documentação de Workflows N8N')
    parser.add_argument('--host', default='127.0.0.1', help='Host')
    parser.add_argument('--port', type=int, default=8000, help='Porta')
    parser.add_argument('--reload', action='store_true', help='Auto-reload para desenvolvimento')

    args = parser.parse_args()

    run_server(host=args.host, port=args.port, reload=args.reload)
