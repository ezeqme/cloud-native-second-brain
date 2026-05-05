---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Operations + Performance"
themes: ["Observability", "GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Orcun Berkem", "Alan Protasio", "AWS"]
sched_url: https://kccnceu2025.sched.com/event/1tx83/taming-50-billion-time-series-operating-global-scale-prometheus-deployments-on-kubernetes-orcun-berkem-alan-protasio-aws
youtube_search_url: https://www.youtube.com/results?search_query=Taming+50+Billion+Time+Series%3A+Operating+Global-Scale+Prometheus+Deployments+on+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taming 50 Billion Time Series: Operating Global-Scale Prometheus Deployments on Kubernetes - Orcun Berkem & Alan Protasio, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Observability]], [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Orcun Berkem, Alan Protasio, AWS
- Schedule: https://kccnceu2025.sched.com/event/1tx83/taming-50-billion-time-series-operating-global-scale-prometheus-deployments-on-kubernetes-orcun-berkem-alan-protasio-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+50+Billion+Time+Series%3A+Operating+Global-Scale+Prometheus+Deployments+on+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taming 50 Billion Time Series: Operating Global-Scale Prometheus Deployments on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx83/taming-50-billion-time-series-operating-global-scale-prometheus-deployments-on-kubernetes-orcun-berkem-alan-protasio-aws
- YouTube search: https://www.youtube.com/results?search_query=Taming+50+Billion+Time+Series%3A+Operating+Global-Scale+Prometheus+Deployments+on+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OqLpKJwKZlk
- YouTube title: Taming 50 Billion Time Series: Operating Global-Scale Prometheus Dep... Orcun Berkem & Alan Protasio
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taming-50-billion-time-series-operating-global-scale-prometheus-deploy/OqLpKJwKZlk.txt
- Transcript chars: 23842
- Keywords: cortex, prometheus, cluster, customer, single, deployment, change, tenants, multiple, everything, deploy, changes, inside, process, scaling, customers, region, capacity

### Resumo baseado na transcript

Uh today we are going to talk about uh operating global scale Prometheus deployments on Kubernetes. Uh I'm Orchin uh principal engineer at AWS uh focusing on open source observability solutions and I'm Alan uh I'm also software engineer at AWS and a cortex maintainer. Uh we wanted to provide a fully managed serverless Prometheus compatible monitoring service by AWS that is scalable, highly available, integrated with AWS services, secure, supports IM authorization as well as data encryption and it can support data retention up to multiple years. So Prometheus is an open-source purpose-built uh time series database that comes with a very powerful query language called PromQL. uh it enables analytical query capabilities on your time series data but uh also integrates really well with Kubernetes and it's widely adopted format and supports wide range of exporters uh in the community. uh meaning uh if you have an ingest heavy rightheavy uh workload uh then your uh queries are going to take a hit or your alarming uh alerting and rule engine will take a hit.

### Excerpt da transcript

Well uh welcome everyone. Uh today we are going to talk about uh operating global scale Prometheus deployments on Kubernetes. Uh I'm Orchin uh principal engineer at AWS uh focusing on open source observability solutions and I'm Alan uh I'm also software engineer at AWS and a cortex maintainer. All right, we have uh a lot of challenges operating at global scale. Uh and on the bottom right side uh you can see a postit that I prepared when I joined the team two and a half years ago about the challenges we had back then and a priority order. We are not going to talk through every single one of the problems and challenges but a subset of the challenges are going to act as our rough agenda today. We're going to touch base on availability, multi-tenency, uh blast radius reduction, operating at global scale and Kubernetes complexity. Before we dive in, let's rewind a bit. Uh in about let's uh talk through uh talk about the ecosystem and how the ecosystem has evolved. Uh so in 2012 uh Prometheus was uh started uh and then open sourced in uh 2015.

uh Cortex project, a Prometheus compatible uh scalable uh open source project released shortly after and we released uh manage Prometheus uh by Amazon um at 2020. We wanted to take away the operational uh burden of uh handling the infrastructure from the users. Uh we have an open-source first uh tenant. Uh so any improvement that we do uh we contribute back to open source community and you can see that uh from our commits uh over the past few years in the cortex repository. So before we launch the service let's go through uh what we wanted to launch back in 2020. Uh we wanted to provide a fully managed serverless Prometheus compatible monitoring service by AWS that is scalable, highly available, integrated with AWS services, secure, supports IM authorization as well as data encryption and it can support data retention up to multiple years. As I mentioned earlier, we uh use Cortex under the hood. Uh but uh we can talk let's talk a little bit about uh Prometheus. So Prometheus is an open-source purpose-built uh time series database that comes with a very powerful query language called PromQL.

uh it enables analytical query capabilities on your time series data but uh also integrates really well with Kubernetes and it's widely adopted format and supports wide range of exporters uh in the community. However, uh it inherently comes with uh limitations. The primary one uh that is our concern is that it's a single machine uh an
