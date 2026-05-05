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
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Jayme Bird", "Manish Gill", "ClickHouse"]
sched_url: https://kccnceu2025.sched.com/event/1tx9J/dancing-with-the-pods-live-migration-of-a-database-fleet-while-serving-millions-of-queries-jayme-bird-manish-gill-clickhouse
youtube_search_url: https://www.youtube.com/results?search_query=Dancing+With+the+Pods%3A+Live+Migration+of+a+Database+Fleet+While+Serving+Millions+of+Queries+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Dancing With the Pods: Live Migration of a Database Fleet While Serving Millions of Queries - Jayme Bird & Manish Gill, ClickHouse

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United Kingdom / London
- Speakers: Jayme Bird, Manish Gill, ClickHouse
- Schedule: https://kccnceu2025.sched.com/event/1tx9J/dancing-with-the-pods-live-migration-of-a-database-fleet-while-serving-millions-of-queries-jayme-bird-manish-gill-clickhouse
- Busca YouTube: https://www.youtube.com/results?search_query=Dancing+With+the+Pods%3A+Live+Migration+of+a+Database+Fleet+While+Serving+Millions+of+Queries+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Dancing With the Pods: Live Migration of a Database Fleet While Serving Millions of Queries.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx9J/dancing-with-the-pods-live-migration-of-a-database-fleet-while-serving-millions-of-queries-jayme-bird-manish-gill-clickhouse
- YouTube search: https://www.youtube.com/results?search_query=Dancing+With+the+Pods%3A+Live+Migration+of+a+Database+Fleet+While+Serving+Millions+of+Queries+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ufY_JFPpzRI
- YouTube title: Dancing With the Pods: Live Migration of a Database Fleet While Serving... Jayme Bird & Manish Gill
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dancing-with-the-pods-live-migration-of-a-database-fleet-while-serving/ufY_JFPpzRI.txt
- Transcript chars: 25973
- Keywords: replicas, migration, stateful, controller, operator, replica, actually, happening, single, cluster, database, queries, inside, customers, migrations, create, autoscaling, managing

### Resumo baseado na transcript

Uh we're going to talk about something we call make before break internally. Uh and then we're going to talk about what is the context behind this migration and how we actually ended up executing this. So if you uh kind of if you have trouble following please check out that talk because in that one I go really in depth about the problem with stateful sets and then how we came about solving those problems. And this is a general high level architecture of when we do autoscaling. And all that information is going to uh come in uh the autoscaler is going to react to that information going to start doing pod evictions. standard VPA also works vertical scaling so the problem is uh thus right so what we want in vertical scaling is we want to have like uh let's say three replicas of one size and then you want to go uh to a different size

### Excerpt da transcript

uh just a quick overview of the agenda. We're going to talk about autoscaling. Uh we're going to talk about something we call make before break internally. Uh and then we're going to talk about what is the context behind this migration and how we actually ended up executing this. So for those who don't know what click house is uh it's an open source column oriented distributed database. It's an OLAP database. Uh so if you want to store like pabytes of data and uh kind of do like really fast aggregations and analytical queries on top of them you can use click house it's open source uh we also have a cloud version uh which uh our team is also part of managing that cloud and it's got all the fully managed features serverless idling separation of compute and storage uh so what happens here is like uh we have pods running inside these click house instances uh and these pods are attached to PVCs that have metadata in them the actual data is stored on object storage as is the trend these days with uh you know fully managed serverless databases.

Uh and then we have like a bring your own cloud offering if you don't want data to ever leave your uh network. So uh like uh most uh uh people who want to manage like uh something on Kubernetes a service or even a database we started with like a stateful set uh uh started with our operator which in turn is managing a stateful set which in turn is of course managing the pods and uh they have the PVC attached to them. Uh I'm going to do some like a lot of context sharing. I'm going to rapidly dump a lot of information here because uh the the background context for the migration is actually a talk I did last year at CubeCon Paris that's called fantastic ordinals. So uh it's going to go really quickly. So if you uh kind of if you have trouble following please check out that talk because in that one I go really in depth about the problem with stateful sets and then how we came about solving those problems. Right? So this is just a quick plug for the background context. Uh okay so uh really quickly autoscaling.

So autoscaling in general in Kubernetes today requires pod evictions. That's because uh every time you want to resize a pod, you want to change a request or the limits, you need to kind of uh you know restart the pod itself. And that is done inside our cloud using the autoscaler, right? Which is responsible for evicting the pod and then a controller is going to go over and then resubmit that pod. In this case, this cont
