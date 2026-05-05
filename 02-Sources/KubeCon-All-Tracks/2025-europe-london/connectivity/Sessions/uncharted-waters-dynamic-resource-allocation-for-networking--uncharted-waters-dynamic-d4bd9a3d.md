---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Miguel Duarte Barroso", "Red Hat", "Lionel Jouin", "Ericsson Software Technology"]
sched_url: https://kccnceu2025.sched.com/event/1txAx/uncharted-waters-dynamic-resource-allocation-for-networking-miguel-duarte-barroso-red-hat-lionel-jouin-ericsson-software-technology
youtube_search_url: https://www.youtube.com/results?search_query=Uncharted+Waters%3A+Dynamic+Resource+Allocation+for+Networking+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Uncharted Waters: Dynamic Resource Allocation for Networking - Miguel Duarte Barroso, Red Hat & Lionel Jouin, Ericsson Software Technology

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United Kingdom / London
- Speakers: Miguel Duarte Barroso, Red Hat, Lionel Jouin, Ericsson Software Technology
- Schedule: https://kccnceu2025.sched.com/event/1txAx/uncharted-waters-dynamic-resource-allocation-for-networking-miguel-duarte-barroso-red-hat-lionel-jouin-ericsson-software-technology
- Busca YouTube: https://www.youtube.com/results?search_query=Uncharted+Waters%3A+Dynamic+Resource+Allocation+for+Networking+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Uncharted Waters: Dynamic Resource Allocation for Networking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAx/uncharted-waters-dynamic-resource-allocation-for-networking-miguel-duarte-barroso-red-hat-lionel-jouin-ericsson-software-technology
- YouTube search: https://www.youtube.com/results?search_query=Uncharted+Waters%3A+Dynamic+Resource+Allocation+for+Networking+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PgCaIyeRn6Y
- YouTube title: Uncharted Waters: Dynamic Resource Allocation for Networking - Miguel Duarte Barroso & Lionel Jouin
- Match score: 0.851
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/uncharted-waters-dynamic-resource-allocation-for-networking/PgCaIyeRn6Y.txt
- Transcript chars: 20832
- Keywords: network, resource, interface, device, interfaces, request, networking, cluster, attachment, resources, allows, available, status, miguel, working, created, called, worker

### Resumo baseado na transcript

I'm here with Lionol and we are presenting a talk titled Uncharted Waters dynamic resource allocation for networking. The plan here is for us to tell a little bit about uh dynamic resource allocation. One thing that is quite good about this is that you will according to the Kubernetes uh networking model there is no on east west traffic and that thing well again in our opinion opinionated way amazing uh the motivation now for this is but Another uh use case that you cannot realize with Kubernetes alone is what if you want more than one interface. So the fact that uh Kubernetes itself does not answer this does not mean that it's not possible. So the Kubernetes uh network plumbing work group came up or came came forward with a the de facto standard for multi-et networking which is implemented by multiscni.

### Excerpt da transcript

Hello everyone. Uh we're here at CubeCon Europe 2025 uh this time around in London. My name is Miguel. I'm here with Lionol and we are presenting a talk titled Uncharted Waters dynamic resource allocation for networking. The plan here is for us to tell a little bit about uh dynamic resource allocation. what it is, it stands short uh short notion is DRA and especially what it means for the Kubernetes multi-et network uh ecosystem. Let's first introduce ourselves. So I'm Lionel. I'm working at Ericson software technology. I'm mostly involved in the CNI community in the multi network community and SIG network and I'm also involved currently in the area to have this multi network happening with the array. Amazing. And I'm uh Miguel Dwart. I'm a software engineer working for Red Hat uh particularly on the Open Shift virtualization networking team. I'm working on pretty much like pushing virtualization features into Open Shift's SDN. And let us walk through the agenda for this presentation. like we will begin with the motivation and the problem statement uh for for this from there we will uh explain and paint the multi-et network landscape today for uh in the Kubernetes ecosystem and from there we will perform like an introduction to uh dynamic resource allocation especially what it means in the context of networking and multi-etworking from there we will uh walk you through the most relevant Kubernetes enhancement proposals uh specifically for multi-et networking and a very dedicated or very specific scheduling use case and we will finalize with a live demo.

So the problem at least as we see it is Kubernetes is opinionated. It is very opinionated according to whom you ask and by this we mean that its networking model is extremely simple and that might end up being like a double-edged sword because what happens is every pod on your cluster will get exactly one interface and every pod in your cluster will be interconnected and able to reach anybody else. So extremely simple but if you don't want that well if you want micro segmentation you can put uh network policies on top to kind of um define access and who gets access to what resource on what port and sort but this thing is expensive and it's expensive in two different ways. The first of which is computationally expensive meaning that every time a pod gets created or you provision in a network policy you have to re the system has to reconcile itself recomputee which IPs can access which IPs on which ports and
