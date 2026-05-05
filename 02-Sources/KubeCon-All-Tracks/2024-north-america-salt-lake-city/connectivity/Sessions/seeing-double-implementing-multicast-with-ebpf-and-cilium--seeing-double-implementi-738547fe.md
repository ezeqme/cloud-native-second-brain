---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Louis DeLosSantos", "Isovalent at Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7qG/seeing-double-implementing-multicast-with-ebpf-and-cilium-louis-delossantos-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Seeing+Double%3F+Implementing+Multicast+with+eBPF+and+Cilium+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Seeing Double? Implementing Multicast with eBPF and Cilium - Louis DeLosSantos, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Louis DeLosSantos, Isovalent at Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7qG/seeing-double-implementing-multicast-with-ebpf-and-cilium-louis-delossantos-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Seeing+Double%3F+Implementing+Multicast+with+eBPF+and+Cilium+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Seeing Double? Implementing Multicast with eBPF and Cilium.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7qG/seeing-double-implementing-multicast-with-ebpf-and-cilium-louis-delossantos-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Seeing+Double%3F+Implementing+Multicast+with+eBPF+and+Cilium+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fX7LL0cIX40
- YouTube title: Seeing Double? Implementing Multicast with eBPF and Cilium - Louis DeLosSantos, Isovalent at Cisco
- Match score: 0.835
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/seeing-double-implementing-multicast-with-ebpf-and-cilium/fX7LL0cIX40.txt
- Transcript chars: 33394
- Keywords: multicast, ebpf, actually, subscriber, source, address, little, membership, redirect, protocol, header, packet, delivery, report, interface, pretty, traffic, simple

### Resumo baseado na transcript

hey my name is lisis D Santos and I'm here to talk about how we implemented multicast with ebpf and psyllium first uh who am I right uh I'm a data path engineer at Cisco uh we were ISO vent before Cisco acquired us I focus on Linux kernel networking and ebpf I've worked in open source for quite some time now and all my free time I like to develop neovin plugins and play around with li Linux desktop development like uh whin and gtk4 stuff okay so what

### Excerpt da transcript

hey my name is lisis D Santos and I'm here to talk about how we implemented multicast with ebpf and psyllium first uh who am I right uh I'm a data path engineer at Cisco uh we were ISO vent before Cisco acquired us I focus on Linux kernel networking and ebpf I've worked in open source for quite some time now and all my free time I like to develop neovin plugins and play around with li Linux desktop development like uh whin and gtk4 stuff okay so what are we going to cover in this talk we're going to do a really gentle uh introduction to multicast and then I'm going to go over how we implemented multicast using EPF and the celium data path it's going to be a super nerdy talk so you can go ahead and follow it uh our BPF code at this link if you want to okay a couple disclaimers before we start I wouldn't necessarily consider myself a multicast expert I got pretty acquainted to it with uh this project but some of the larger multicast deployments out there um just guard your questions as far as how deep you want to go uh at the end we're going to talk about multicast in the context of kubernetes and celium so any kind of sources or subscribers to multicast groups outside the cluster are a little bit of uh out of scope for this talk and and again we're going to focus on the ebpf data path right all right so what is multicast right uh it was introduced in RFC 1112 it's a layer three technology right so it works at the IP layer any kind of layers on top uh any protocols on top are usually connectionless it's very common to see multicast and UDP working together and multicast is the unicast delivery to a group of hosts done efficiently right it removes the burden from the source so if you look at that diagram right there you don't see the source on the left sending packets to each uh subscriber instead the IP infrastructure in the middle is doing that work for you so where is multicast used broadcasting and media streaming right your favorite movie sometimes it's being delivered to millions of clients at a time in financial services it's pretty popular uh Market update data is usually like broadcasted out to a bunch of subscribers and online gaming is another one where you might have a session with a bunch of online Gamers and you want to broadcast the game state to everyone all right so how does it work uh the first thing we should talk about is uh multicast group addresses these are just IP addresses right uh they're class D addresses there are some specific one
