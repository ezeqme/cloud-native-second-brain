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
speakers: ["Dario Tranchitella", "Technical Lead"]
sched_url: https://kccnceu2025.sched.com/event/1tcvc/project-lightning-talk-capsule-launching-multi-tenancy-to-new-kubernetes-horizons-dario-tranchitella-technical-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Capsule%3A+Launching+Multi-Tenancy+to+New+Kubernetes+Horizons+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Capsule: Launching Multi-Tenancy to New Kubernetes Horizons - Dario Tranchitella, Technical Lead

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Dario Tranchitella, Technical Lead
- Schedule: https://kccnceu2025.sched.com/event/1tcvc/project-lightning-talk-capsule-launching-multi-tenancy-to-new-kubernetes-horizons-dario-tranchitella-technical-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Capsule%3A+Launching+Multi-Tenancy+to+New+Kubernetes+Horizons+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Capsule: Launching Multi-Tenancy to New Kubernetes Horizons.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcvc/project-lightning-talk-capsule-launching-multi-tenancy-to-new-kubernetes-horizons-dario-tranchitella-technical-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Capsule%3A+Launching+Multi-Tenancy+to+New+Kubernetes+Horizons+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=02dSHShBVuk
- YouTube title: Project Lightning Talk: Capsule: Launching Multi-Tenancy to New Kubernetes Hor... Dario Tranchitella
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-capsule-launching-multi-tenancy-to-new-kubernet/02dSHShBVuk.txt
- Transcript chars: 5036
- Keywords: essentially, capsule, trying, cluster, clusters, multiple, tenant, creating, spaces, capture, tenants, adopters, instead, definition, amount, resource, engage, source

### Resumo baseado na transcript

My name is Dario and I will I am the creator of project capsule and I got an ele elevator pitch here. So essentially we try to solve the multienance in Kubernetes and keep in mind that I'm very happy to be here because capture has been my first open source project now it's part of CNCF and trying to keep it short essentially we struggled when we had multiple tenants using the same Kubernetes cluster. So essentially we try to solve the main problem of cubectl get name space and I just want to get the list of my name spaces. uh classics uh is the main contributor and we have also big scale and we got also some nice adopters because we have a DoD agency from the US even though we are in Europe.

### Excerpt da transcript

My name is Dario and I will I am the creator of project capsule and I got an ele elevator pitch here. So essentially we try to solve the multienance in Kubernetes and keep in mind that I'm very happy to be here because capture has been my first open source project now it's part of CNCF and trying to keep it short essentially we struggled when we had multiple tenants using the same Kubernetes cluster. So uh the old way was creating multiple clusters and here instead with project capsule what you can do is to try to enhance the Kubernetes capabilities with the tenant definition. So it's a way to say I have multiple users and they can use the same cluster but defining some boundaries. So creating a sort of virtual slice of the Kubernetes cluster and in a picture this is way more simpler uh trying to understand how it works because essentially you can end up with multiple Kubernetes clusters and for those who are operating Kubernetes clusters you can imagine the pain or you can have a huge single point of failure which is a huge cluster.

So this is a slide from one of the adopters and and I really love that and essentially uh um that's how we say in Italy sometimes kum granosalis so it means with a grain of salt you need to find the perfect balance and I guess that capsule essentially is trying to uh intercept that need so you can use small clusters not small clusters but a small amount of clusters rather than uh cluster scroll and also keep in mind that I'm huge Dune fan And essentially uh there is a reference here but I'm trying to explain how it works. So essentially you have the cluster administrator that defines the tenant definition. It's a cluster scope resource. So it's githops compliant and after that you have multiple tenants. They could be a trades they could be haron and the main benefit here is that it's not uh imperative but rather it's self-service. So a traders or haronent they can create their own name spaces and after that we have capsule which is uh our policy engine. It's a framework where you can define all the policies.

So you can create a maximum amount of pods a max maximum amount of name spaces and the arbback and everything there is automatically reconciled by the operator. Um how it works essentially so as I said before we are relying on CRDs. Uh we are leveraging on kubernetes primitives. So essentially we are using the arbback we are using the resource quota the limit ranges the network policies you can replicate everything acros
