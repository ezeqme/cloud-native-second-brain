---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: ["Design Considerations and Debates | Project Lightning Talk"]
sched_url: https://kccncna2024.sched.com/event/1iW9N/linkerd-adding-federated-services-to-linkerd-design-considerations-and-debates-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Linkerd%3A+Adding+Federated+Services+to+Linkerd+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Linkerd: Adding Federated Services to Linkerd - Design Considerations and Debates | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Salt Lake City
- Speakers: Design Considerations and Debates | Project Lightning Talk
- Schedule: https://kccncna2024.sched.com/event/1iW9N/linkerd-adding-federated-services-to-linkerd-design-considerations-and-debates-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Linkerd%3A+Adding+Federated+Services+to+Linkerd+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Linkerd: Adding Federated Services to Linkerd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9N/linkerd-adding-federated-services-to-linkerd-design-considerations-and-debates-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Linkerd%3A+Adding+Federated+Services+to+Linkerd+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qXrmhlXP4tw
- YouTube title: Linkerd: Adding Federated Services to Linkerd - Design Considerations and Debates | PLT
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/linkerd-adding-federated-services-to-linkerd/qXrmhlXP4tw.txt
- Transcript chars: 5210
- Keywords: linker, little, cluster, federated, clusters, considerations, security, simple, routes, having, linkerd, design, multicluster, adding, henderson, customer, success, engineer

### Resumo baseado na transcript

hello my name is Phil Henderson I'm a customer success engineer at buyant um creators of linker D today I'm going to talk about adding feder a services to Linker D and the design considerations and baates that went into it again my name is Phil Henderson customer success engineer there's my face same one that's on me now um You can find me on GitHub or slack I don't have any social media besides LinkedIn and there's probably more people in this room right now than I have on

### Excerpt da transcript

hello my name is Phil Henderson I'm a customer success engineer at buyant um creators of linker D today I'm going to talk about adding feder a services to Linker D and the design considerations and baates that went into it again my name is Phil Henderson customer success engineer there's my face same one that's on me now um You can find me on GitHub or slack I don't have any social media besides LinkedIn and there's probably more people in this room right now than I have on LinkedIn so feel free to find me and add me um but we'll go in that who's who here is familiar with Linker D okay good handful for those who aren't I'm going to give you a quick little lesson in it Linker D is the world's fastest service mesh that brings security reliability and observability to your applications in that order no exceptions it's an ultralight simple secure um purpose-built proxy which is different than other ones um link puts Simplicity and Security First it just works so there's zero zero changes you need to make on your applications um it's simple and it's ultra light and I'm going to keep saying that it's very important especially at this cubec Con when Ai and ml is a big topic so keep that in mind ultr light you can see even the little Footprints down there at the bottom um right now with multicluster and Linker D we bring we make it a little bit more resilient scalable and we have effective workload isolation who here is already using multicluster setups with their uh their kubernetes clusters and services anyone some okay who are you know trying to mirror those Services into other clusters so they can span their things okay so right now in Linker D it's pretty easy to do you can do it with the HTTP routes we have things mirring from one cluster to the next and it has the same built-in security and reliability that linkerd has inherently um but with this there's some scalability considerations that you need to you know consider if you've used HTTP routes before you know that there's some some things to it where if you don't have a service available it's going to start throwing some 500s which you don't want your application to do that and when you start spanning more than one cluster and start you know my my example here is just another one but when you start pinning you know half a dozen dozen clusters together having these HTTP routes can be a little bit more complex than you really want so with Federated Services we're going to be able to bring that all into one
