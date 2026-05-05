---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Yong Tang", "Ivanti", "John Belamaric", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2EF5D/when-dns-blinks-scaling-and-hardening-coredns-in-critical-cloud-infrastructure-yong-tang-ivanti-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=When+DNS+Blinks%3A+Scaling+and+Hardening+CoreDNS+in+Critical+Cloud+Infrastructure+CNCF+KubeCon+2026
slides: []
status: parsed
---

# When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infrastructure - Yong Tang, Ivanti & John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yong Tang, Ivanti, John Belamaric, Google
- Schedule: https://kccnceu2026.sched.com/event/2EF5D/when-dns-blinks-scaling-and-hardening-coredns-in-critical-cloud-infrastructure-yong-tang-ivanti-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=When+DNS+Blinks%3A+Scaling+and+Hardening+CoreDNS+in+Critical+Cloud+Infrastructure+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infrastructure.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF5D/when-dns-blinks-scaling-and-hardening-coredns-in-critical-cloud-infrastructure-yong-tang-ivanti-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=When+DNS+Blinks%3A+Scaling+and+Hardening+CoreDNS+in+Critical+Cloud+Infrastructure+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9UIPskZ07dY
- YouTube title: When DNS Blinks: Scaling and Hardening CoreDNS in Critical Cloud Infra... Yong Tang & John Belamaric
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/when-dns-blinks-scaling-and-hardening-coredns-in-critical-cloud-infras/9UIPskZ07dY.txt
- Transcript chars: 25119
- Keywords: server, coding, actually, snorts, central, cordns, cluster, running, internet, plug-in, caching, sockets, google, little, number, connection, failures, thousands

### Resumo baseado na transcript

After that we're going to uh discuss the lessons we learned over the past year especially some of the uh DS related incidents across internet and then the mitigations and how to make uh DNS uh robust reliable and flexible in uh critical cloud infrastructures. Uh one of the biggest feas uh advantage of coding is that it's a plug-in based architecture which means it can be easily extended. polling multiplex connection and API limiting on quantic plugin uh on security slide. I mean, if you were at the keynotes, you saw DNS uh we had we had a DNS failure there that caused some problems. So prefetch is a configuration um that allows you to kind of uh as it sees records that are frequently used in your in your um in your DNS query stream. One is in a caching architecture, one is in an authoritative server architecture.

### Excerpt da transcript

Good morning. Thanks everyone for joining this session. My name is Yan Tang. This is Google from uh this is John Palmer from Google. Uh today we are going to discuss about audience project. Uh both [snorts] John and me uh continues of guidance project. We have been uh with audience since at the beginning. That's almost like 10 years. Yes, that's it's a little amazing. >> So in today's session we are going to cover several areas. First we're going to introduce coding as a little background. Then we're going to talk about the project update. After that we're going to uh discuss the lessons we learned over the past year especially some of the uh DS related incidents across internet and then the mitigations and how to make uh DNS uh robust reliable and flexible in uh critical cloud infrastructures. To start with, coding as everyone knows is a flexible DNS server go. Uh it was um developed almost like more than 10 years ago actually. Uh [snorts] it has a focus on service discovery. Uh one of the biggest feas uh advantage of coding is that it's a plug-in based architecture which means it can be easily extended.

If there's any new features or functionalities you you want to add and it's not in the uh existing uh plug-in then you can write write a plug-in uh yourself uh easily as long as you know how to write in go the the coding has been the default DNS server in Kubernetes for since um 2017 that's almost like 10 years as well [snorts] uh because of the adoption of K kubernetes the coding itself has seen a wide adoption as well. uh we have a lot of uh uh usage all the place we have lots of u like uh companies organization institution they all use coding as whenever they use kubernetes uh in addition to uh its association with kubernetes coding also support is also DS server so it support additional protocols like DNS DNS over to >> [snorts] >> uh with gpc quick and http E3. Uh finally, coding SS also support uh cloud integration. [snorts] Uh if you have a servers uh DS service AWS, a Google cloud, you actually can use to DS as a central point of information to connect to different back end to uh to support different back end so that you have DNS with central place to hold all the information.

uh coding has been growing exclusively for the past 10 years. Uh as of right now we have more than 400 contributors. We have 14,000 stars. We also have growing list of for public adopters. The number of public adopted here is just limited because u the adopted here just th
