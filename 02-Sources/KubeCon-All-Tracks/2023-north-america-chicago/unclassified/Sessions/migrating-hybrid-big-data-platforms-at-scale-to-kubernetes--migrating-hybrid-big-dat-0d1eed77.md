---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Unclassified"
themes: ["Platform Engineering", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Sunil Govindan", "Cloudera"]
sched_url: https://kccncna2023.sched.com/event/1R2rB/migrating-hybrid-big-data-platforms-at-scale-to-kubernetes-sunil-govindan-cloudera
youtube_search_url: https://www.youtube.com/results?search_query=Migrating+Hybrid+Big+Data+Platforms+at+Scale+to+Kubernetes+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Migrating Hybrid Big Data Platforms at Scale to Kubernetes - Sunil Govindan, Cloudera

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Platform Engineering]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Sunil Govindan, Cloudera
- Schedule: https://kccncna2023.sched.com/event/1R2rB/migrating-hybrid-big-data-platforms-at-scale-to-kubernetes-sunil-govindan-cloudera
- Busca YouTube: https://www.youtube.com/results?search_query=Migrating+Hybrid+Big+Data+Platforms+at+Scale+to+Kubernetes+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Migrating Hybrid Big Data Platforms at Scale to Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rB/migrating-hybrid-big-data-platforms-at-scale-to-kubernetes-sunil-govindan-cloudera
- YouTube search: https://www.youtube.com/results?search_query=Migrating+Hybrid+Big+Data+Platforms+at+Scale+to+Kubernetes+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1NepjxK4XLM
- YouTube title: Migrating Hybrid Big Data Platforms at Scale to Kubernetes - Sunil Govindan, Cloudera
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/migrating-hybrid-big-data-platforms-at-scale-to-kubernetes/1NepjxK4XLM.txt
- Transcript chars: 32707
- Keywords: platform, engines, itself, storage, cluster, application, resource, compute, unicorn, finally, running, challenges, second, actually, mentioned, capacity, looking, factor

### Resumo baseado na transcript

it's so nice to see everyone here at Chicago I'm Sunil Goan from cloud I lead the compute platform team and Unicon scheduling team at clra I'm in this big data space for over a decade and I contribute majorly to the Unicorn schuer which is a native batch scheduler for kubernetes in various rols so in today's session I will I'll be covering the Big Data migration Journey um TOS kubernetes from cloud so let us take an example of an Enterprise um company focusing on adopting AI so

### Excerpt da transcript

it's so nice to see everyone here at Chicago I'm Sunil Goan from cloud I lead the compute platform team and Unicon scheduling team at clra I'm in this big data space for over a decade and I contribute majorly to the Unicorn schuer which is a native batch scheduler for kubernetes in various rols so in today's session I will I'll be covering the Big Data migration Journey um TOS kubernetes from cloud so let us take an example of an Enterprise um company focusing on adopting AI so they'll be looking at various categories and trying to assess the impact of the AA adoption and as you can see adopting a could increase the productivity of the R&D or generating faster content for the marketing team or even saving CS for their uh HR team as well the common underlying factor to derive such a big Improvement is nothing but data yes the data itself is the differentiating factor here and that will be helping to power the a adoption so I want to take a a peak look at the data itself and its relevance the first one is data explosion around 75% of the data is not structured and Cloud ra is managing 25 exabytes of data that is roughly around 25 20% of the overall data right and 200 trillion objects are there in uh S3 as of 2023 yes uh everyone needs access to this data as well right and all the type of application be it AI or non AI the access is um expected and we are seeing around 50x uh increase in the consumer side of um access however the question is is storing and managing the data is it enough I'll say no because you need to get the best value proposition out of the data otherwise it doesn't matter so in order to do that you need some powerful engines that can help to uh get that insights so here's a quick overview uh about the the data life cycle and the use cases that cloud usually solves uh using the Big Data engines so the first use case as you see it's a collect that nothing but the data injection so this enables the customers to streams uh the data into their data product by uh providing capabilities such as like analyzing the streaming data with complex patterns or similar um actions and gain some uh in out of that and one of the examples could be risk analysis or fraud detection so in the data engineering that a second use case uh it provides a tool set uh for ETL uh um processes and it helps to to uh cover a large set of users the third one is Warehouse it enables actually um business intelligence use cases and it helps to make sure that you get do the righ
