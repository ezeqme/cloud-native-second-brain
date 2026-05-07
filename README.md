# Cloud Native Second Brain

Base de conhecimento em formato Obsidian para estudar, pesquisar e conectar conteúdos do ecossistema cloud native.

O repositório começou focado em observabilidade, mas agora cobre trilhas completas de Cloud Native/KubeCon, PromCon e eventos relacionados da CNCF: Kubernetes, plataforma, segurança, networking, service mesh, runtime, storage, performance, operações, observabilidade, AI/ML e outros temas do ecossistema.

## Objetivo

Transformar agendas, vídeos, metadados e transcrições públicas de conferências cloud native em um vault navegável para:

- estudar tendências técnicas do ecossistema CNCF;
- encontrar talks por evento, trilha, projeto ou tema;
- construir mapas de conhecimento reutilizáveis;
- apoiar pesquisa, escrita, talks, treinamentos e decisões técnicas;
- acompanhar a evolução histórica de temas cloud native.

## Conteúdo atual

- KubeCon + CloudNativeCon com múltiplas trilhas e edições históricas.
- Observability Day e trilhas históricas de observabilidade.
- PromCon e conteúdos relacionados a Prometheus.
- Metadados, links, manifests e automações para enriquecimento via YouTube/CNCF.
- Estrutura compatível com Obsidian, usando links wiki (`[[...]]`) e mapas de conteúdo.

Resumo aproximado do vault no momento:

- `02-Sources/KubeCon-All-Tracks/`: 4.865 notas de sessões.
- `02-Sources/KubeCon/`: 220 notas focadas em KubeCon/observabilidade e eventos colocalizados.
- `02-Sources/PromCon/`: 215 notas de PromCon.
- Total: mais de 5.400 arquivos Markdown.

## Estrutura

```text
00-Inbox/                  Capturas rápidas e notas ainda não processadas
01-Maps/                   MOCs / mapas de conteúdo por tema, evento ou trilha
02-Sources/                Fontes primárias organizadas por evento e sessão
03-Topics/                 Notas permanentes por tema cloud native
04-Projects/               Trilhas de pesquisa, outputs futuros e trabalhos derivados
05-Templates/              Templates Obsidian
_sources/                  Dados brutos, manifests e arquivos de reprocessamento
scripts/                   Automação de coleta, indexação e enriquecimento
```

## Mapas principais

- `01-Maps/KubeCon All Tracks.md`
- `01-Maps/Observability.md`
- `01-Maps/KubeCon Historical Observability.md`
- `01-Maps/PromCon.md`
- `01-Maps/KubeCon-Themes/`
- `01-Maps/PromCon-Themes/`

## Como usar

### No Obsidian

Este repositório já está organizado como um vault Obsidian. Para abrir:

1. Clone o repositório:

   ```bash
   git clone <repo-url>
   cd cloud-native-second-brain
   ```

2. Abra o Obsidian.
3. Clique em **Open folder as vault** / **Abrir pasta como cofre**.
4. Selecione a pasta `cloud-native-second-brain` clonada.
5. Quando o vault abrir, comece pelos mapas em `01-Maps/`:
   - `01-Maps/KubeCon All Tracks.md`
   - `01-Maps/Observability.md`
   - `01-Maps/PromCon.md`
6. Navegue pelas sessões em `02-Sources/`.
7. Promova aprendizados relevantes para `03-Topics/`.

Dicas:

- Use o **Graph View** do Obsidian para visualizar conexões entre eventos, trilhas e temas.
- Use a busca global do Obsidian para encontrar projetos, tecnologias e speakers.
- Os links internos usam o formato wiki `[[Nome da nota]]`, compatível com Obsidian.
- A pasta `_sources/` contém dados brutos/manifests e pode ser ignorada na leitura diária.

### Via terminal

```bash
git clone <repo-url>
cd cloud-native-second-brain
```

Use busca textual, `ripgrep`, scripts próprios ou ferramentas de IA/local RAG sobre os arquivos Markdown.

Exemplos:

```bash
rg "OpenTelemetry" 02-Sources/
rg "platform engineering" 01-Maps/ 02-Sources/
```

### Site público com GitHub Pages

Este repositório inclui uma primeira configuração para publicar o vault como site estático com Quartz e GitHub Pages.

- A publicação acontece pelo workflow `.github/workflows/deploy-pages.yml` em pushes para `main`.
- O workflow baixa o Quartz v4, copia apenas arquivos Markdown do vault para o build e exclui `_sources/`, `bin/`, `scripts/`, `.git`, `.github`, `05-Templates/` e saídas locais.
- A configuração fica em `.github/quartz/`, com Graph View habilitado e parâmetros mais conservadores para um vault grande.
- No GitHub, habilite **Settings > Pages > Source > GitHub Actions** antes do primeiro deploy.

Build local:

```bash
npm run site:build
```

Preview local:

```bash
npm run site:serve
```

Esses comandos exigem Node.js 22+, npm 10.9.2+ e acesso ao GitHub/npm para baixar o Quartz e suas dependências na primeira execução. A saída local fica em `.quartz/public/` e não deve ser commitada.

## Automação

Os scripts em `scripts/` ajudam a coletar, indexar e enriquecer dados de eventos e vídeos.

Principais scripts:

- `scripts/index_kubecon_all_tracks.py` — indexa múltiplas trilhas da KubeCon.
- `scripts/index_historical_observability.py` — indexa histórico de observabilidade.
- `scripts/index_observability_day_2026.py` — indexa Observability Day Europe 2026.
- `scripts/index_promcon.py` — indexa PromCon.
- `scripts/sync_cncf_playlists.py` — sincroniza playlists públicas da CNCF.
- `scripts/enrich_from_youtube.py` — enriquece notas com dados/transcrições do YouTube quando disponíveis.

> Os scripts podem depender de ferramentas externas, dados públicos e disponibilidade das fontes originais. Rode com cuidado e revise os diffs antes de publicar alterações grandes.

## Fontes

Este vault usa principalmente fontes públicas como:

- agendas da Linux Foundation / Sched;
- canal da CNCF no YouTube;
- playlists e páginas públicas de eventos;
- metadados e transcrições disponíveis publicamente.

## Aviso sobre conteúdo de terceiros

Este repositório organiza metadados, links, resumos e material de estudo baseado em conteúdo público de terceiros.

Vídeos, slides, transcrições, nomes de eventos, marcas e demais materiais originais continuam pertencendo aos seus respectivos autores, palestrantes, organizações ou plataformas. Antes de redistribuir transcrições completas, gerar material comercial ou republicar conteúdo derivado, verifique os direitos e licenças aplicáveis das fontes originais.

## Contribuição

Contribuições são bem-vindas, especialmente para:

- corrigir metadados de sessões;
- melhorar mapas de conteúdo;
- adicionar links para vídeos/slides oficiais;
- organizar temas cloud native;
- melhorar scripts de indexação;
- reduzir duplicações e inconsistências de nomenclatura.

Sugestão de fluxo:

1. Abra uma issue descrevendo o problema ou melhoria.
2. Envie um pull request com alterações pequenas e revisáveis.
3. Evite adicionar conteúdo protegido por direitos autorais sem permissão clara.

## Licença

Este repositório usa um modelo de licença dual:

- **Código, scripts e automações:** MIT License.
- **Notas originais, mapas, documentação e estrutura do vault:** Creative Commons Attribution 4.0 International (CC BY 4.0).

Veja [`LICENSE`](LICENSE).

Conteúdos de terceiros referenciados, resumidos, transcritos ou linkados não são relicenciados por este projeto. Eles permanecem sujeitos às licenças e termos de seus respectivos donos e plataformas de origem.

Para orientações de atribuição, veja [`NOTICE.md`](NOTICE.md).
