---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Storage Data", "Kubernetes Core", "SRE Reliability"]
speakers: ["Irvin Lim", "Hailin Xiang", "Shopee"]
sched_url: https://kccnceu2023.sched.com/event/1HyWO/colocate-hadoop-yarn-with-kubernetes-to-save-massive-costs-on-big-data-irvin-lim-hailin-xiang-shopee
youtube_search_url: https://www.youtube.com/results?search_query=Colocate+Hadoop+YARN+with+Kubernetes+to+Save+Massive+Costs+on+Big+Data+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Colocate Hadoop YARN with Kubernetes to Save Massive Costs on Big Data - Irvin Lim & Hailin Xiang, Shopee

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Irvin Lim, Hailin Xiang, Shopee
- Schedule: https://kccnceu2023.sched.com/event/1HyWO/colocate-hadoop-yarn-with-kubernetes-to-save-massive-costs-on-big-data-irvin-lim-hailin-xiang-shopee
- Busca YouTube: https://www.youtube.com/results?search_query=Colocate+Hadoop+YARN+with+Kubernetes+to+Save+Massive+Costs+on+Big+Data+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Colocate Hadoop YARN with Kubernetes to Save Massive Costs on Big Data.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyWO/colocate-hadoop-yarn-with-kubernetes-to-save-massive-costs-on-big-data-irvin-lim-hailin-xiang-shopee
- YouTube search: https://www.youtube.com/results?search_query=Colocate+Hadoop+YARN+with+Kubernetes+to+Save+Massive+Costs+on+Big+Data+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Dqcc9fTfnJs
- YouTube title: Colocate Hadoop YARN with Kubernetes to Save Massive Costs on Big Data - Irvin Lim & Hailin Xiang
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/colocate-hadoop-yarn-with-kubernetes-to-save-massive-costs-on-big-data/Dqcc9fTfnJs.txt
- Transcript chars: 38832
- Keywords: actually, metrics, resource, product, resources, manager, memory, workloads, question, company, support, clusters, utilization, priority, cluster, hadoop, business, machine

### Resumo baseado na transcript

hi everyone yeah so uh good morning uh we're excited to start our sharing today and I hope everyone's settled down and making yourself comfortable so uh we're excited to start sharing today on how we co-locate Hadoop yarn jobs with kubernetes in order to save massive costs on Big Data my name is Irvin and with menu today is my teammate hylin yeah yeah and we're both platform Engineers working in the engineering infrastructure team at shopee so uh before we start I just I just want to give section we'll look at how we can isolate noisy neighbors or in other words we'll explore how we can minimize the effects caused by co-locating batch workloads on the same node as product services to resolve the problem that Highland has Illustrated earlier so before I proceed any further we first need to have a system to categorize workloads based on their latency requirements we found that the original kubernetes Port Qs classes were insufficient to represent these latency requirements and so we extended them to introduce a few new

### Excerpt da transcript

hi everyone yeah so uh good morning uh we're excited to start our sharing today and I hope everyone's settled down and making yourself comfortable so uh we're excited to start sharing today on how we co-locate Hadoop yarn jobs with kubernetes in order to save massive costs on Big Data my name is Irvin and with menu today is my teammate hylin yeah yeah and we're both platform Engineers working in the engineering infrastructure team at shopee so uh before we start I just I just want to give a quick introduction of our company so we are from shopee an e-commerce platform that operates across multiple markets across the world today we are the leading e-commerce platform in Southeast Asia Taiwan and Brazil we are also the number one shopping app in these markets by average monthly active users as well as total time spending app we continue to grow in scale so we can build on our strong brand recognition across the region so why did I just share all of this with you guys today so as an e-commerce platform I cannot understand the importance of robust and scalable infrastructure to support our fast growth and large user base across the world we have completely embraced kubernetes within our company running hundreds of thousands of clusters oh sorry hundreds of thousands of ports across tens of thousands of nodes within hundreds of clusters on more than 10 data centers spanning across the globe as we support the growth of the business we expect these numbers to keep increasing in the months and years ahead so now that introductions are out of the way let me dive right into the problem that we want to share with you guys today so one of the largest and most important days at shopee are what we call campaign days we run and operate several large campaigns every year including the 99 super shopping day in September as well as the 11 11 big sale in November as you might expect supporting an e-commerce platform's poses several unique and difficult challenges for us in order to support millions of active users on our platform we need huge amounts of compute resources large numbers of users tend to log on to shopee at the same time since many of our larger markets are in the same few time zones around the region during low volume periods at night we also experience rather deep trials in which large amounts of our resources remain idle and underutilized so to make things even worse during large campaigns like mentioned in on the previous slide we also have even higher Peak
