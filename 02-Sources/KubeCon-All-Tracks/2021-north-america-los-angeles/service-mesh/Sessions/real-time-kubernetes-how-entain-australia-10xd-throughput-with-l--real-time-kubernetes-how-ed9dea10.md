---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Service Mesh"
themes: ["AI ML", "Networking", "Kubernetes Core"]
speakers: ["Steve Gray", "Entain Australia"]
sched_url: https://kccncna2021.sched.com/event/lV5j/real-time-kubernetes-how-entain-australia-10xd-throughput-with-linkerd-steve-gray-entain-australia
youtube_search_url: https://www.youtube.com/results?search_query=Real-time+Kubernetes%3A+How+Entain+Australia+10x%27d+throughput+with+Linkerd+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Real-time Kubernetes: How Entain Australia 10x'd throughput with Linkerd - Steve Gray, Entain Australia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Steve Gray, Entain Australia
- Schedule: https://kccncna2021.sched.com/event/lV5j/real-time-kubernetes-how-entain-australia-10xd-throughput-with-linkerd-steve-gray-entain-australia
- Busca YouTube: https://www.youtube.com/results?search_query=Real-time+Kubernetes%3A+How+Entain+Australia+10x%27d+throughput+with+Linkerd+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Real-time Kubernetes: How Entain Australia 10x'd throughput with Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV5j/real-time-kubernetes-how-entain-australia-10xd-throughput-with-linkerd-steve-gray-entain-australia
- YouTube search: https://www.youtube.com/results?search_query=Real-time+Kubernetes%3A+How+Entain+Australia+10x%27d+throughput+with+Linkerd+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PKhQXjb6cB4
- YouTube title: Real-time Kubernetes: How Entain Australia 10x'd throughput with Linkerd - Steve Gray
- Match score: 1.007
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/real-time-kubernetes-how-entain-australia-10xd-throughput-with-linkerd/PKhQXjb6cB4.txt
- Transcript chars: 16536
- Keywords: platform, started, across, mesh, linker, journey, connections, within, australia, deployments, individual, balancing, operate, trading, business, network, servers, became

### Resumo baseado na transcript

hello my name is stephen gray and i'm here today to talk about real-time kubernetes and how enta and australia achieved 10 times the throughput with linker d entane is a ftse 100 company and one of the world's largest sports betting and gaming groups operating in the online and retail sectors we operate all across the world with brands and teams in dozens of countries globally and australia is one of them as the head of trading solutions here in australia i lead the team of engineers that build

### Excerpt da transcript

hello my name is stephen gray and i'm here today to talk about real-time kubernetes and how enta and australia achieved 10 times the throughput with linker d entane is a ftse 100 company and one of the world's largest sports betting and gaming groups operating in the online and retail sectors we operate all across the world with brands and teams in dozens of countries globally and australia is one of them as the head of trading solutions here in australia i lead the team of engineers that build and operate our trading platform pairing our regional business we've transitioned over the last few years from a non-agile release cycle to a lean agile management practice with ownership and self-support of our solutions we use chaos engineering automated tests continuous deployments and even spot nodes to optimize our cost base our team is responsible for managing the torrent of data coming into the business reacting to it in real time various data providers from all over the world feed us information continuously as sports and races happen all across the world these come into our trading platform that we've built here in australia our trading team interact with that platform as their main line of business tool this then feeds into our transactional platform and our customers interact with that platform so specifically what we do is this piece here in the middle our software stack is based on very contemporary tools so we use go as our main programming language for messaging and distribution of data we use apache kafka um mongodb is our main dollar store but we do use other technologies such as python r rabbitmq and even net core entire platform is based on cloud native technologies we host on kubernetes we are using linker d as our service mesh all of our network communications use grpc and we use tracing instrumentation using the jaeger and open tracing projects and we do our deployments with hell in terms of key metrics about our team as well we operate five clusters there are 250 plus cloud servers in that environment there are zero relational databases we have hundreds of deployments of our software managed by a team of 13 engineers of which only one of them is a dedicated devops engineer it wasn't always this way our microservices journey started off just with a single application it powered the entire business all of our customer facing applications but also the entire back of house trading operation it was so large and unassailable we called it the monolit
