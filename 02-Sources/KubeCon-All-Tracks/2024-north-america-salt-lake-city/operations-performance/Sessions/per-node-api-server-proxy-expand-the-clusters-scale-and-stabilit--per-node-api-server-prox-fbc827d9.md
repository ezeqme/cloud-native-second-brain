---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Weizhou Lan", "Iceber Gu", "DaoCloud"]
sched_url: https://kccncna2024.sched.com/event/1i7ox/per-node-api-server-proxy-expand-the-clusters-scale-and-stability-weizhou-lan-iceber-gu-daocloud
youtube_search_url: https://www.youtube.com/results?search_query=Per-Node+Api-Server+Proxy%3A+Expand+the+Cluster%27s+Scale+and+Stability+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Per-Node Api-Server Proxy: Expand the Cluster's Scale and Stability - Weizhou Lan & Iceber Gu, DaoCloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Weizhou Lan, Iceber Gu, DaoCloud
- Schedule: https://kccncna2024.sched.com/event/1i7ox/per-node-api-server-proxy-expand-the-clusters-scale-and-stability-weizhou-lan-iceber-gu-daocloud
- Busca YouTube: https://www.youtube.com/results?search_query=Per-Node+Api-Server+Proxy%3A+Expand+the+Cluster%27s+Scale+and+Stability+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Per-Node Api-Server Proxy: Expand the Cluster's Scale and Stability.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ox/per-node-api-server-proxy-expand-the-clusters-scale-and-stability-weizhou-lan-iceber-gu-daocloud
- YouTube search: https://www.youtube.com/results?search_query=Per-Node+Api-Server+Proxy%3A+Expand+the+Cluster%27s+Scale+and+Stability+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=O7w7e2iA7lA
- YouTube title: Per-Node Api-Server Proxy: Expand the Cluster's Scale and Stability - Weizhou Lan & Iceber Gu
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/per-node-api-server-proxy-expand-the-clusters-scale-and-stability/O7w7e2iA7lA.txt
- Transcript chars: 15531
- Keywords: server, resources, controllers, request, redirection, balancing, requests, resolution, cluster, solution, global, control, inform, resource, scenarios, forwarding, stability, session

### Resumo baseado na transcript

hi everyone uh let's get started uh I'm here to present an interesting uh session uh pronote API server proxy expand the Clusters uh scale and stability uh I'm we l and uh my co-speaker isber is we are from Dark Cloud uh Shanghai in China and iceberg is responsible for the API server uh proxy while I worked on the network part we worked together to uh complete an interesting uh future shared in this session uh unfortunately uh iberg can cannot be uh attend in person uh because

### Excerpt da transcript

hi everyone uh let's get started uh I'm here to present an interesting uh session uh pronote API server proxy expand the Clusters uh scale and stability uh I'm we l and uh my co-speaker isber is we are from Dark Cloud uh Shanghai in China and iceberg is responsible for the API server uh proxy while I worked on the network part we worked together to uh complete an interesting uh future shared in this session uh unfortunately uh iberg can cannot be uh attend in person uh because only to the Visa issue so for the first half of this session uh it will be explained through his uh pre uh pre-recorded uh audence and at the second half I will personally uh expand the part that I'm responsible for okay uh first of all um let me briefly explain the content of this uh session our goal is to uh expand the Clusters uh skill and stability uh as we know as the cluster uh scals up we may encounter we may encounter uh various problems and uh this session just focuses on uh optimization of the API server uh then I will introduce uh a solution to R uh reduce the St of API server by a proxy uh which can be deployed in uh Global or Regional nodes uh to prox uh access to AP server finally I will explain how to uh proxy API server requests transparently okay let's uh listen to what isber want to say think about it when you are not using control to control or view the cluster can your APS Ser rest no who is constantly requesting your APS server is the controllers and to describe what follows more simply we'll start by referring to all inform based on common as controllers this D the entire communties and declarative declara resources for example your schedu control manager c pro and so on yes the custom controllers that are constantly being added as your business needs grow compes uses open API to organize resources and give you the freedom to operate class resources inform based on the list and what requests always you to implement a controller that listen and reconcile resources these three usually designs give developers the freedom to implement the future they want but this has also led to fragmentation of thees ecosystem where a wide variety of Futures in ques clust are implemented as controllers count the number of the project and the land scope and take a look at your cast there are no less than 10 components that use inform and these components are not controllable by old people or commities sometimes we have to deploy them on each know as required to fulfill the requirem
