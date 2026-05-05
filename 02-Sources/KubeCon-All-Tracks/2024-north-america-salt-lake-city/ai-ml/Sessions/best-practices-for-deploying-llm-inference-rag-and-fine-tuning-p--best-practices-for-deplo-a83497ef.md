---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Meenakshi Kaushik", "Shiva Krishna Merla", "NVIDIA"]
sched_url: https://kccncna2024.sched.com/event/1i7rc/best-practices-for-deploying-llm-inference-rag-and-fine-tuning-pipelines-on-k8s-meenakshi-kaushik-shiva-krishna-merla-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Best+Practices+for+Deploying+LLM+Inference%2C+RAG+and+Fine+Tuning+Pipelines+on+K8s+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Best Practices for Deploying LLM Inference, RAG and Fine Tuning Pipelines on K8s - Meenakshi Kaushik & Shiva Krishna Merla, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Meenakshi Kaushik, Shiva Krishna Merla, NVIDIA
- Schedule: https://kccncna2024.sched.com/event/1i7rc/best-practices-for-deploying-llm-inference-rag-and-fine-tuning-pipelines-on-k8s-meenakshi-kaushik-shiva-krishna-merla-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Best+Practices+for+Deploying+LLM+Inference%2C+RAG+and+Fine+Tuning+Pipelines+on+K8s+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Best Practices for Deploying LLM Inference, RAG and Fine Tuning Pipelines on K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rc/best-practices-for-deploying-llm-inference-rag-and-fine-tuning-pipelines-on-k8s-meenakshi-kaushik-shiva-krishna-merla-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Best+Practices+for+Deploying+LLM+Inference%2C+RAG+and+Fine+Tuning+Pipelines+on+K8s+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EmGe_58524g
- YouTube title: Best Practices for Deploying LLM Inference, RAG and Fine Tuning Pipelines... M. Kaushik, S.K. Merla
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/best-practices-for-deploying-llm-inference-rag-and-fine-tuning-pipelin/EmGe_58524g.txt
- Transcript chars: 29373
- Keywords: inference, gpu, models, across, server, adapters, pipeline, cluster, single, nvidia, operator, running, serving, adapter, inferencing, foundation, storage, observability

### Resumo baseado na transcript

hello everyone welcome to the session and uh thank you for making it to almost the last session of the conference my name is minaki Kosik and I want to introduce my co-speaker Shiva Krishna Mara we both work at Nvidia and are responsible for helping customers deploy and life cycle manage Nvidia inference microservice in short known as Nims on kubernetes and uh we see customers using variety of deployments from Helm charts to casers to our open source Nim operator today we are going to share some of

### Excerpt da transcript

hello everyone welcome to the session and uh thank you for making it to almost the last session of the conference my name is minaki Kosik and I want to introduce my co-speaker Shiva Krishna Mara we both work at Nvidia and are responsible for helping customers deploy and life cycle manage Nvidia inference microservice in short known as Nims on kubernetes and uh we see customers using variety of deployments from Helm charts to casers to our open source Nim operator today we are going to share some of the learnings in helping our customers and uh the agenda for today's uh uh session is as follows we're going to start with overview and then look at components of inference and fine tuning they're are different from a typical microservice and then look at some of the emerging Technologies such as AI agents and finally conclusion so generative AI is giving rise to Sovereign clouds because customer customer wants data sovereignity security and privacy and uh most of the Enterprise really want to customize because they want to provide uh business specific answers as seen from this chatbot so let's take a look at these pipelines so a simplistic inference pipeline is you would have a large language model front ended with a guard rail uh for a rack pipeline you would uh have an uh you you would have an Enterprise data and you would use an embedding model to index your data using a vector database and then in response to the customer query um you would use a llm framework such as a l chain and use an embedding model to retrieve the relevant chunks and then finally rerank it combine it with a query and provide the response finally uh for fine-tuning models you would run a fine-tuning job and then evaluate and if it is good enough use your uh uh L of adapters generate lot of adapters and fine tune and start serving so when we take a look at these pipelines there are inference servers such as embedding reranking and large language models and then there are fine-tuning jobs which is in uh blue and dependencies which are really well-known Services microservices which we know about which is Vector databases or uh even guard rails and evaluator so we are going to focus more on inference servers and fine tuning jobs in this presentation so when we took take a look at current landscape there is awesome work which is going on in open source Community it uh there are uh there are inference server server platforms as well as training platforms such as kerve CU flow and also our op
