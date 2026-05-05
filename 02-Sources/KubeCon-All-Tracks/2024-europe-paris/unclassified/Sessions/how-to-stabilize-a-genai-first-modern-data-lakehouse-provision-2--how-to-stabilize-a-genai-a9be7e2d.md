---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML", "Storage Data"]
speakers: ["Shirley Yang", "LinkedIn"]
sched_url: https://kccnceu2024.sched.com/event/1YeQe/how-to-stabilize-a-genai-first-modern-data-lakehouse-provision-20000-ephemeral-data-lakesyear-shirley-yang-linkedin
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Stabilize+a+GenAI-First%2C+Modern+Data+LakeHouse%3A+Provision+20%2C000+Ephemeral+Data+Lakes%2FYear+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How to Stabilize a GenAI-First, Modern Data LakeHouse: Provision 20,000 Ephemeral Data Lakes/Year - Shirley Yang, LinkedIn

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: France / Paris
- Speakers: Shirley Yang, LinkedIn
- Schedule: https://kccnceu2024.sched.com/event/1YeQe/how-to-stabilize-a-genai-first-modern-data-lakehouse-provision-20000-ephemeral-data-lakesyear-shirley-yang-linkedin
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Stabilize+a+GenAI-First%2C+Modern+Data+LakeHouse%3A+Provision+20%2C000+Ephemeral+Data+Lakes%2FYear+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How to Stabilize a GenAI-First, Modern Data LakeHouse: Provision 20,000 Ephemeral Data Lakes/Year.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeQe/how-to-stabilize-a-genai-first-modern-data-lakehouse-provision-20000-ephemeral-data-lakesyear-shirley-yang-linkedin
- YouTube search: https://www.youtube.com/results?search_query=How+to+Stabilize+a+GenAI-First%2C+Modern+Data+LakeHouse%3A+Provision+20%2C000+Ephemeral+Data+Lakes%2FYear+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=L02zdTo7HT0
- YouTube title: How to Stabilize a GenAI-First, Modern Data LakeHouse: Provision 20,000 Ephemeral Data Lakes/Year
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-to-stabilize-a-genai-first-modern-data-lakehouse-provision-20-000/L02zdTo7HT0.txt
- Transcript chars: 28187
- Keywords: actually, basically, linkedin, cluster, production, clusters, everything, engineers, matrix, release, change, couple, product, wanted, little, offline, engineer, deploy

### Resumo baseado na transcript

let's get started so thank you everyone for attending my talk today my name is Shirley yam and I'm an engineering manager in LinkedIn today we're going to talk about how LinkedIn stabilized and ji First Data lak house by provision 20,000 ephemeral clusters every year so a little bit about myself uh I've been LinkedIn for seven years currently I'm working in linkedin's Big Data platform team so there are two areas I'm responsible for one is the foundations team uh which is handles all horizontal stuff within the

### Excerpt da transcript

okay cool uh it's 11: a.m. let's get started so thank you everyone for attending my talk today my name is Shirley yam and I'm an engineering manager in LinkedIn today we're going to talk about how LinkedIn stabilized and ji First Data lak house by provision 20,000 ephemeral clusters every year so a little bit about myself uh I've been LinkedIn for seven years currently I'm working in linkedin's Big Data platform team so there are two areas I'm responsible for one is the foundations team uh which is handles all horizontal stuff within the offline stat including developer productivity that is how we build this product uh security um cost efficiency as well as some of resilience stuff the other area is the um LinkedIn airflow team where we are working on all the data processing jobs and also some of the workflow orchestration within LinkedIn okay so agendas today we we started by talking about our Pro U problem statements and we will share our approach on solving this problem as well as the results we'll also share some of the learnings and continuous development we'll summarize our talk lastly and also we'll touch a little bit on our next steps when I talked about uh 20K Emeral clusters I want to First share about the LinkedIn offline stack and our uh what the Clusters our ephemeral clusters are simulating so currently LinkedIn has about 10 plus Hado clusters which can be transfered to more than 35k total notes and 400 four plus extra bu storage so we run 500k jobs per day and this can be transferred to around 100 million containers allocations every day now the whole offline stack we have a 100 Engineers working on that which includes both STS and sres and and we are maintaining uh 30 plus core Services we'll keep growing on that our users are definitely the whole LinkedIn uh including AI Engineers data scientists analysts and everyone who actually request access for the offline stack so what are the challenges if we're running at such a large scale so I want to share two examples here these are two slack messages I um took a screenshot so the first one is actually a machine learning Arrow from emoji you can see our AI Engineers are pretty frustrated because the 11 hours drob failed again and the reason was because the um they trying to release the checkpoint and fail due to an hdfs connection arrow and uh the second one is actually um kind of a common issues within uh LinkedIn because we our services are interdependent among each other and in this specific
