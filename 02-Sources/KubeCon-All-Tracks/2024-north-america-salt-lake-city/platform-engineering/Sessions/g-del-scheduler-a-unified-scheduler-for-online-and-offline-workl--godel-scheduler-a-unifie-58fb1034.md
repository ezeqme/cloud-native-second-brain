---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Bing Li", "Yue Yin", "Lintong Jiang", "ByteDance"]
sched_url: https://kccncna2024.sched.com/event/1i7oo/godel-scheduler-a-unified-scheduler-for-online-and-offline-workloads-bing-li-yue-yin-lintong-jiang-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=G%C3%96Del+Scheduler%3A+A+Unified+Scheduler+for+Online+and+Offline+Workloads+CNCF+KubeCon+2024
slides: []
status: parsed
---

# GÖDel Scheduler: A Unified Scheduler for Online and Offline Workloads - Bing Li, Yue Yin & Lintong Jiang, ByteDance

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Bing Li, Yue Yin, Lintong Jiang, ByteDance
- Schedule: https://kccncna2024.sched.com/event/1i7oo/godel-scheduler-a-unified-scheduler-for-online-and-offline-workloads-bing-li-yue-yin-lintong-jiang-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=G%C3%96Del+Scheduler%3A+A+Unified+Scheduler+for+Online+and+Offline+Workloads+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre GÖDel Scheduler: A Unified Scheduler for Online and Offline Workloads.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oo/godel-scheduler-a-unified-scheduler-for-online-and-offline-workloads-bing-li-yue-yin-lintong-jiang-bytedance
- YouTube search: https://www.youtube.com/results?search_query=G%C3%96Del+Scheduler%3A+A+Unified+Scheduler+for+Online+and+Offline+Workloads+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PiUAdclow_4
- YouTube title: GÖDel Scheduler: A Unified Scheduler for Online and Offline Workloads - B. Li, Y. Yin, L. Jiang
- Match score: 0.957
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/g-del-scheduler-a-unified-scheduler-for-online-and-offline-workloads/PiUAdclow_4.txt
- Transcript chars: 27437
- Keywords: scheduling, resource, online, scheduler, cluster, affinity, offline, resources, reservation, topology, scheduled, workload, framework, worker, deployment, another, within, network

### Resumo baseado na transcript

hello everyone thanks for joining the session uh today we're going to talk about gerle which is a unified scheduler for online and offline workload uh yeah I'm Lon this is my teammate y uh we are from scheduling and orchestration team from B Dan uh gero actually it's a alternative uh scheduler in kubernetes cluster uh it was designed for resolve our major uh major pain points uh inhouse by dance and it was open source late 20 23 uh here's a agenda for today we're going to break we can Scale app this uh deployment and we can check the scheduling results again okay so we can see that the scaled app Parts they are directly scheduled on the exact the same previous three nodes which is two worker two and uh one

### Excerpt da transcript

hello everyone thanks for joining the session uh today we're going to talk about gerle which is a unified scheduler for online and offline workload uh yeah I'm Lon this is my teammate y uh we are from scheduling and orchestration team from B Dan uh gero actually it's a alternative uh scheduler in kubernetes cluster uh it was designed for resolve our major uh major pain points uh inhouse by dance and it was open source late 20 23 uh here's a agenda for today we're going to break it down into two part uh four parts uh first uh firstly we're going to take a high level review of girdle and uh including some backgrounds and the high level uh architecture after that we're going to work through some key features we introduce in girle and along with some uh fantastic demo uh after that we are going to cover some of the achievement we have made so far uh in both uh production and the Academia uh to wrap up this session we're going to uh cover some of the related uh future work sitting on our road map okay yeah let's take a look at the overview first uh somebody might already have the question in your mind and why do we need another scheduler since there are so many option available in the community community and why don't we just use that so yeah as I said we we designed the schedule to resolve our major point we uh faced with in the uh in bance so uh first thing first uh it is a uh infrastructure scale uh yeah let's take a look at the number together so within bance there are more than uh 500 uh large scale cluster of the world uh uh regarding about large CL large scale cluster we mean uh cluster with more than a thousand uh uh nodes and uh in the largest cluster there are there are around like 20K heterogeneous server and around 1 million pods so yeah I believe that's huge and uh from another perspective uh over 200 uh million of containerized application including both online and offline application uh ring in within our Global infrastructure every day okay here's another reason um we have heterogenous workload from different business group and uh different types of uh workload have different performance metrics so uh specifically for uh uh offline applications such as merine learning training badge jobs uh focus more on uh minimizing the completion time uh while for uh others like uh data processing video coding and streaming uh emphasize more on uh cput and uh on the other hand like on online application uh uh something like microservices inference and the rec
