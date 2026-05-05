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
themes: ["AI ML", "Security", "Networking", "Kubernetes Core"]
speakers: ["Matheus Morais", "Sicredi"]
sched_url: https://kccnceu2024.sched.com/event/1YeRT/cilium-clustermesh-in-action-strengthening-security-across-distributed-kubernetes-clusters-matheus-morais-sicredi
youtube_search_url: https://www.youtube.com/results?search_query=Cilium+ClusterMesh+in+Action%3A+Strengthening+Security+Across+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cilium ClusterMesh in Action: Strengthening Security Across Distributed Kubernetes Clusters - Matheus Morais, Sicredi

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Service Mesh]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Matheus Morais, Sicredi
- Schedule: https://kccnceu2024.sched.com/event/1YeRT/cilium-clustermesh-in-action-strengthening-security-across-distributed-kubernetes-clusters-matheus-morais-sicredi
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium+ClusterMesh+in+Action%3A+Strengthening+Security+Across+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cilium ClusterMesh in Action: Strengthening Security Across Distributed Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRT/cilium-clustermesh-in-action-strengthening-security-across-distributed-kubernetes-clusters-matheus-morais-sicredi
- YouTube search: https://www.youtube.com/results?search_query=Cilium+ClusterMesh+in+Action%3A+Strengthening+Security+Across+Distributed+Kubernetes+Clusters+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=MSqI-gBiCrc
- YouTube title: Cilium ClusterMesh in Action: Strengthening Security Across Distributed Kubernetes Clusters
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cilium-clustermesh-in-action-strengthening-security-across-distributed/MSqI-gBiCrc.txt
- Transcript chars: 28239
- Keywords: cluster, clusters, mesh, connect, infrastructure, important, access, console, enable, amazon, working, premise, network, basically, course, traffic, running, control

### Resumo baseado na transcript

well let's get started uh first of all uh thank you very much for being here I wasn't expecting so full crow like that so I hope you can enjoy some of the the informations that I have to to present here uh my name is Matos I'm from Brazil uh on a company called CI which is a credit union [Music] uh just a few words about CI uh CI is the first Brazil Credit Union founded in 192 so um it's a pretty old company uh it's one

### Excerpt da transcript

well let's get started uh first of all uh thank you very much for being here I wasn't expecting so full crow like that so I hope you can enjoy some of the the informations that I have to to present here uh my name is Matos I'm from Brazil uh on a company called CI which is a credit union [Music] uh just a few words about CI uh CI is the first Brazil Credit Union founded in 192 so um it's a pretty old company uh it's one of the largest credit Brazil Credit Union with more than 7.5 million members when we call Members this is a term to the credit union it really means clients so we have more than 40,000 employees and it's present on every Brazilian State um it's important to mention that all we all our critical workloads or great part of it run inside kubernetes infrastructure so uh things like instant payment and ATM operations all that rely on on applications that run inside kubernetes so just a few words about me I'm a platform specialist at secr working for the container regestration team I'm in the company for almost uh 18 years now I'm a free soft Enthusiast I was always involved with free soft after open source projects I was involved with de G Linux in the past deing G her and open D and stuffs like that so my job is really replace prop assistance with free software I am a retired football player but sometimes I insist to play again I regret every time because I got injured I'm a father of two beautiful girls it's a teenager and a child so I'm not used it to solve conflicts in kubernetes upgrades I'm also expert in solving conflicts at home I'm a competitive Pokemon gen 3 OU player if you want what does mean I am shahu bhz on pokemo sh down.com uh they said it's a child game and really is a child game sorry sorry Mom I'm a football lover I'm a support of the best team in Brazil which is Club Atletico we call them Gallo which means rooster in Portuguese so okay let's go what it means what it really important now what we see in this presentation well we will have a brief introduction about secr infrastructure related to kubernetes uh our sesh proof of concept run uh how do we automated our s smesh configuration that's a pretty important point because we Face a lot of challenges uh just before I get started really how many of you here if you can raise your hands are using service Imes from in somehow okay and how many of you you are using celum cluster mesh okay so okay the people with celum cluster mesh will see uh I think important things here um the
