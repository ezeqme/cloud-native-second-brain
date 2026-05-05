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
themes: ["AI ML", "Kubernetes Core", "SRE Reliability", "Community Governance"]
speakers: ["Zbynek Roubalik", "Jan Wozniak", "Kedify"]
sched_url: https://kccncna2025.sched.com/event/27NmY/efficient-kubernetes-autoscaling-news-challenges-and-best-practices-with-keda-zbynek-roubalik-jan-wozniak-kedify
youtube_search_url: https://www.youtube.com/results?search_query=Efficient+Kubernetes+Autoscaling%3A+News%2C+Challenges%2C+and+Best+Practices+With+KEDA+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Efficient Kubernetes Autoscaling: News, Challenges, and Best Practices With KEDA - Zbynek Roubalik & Jan Wozniak, Kedify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Zbynek Roubalik, Jan Wozniak, Kedify
- Schedule: https://kccncna2025.sched.com/event/27NmY/efficient-kubernetes-autoscaling-news-challenges-and-best-practices-with-keda-zbynek-roubalik-jan-wozniak-kedify
- Busca YouTube: https://www.youtube.com/results?search_query=Efficient+Kubernetes+Autoscaling%3A+News%2C+Challenges%2C+and+Best+Practices+With+KEDA+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Efficient Kubernetes Autoscaling: News, Challenges, and Best Practices With KEDA.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27NmY/efficient-kubernetes-autoscaling-news-challenges-and-best-practices-with-keda-zbynek-roubalik-jan-wozniak-kedify
- YouTube search: https://www.youtube.com/results?search_query=Efficient+Kubernetes+Autoscaling%3A+News%2C+Challenges%2C+and+Best+Practices+With+KEDA+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-frz79uMCgo
- YouTube title: Efficient Kubernetes Autoscaling: News, Challenges, and Best Practi... Zbynek Roubalik & Jan Wozniak
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/efficient-kubernetes-autoscaling-news-challenges-and-best-practices-wi/-frz79uMCgo.txt
- Transcript chars: 34727
- Keywords: scaling, metrics, scaled, prometheus, please, replicas, specify, metric, object, actually, resource, traffic, custom, autoscaling, little, workloads, workload, backend

### Resumo baseado na transcript

And is there anyone who doesn't know what ka is or maybe just heard about it and don't know the details. So uh I will try to do very short introduction to keta very short one for the people who don't know what it is. So from the beginning we try to reuse as much concepts from Kubernetes as possible. Ka operates on a bunch of custom resources uh and it manages the workloads, scale them and also scale to zero. It opens the connections to the external services that we are using for uh the scanning decisions and uh then it forwards metrics and the metrics are been uh are being consumed by HPA controller in Kubernetes API. So the HPA as it would like to scale it asks keta metric server uh for an update on the metrics.

### Excerpt da transcript

Hello and welcome to our session about uh Keta. Uh my name is Jan. Uh I'm a software engineer. Uh also a recent addition to the KDA maintainer squad. And I work for this guy, a man with unpronouncable name. So hello guys. Uh I'm glad to see so many faces here. My name is Binak. Very hard to pronounce check name. Apologies for that. Uh I'm also Ka maintainer. I'm with the project since the inception. And I'm also founder and CTO at Kify. At Kify we provide enterprise version of Ka. All right let's start it. So um actually before we start so we introduce ourselves. So maybe would be nice to know a little bit more about you you folks. So may I ask you who runs Kadine production? Is there anyone? Nice. Nice. Is there anyone who is considering running Kadine production? Okay. Nice. And is there anyone who doesn't know what ka is or maybe just heard about it and don't know the details. All right, I can see bunch of folks. Great. So we have a great coverage. So uh I will try to do very short introduction to keta very short one for the people who don't know what it is.

We'll briefly cover new features and then we'll spend some time on best practices and some challenges that you can face when you are going to do autoscaling. So what is kada? With KDA, we tries to make Kubernetes autoscaling as simple as possible. So, we allow you to scale your uh your workloads or schedule any Kubernetes jobs based on events, custom metrics, not just CPU or memory uh consumption and metrics like standard HPA on Kubernetes. Uh we have I believe 65 plus maybe almost close to 80 uh integrated event sources. So, the event source is the source for the scaling decision, Prometheus and Kafka. And a fun fact uh we usually like to pronounce it kada not kada uh because kada in our language that actually means manure. So >> yeah yeah yeah please do that or whatever you want but please don't use ka ka no ka is the best one. All right uh we have a awesome community we have a lot of a lot of contributors. Um there is a if you are a user we have also like the survey which help us understand what's missing in the project or what not.

So please fill it if if possible if not it's fine. Uh so what is KDA? I will try to do KDA in maybe two minutes. So please don't take >> All right. All right. Yeah it never happened since two minutes. So >> all right let's see. So KA uh is obviously built on top of Kubernetes. So from the beginning we try to reuse as much concepts from Kubernetes as possible. we don
