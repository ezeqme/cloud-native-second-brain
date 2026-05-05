---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Service Mesh"
themes: ["Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sumit Mathur", "Sushanth Kamath A", "Intuit"]
sched_url: https://kccnceu2024.sched.com/event/1YeSt/scaling-service-mesh-self-service-beyond-300-clusters-sumit-mathur-sushanth-kamath-a-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+Service+Mesh%3A+Self+Service+Beyond+300+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Scaling Service Mesh: Self Service Beyond 300 Clusters - Sumit Mathur & Sushanth Kamath A, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Sumit Mathur, Sushanth Kamath A, Intuit
- Schedule: https://kccnceu2024.sched.com/event/1YeSt/scaling-service-mesh-self-service-beyond-300-clusters-sumit-mathur-sushanth-kamath-a-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+Service+Mesh%3A+Self+Service+Beyond+300+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Scaling Service Mesh: Self Service Beyond 300 Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSt/scaling-service-mesh-self-service-beyond-300-clusters-sumit-mathur-sushanth-kamath-a-intuit
- YouTube search: https://www.youtube.com/results?search_query=Scaling+Service+Mesh%3A+Self+Service+Beyond+300+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Iz9_FDEKF5M
- YouTube title: Scaling Service Mesh: Self Service Beyond 300 Clusters - Sumit Mathur & Sushanth Kamath A, Intuit
- Match score: 0.816
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/scaling-service-mesh-self-service-beyond-300-clusters/Iz9_FDEKF5M.txt
- Transcript chars: 29799
- Keywords: traffic, gateway, mesh, clusters, client, limiting, config, dialing, custom, cluster, configure, change, clients, request, across, object, hosted, changes

### Resumo baseado na transcript

uh thanks everyone for joining the session today uh after a break uh hope you had a nice break so uh we are going to start the session now uh let me introduce myself uh I am Sumit matur uh engineering manager in intute of traffic team and with me uh I have shushant he is a traffic lead in in and our topic uh is scaling service MH uh selfservice Beyond 300 clusters so uh we are going to uh talk about what is scaling means here what is

### Excerpt da transcript

uh thanks everyone for joining the session today uh after a break uh hope you had a nice break so uh we are going to start the session now uh let me introduce myself uh I am Sumit matur uh engineering manager in intute of traffic team and with me uh I have shushant he is a traffic lead in in and our topic uh is scaling service MH uh selfservice Beyond 300 clusters so uh we are going to uh talk about what is scaling means here what is self service means here what is that uh 300 cluster so we are going to break down all of this uh in next 30 minutes uh let's get a started what is intute is and what we have done so intute is a fintech company uh based out of us and it has uh accounting and tax products uh and we believe in open source and some of our uh open source contri itions are like Argo Admiral and at the end we are end user customers also like kubernetes sto Prometheus uh this is the scale at uh which we operate uh like more than 300 plus kubernetes clusters 16,000 plus name spaces more than 2,000 microservices so it's like a factory of microservices that we have and then more than thousands of teams with 10,000 developers who are using our platforms and uh we are on the Journey of uh modern s platform and building the lot of abstraction uh so that we ease the life of the developers uh from the traffic team uh this is our contribution to the sto Community the Admiral uh you can check uh more about Admiral on the gab link but at a high level uh Admiral allows us for the cross-cluster communication and the service Discovery in service mesh world uh let's uh before we go uh Deep dive in like what's the today's topic and everything I just want to make sure like uh we all understand uh some of the basic terms of traffic so may I know uh how many of you know API Gateway good uh do you know uh what sto is nice do you know what service meshes thanks so I see a good amount of audience who knows these terminologies and there are few who don't know so let's uh start with that understanding those basic terminologies of traffic and uh so this is our agenda where we are going to cover what is API Gateway what is service mesh what are the common functionalities like rate limiting traffic dialing what's problem uh statement why we are here why you are here and then the solutioning part of it and what's there in the road map for us so uh let's look at uh what API Gateway is so uh consider uh a developer who is developing the API is writing the business Logic for your c
