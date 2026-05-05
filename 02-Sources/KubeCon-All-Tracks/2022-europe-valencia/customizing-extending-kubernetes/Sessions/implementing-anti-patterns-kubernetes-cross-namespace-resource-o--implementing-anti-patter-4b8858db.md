---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Tom Coufal", "Red Hat"]
sched_url: https://kccnceu2022.sched.com/event/ytqC/implementing-anti-patterns-kubernetes-cross-namespace-resource-ownership-tom-coufal-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Implementing+Anti-patterns%3A+Kubernetes+Cross-namespace+Resource+Ownership+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Implementing Anti-patterns: Kubernetes Cross-namespace Resource Ownership - Tom Coufal, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Tom Coufal, Red Hat
- Schedule: https://kccnceu2022.sched.com/event/ytqC/implementing-anti-patterns-kubernetes-cross-namespace-resource-ownership-tom-coufal-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Implementing+Anti-patterns%3A+Kubernetes+Cross-namespace+Resource+Ownership+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Implementing Anti-patterns: Kubernetes Cross-namespace Resource Ownership.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqC/implementing-anti-patterns-kubernetes-cross-namespace-resource-ownership-tom-coufal-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Implementing+Anti-patterns%3A+Kubernetes+Cross-namespace+Resource+Ownership+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iWz5AAbbT-c
- YouTube title: Implementing Anti-patterns: Kubernetes Cross-namespace Resource Ownership - Tom Coufal, Red Hat
- Match score: 0.963
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/implementing-anti-patterns-kubernetes-cross-namespace-resource-ownersh/iWz5AAbbT-c.txt
- Transcript chars: 23131
- Keywords: resource, namespace, meteor, namespaces, resources, cluster, deleted, ownership, references, reference, shower, delete, commas, implement, controller, finalizer, usually, garbage

### Resumo baseado na transcript

hello can you hear me good um hello everybody welcome to implementing antipatterns aka implementing cross namespace resource ownership in kubernetes uh i hope i won't disappoint you uh with this talk i know i will disappoint you with it being an anti-pattern and implementing it in kubernetes and i hope you're not too disappointed by that so what we're gonna do today um i'm gonna talk a bit about some kubernetes concepts um that we usually use and we usually see like ownerships dependents name spaces garbage collection and

### Excerpt da transcript

hello can you hear me good um hello everybody welcome to implementing antipatterns aka implementing cross namespace resource ownership in kubernetes uh i hope i won't disappoint you uh with this talk i know i will disappoint you with it being an anti-pattern and implementing it in kubernetes and i hope you're not too disappointed by that so what we're gonna do today um i'm gonna talk a bit about some kubernetes concepts um that we usually use and we usually see like ownerships dependents name spaces garbage collection and the rules that goes with those concepts then we're gonna try to exploit and implement and do some forbidden stuff that kubernetes disallow in the documentation and in the implementation as well and we're gonna try to do so without smashing through the walls of kubernetes implementation we're gonna bend the rules so it fits our uh our very anti-patternish wrong use case that i'm gonna in the meantime try to justify to you uh so you see that we really need to do something like that so first things first uh who am i uh my name is tom tofal i work as a software engineer at red hat at the office of the cto in emerging technologies what do we do we research various topics we experiment with managed services open services and things like that and one of our key area of focus is analytics data science uh oriented workloads and uh things like that so that's where this use case originated from and i'm gonna talk to that a bit later so what i'm gonna be talking about there's a very nice coincidence uh yesterday there was this book signing event at the redhead booth i didn't know about that before beforehand so i've added the slide in the last minute about kubernetes pattern patterns book uh by colleagues of mine at redhead honestly i haven't read this book if those offers are here i'm sorry i'm sure it's a very nice book uh and since i haven't tried it uh i'm gonna be doing anti-patterns so we're gonna shoot the deck and uh we're gonna smash through it no what just happened good so how we're gonna do it this is the agenda as usual first we're gonna start with introducing some concepts to you uh going through the most basic stuff for most of you maybe but also going to some some more advanced things uh so hopefully uh it's not just a recap and we will get some some new connections between those concepts then i'm gonna provoke you with the use case um and then we're gonna explore only one solution because we don't have time for more and really uh we'v
