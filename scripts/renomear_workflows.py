#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

# Dicionário de tradução de termos comuns
TRADUCOES = {
    # Termos gerais
    'Manual': 'Manual',
    'Schedule': 'Agendado',
    'Disparado': 'Disparador',
    'Webhook': 'Webhook',
    'Automation': 'Automação',
    'Automate': 'Automatizar',
    'Create': 'Criar',
    'Update': 'Atualizar',
    'Delete': 'Excluir',
    'Import': 'Importar',
    'Export': 'Exportar',
    'Send': 'Enviar',
    'Process': 'Processar',
    'Monitor': 'Monitorar',
    'Sync': 'Sincronizar',
    'Complex': 'Complexo',
    'Scheduled': 'Agendado',
    'Cron': 'Cron',
    'Interval': 'Intervalo',
    'Error': 'Erro',
    'Wait': 'Aguardar',
    'Filter': 'Filtrar',
    'Code': 'Código',
    'Splitout': 'Dividir',
    'Stopanderror': 'PararErro',
    'Form': 'Formulário',
    'Debughelper': 'AjudaDepuracao',
    'Aggregate': 'Agregar',
    'Limit': 'Limite',
    'Respondtowebhook': 'ResponderWebhook',
    'Readbinaryfile': 'LerArquivoBinario',
    'Writebinaryfile': 'EscreverArquivoBinario',
    'Movebinarydata': 'MoverDadosBinarios',
    'Converttofile': 'ConverterParaArquivo',
    'Extractfromfile': 'ExtrairDeArquivo',
    'Editimage': 'EditarImagem',
    'Itemlists': 'ListasItens',
    'Executecommand': 'ExecutarComando',
    'Executeworkflow': 'ExecutarWorkflow',
    
    # Serviços e plataformas
    'Telegram': 'Telegram',
    'GoogleSheets': 'PlanilhasGoogle',
    'GoogleDrive': 'GoogleDrive',
    'GoogleCalendar': 'GoogleCalendar',
    'Slack': 'Slack',
    'Discord': 'Discord',
    'GitHub': 'GitHub',
    'GitLab': 'GitLab',
    'Twitter': 'Twitter',
    'Facebook': 'Facebook',
    'Instagram': 'Instagram',
    'LinkedIn': 'LinkedIn',
    'YouTube': 'YouTube',
    'Notion': 'Notion',
    'Airtable': 'Airtable',
    'Trello': 'Trello',
    'Asana': 'Asana',
    'ClickUp': 'ClickUp',
    'Monday': 'Monday',
    'Jira': 'Jira',
    'Zendesk': 'Zendesk',
    'HubSpot': 'HubSpot',
    'Pipedrive': 'Pipedrive',
    'Salesforce': 'Salesforce',
    'Mailchimp': 'Mailchimp',
    'SendGrid': 'SendGrid',
    'Stripe': 'Stripe',
    'PayPal': 'PayPal',
    'Shopify': 'Shopify',
    'WooCommerce': 'WooCommerce',
    'WordPress': 'WordPress',
    'Magento': 'Magento',
    'BigCommerce': 'BigCommerce',
    'AWS': 'AWS',
    'Azure': 'Azure',
    'GCP': 'GCP',
    'MongoDB': 'MongoDB',
    'PostgreSQL': 'PostgreSQL',
    'MySQL': 'MySQL',
    'SQLServer': 'SQLServer',
    'SQLite': 'SQLite',
    'Redis': 'Redis',
    'Elasticsearch': 'Elasticsearch',
    'Kafka': 'Kafka',
    'RabbitMQ': 'RabbitMQ',
    'NATS': 'NATS',
    'MQTT': 'MQTT',
    'OpenAI': 'OpenAI',
    'HuggingFace': 'HuggingFace',
    'StabilityAI': 'StabilityAI',
    'Replicate': 'Replicate',
    'Pinecone': 'Pinecone',
    'Weaviate': 'Weaviate',
    'Qdrant': 'Qdrant',
    'Milvus': 'Milvus',
    'Chroma': 'Chroma',
    'Puppeteer': 'Puppeteer',
    'Playwright': 'Playwright',
    'Selenium': 'Selenium',
    'BeautifulSoup': 'BeautifulSoup',
    'Cheerio': 'Cheerio',
    'PuppeteerToIstanbul': 'PuppeteerToIstanbul',
    'PuppeteerToVideo': 'PuppeteerToVideo',
    'PuppeteerToPDF': 'PuppeteerToPDF',
    'PuppeteerToHar': 'PuppeteerToHar',
    'PuppeteerToMHTML': 'PuppeteerToMHTML',
    'PuppeteerToPNG': 'PuppeteerToPNG',
    'PuppeteerToJPEG': 'PuppeteerToJPEG',
    'PuppeteerToWebP': 'PuppeteerToWebP',
    'PuppeteerToTIFF': 'PuppeteerToTIFF',
    'PuppeteerToBMP': 'PuppeteerToBMP',
    'PuppeteerToGIF': 'PuppeteerToGIF',
    'PuppeteerToICO': 'PuppeteerToICO',
    'PuppeteerToSVG': 'PuppeteerToSVG',
    'PuppeteerToWebM': 'PuppeteerToWebM',
    'PuppeteerToMP4': 'PuppeteerToMP4',
    'PuppeteerToMOV': 'PuppeteerToMOV',
    'PuppeteerToAVI': 'PuppeteerToAVI',
    'PuppeteerToWMV': 'PuppeteerToWMV',
    'PuppeteerToFLV': 'PuppeteerToFLV',
    'PuppeteerToMKV': 'PuppeteerToMKV',
    'PuppeteerTo3GP': 'PuppeteerTo3GP',
    'PuppeteerToMP3': 'PuppeteerToMP3',
    'PuppeteerToWAV': 'PuppeteerToWAV',
    'PuppeteerToOGG': 'PuppeteerToOGG',
    'PuppeteerToAAC': 'PuppeteerToAAC',
    'PuppeteerToWMA': 'PuppeteerToWMA',
    'PuppeteerToFLAC': 'PuppeteerToFLAC',
    'PuppeteerToAIFF': 'PuppeteerToAIFF',
    'PuppeteerToM4A': 'PuppeteerToM4A',
    'PuppeteerToMPEG': 'PuppeteerToMPEG',
    'PuppeteerToMPG': 'PuppeteerToMPG',
    'PuppeteerToMPE': 'PuppeteerToMPE',
    'PuppeteerToMP2': 'PuppeteerToMP2',
    'PuppeteerToM3U': 'PuppeteerToM3U',
    'PuppeteerToM4V': 'PuppeteerToM4V',
    'PuppeteerToMP4V': 'PuppeteerToMP4V',
    'PuppeteerToM4P': 'PuppeteerToM4P',
    'PuppeteerToM4B': 'PuppeteerToM4B',
    'PuppeteerToM4R': 'PuppeteerToM4R',
    'PuppeteerToM4V': 'PuppeteerToM4V',
    'PuppeteerToF4V': 'PuppeteerToF4V',
    'PuppeteerToF4P': 'PuppeteerToF4P',
    'PuppeteerToF4A': 'PuppeteerToF4A',
    'PuppeteerToF4B': 'PuppeteerToF4B',
    'PuppeteerToM4U': 'PuppeteerToM4U',
    'PuppeteerToM4A': 'PuppeteerToM4A',
    'PuppeteerToM4R': 'PuppeteerToM4R',
    'PuppeteerToM4P': 'PuppeteerToM4P',
    'PuppeteerToM4B': 'PuppeteerToM4B',
    'PuppeteerToM4V': 'PuppeteerToM4V',
    'PuppeteerToF4V': 'PuppeteerToF4V',
    'PuppeteerToF4P': 'PuppeteerToF4P',
    'PuppeteerToF4A': 'PuppeteerToF4A',
    'PuppeteerToF4B': 'PuppeteerToF4B',
    'PuppeteerToM4U': 'PuppeteerToM4U',
}

def traduzir_termo(termo):
    """Traduz um termo do inglês para o português, se existir no dicionário."""
    return TRADUCOES.get(termo, termo)

def traduzir_nome_arquivo(nome_arquivo):
    """Traduz os termos no nome do arquivo."""
    # Extrai a extensão do arquivo
    nome_base, extensao = os.path.splitext(nome_arquivo)
    
    # Divide o nome do arquivo em partes usando '_' como separador
    partes = nome_base.split('_')
    
    # Traduz cada parte do nome do arquivo
    partes_traduzidas = [traduzir_termo(parte) for parte in partes]
    
    # Junta as partes traduzidas com '_' e adiciona a extensão
    return '_'.join(partes_traduzidas) + extensao

def renomear_arquivos_na_pasta(caminho_pasta, modo_simulado=True):
    """
    Renomeia arquivos na pasta especificada, traduzindo termos do inglês para o português.
    
    Args:
        caminho_pasta (str): Caminho para a pasta contendo os arquivos a serem renomeados.
        modo_simulado (bool): Se True, apenas mostra as alterações sem executá-las.
    """
    # Garante que o caminho da pasta existe
    if not os.path.isdir(caminho_pasta):
        print(f"Erro: O caminho '{caminho_pasta}' não é uma pasta válida.")
        return
    
    # Lista todos os arquivos na pasta
    try:
        arquivos = os.listdir(caminho_pasta)
    except Exception as e:
        print(f"Erro ao listar arquivos na pasta '{caminho_pasta}': {e}")
        return
    
    # Filtra apenas arquivos JSON
    arquivos_json = [f for f in arquivos if f.lower().endswith('.json')]
    
    if not arquivos_json:
        print(f"Nenhum arquivo JSON encontrado na pasta '{caminho_pasta}'.")
        return
    
    print(f"\n{'='*80}")
    print(f"INICIANDO RENOMEIAÇÃO DE ARQUIVOS{' (MODO SIMULADO)' if modo_simulado else ''}")
    print(f"Pasta: {caminho_pasta}")
    print(f"Total de arquivos JSON encontrados: {len(arquivos_json)}")
    print("-" * 80)
    
    # Contadores para relatório
    total_renomeados = 0
    total_ignorados = 0
    total_erros = 0
    
    # Dicionário para armazenar mapeamento de nomes antigos para novos
    mapeamento_renomeacao = {}
    
    # Primeira passada: verifica se há conflitos de nomes
    for nome_arquivo in arquivos_json:
        try:
            novo_nome = traduzir_nome_arquivo(nome_arquivo)
            
            # Verifica se o nome foi alterado
            if novo_nome != nome_arquivo:
                mapeamento_renomeacao[nome_arquivo] = novo_nome
        except Exception as e:
            print(f"Erro ao processar o arquivo '{nome_arquivo}': {e}")
            total_erros += 1
    
    # Verifica se há conflitos de nomes
    nomes_unicos = set()
    tem_conflitos = False
    
    for nome_antigo, novo_nome in mapeamento_renomeacao.items():
        if novo_nome in nomes_unicos:
            print(f"AVISO: Conflito de nomes detectado para '{novo_nome}'. O arquivo '{nome_antigo}' não será renomeado.")
            tem_conflitos = True
        nomes_unicos.add(novo_nome)
    
    if tem_conflitos:
        print("\nAVISO: Foram detectados conflitos de nomes. Alguns arquivos não serão renomeados.")
        print("Por favor, resolva os conflitos manualmente e execute o script novamente.")
        return
    
    # Segunda passada: renomeia os arquivos
    for nome_antigo, novo_nome in mapeamento_renomeacao.items():
        try:
            caminho_antigo = os.path.join(caminho_pasta, nome_antigo)
            caminho_novo = os.path.join(caminho_pasta, novo_nome)
            
            # Verifica se o arquivo de destino já existe
            if os.path.exists(caminho_novo):
                print(f"AVISO: O arquivo de destino já existe. Pulando: {nome_antigo} -> {novo_nome}")
                total_ignorados += 1
                continue
            
            if modo_simulado:
                print(f"[SIMULAÇÃO] {nome_antigo} -> {novo_nome}")
            else:
                os.rename(caminho_antigo, caminho_novo)
                print(f"[RENOMEADO] {nome_antigo} -> {novo_nome}")
            
            total_renomeados += 1
            
        except Exception as e:
            print(f"Erro ao renomear o arquivo '{nome_antigo}': {e}")
            total_erros += 1
    
    # Gera relatório
    print("\n" + "="*80)
    print("RELATÓRIO DE RENOMEAÇÃO")
    print("-" * 80)
    print(f"Total de arquivos processados: {len(arquivos_json)}")
    print(f"Arquivos renomeados: {total_renomeados}")
    print(f"Arquivos ignorados: {total_ignorados}")
    print(f"Erros: {total_erros}")
    
    if modo_simulado and total_renomeados > 0:
        print("\nNOTA: Nenhum arquivo foi alterado (modo simulado).")
        print("Para aplicar as alterações, execute o script com o parâmetro '--aplicar'.")
    
    print("="*80 + "\n")

if __name__ == "__main__":
    import sys
    
    # Verifica se o caminho da pasta foi fornecido como argumento
    if len(sys.argv) < 2:
        print("Uso: python renomear_workflows.py <caminho_da_pasta> [--aplicar]")
        print("\nExemplos:")
        print("  python renomear_workflows.py ./workflows              # Modo simulado (padrão)")
        print("  python renomear_workflows.py ./workflows --aplicar   # Aplica as alterações")
        sys.exit(1)
    
    caminho_pasta = sys.argv[1]
    modo_simulado = '--aplicar' not in sys.argv[2:]
    
    # Executa a função principal
    renomear_arquivos_na_pasta(caminho_pasta, modo_simulado)
