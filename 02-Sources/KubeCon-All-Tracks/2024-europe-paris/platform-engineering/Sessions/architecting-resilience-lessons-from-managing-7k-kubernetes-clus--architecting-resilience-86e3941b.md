---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Kwanghun Choi", "Gyutae Bae", "Kakao"]
sched_url: https://kccnceu2024.sched.com/event/1YeLc/architecting-resilience-lessons-from-managing-7k+-kubernetes-clusters-at-scale-kwanghun-choi-gyutae-bae-kakao
youtube_search_url: https://www.youtube.com/results?search_query=Architecting+Resilience%3A+Lessons+from+Managing+7K%2B+Kubernetes+Clusters+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Architecting Resilience: Lessons from Managing 7K+ Kubernetes Clusters at Scale - Kwanghun Choi & Gyutae Bae, Kakao

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Kwanghun Choi, Gyutae Bae, Kakao
- Schedule: https://kccnceu2024.sched.com/event/1YeLc/architecting-resilience-lessons-from-managing-7k+-kubernetes-clusters-at-scale-kwanghun-choi-gyutae-bae-kakao
- Busca YouTube: https://www.youtube.com/results?search_query=Architecting+Resilience%3A+Lessons+from+Managing+7K%2B+Kubernetes+Clusters+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Architecting Resilience: Lessons from Managing 7K+ Kubernetes Clusters at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLc/architecting-resilience-lessons-from-managing-7k+-kubernetes-clusters-at-scale-kwanghun-choi-gyutae-bae-kakao
- YouTube search: https://www.youtube.com/results?search_query=Architecting+Resilience%3A+Lessons+from+Managing+7K%2B+Kubernetes+Clusters+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WRACr5nXl9U
- YouTube title: Architecting Resilience: Lessons from Managing 7K+ Kubernetes Clusters at Scale
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/architecting-resilience-lessons-from-managing-7k-kubernetes-clusters-a/WRACr5nXl9U.txt
- Transcript chars: 21412
- Keywords: cluster, clusters, developers, traffic, single, structure, center, millisecond, latency, however, manage, multiple, control, reduce, failure, question, deployed, running

### Resumo baseado na transcript

okay hello everyone welcome everyone thank you for coming we are excited to be here at kilon this is our first time as a speaker in Paris so and lastly thank you cncf for hosting shout out to all the staff and volunteers here and let's just start so today we are going to talk about the architecting resilience and what we learn from managing over s 7,000 kubernetes clusters at scale um uh I am Quang Choy people call me honi and beside me is c yeah okay um

### Excerpt da transcript

okay hello everyone welcome everyone thank you for coming we are excited to be here at kilon this is our first time as a speaker in Paris so and lastly thank you cncf for hosting shout out to all the staff and volunteers here and let's just start so today we are going to talk about the architecting resilience and what we learn from managing over s 7,000 kubernetes clusters at scale um uh I am Quang Choy people call me honi and beside me is c yeah okay um we are Cloud engineer at Kaka we developed and maintain a private kubernetes clusters as a service which runs on open stack based infrastructure yeah hi I'm C I'm a kubernetes as a service team leader in Kaka uh thank you for attending our session we hope our experience uh can help you thank you so before we start uh let me introduce our team we Pro provide kubernetes as a service in the company which is called dkos and dkos stands for data center of kaka operating system and as a member of the private kubernetes service team of kaka we manage over uh more than 7,000 clusters which consists of more than 120,000 nodes and the Clusters are deployed in different zones at Kaka we consider a single data center as a single zone and lastly we get a lot of one calls every week uh we hope developers get kubernetes up and running properly by the way we only have seven people on the team so every week is very tough so this is the sad story uh back in in October 2022 there was a data center fire and we had a significant economic and social impact because of the variety variety of services such as messenger Maps comics online shopping Banking and taxes the Koreans use every day the impact was significant since all of the services run on kaka's multiple kubernetes clusters the failure in a data center affected these multiple services so here's what really happened that day when the data center suddenly lost power all of our kubernetes notes in the data center shut down developers needed to migrate their kubernetes to a new Zone to restore Services uh however the developers didn't have time to migrate their clusters to new zones because it happens so suddenly and even if there was enough time it take some time to set up new clusters and deploy new applications set up load balancers Security checks and proxies and so on so there are a lot of things to take care of and in addition as the kubernetes notes they were down in the data center came back up it was difficult to uh determine the impact of bringing the service back
