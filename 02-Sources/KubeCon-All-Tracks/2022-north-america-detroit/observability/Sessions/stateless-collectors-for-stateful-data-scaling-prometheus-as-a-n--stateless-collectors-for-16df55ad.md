---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["AI ML", "Observability", "Storage Data", "SRE Reliability"]
speakers: ["Danny Clark", "Google"]
sched_url: https://kccncna2022.sched.com/event/182IV/stateless-collectors-for-stateful-data-scaling-prometheus-as-a-node-agent-danny-clark-google
youtube_search_url: https://www.youtube.com/results?search_query=Stateless+Collectors+For+Stateful+Data%3A+Scaling+Prometheus+As+a+Node+Agent+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Stateless Collectors For Stateful Data: Scaling Prometheus As a Node Agent - Danny Clark, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Danny Clark, Google
- Schedule: https://kccncna2022.sched.com/event/182IV/stateless-collectors-for-stateful-data-scaling-prometheus-as-a-node-agent-danny-clark-google
- Busca YouTube: https://www.youtube.com/results?search_query=Stateless+Collectors+For+Stateful+Data%3A+Scaling+Prometheus+As+a+Node+Agent+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Stateless Collectors For Stateful Data: Scaling Prometheus As a Node Agent.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IV/stateless-collectors-for-stateful-data-scaling-prometheus-as-a-node-agent-danny-clark-google
- YouTube search: https://www.youtube.com/results?search_query=Stateless+Collectors+For+Stateful+Data%3A+Scaling+Prometheus+As+a+Node+Agent+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yk2aaAyxgKw
- YouTube title: Stateless Collectors For Stateful Data: Scaling Prometheus As a Node Agent - Danny Clark, Google
- Match score: 0.965
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/stateless-collectors-for-stateful-data-scaling-prometheus-as-a-node-ag/yk2aaAyxgKw.txt
- Transcript chars: 31369
- Keywords: prometheus, cluster, server, namespace, resource, metrics, operator, custom, workloads, scrape, monitoring, scraping, resources, infrastructure, configuration, single, thanos, scaling

### Resumo baseado na transcript

name is Danny Clark I'm a software engineer at Google working on cloud monitoring specifically helping to build out Google Cloud managed service for Prometheus Google Cloud's managed Prometheus offering in general I'm an avid geek for observability tools distributed systems and all things Cloud native and you can reach me on Twitter and GitHub at Pinto Hutch here's an outline of what we'll be going over today first I'll give a background into conventional ways to scale Prometheus today then I'll go into the trade-offs that we were making

### Excerpt da transcript

name is Danny Clark I'm a software engineer at Google working on cloud monitoring specifically helping to build out Google Cloud managed service for Prometheus Google Cloud's managed Prometheus offering in general I'm an avid geek for observability tools distributed systems and all things Cloud native and you can reach me on Twitter and GitHub at Pinto Hutch here's an outline of what we'll be going over today first I'll give a background into conventional ways to scale Prometheus today then I'll go into the trade-offs that we were making when we were analyzing those scenarios when setting out to build a managed service I'll then go into the finer details of our operator-based approach and custom resources and conclude with some future direction of the project some prerequisites for the audience you've run and configured Prometheus before even if only a little bit and you have some familiarity with kubernetes custom resource definitions or crds and the operator pattern so what is Prometheus specifically the Prometheus server it's a metrics-based monitoring and alerting Tool and what it's really good at what it was built to do was to be deployed as a single process running as a single server running alongside your workloads specifically tailored to monitor live numeric metric data through polling or scraping and by live I mean persistence on the order of weeks as opposed to months or years of data larger instances can be scaled pretty well via fine-tuning but what Prometheus is not at least out of the box is scalable long-term storage I like to think of Prometheus more like a traditional postgres database running on a single node in your cluster as opposed to something like Cassandra running on a fleet of nodes doing talks over the network and at this point it's really become a ubiquitous for metrics infrastructure in kubernetes in fact kubernetes components themselves use Prometheus to metrics format for their monitoring so how do we deploy Prometheus on kubernetes today we use Prometheus operators that de facto standard it's battle tested foundational was one of the first kubernetes operators and how most people tend to deploy Prometheus operators using the cube Prometheus stack which gives you a Soup To Nuts monitoring infrastructure in your cluster specifically Prometheus operator AJ Prometheus ha alert manager some grafana dashboarding common metrics exporters like Cube State metrics node exporter Etc as well as some recommended Prometheus recording and
