---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Performance"
themes: ["SRE Reliability"]
speakers: ["Vincent Sevel", "Lombard Odier SA"]
sched_url: https://kccnceu2022.sched.com/event/ytkd/how-lombard-odier-deployed-vpa-to-increase-resource-usage-efficiency-vincent-sevel-lombard-odier-sa
youtube_search_url: https://www.youtube.com/results?search_query=How+Lombard+Odier+Deployed+VPA+to+Increase+Resource+Usage+Efficiency+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Lombard Odier Deployed VPA to Increase Resource Usage Efficiency - Vincent Sevel, Lombard Odier SA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Vincent Sevel, Lombard Odier SA
- Schedule: https://kccnceu2022.sched.com/event/ytkd/how-lombard-odier-deployed-vpa-to-increase-resource-usage-efficiency-vincent-sevel-lombard-odier-sa
- Busca YouTube: https://www.youtube.com/results?search_query=How+Lombard+Odier+Deployed+VPA+to+Increase+Resource+Usage+Efficiency+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Lombard Odier Deployed VPA to Increase Resource Usage Efficiency.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytkd/how-lombard-odier-deployed-vpa-to-increase-resource-usage-efficiency-vincent-sevel-lombard-odier-sa
- YouTube search: https://www.youtube.com/results?search_query=How+Lombard+Odier+Deployed+VPA+to+Increase+Resource+Usage+Efficiency+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eAAio3KFm6w
- YouTube title: How Lombard Odier Deployed VPA to Increase Resource Usage Efficiency - Vincent Sevel
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-lombard-odier-deployed-vpa-to-increase-resource-usage-efficiency/eAAio3KFm6w.txt
- Transcript chars: 28493
- Keywords: workload, cluster, request, resources, memory, recommendation, resource, actually, basically, situation, capacity, worker, working, another, workloads, startup, context, starting

### Resumo baseado na transcript

today we're going to talk about uh resource efficiency in the context of allocation in a kubernetes cluster hi my name is vincent saval i'm working for a company called lombardier i'm an architect i'm i'm involved in a cross-unit team called platform ops which aims at delivering uh the platform as a product and in that context i'm involved in different uh projects uh i've been involved in openshift for quite some time now and specifically deployment on openshift and lately i've been involved in uh um our deployment

### Excerpt da transcript

today we're going to talk about uh resource efficiency in the context of allocation in a kubernetes cluster hi my name is vincent saval i'm working for a company called lombardier i'm an architect i'm i'm involved in a cross-unit team called platform ops which aims at delivering uh the platform as a product and in that context i'm involved in different uh projects uh i've been involved in openshift for quite some time now and specifically deployment on openshift and lately i've been involved in uh um our deployment of kafka on the openshift platform plus the uh the corpus application framework all right so lombardia is a private bank based in switzerland and uh we've got the traditional lines of businesses that you would expect and plus something that we call technology for banking what we're doing is that we develop internally our own car banking system which we make available to the bank itself obviously but to other external uh then in that context we represent our code banking system so that we can operate uh their activity from our data centers based in in switzerland uh so we have uh four i mean traditional functional development streams uh and a very modular uh architecture that was started 25 years ago uh with many technology uh the last 15 years we invested a lot on on java but that's not the indian the only technology and uh we've got a lot of flexibility in our system thanks to this to this architecture but a few challenges as well all right in 2020 we started a large modernization initiative called gx where we're looking at the functional side but also at the technical side and we started introducing new technology openshift being one of the first one so the story uh starts probably a year and a half ago when we were starting to ramp up our workload on our kubernetes cluster and we started seeing this kind of message uh a little bit too often um then well basically there were two reasons for this uh the first reason is the was the uh the the cluster we were using was pretty small uh and the the workload was starting to pile up but the other reason was we did not have a good understanding about how resource allocation works inside the kubernetes cluster so um for some time we try to solve that with extra capacity that we were adding to the cluster but that that didn't get us very far eventually we are actually to i mean handle the handle the problem all right so what we're going to talk about today is optimizing placement of pods in a cluster so
