---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Lin Sun", "Louis Ryan", "Solo.io", "Raymond Wong", "Forbes"]
sched_url: https://kccnceu2025.sched.com/event/1tczp/istio-the-past-present-and-future-of-the-project-and-community-lin-sun-louis-ryan-soloio-raymond-wong-forbes
youtube_search_url: https://www.youtube.com/results?search_query=Istio%3A+The+Past%2C+Present+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Istio: The Past, Present and Future of the Project and Community - Lin Sun & Louis Ryan, Solo.io; Raymond Wong, Forbes

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Lin Sun, Louis Ryan, Solo.io, Raymond Wong, Forbes
- Schedule: https://kccnceu2025.sched.com/event/1tczp/istio-the-past-present-and-future-of-the-project-and-community-lin-sun-louis-ryan-soloio-raymond-wong-forbes
- Busca YouTube: https://www.youtube.com/results?search_query=Istio%3A+The+Past%2C+Present+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Istio: The Past, Present and Future of the Project and Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczp/istio-the-past-present-and-future-of-the-project-and-community-lin-sun-louis-ryan-soloio-raymond-wong-forbes
- YouTube search: https://www.youtube.com/results?search_query=Istio%3A+The+Past%2C+Present+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=poBOYc_EkpA
- YouTube title: Istio: The Past, Present and Future of the Project and Communi... Lin Sun, Louis Ryan & Raymond Wong
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/istio-the-past-present-and-future-of-the-project-and-community/poBOYc_EkpA.txt
- Transcript chars: 28797
- Keywords: gateway, ambient, traffic, waypoint, application, mesh, actually, little, obviously, running, control, gateways, started, ingress, raymond, egress, cluster, issues

### Resumo baseado na transcript

We are here talking about the ISTO project again and we're going to take you through the history of Isto and also the present of ISTO and I thought who would be the best person to talk about the present and one of our users in the community. Now I'm going to pass over to Raymond who is actually giving his first ever conference talk. A quick introduction of ambient is uh we purposefully have a two-layer architecture of ambient of the layer four layer. the layer seven layer because we have a two layer architecture we decided to bring the same familiar concept you have on the gateway to the mesh so essentially the Same envoy proxy that used to control your ingress traffic and also your egress traffic Uh this is actually one of the blog we just published recently and about TCP throughput by John how in the community you can see uh ambient has the highest throughput when we use I perform Iperf to run the performance test and what's really Uh out of the box you get MTLS you know encryption talking to services who doesn't want that observability you get Kali pre Prometheus metrics that helps you know troubleshooting any issues that you might encounter.

### Excerpt da transcript

Hello, good afternoon everybody. We are here talking about the ISTO project again and we're going to take you through the history of Isto and also the present of ISTO and I thought who would be the best person to talk about the present and one of our users in the community. So let me quickly introduce myself. Lensa I'm the head of open source at solo. I'm also a CNCF ambassador and one of the CNCF TOC member. Now I'm going to pass over to Raymond who is actually giving his first ever conference talk. Hello. Thank you. Uh I'm Raven. I'm a senior architect at Forbes. And then you get it over with as quickly as possible, right? Uh I'm Louis Ryan. I'm the CTO at Solo. I work with Lynn. Uh I've worked with Lynn for a long time. I've obviously been involved in the STO project since the very beginning and delighted to be here talking to you guys again for the eighth year in a row. So let's get this ball rolling. Awesome. So past history, me and present present and future of Isto. So we invited the founder of ISO to talk about that.

All right. Uh let's get started. So when we started Isto eight years ago, correct me if I said anything wrong, Louie, uh we set the goal, we want to project to be transparent to your application workload. And I honestly looking back I think we failed that goal for a very very long time because when we first started with ISTO um we we ask you to run the sidecar along with your application container within that same application pod right so whenever you enroll yourself your application into the mesh you have to restart whenever there's onboy CVE that comes with the proxy see you have to restart your application. So honestly looking back I really think we failed that goal eight years and for the past uh few years as well. Um so as we evolve on the ISTO project uh I think Louie uh the Google team uh along with the rest of the community plays a big role in drive is to CNCF. So one of the biggest thing with ISTO was it was holding by Google and Google owns the copyright of the ISTO project which prevents some of our adopters adopting ISTO some of our contributors contributing to ISTL.

So we were very very excited that is joined CNCF uh in 2022 and what's also exciting in the same year is we started challenging ourself how can we be more transparent to the application workload. This is when we introduced STO in ambient mode. Just quickly introduction of ambient by the way it reaches GA in Salt Lake City last year. A quick introduction of am
