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
themes: ["Kubernetes Core"]
speakers: ["Casey Davenport", "Tigera", "Dan Winship", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7o7/how-the-tables-have-turned-kubernetes-says-goodbye-to-iptables-casey-davenport-tigera-dan-winship-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=How+the+Tables+Have+Turned%3A+Kubernetes+Says+Goodbye+to+Iptables+CNCF+KubeCon+2024
slides: []
status: parsed
---

# How the Tables Have Turned: Kubernetes Says Goodbye to Iptables - Casey Davenport, Tigera & Dan Winship, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Casey Davenport, Tigera, Dan Winship, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7o7/how-the-tables-have-turned-kubernetes-says-goodbye-to-iptables-casey-davenport-tigera-dan-winship-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=How+the+Tables+Have+Turned%3A+Kubernetes+Says+Goodbye+to+Iptables+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre How the Tables Have Turned: Kubernetes Says Goodbye to Iptables.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7o7/how-the-tables-have-turned-kubernetes-says-goodbye-to-iptables-casey-davenport-tigera-dan-winship-red-hat
- YouTube search: https://www.youtube.com/results?search_query=How+the+Tables+Have+Turned%3A+Kubernetes+Says+Goodbye+to+Iptables+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yOGHb2HjslY
- YouTube title: How the Tables Have Turned: Kubernetes Says Goodbye to Iptables - Casey Davenport & Dan Winship
- Match score: 0.896
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/how-the-tables-have-turned-kubernetes-says-goodbye-to-iptables/yOGHb2HjslY.txt
- Transcript chars: 30608
- Keywords: tables, calico, actually, updates, network, packet, ebpf, latency, filter, already, change, performance, policy, version, pretty, probably, default, smaller

### Resumo baseado na transcript

welcome everybody my name is uh Casey Davenport I'm an engineer at igera working on Calico my name is Dan winchip I'm an engineer at Red Hat uh working on open shift networking and uh yeah we're here to talk about how the tables have turned um specifically uh our journey moving kubernetes and and Calico from uh IP tables to NF tables um quick rundown of what we're going to talk about today so I'm going to start just with brief overview of Ip tables and NF tables um

### Excerpt da transcript

welcome everybody my name is uh Casey Davenport I'm an engineer at igera working on Calico my name is Dan winchip I'm an engineer at Red Hat uh working on open shift networking and uh yeah we're here to talk about how the tables have turned um specifically uh our journey moving kubernetes and and Calico from uh IP tables to NF tables um quick rundown of what we're going to talk about today so I'm going to start just with brief overview of Ip tables and NF tables um some history about them and their their usage in the kubernetes ecosystem um and we're going to talk about why we need to leave IP tables in the first place and how we ended up on N of tables as a replacement um finally we'll talk a little bit about some of the initial results from uh the work we've done so far uh yeah so a lot of terms get thrown around here IP tables NF tables even IP tables nft um both IP tables and NF tables are tools that allow you to configure networking in Linux um and they're both primarily split into two parts um there's an API component that exists within the kernel uh and there's a user space component there's a tool that applications can use to read state from the API and write um configuration back into that API uh and under the hood both of of them are configuring net filter um which is the primary packet manipulation system um within the Linux kernel uh they both can do things like packet manipulation forwarding um filtering net Etc um and in the early days of kubernetes um we picked IP tables uh as the service implementation in Cube proxy as well as Network policy implementation in Calico NF tables existed at the time but it wasn't quite as mature as IP tables was it wasn't quite as ubiquitous as IP tables was and so it was it was the right choice at the time uh along the way uh IP tables nft came along uh this was in IP tables version 1.8.1 and it sort of acted as a drop in replacement for the existing user space tool that provided the same feature set but under the hood was talking to the NF tables API and this allowed kernel development to switch from IP tables API over to nft tables API without disrupting the ecosystem of applications that had been built on top of Ip tables um it's worth noting though that even though we were using the NF tables API under the covers applications are still limited to the the feature set and capabilities of Ip tables when using this and it uh it caused some problems in the kubernetes space uh specifically um as we went through
