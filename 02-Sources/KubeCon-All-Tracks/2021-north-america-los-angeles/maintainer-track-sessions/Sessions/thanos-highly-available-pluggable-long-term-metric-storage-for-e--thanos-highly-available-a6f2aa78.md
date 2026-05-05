---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Wiard van Rij", "Fullstaq"]
sched_url: https://kccncna2021.sched.com/event/lV8a/thanos-highly-available-pluggable-long-term-metric-storage-for-everyone-wiard-van-rij-fullstaq
youtube_search_url: https://www.youtube.com/results?search_query=Thanos%3A+Highly+Available%2C+Pluggable%2C+Long+Term+Metric+Storage+for+Everyone%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Thanos: Highly Available, Pluggable, Long Term Metric Storage for Everyone! - Wiard van Rij, Fullstaq

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Wiard van Rij, Fullstaq
- Schedule: https://kccncna2021.sched.com/event/lV8a/thanos-highly-available-pluggable-long-term-metric-storage-for-everyone-wiard-van-rij-fullstaq
- Busca YouTube: https://www.youtube.com/results?search_query=Thanos%3A+Highly+Available%2C+Pluggable%2C+Long+Term+Metric+Storage+for+Everyone%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Thanos: Highly Available, Pluggable, Long Term Metric Storage for Everyone!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV8a/thanos-highly-available-pluggable-long-term-metric-storage-for-everyone-wiard-van-rij-fullstaq
- YouTube search: https://www.youtube.com/results?search_query=Thanos%3A+Highly+Available%2C+Pluggable%2C+Long+Term+Metric+Storage+for+Everyone%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VG_TtLg84ME
- YouTube title: Thanos: Highly Available, Pluggable, Long Term Metric Storage for Everyone!- Wiard van Rij, Fullstaq
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/thanos-highly-available-pluggable-long-term-metric-storage-for-everyon/VG_TtLg84ME.txt
- Transcript chars: 19570
- Keywords: prometheus, cluster, component, basically, metrics, scraping, components, metric, server, perhaps, another, everyone, little, grafana, multiple, retention, allows, unified

### Resumo baseado na transcript

welcome los angeles and everyone online it's a crazy time but thanks so much for having me here and today i'm going to talk about thanos cncf project and the title is highly available pluggable long-term storage metric for everyone it's one of my most longest title effort for a talk really excited to talk about this first of all a little bit about myself i'm from the netherlands or holland and i'm a buzzword engineer basically i do everything that i like which really depends on the moment so

### Excerpt da transcript

welcome los angeles and everyone online it's a crazy time but thanks so much for having me here and today i'm going to talk about thanos cncf project and the title is highly available pluggable long-term storage metric for everyone it's one of my most longest title effort for a talk really excited to talk about this first of all a little bit about myself i'm from the netherlands or holland and i'm a buzzword engineer basically i do everything that i like which really depends on the moment so this can be sre or devops or at the moment observability i do this at full stack i really like open source software and especially anything related to kubernetes and on the side i do a little bit of hacking for example on hacker1 these are just things that i really like to enjoy in my spare time besides working with wood i really love to create things so now we got the basic comfort let's get started with our talk and we have to start with prometheus first i want to give you a little introduction since this is a talk for everyone i want to give you this introduction about prometheus perhaps you have heard of it perhaps you are using it i personally really love this this project it's it's a lie for uh quite a while it's heavily used especially also on kubernetes but what is it that it does well prometheus is a key player for this part this is an http page and it's surfing metrics it's just displaying text in a metric format and for example this page is actually displaying metrics about an hcsb server for example about the request duration but also about how many requests we had in total and what was the code the acp code that was for a given request and what are the counters for this and for example for an ectp web server this is pretty nice information to have because you can see for example how many 500 errors do i have and this is really nice but we want to go from such a page as this towards something like this and this is grafana and it's it's a visualization tool and what you can see here are different graphs but these graphs are are metrics plotted over time and this is really nice but we can also do different things such as alert and this is an example of an alert that we have created with prometheus and this is an alert for a high load so if the node load one is above 0.5 um well it runs into a firing state so we can get a notification that something with a metric happened and it passes some threshold and we got an alert so it's important to get a top-down view
