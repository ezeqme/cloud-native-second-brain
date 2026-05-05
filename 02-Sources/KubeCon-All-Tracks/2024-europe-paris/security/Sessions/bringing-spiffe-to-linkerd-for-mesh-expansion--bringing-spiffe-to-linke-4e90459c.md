---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Security"
themes: ["Security"]
speakers: ["Zahari Dichev", "Buoyant"]
sched_url: https://kccnceu2024.sched.com/event/1YeOv/bringing-spiffe-to-linkerd-for-mesh-expansion-zahari-dichev-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Bringing+SPIFFE+to+Linkerd+for+Mesh+Expansion+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Bringing SPIFFE to Linkerd for Mesh Expansion - Zahari Dichev, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: Zahari Dichev, Buoyant
- Schedule: https://kccnceu2024.sched.com/event/1YeOv/bringing-spiffe-to-linkerd-for-mesh-expansion-zahari-dichev-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Bringing+SPIFFE+to+Linkerd+for+Mesh+Expansion+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Bringing SPIFFE to Linkerd for Mesh Expansion.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeOv/bringing-spiffe-to-linkerd-for-mesh-expansion-zahari-dichev-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Bringing+SPIFFE+to+Linkerd+for+Mesh+Expansion+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZLCJW--J6s0
- YouTube title: Bringing SPIFFE to Linkerd for Mesh Expansion - Zahari Dichev, Buoyant
- Match score: 0.884
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/bringing-spiffe-to-linkerd-for-mesh-expansion/ZLCJW--J6s0.txt
- Transcript chars: 28170
- Keywords: identity, actually, certificate, workload, mesh, cluster, particular, account, running, workloads, essentially, infrastructure, traffic, certificates, hardware, expansion, organizations, identities

### Resumo baseado na transcript

hello everyone and welcome to the talk titled uh bringing spify to Linker for mesh expansion and in this talk we are going to take a look at how linkerd the service mesh augmented its identity system in order to allow for uh meshing external workloads or actually making workloads that are not part of kubernetes part of the mesh um my name is zahari DV and I'm a software engineer at buyant uh the creators of linker and if you ever want to connect or chat you can always

### Excerpt da transcript

hello everyone and welcome to the talk titled uh bringing spify to Linker for mesh expansion and in this talk we are going to take a look at how linkerd the service mesh augmented its identity system in order to allow for uh meshing external workloads or actually making workloads that are not part of kubernetes part of the mesh um my name is zahari DV and I'm a software engineer at buyant uh the creators of linker and if you ever want to connect or chat you can always reach me on any of these channels I'm always happy to chat so in this talk we are going to um first of all take a look at make the case for mesh expansion so what is it and why might organizations actually need that functionality and then we are going to look at why workload identity matters both within and outside of the cluster and what are the guarantees that you get with the encryption and identity that's implemented in modern service meshes we're going to take a look at how that specifically Works in Linker D so with mtls and we are going to discuss some of the challenges that appear once you once you cross the boundary and you end up on a bare metal machine that's not part of kubernetes and then we are going to look at how we use spire and spiffy and leverage this technology in order to solve these problems and hopefully at the end we can have some time for a Q&A if you want to ask questions about any of that so first of all let's actually um take a look at what is mesh expansion and why organizations might need that so really if I have to put it succinctly um mesh expansion is the process of actually um making non- kubernetes workloads part of the service mesh and the main motivation for doing that is to enable hybrid Cloud infrastructure scenarios where you have part of your infrastructure on let's say bare metal machines or om Prem boxes uh but you want to be able to connect uh this infrastructure to kubernetes and the workloads in kubernetes communicate with it as if this infrastructure was native kubernetes workloads and this is really for the reason to kind of gain this uh to to to be able to be generic over the specifics of of your infrastructure so whether this is whether this workload is hosted on a local data center or on the cloud like that shouldn't really matter you should still be able to get all the nice things that you get when you're Ser using a service mesh namely um security guarantees reliability features such as uh circuit breaking load balancing uh traffic policy a
