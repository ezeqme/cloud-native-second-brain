---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Christopher Bradford", "DataStax", "Ty Morton", "Google"]
sched_url: https://kccncna2021.sched.com/event/lV2m/taking-your-database-beyond-the-border-of-a-single-kubernetes-cluster-christopher-bradford-datastax-ty-morton-google
youtube_search_url: https://www.youtube.com/results?search_query=Taking+Your+Database+Beyond+the+Border+of+a+Single+Kubernetes+Cluster+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Taking Your Database Beyond the Border of a Single Kubernetes Cluster - Christopher Bradford, DataStax & Ty Morton, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Christopher Bradford, DataStax, Ty Morton, Google
- Schedule: https://kccncna2021.sched.com/event/lV2m/taking-your-database-beyond-the-border-of-a-single-kubernetes-cluster-christopher-bradford-datastax-ty-morton-google
- Busca YouTube: https://www.youtube.com/results?search_query=Taking+Your+Database+Beyond+the+Border+of+a+Single+Kubernetes+Cluster+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Taking Your Database Beyond the Border of a Single Kubernetes Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV2m/taking-your-database-beyond-the-border-of-a-single-kubernetes-cluster-christopher-bradford-datastax-ty-morton-google
- YouTube search: https://www.youtube.com/results?search_query=Taking+Your+Database+Beyond+the+Border+of+a+Single+Kubernetes+Cluster+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Fz3CYmil_Yg
- YouTube title: Taking Your Database Beyond the Border of a Single Kubernetes Cl... Christopher Bradford & Ty Morton
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/taking-your-database-beyond-the-border-of-a-single-kubernetes-cluster/Fz3CYmil_Yg.txt
- Transcript chars: 23497
- Keywords: cluster, running, single, talking, clusters, little, environment, around, routing, network, across, multi-cluster, looking, addresses, specifically, within, address, application

### Resumo baseado na transcript

welcome everyone thanks for joining us today we're going to be talking about taking your database beyond the border of a single cluster specifically kubernetes cluster my name is ty morton and i'm a google cloud customer engineer and i am joined by hi i'm christopher bradford i'm the kate sandra project lead and i work for data stacks so let's get started here and discuss the high level goals so right now we're assuming that we're running a database and a single kubernetes cluster in a single region in kubernetes you don't have a little windows system error that pops up in the gcp console um but it's it's worth understanding what's happening here if i have a cluster that has one ip space and then i have another cluster for the same ip

### Excerpt da transcript

welcome everyone thanks for joining us today we're going to be talking about taking your database beyond the border of a single cluster specifically kubernetes cluster my name is ty morton and i'm a google cloud customer engineer and i am joined by hi i'm christopher bradford i'm the kate sandra project lead and i work for data stacks so let's get started here and discuss the high level goals so right now we're assuming that we're running a database and a single kubernetes cluster in a single region in this case we're talking about apache cassandra running on six nodes two per zone across three cents in a raising region if you look at our example here we're using the zone name for gcp but it works for other clouds too and even on-prem and here's where we want to be right we want two regions each with a logical cassandra data data center and that in turn translates to two kubernetes clusters one per region why would we want to do this high availability better performance geo locality we want to scale up this this effectively gives us double the capacity but you did not join the talk on why cassandra is awesome we don't have enough time for that so let's dig into how we make this happen so it seems kind of simple at first right maybe i already have some automation to spin up a kubernetes cluster that might be terraform scripts that might just be some sweet command line scripts i might be clicking through the console um we can just deploy it spin it up call it done right maybe it'll just work well depending on your environment it might work well parts of it might work some parts might work a little bit some may make you think that they're working and they're not you might have a stray firewall rule hanging out um in some cases it could be just a couple little tweaks and you're on to the next task but in others maybe not so much so what we really want to equip you with here is many of the common pitfalls that you're going to run into as you go into this this multi-cluster scenario and make sure that you're ready to go and even if some of these things are working out of the gate for you you should understand what those pieces are because maybe as you grow into a multi-cloud environment or you expand into uh into another kubernetes version or maybe you have different types of clusters out there understanding these these basics and the fine building blocks underneath the hood can really enable you to uh to come up with some advanced solutions and ultimately somet
