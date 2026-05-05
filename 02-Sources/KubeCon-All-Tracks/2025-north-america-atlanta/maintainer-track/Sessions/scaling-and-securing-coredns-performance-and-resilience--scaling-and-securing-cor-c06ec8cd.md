---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Storage Data", "SRE Reliability", "Community Governance"]
speakers: ["Yong Tang", "DataDirect Networks", "John Belamaric", "Google"]
sched_url: https://kccncna2025.sched.com/event/27Nn5/scaling-and-securing-coredns-performance-and-resilience-yong-tang-datadirect-networks-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=Scaling+and+Securing+CoreDNS%3A+Performance+and+Resilience+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scaling and Securing CoreDNS: Performance and Resilience - Yong Tang, DataDirect Networks & John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Storage Data]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Yong Tang, DataDirect Networks, John Belamaric, Google
- Schedule: https://kccncna2025.sched.com/event/27Nn5/scaling-and-securing-coredns-performance-and-resilience-yong-tang-datadirect-networks-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=Scaling+and+Securing+CoreDNS%3A+Performance+and+Resilience+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scaling and Securing CoreDNS: Performance and Resilience.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Nn5/scaling-and-securing-coredns-performance-and-resilience-yong-tang-datadirect-networks-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=Scaling+and+Securing+CoreDNS%3A+Performance+and+Resilience+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RodoZHYEXTY
- YouTube title: Scaling and Securing CoreDNS: Performance and Resilience - Yong Tang & John Belamaric
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scaling-and-securing-coredns-performance-and-resilience/RodoZHYEXTY.txt
- Transcript chars: 20712
- Keywords: coding, actually, server, socket, little, itself, plug-in, change, multisocket, vendors, record, significant, discuss, plugin, session, maintainer, around, feature

### Resumo baseado na transcript

I know it's the last day and it's almost the end of the Kubicon, so it's a little tough to to come here. Uh my co-speaker John Balmer, he unfortunately cannot attend this session. So since then has been adopted and uh has been added as a default DNS server for Kubernetes that triggered the explosive growth of adoption. this year we added one more maintainer that's from v uh he is from Finland that demonstrate coordinates as outreach to uh to around the world uh village John uh several months ago as a maintainer he made significant change to security he contributed to There are also some other features like multiclass support for kubernetes clin uh several uh special features like a prefer option in low balance plugin as well as a fall through support in gc and four five plugin. Uh as I mentioned just moments ago, we found a couple of security vulnerabilities by our newly uh new maintainer.

### Excerpt da transcript

Okay, so let's get started. First of all, thanks for coming to this session. I know it's the last day and it's almost the end of the Kubicon, so it's a little tough to to come here. But my name is Yan Tong. I'm a maintainer of cords project. Uh my co-speaker John Balmer, he unfortunately cannot attend this session. So I'm going to host this session on my own. Uh let's get started. Uh in today's session, I'm going to discuss about several topics. First I'm going to introduce a little uh little background about the coding as project itself. Uh I'm going to discuss about what what has been happened for the past year and the different update as well as the releases. uh then I'm going to go deep dive into coding project discuss about how to screening app uh especially for virtual schooling of the performance with the newly added multi multis socket plug-in uh and also I'm going to discuss about the service discovery with poding uh especially how can be can be a single source of tools to sync up with different cloud vendors for DS record uh finally uh I'm going to discuss about the uh community involvement how you might be able to help coding as a project.

Uh as many of you know cordinas is a flex server written in go uh it has been there for quite few years. It it started around 2016 at the beginning it was uh actually it was a fork of caddy web server. uh over the years we make a uh significant change to convert the uh cadis ATP traffic into UTP traffic processing. Uh we also add a lot of features uh over the years. Uh one of the signal feature is about the Kubernetes integration. So since then has been adopted and uh has been added as a default DNS server for Kubernetes that triggered the explosive growth of adoption. uh because of the growth of Kubernetes itself. The one of the biggest uh uh advantage of coding as is coding as it's plug-in based. So which means it can be easily extended. Uh in other word if you have a need for a new feature and the feature is not available in current coordinate project uh you actually can just write a plug-in yourself with a minimum line of Golan Golan code. >> [snorts] >> Uh in fact with uh with today's AI you probably can even do it on your own even if you don't know anything about colon you can give it a try for sure [snorts] uh the coding as as many of you know it's a DNS server uh first and foremost a DNS server so it supports uh DNS protocol but it also support DNS over other protocol like DS over to DNS over gc and D
