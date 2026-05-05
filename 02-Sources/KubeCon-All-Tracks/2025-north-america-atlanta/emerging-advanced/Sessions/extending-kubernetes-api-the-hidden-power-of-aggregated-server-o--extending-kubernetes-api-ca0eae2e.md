---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Amir Malka", "ARMO"]
sched_url: https://kccncna2025.sched.com/event/27Fam/extending-kubernetes-api-the-hidden-power-of-aggregated-server-objects-amir-malka-armo
youtube_search_url: https://www.youtube.com/results?search_query=Extending+Kubernetes+API%3A+The+Hidden+Power+of+Aggregated+Server+Objects+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Extending Kubernetes API: The Hidden Power of Aggregated Server Objects - Amir Malka, ARMO

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Amir Malka, ARMO
- Schedule: https://kccncna2025.sched.com/event/27Fam/extending-kubernetes-api-the-hidden-power-of-aggregated-server-objects-amir-malka-armo
- Busca YouTube: https://www.youtube.com/results?search_query=Extending+Kubernetes+API%3A+The+Hidden+Power+of+Aggregated+Server+Objects+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Extending Kubernetes API: The Hidden Power of Aggregated Server Objects.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fam/extending-kubernetes-api-the-hidden-power-of-aggregated-server-objects-amir-malka-armo
- YouTube search: https://www.youtube.com/results?search_query=Extending+Kubernetes+API%3A+The+Hidden+Power+of+Aggregated+Server+Objects+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ifwNDvRSQWU
- YouTube title: Extending Kubernetes API: The Hidden Power of Aggregated Server Objects - Amir Malka, ARMO
- Match score: 0.977
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/extending-kubernetes-api-the-hidden-power-of-aggregated-server-objects/ifwNDvRSQWU.txt
- Transcript chars: 14831
- Keywords: server, request, resource, objects, aggregated, cubecape, basically, implement, storage, servers, resources, client, memory, vulnerability, asbomb, external, cluster, everything

### Resumo baseado na transcript

I'm also a core maintainer of cubecape CNCF incubating project and a gopheron speaker. So the agenda for today is uh we're going to start by um looking on the differences between CRDs and aggregated API servers. So in order to become like a fully open source solution uh we um looked in a way that we are going to keep all the data inside the cluster and one of the important thing for us was that our users were Kubernetes users. So we wanted them to to not learn like a new API and so that everything remains in the Kubernetes ecosystem and so Kubernetes basically gives you two ways to extend its API. um they you define a new resource type in a YAML and basically the Kubernetes API server does all the heavy lifting for you. So like with extension API server, you build your own uh standalone API server like Kubernetes does and so you're fully in control when it comes to storage discovery and all the logic and behavior of that server.

### Excerpt da transcript

So um I'm air software architect at Armo. I'm also a core maintainer of cubecape CNCF incubating project and a gopheron speaker. This is my first uh cubecon as a speaker. [gasps] Uh you can find me on LinkedIn and or GitHub. So the agenda for today is uh we're going to start by um looking on the differences between CRDs and aggregated API servers. Um we'll see how uh how these aggregated API servers work and we'll take a look on a use case how we in cubecape develop our own uh server and also uh we'll uh go over the lessons we learned in production and like when to choose this path and when not to. Um uh so that's about like the agenda for today and before I dive in to talk about aggregated API servers uh let me set the context on cubecape. So cubecape is a security platform. It aims to cover all aspects of uh security aspects in a single project. So what we do is we do vulnerability scanning for container images. We do configuration scanning of workloads against best practices. We also do workload behavior monitoring with eBPF.

And so in general, we generate a lot of data. So if I look on the vulnerability scanning flow, so in order to uh be able to create a vulnerability report, first you have to generate an asbomb. And so what we do is that we generate an asbomb. An asbomb is a list of all the components that make up a container image and it can be quite large. So once you've generated an asbomb, it passes through the vulnerability scanner and then it gets sent to some external API. This is how we used to work like back at the beginning of cubecape. And so becoming open source had its uh requirements or challenges. So in order to become like a fully open source solution uh we um looked in a way that we are going to keep all the data inside the cluster and one of the important thing for us was that our users were Kubernetes users. So we wanted them to to not learn like a new API and so that everything remains in the Kubernetes ecosystem and so Kubernetes basically gives you two ways to extend its API. One is with CRDs.

CRDs or custom resources are very easy to implement. It's like the lightweight route. um they you define a new resource type in a YAML and basically the Kubernetes API server does all the heavy lifting for you. So you have arbach out of the box validation. Um you can use CL expressions for like complex validations and everything gets stored in at CD and so the second option is with extension API server. That's the main subject for the ta
