---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Yong Tang", "Ivanti"]
sched_url: https://kccnceu2023.sched.com/event/1HyT0/scale-the-internet-with-dns-a-coredns-deep-dive-yong-tang-ivanti
youtube_search_url: https://www.youtube.com/results?search_query=Scale+the+Internet+with+DNS%3A+A+CoreDNS+Deep+Dive+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Scale the Internet with DNS: A CoreDNS Deep Dive - Yong Tang, Ivanti

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yong Tang, Ivanti
- Schedule: https://kccnceu2023.sched.com/event/1HyT0/scale-the-internet-with-dns-a-coredns-deep-dive-yong-tang-ivanti
- Busca YouTube: https://www.youtube.com/results?search_query=Scale+the+Internet+with+DNS%3A+A+CoreDNS+Deep+Dive+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Scale the Internet with DNS: A CoreDNS Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyT0/scale-the-internet-with-dns-a-coredns-deep-dive-yong-tang-ivanti
- YouTube search: https://www.youtube.com/results?search_query=Scale+the+Internet+with+DNS%3A+A+CoreDNS+Deep+Dive+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bfUzLOFwns8
- YouTube title: Scale the Internet with DNS: A CoreDNS Deep Dive - Yong Tang, Ivanti
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/scale-the-internet-with-dns-a-coredns-deep-dive/bfUzLOFwns8.txt
- Transcript chars: 30005
- Keywords: plugin, coding, several, probably, actually, request, server, company, another, source, discovery, windows, little, question, itself, configuration, cluster, session

### Resumo baseado na transcript

okay let's uh let's get started first of all thanks for everyone who joined this session my name is quoting as project young Tang is my GitHub Handle by the way if you have any questions after the session and do you want to ask you how please reach out to me in GitHub my GitHub profile also consists of my email so you can send me email as well if you like in today's session I'm going to discuss about several things first of all I'm going to give

### Excerpt da transcript

okay let's uh let's get started first of all thanks for everyone who joined this session my name is quoting as project young Tang is my GitHub Handle by the way if you have any questions after the session and do you want to ask you how please reach out to me in GitHub my GitHub profile also consists of my email so you can send me email as well if you like in today's session I'm going to discuss about several things first of all I'm going to give a brief introduction of coding as after that I will also discuss about the coding as projects Community as well as the latest update and then I will discuss about the service Discovery and the DNS especially about the how to use quoting as for service Discovery finally I will work through a goal on plugin for codeine as and show you how easy it is to write a Golan plugin for coding as in less than 100 lines of code as many of you know coding as is flex loading and server greeting in golang it has a focus on service Discovery the biggest difference between coding Us and other DNA server is that coding as has a plugin based architecture it can be easily extended what does that mean if you have any new feature or anything that you want and you are not able to find it in existing plugins you can actually write a plugin yourself as long as you know how to write and go long actually at the end of the session I will walk you through one demo plugin to show it according as has been the default DNS server since several years ago and because of that if you uh if you ever use kubernetes you'll certainly have already used according as according as uh is a DS server first and foremost so it is support DS it also supports some of the DNS related protocols like DSO TLS and DNS over grpc the latest development in DS is that there are some additional protocols like DNS over atp3 being discussed and being standardized we are working on to adding additional protocol support for the for coding asset level the biggest feature of coding as in comparison with other DNS DNS server is that the accordion has a very rich Cloud integration as you can see coding and support the different cloud data sync up with different Windows like AWS roughly three like AZ like a Google Cloud DNS the project of coding us was started by Mick jiben several years ago actually I think Nick started the project around the 2016.

it has been almost seven years so I'm going to say it's a successful project has been used widely across the cloud native ecosystem it a
