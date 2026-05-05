---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Giri Kuncoro", "Joseph Pallamidessi", "TikTok"]
sched_url: https://kccncna2025.sched.com/event/27FbS/tiktoks-ipv6-journey-to-cilium-pitfalls-and-lessons-learned-giri-kuncoro-joseph-pallamidessi-tiktok
youtube_search_url: https://www.youtube.com/results?search_query=TikTok%27s+IPv6+Journey+To+Cilium%3A+Pitfalls+and+Lessons+Learned+CNCF+KubeCon+2025
slides: []
status: parsed
---

# TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned - Giri Kuncoro & Joseph Pallamidessi, TikTok

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Giri Kuncoro, Joseph Pallamidessi, TikTok
- Schedule: https://kccncna2025.sched.com/event/27FbS/tiktoks-ipv6-journey-to-cilium-pitfalls-and-lessons-learned-giri-kuncoro-joseph-pallamidessi-tiktok
- Busca YouTube: https://www.youtube.com/results?search_query=TikTok%27s+IPv6+Journey+To+Cilium%3A+Pitfalls+and+Lessons+Learned+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FbS/tiktoks-ipv6-journey-to-cilium-pitfalls-and-lessons-learned-giri-kuncoro-joseph-pallamidessi-tiktok
- YouTube search: https://www.youtube.com/results?search_query=TikTok%27s+IPv6+Journey+To+Cilium%3A+Pitfalls+and+Lessons+Learned+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y0qlhiKtDGo
- YouTube title: TikTok's IPv6 Journey To Cilium: Pitfalls and Lessons Learned - Giri Kuncoro & Joseph Pallamidessi
- Match score: 0.861
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/tiktoks-ipv6-journey-to-cilium-pitfalls-and-lessons-learned/y0qlhiKtDGo.txt
- Transcript chars: 28161
- Keywords: selium, cluster, basically, network, celium, working, encapsulation, native, security, control, actually, center, packet, journey, kernel, policy, question, machine

### Resumo baseado na transcript

Thanks for joining us for this late afternoon session about Tik Tok's journey to IPv6 only cluster with uh with selium. Uh we so I'm Joseph, [snorts] here's Giri and we work specifically in the security engineering department at Tik Tok as specifically in the SE team. And then we run those community clusters bootstrap those Kubernetes cluster on top of those of those machine. And finally, we have our security teams that run their workload and their services on top of those Kubernetes clusters. So those security services everything related to authentication, authorization, identity man um identity management, key management, signing, encryptions, those are relatively low-level um internal services that basically are used at scale internally at Tik Tok and Bance for all the internal platforms. So you can probably more or less different work a different load on each of those region but you can probably extrapolate those number time 100 and that will represent our global or global metrics.

### Excerpt da transcript

Hey, hello everyone. Thanks for joining us for this late afternoon session about Tik Tok's journey to IPv6 only cluster with uh with selium. So we're from uh we're from Tik Tok. Uh we so I'm Joseph, [snorts] here's Giri and we work specifically in the security engineering department at Tik Tok as specifically in the SE team. So the security engineering department is a department that provide low-level security capability and services and as part of our work as SE we also manage bootstrap and manage kubernetes kubernetes cluster. Um first let's talk a little bit about why are we using sdium in the first place at tik tok. Um so a little bit of context about our our infrastructure. So like I say security engineering department who provides the services. Uh at Tik Tok we basically have this concept of concept of virtual data center like VDCs and they can be basically a public cloud machine private cloud machine VMs or bare metal. It's kind of a mix of a lot of things that can come from a lot of places but they like logically logically um let's say virtual data centers.

It's a globally distributed um multiDC architecture. We have about 10 logical region and and that's basically represent about 130 virtual data centers. Uh so basically logical region usually associated with with a geographical region but not only. So where we like we basically at this uh the layer we operate at is we have those data center team kind of providing those physical machine on prem machine those VMs that they source for either like public cloud or that run run ourself. Um and then we have the the kernel ops and the kernel team basically responsible for providing images can kernel and basically um some other software like um some other software like mostly related to like um observability of those of the machines themselves. And then we run those community clusters bootstrap those Kubernetes cluster on top of those of those machine. And finally, we have our security teams that run their workload and their services on top of those Kubernetes clusters. So, just to give you a rough idea of what we're talking about here.

So those security services everything related to authentication, authorization, identity man um identity management, key management, signing, encryptions, those are relatively low-level um internal services that basically are used at scale internally at Tik Tok and Bance for all the internal platforms. Um they're relatively low level. They usually usually try and connect
