---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Visualization Dashboards", "Community"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/managing-prometheus-in-a-security-focused-environment-linux-monitoring-at-huk-coburg/
youtube_url: https://www.youtube.com/watch?v=qwWw41LEoSU
youtube_search_url: https://www.youtube.com/results?search_query=Managing+Prometheus+in+a+Security-focused+Environment+--+Linux+Monitoring+at+HUK-COBURG+PromCon+2019
video_match_score: 1.025
status: video-found
---

# Managing Prometheus in a Security-focused Environment -- Linux Monitoring at HUK-COBURG

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Visualization Dashboards]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/managing-prometheus-in-a-security-focused-environment-linux-monitoring-at-huk-coburg/
- YouTube: https://www.youtube.com/watch?v=qwWw41LEoSU

## Resumo

Speaker: Christian Hoffmann Prometheus offers lots of features and flexibility which often leaves newcomers with lots of open questions: Which service discovery to use? How to secure access to metrics? Which architecture to implement?

## Abstract oficial

Speaker: Christian Hoffmann

Prometheus offers lots of features and flexibility which often leaves newcomers with lots of open questions: Which service discovery to use? How to secure access to metrics? Which architecture to implement? In order to provide some input back to the community, this talk will outline how we run Prometheus at HUK-COBURG in order to provide a multi-tenant turn-key monitoring experience in a security-focused environment. It covers basic decisions like scrape intervals and service discovery and extends to the implementation of encrypted and authenticated connections to monitoring targets using sshified and team-aware access to Prometheus/Grafana access via prometheus-filter-proxy.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/managing-prometheus-in-a-security-focused-environment-linux-monitoring-at-huk-coburg/
- YouTube: https://www.youtube.com/watch?v=qwWw41LEoSU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qwWw41LEoSU
- YouTube title: PromCon EU 2019: Managing Prometheus in a Security-focused Environment Linux Monitoring @ HUK-COBURG
- Match score: 1.025
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/managing-prometheus-in-a-security-focused-environment-linux-monitoring/qwWw41LEoSU.txt
- Transcript chars: 20744
- Keywords: prometheus, monitoring, server, servers, target, access, actual, metrics, exporter, puppet, management, custom, actually, application, central, second, exporters, process

### Resumo baseado na transcript

[Music] so hello everyone my name is Kristen Hoffman and before I actually dive into the technical part of my talk I've got a quick question who has heard of Conway's law ok surprisingly much people I'm still going to give my interpretation of Conway's law it basically says the system designs are going to resemble the organizational structures at some point in time so this is why I'm going to give a short introduction into the structure of our company which is the cool book we are a German

### Excerpt da transcript

[Music] so hello everyone my name is Kristen Hoffman and before I actually dive into the technical part of my talk I've got a quick question who has heard of Conway's law ok surprisingly much people I'm still going to give my interpretation of Conway's law it basically says the system designs are going to resemble the organizational structures at some point in time so this is why I'm going to give a short introduction into the structure of our company which is the cool book we are a German influence company targeted as consumers we are the Lockett largest kauri ensure efficient you know consumers we've got about 12 million customers and 10,000 employees within October there are multiple departments even multiple IT related departments and we've got about 800 people working there in IT related shops so we are certainly not some kind of startup rather we have lots of teams lots of policies lots of regulatory stuff high data security policies and so on one of these IT related departments is the Linux platform development team and we would describe ourselves as some kind of managed infrastructure as a service provider so we provide Linux machines to our internal customers and we manage around 900 service based on wretched Enterprise Linux these services are distributed across two main datacenters I am one of the 10 people in exactly this team I join in 2016 and I would describe myself as some kind of Linux and open source and fields and SUSE yes so much for the organizational part where I work we've got lots of other teams as I said so we've got application owners who run databases who run rep servers who run insurance software and these application owners are the ones who use our Linux servers as the base we've also got an dedicated operations team which handle the on-call situations which I'm going to describe later so now let's dive into the actual technical parts I'm going to describe our Prometheus setup how we run it and what our basic configuration looks like but I'm going to focus on the parts where I think our separate setup is special so let's start with scraping or with the actual Prometheus service when we started we thought about how many Prometheus servers are we going to run and where should we place them the common recommendation seems to be run your Prometheus service as close to the monitoring target as possible but what does close actually mean we thought about this and we came up with multiple ideas what this could mean we first thought abo
