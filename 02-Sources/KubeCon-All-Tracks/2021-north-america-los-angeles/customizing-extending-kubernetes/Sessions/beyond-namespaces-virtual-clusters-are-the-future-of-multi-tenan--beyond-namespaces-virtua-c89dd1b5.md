---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Customizing + Extending Kubernetes"
themes: ["Kubernetes Core"]
speakers: ["Lukas Gentele", "Loft Labs"]
sched_url: https://kccncna2021.sched.com/event/lV26/beyond-namespaces-virtual-clusters-are-the-future-of-multi-tenancy-lukas-gentele-loft-labs
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+Namespaces%3A+Virtual+Clusters+are+the+Future+of+Multi-Tenancy+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Beyond Namespaces: Virtual Clusters are the Future of Multi-Tenancy - Lukas Gentele, Loft Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Lukas Gentele, Loft Labs
- Schedule: https://kccncna2021.sched.com/event/lV26/beyond-namespaces-virtual-clusters-are-the-future-of-multi-tenancy-lukas-gentele-loft-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+Namespaces%3A+Virtual+Clusters+are+the+Future+of+Multi-Tenancy+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Beyond Namespaces: Virtual Clusters are the Future of Multi-Tenancy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV26/beyond-namespaces-virtual-clusters-are-the-future-of-multi-tenancy-lukas-gentele-loft-labs
- YouTube search: https://www.youtube.com/results?search_query=Beyond+Namespaces%3A+Virtual+Clusters+are+the+Future+of+Multi-Tenancy+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QddWNqchD9I
- YouTube title: Beyond Namespaces: Virtual Clusters are the Future of Multi-Tenancy - Lukas Gentele, Loft Labs
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/beyond-namespaces-virtual-clusters-are-the-future-of-multi-tenancy/QddWNqchD9I.txt
- Transcript chars: 32156
- Keywords: cluster, virtual, clusters, namespace, actually, namespaces, create, server, underlying, inside, resources, working, pretty, multi-tenancy, v-cluster, spaces, vcluster, running

### Resumo baseado na transcript

all right welcome everyone uh to the talk beyond namespaces virtual clusters are the future of multi-tenancy i'm lucas and i'm the ceo of loft labs in i'm based in san francisco but originally from germany so you know excuse the funny accent together with my team we're working on some really exciting uh things in the kubernetes space our commercial product loft essentially enables large companies you know to provide self-service isolated name spaces to a large number of engineers really like an internal provisioning platform for kubernetes so

### Excerpt da transcript

all right welcome everyone uh to the talk beyond namespaces virtual clusters are the future of multi-tenancy i'm lucas and i'm the ceo of loft labs in i'm based in san francisco but originally from germany so you know excuse the funny accent together with my team we're working on some really exciting uh things in the kubernetes space our commercial product loft essentially enables large companies you know to provide self-service isolated name spaces to a large number of engineers really like an internal provisioning platform for kubernetes so we really care a lot about multi-tenancy about user experience developer experience and about self-service and because we care so much about these topics we're also heavily involved in open source we're working on four different open source projects our oldest project is called devspace it's a developer tool for kubernetes and it's essentially a replacement for docker compose that is designed to be you know for kubernetes that you you know can you know streamline your workflow with kubernetes the same way as you can do with docker compose with your local docker daemon but now you can also do that with a remote kubernetes cluster we're also working on kiosk which is a multi-tenancy extension for kubernetes and and on js policy which is a policy engine that allows you to write policies in javascript or typescript making it much easier you know to write these policies and maintain them over a long period of time even with someone you know in the company leaves that you know was the ricoh expert um writing policies beforehand and one of the projects that we're working on uh is v-cluster and that's what we're actually going to talk about uh today it's a really really exciting project around virtual communities clusters so let's dive in beyond namespaces virtual clusters are the future of multi-tenancy gosh that's a pretty heavyweight title right i don't even know where you are you know where you're attending this session the future of multi-tenancy wow what is that right uh virtual clusters never heard of that um you're probably all here because the first part right beyond namespaces right you know namespaces yeah i got this right um i think everybody attending kubecon probably knows what a namespace is but do you really know what a namespace if we actually ask google what is a kubernetes namespace i mean you know google came up with kubernetes after all right so let's just take a look and if we go to the kubernetes docume
