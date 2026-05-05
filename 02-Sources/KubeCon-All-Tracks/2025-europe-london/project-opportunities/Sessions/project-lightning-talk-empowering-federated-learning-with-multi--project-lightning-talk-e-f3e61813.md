---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["Kubernetes Core"]
speakers: ["Meng Yan", "Software Engineer"]
sched_url: https://kccnceu2025.sched.com/event/1tcvi/project-lightning-talk-empowering-federated-learning-with-multi-cluster-management-for-privacy-and-efficiency-meng-yan-software-engineer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Federated+Learning+with+Multi-Cluster+Management+for+Privacy+and+Efficiency+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Empowering Federated Learning with Multi-Cluster Management for Privacy and Efficiency - Meng Yan, Software Engineer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Meng Yan, Software Engineer
- Schedule: https://kccnceu2025.sched.com/event/1tcvi/project-lightning-talk-empowering-federated-learning-with-multi-cluster-management-for-privacy-and-efficiency-meng-yan-software-engineer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Federated+Learning+with+Multi-Cluster+Management+for+Privacy+and+Efficiency+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Empowering Federated Learning with Multi-Cluster Management for Privacy and Efficiency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvi/project-lightning-talk-empowering-federated-learning-with-multi-cluster-management-for-privacy-and-efficiency-meng-yan-software-engineer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Empowering+Federated+Learning+with+Multi-Cluster+Management+for+Privacy+and+Efficiency+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=j7QfkNU8XM8
- YouTube title: Project Lightning Talk: Empowering Federated Learning with Multi-Cluster Management for... Meng Yan
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-empowering-federated-learning-with-multi-cluste/j7QfkNU8XM8.txt
- Transcript chars: 3189
- Keywords: cluster, learning, federated, privacy, server, training, multicluster, updates, aggregator, management, clusters, global, managed, status, private, manage, locally, question

### Resumo baseado na transcript

Imagine you have public and private clusters each with sensitive debt and now you want to train a language model using all of it without exposing that debt. Well, to manage those clusters, we rely on open cluster management or OCM. And in federated learning those collaborators pull the global model from the aggregator and train nolay push those model updates back to the aggregator. So naturally the hub cluster acts like the aggregator or server in federated learning and each managed cluster applies the role of uh collaborator or clint. It manages the whole model training life cycle across multicluster and also use CRD to define the workflow support different uh popular federated learning runtimes like uh open FL and more. training and once all the clients and the server is ready the stures come into running while the federated learning workflow kicks off the lends the P model from the server train locally on their private data and push those updates back to the server

### Excerpt da transcript

Uh my name is Yam and I'm a software engineer at Red Hat. Today I will share a user case that involving three topics. The first one is multicluster AI model training and data privacy. Imagine you have public and private clusters each with sensitive debt and now you want to train a language model using all of it without exposing that debt. Well, to manage those clusters, we rely on open cluster management or OCM. And for that privacy, we use federated learning. It let each cluster train locally and just send the model updates not the real data which get combined into a global model. So, privacy is built from start. And the next question is how do we combine those two system together? Before start here is a quick overview of OCM. It's a Kubernetes multicluster orchestration and it's also a CCF sandbox project based on hub spoke architecture. Uh the central control plan lambda hub cluster which those manage cluster it also provide some open APIs like manifest work open uh placement to schedule your workload across those clusters.

So and well then the next question is why did we pick OCM for federated learning? The answer is straightforward that is OCM natively supports federated learning. In OCM uh those managed cluster pull their deserved status from the hub cluster and push those status back to the hub cluster. And in federated learning those collaborators pull the global model from the aggregator and train nolay push those model updates back to the aggregator. So naturally the hub cluster acts like the aggregator or server in federated learning and each managed cluster applies the role of uh collaborator or clint. To make those integration seamless, we in uh we we built a controller. It manages the whole model training life cycle across multicluster and also use CRD to define the workflow support different uh popular federated learning runtimes like uh open FL and more. So if you are already using one of those frameworks, you can just plug it in and you don't need to rewrite your training code. Here's how you get started.

First, you need to containerize your application and then uh create a customer resource reference that image. Initially the resource status show as waiting that means the hub that means the server is set on the hub and the system now scheduling those aggregator or client to those managed cluster claim to have the data uh have the data needed for mode training and once all the clients and the server is ready the stures come into running
