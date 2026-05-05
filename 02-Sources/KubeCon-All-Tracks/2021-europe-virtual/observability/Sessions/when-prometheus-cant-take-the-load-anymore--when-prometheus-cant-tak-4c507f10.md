---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Observability"
themes: ["Observability"]
speakers: ["Liron Cohen", "Riskified"]
sched_url: https://kccnceu2021.sched.com/event/iE4q/when-prometheus-cant-take-the-load-anymore-liron-cohen-riskified
youtube_search_url: https://www.youtube.com/results?search_query=When+Prometheus+Can%E2%80%99t+Take+the+Load+Anymore+CNCF+KubeCon+2021
slides: []
status: parsed
---

# When Prometheus Can’t Take the Load Anymore - Liron Cohen, Riskified

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Virtual / Virtual
- Speakers: Liron Cohen, Riskified
- Schedule: https://kccnceu2021.sched.com/event/iE4q/when-prometheus-cant-take-the-load-anymore-liron-cohen-riskified
- Busca YouTube: https://www.youtube.com/results?search_query=When+Prometheus+Can%E2%80%99t+Take+the+Load+Anymore+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre When Prometheus Can’t Take the Load Anymore.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4q/when-prometheus-cant-take-the-load-anymore-liron-cohen-riskified
- YouTube search: https://www.youtube.com/results?search_query=When+Prometheus+Can%E2%80%99t+Take+the+Load+Anymore+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=parm7--PQIE
- YouTube title: When Prometheus Can’t Take the Load Anymore - Liron Cohen, Riskified
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/when-prometheus-cant-take-the-load-anymore/parm7--PQIE.txt
- Transcript chars: 25514
- Keywords: storage, prometheus, cortex, thanos, components, queries, architecture, metrics, performance, samples, multiple, series, solution, push-based, object, long-term, caching, remote

### Resumo baseado na transcript

hi everyone my name is lyron cohen and today i will talk about some of the different solutions for achieving highly available long-term scalable prometheus a little bit about myself before we start i have been a devops and site reliability engineer for the past seven years before my current job as an sre at riskyfied i was a devops consultant in multiple companies and when i'm not working or studying i enjoy traveling diving and basically anything water related as you can probably tell by my happy face in

### Excerpt da transcript

hi everyone my name is lyron cohen and today i will talk about some of the different solutions for achieving highly available long-term scalable prometheus a little bit about myself before we start i have been a devops and site reliability engineer for the past seven years before my current job as an sre at riskyfied i was a devops consultant in multiple companies and when i'm not working or studying i enjoy traveling diving and basically anything water related as you can probably tell by my happy face in this photo so before we will dive into the different solutions we decided to check let's briefly talk about the issues we had so what we started with was an architecture used by a lot of people and companies two prometheus servers that scrapes matrix from the same targets both monitor the same sets of jobs for high availability where each prometheus has its own local disk for durability we're running on aws so in our case it's ebs what are the issues with this architecture well it's not scalable it's not really highly available if one prometheus is going down or in the process of rolling update there will be gaps in the data we will see for example in grafana so we can't really load balance between the different instances there is no centralization no global view of data if for example we want to query multiple clusters we can't and there is no long term storage of data we can configure a retention of multiple years as an example this way so we knew we needed a solution for all of these issues and we knew that there are some tools that can help us eventually we were left with three potential tools we decided we wanted to choose from number three cortex and tongues it's important to note that i'm not representing any of these projects i'm not part of the maintainers of none of them we simply wanted to examine their different architectures to understand what each tool can offer what are the advantages and disadvantages of each soul and how they differ from each other why did we want to know this all these projects have some similarities they are all written in go open source projects that are compatible with prometheus and they all offer us a solution that can suit the issues we just talked about all these projects offers a long-term storage for our metrics a global view of data they are horizontally scalable and making sure our metrics are highly available and durable all these solutions provide replication of time series data across regions and or availab
