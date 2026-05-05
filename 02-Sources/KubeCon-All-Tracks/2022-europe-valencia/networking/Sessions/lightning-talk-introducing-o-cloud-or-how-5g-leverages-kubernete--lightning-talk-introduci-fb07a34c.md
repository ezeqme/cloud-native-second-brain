---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Networking"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Nikolay Nikolaev", "Juniper Networks"]
sched_url: https://kccnceu2022.sched.com/event/ytwX/lightning-talk-introducing-o-cloud-or-how-5g-leverages-kubernetes-nikolay-nikolaev-juniper-networks
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Introducing+O-Cloud%2C+or+How+5G+Leverages+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Lightning Talk: Introducing O-Cloud, or How 5G Leverages Kubernetes - Nikolay Nikolaev, Juniper Networks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Networking]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Nikolay Nikolaev, Juniper Networks
- Schedule: https://kccnceu2022.sched.com/event/ytwX/lightning-talk-introducing-o-cloud-or-how-5g-leverages-kubernetes-nikolay-nikolaev-juniper-networks
- Busca YouTube: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Introducing+O-Cloud%2C+or+How+5G+Leverages+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Lightning Talk: Introducing O-Cloud, or How 5G Leverages Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytwX/lightning-talk-introducing-o-cloud-or-how-5g-leverages-kubernetes-nikolay-nikolaev-juniper-networks
- YouTube search: https://www.youtube.com/results?search_query=Lightning+Talk%3A+Introducing+O-Cloud%2C+or+How+5G+Leverages+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VLQJ_Awp2x0
- YouTube title: Lightning Talk: Introducing O-Cloud, or How 5G Leverages Kubernetes - Nikolay Nikolaev
- Match score: 0.964
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/lightning-talk-introducing-o-cloud-or-how-5g-leverages-kubernetes/VLQJ_Awp2x0.txt
- Transcript chars: 5234
- Keywords: networking, network, native, workloads, hardware, technologies, software, infrastructure, platform, virtualization, interface, principles, clarification, typically, access, defines, clusters, management

### Resumo baseado na transcript

hello my name is nikola miklev i'm a senior staff engineer with juniper networks currently my focus is to the application of the cloud native technologies within the delco domain and today i'm going to talk to you about the open run and how it adopts kubernetes let's start the modernization of the way we do networking started about 15 years ago with the introduction of the software defined networking and when this trend was combined with the concept of virtualization of the hardware resources uh the networking function virtualization

### Excerpt da transcript

hello my name is nikola miklev i'm a senior staff engineer with juniper networks currently my focus is to the application of the cloud native technologies within the delco domain and today i'm going to talk to you about the open run and how it adopts kubernetes let's start the modernization of the way we do networking started about 15 years ago with the introduction of the software defined networking and when this trend was combined with the concept of virtualization of the hardware resources uh the networking function virtualization was about the nfv it allowed for running specialized networking workloads on top of the commodity hardware like cpus memory and network interface cards the rising proliferation of cloud native technologies in principles created a new wave of networking virtualization the clarification of the networking domain allowed for building currently scalable applications and creating closely coupled systems that are resilient manageable and observable this is a direct quote from the cncf's cloud native definition but my favorite part of these qualities make high impact changes frequently and predictably with minimal tile this is a huge game changer for the networking quote where typically a new software rollout can take months while all of this was happening the telecom industry kept running through the newer and newer generations of their networking architectures 3g 4g but when 5g was introduced it proposed various new use cases such as self-driving cars and e-health this puts huge demand on the flexibility of the underlying infrastructure where virtualizing networking functions was a natural fit but adding the cloud native principles in the mix makes it even more appealing to the telcos to adopt let's zoom a bit atelico network is typically split into the core network radio access network or run and uh the back home uh which we call the infrastructure that connects the core and around while the core network was a relatively natural fit for the nfvm codification the radio access network was typically more rigid and hard to revolutionize yet people started looking at it and in an attempt to align its implementation with any vm clarification trends so that's how in 2018 the open run alliance was born it defines the standardized logical architecture of the radioaccess network and the interfaces between its components it also defines various splits or functionality distributions across physical and cloud instances to facilitate this design
