---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Wanhae Lee", "Seok-yong Hong", "Kakao Corp"]
sched_url: https://kccncna2022.sched.com/event/182G8/surviving-from-endless-issues-coming-from-7k+-kubernetes-clusters-wanhae-lee-seok-yong-hong-kakao-corp
youtube_search_url: https://www.youtube.com/results?search_query=Surviving+From+Endless+Issues+Coming+From+7K%2B+Kubernetes+Clusters+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Surviving From Endless Issues Coming From 7K+ Kubernetes Clusters - Wanhae Lee & Seok-yong Hong, Kakao Corp

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Wanhae Lee, Seok-yong Hong, Kakao Corp
- Schedule: https://kccncna2022.sched.com/event/182G8/surviving-from-endless-issues-coming-from-7k+-kubernetes-clusters-wanhae-lee-seok-yong-hong-kakao-corp
- Busca YouTube: https://www.youtube.com/results?search_query=Surviving+From+Endless+Issues+Coming+From+7K%2B+Kubernetes+Clusters+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Surviving From Endless Issues Coming From 7K+ Kubernetes Clusters.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182G8/surviving-from-endless-issues-coming-from-7k+-kubernetes-clusters-wanhae-lee-seok-yong-hong-kakao-corp
- YouTube search: https://www.youtube.com/results?search_query=Surviving+From+Endless+Issues+Coming+From+7K%2B+Kubernetes+Clusters+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dMwQEUl9IZg
- YouTube title: Surviving From Endless Issues Coming From 7K+ Kubernetes Clusters - Wanhae Lee & Seok-yong Hong
- Match score: 0.911
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/surviving-from-endless-issues-coming-from-7k-kubernetes-clusters/dMwQEUl9IZg.txt
- Transcript chars: 16305
- Keywords: cluster, clusters, developers, issues, detect, access, thousand, scripts, detector, question, developer, called, in-house, saying, handle, thanks, coming, korean

### Resumo baseado na transcript

hi everyone [Music] thank you thank you for attending our talk on Surviving from Andrew's issue coming from 7 000 plus kubernetes clusters first of all I'm very excited to be here because it's my first time abroad in three years since covid-19 pandemic my Korean name is but you can call me or just Dennis I'm A Cloud native cell reader at cacao developing a private cloud and I'm Juan here I'm also from Seoul South of South Korea and I'm also working as a cloud engineer at cacao

### Excerpt da transcript

hi everyone [Music] thank you thank you for attending our talk on Surviving from Andrew's issue coming from 7 000 plus kubernetes clusters first of all I'm very excited to be here because it's my first time abroad in three years since covid-19 pandemic my Korean name is but you can call me or just Dennis I'm A Cloud native cell reader at cacao developing a private cloud and I'm Juan here I'm also from Seoul South of South Korea and I'm also working as a cloud engineer at cacao Corporation and first time in North America and cupcan also for cook corn as a speaker hello despite the enormous size of kubernetes clusters I believe many of us here do not know what company this is Cacao is the Mobile Life platform companies that serve messenger portal Bank Mobility Commerce web terms and more we cannot say everything here so if you're curious visit kakaokov.com for more information one thing in common is that all of them are internet service that need a server as you can guess most of the service in cacao are running in kubernetes now we started our transport from Apache methods to kubernetes in 2080 and 99 was complete this year when we decide to use kubernetes there are many concerns about how to provide kubernetes to in-house Developers the biggest consolation in adapting kubernetes was whether to provide a single Raji cluster as a talent for namespace or provides separate clusters for each organization or service we consider various factors such as close to management resource efficiency security freedom of development extra in conclusion we decide to provide lots of small clusters because isolation and security guarantees are essential requirements for compliance so we developed our own private kubernetes service to provide the kubernetes cluster to in-house development developers you know automated way is called dkos it only take it only takes three steps to get on new kubernetes clusters login set cluster names and select region and done and this newer we will create kubernetes clusters not only in cacao's private clouds but only about also in public clouds such as AWS delivering a kubernetes cluster in automate way while ensuring High isolation and freedom through self-service has about good news and bad news good news is the number of kubernetes clusters grow grows successfully and more than seven thousand plus clusters are operated bad news is so deep our Encore issue are we have moved the clouds successfully by delivering automated kubernetes service t
