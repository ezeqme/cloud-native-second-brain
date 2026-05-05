---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Jeffrey Carpenter", "DataStax"]
sched_url: https://kccncna2021.sched.com/event/lV3V/how-to-put-a-database-in-kubernetes-jeffrey-carpenter-datastax
youtube_search_url: https://www.youtube.com/results?search_query=How+to+put+a+Database+in+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How to put a Database in Kubernetes - Jeffrey Carpenter, DataStax

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Jeffrey Carpenter, DataStax
- Schedule: https://kccncna2021.sched.com/event/lV3V/how-to-put-a-database-in-kubernetes-jeffrey-carpenter-datastax
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+put+a+Database+in+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How to put a Database in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3V/how-to-put-a-database-in-kubernetes-jeffrey-carpenter-datastax
- YouTube search: https://www.youtube.com/results?search_query=How+to+put+a+Database+in+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UgtYlvIv36Q
- YouTube title: How to put a Database in Kubernetes - Jeffrey Carpenter, DataStax
- Match score: 0.802
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-to-put-a-database-in-kubernetes/UgtYlvIv36Q.txt
- Transcript chars: 31958
- Keywords: storage, database, cassandra, persistent, actually, volume, stateful, deployment, cluster, volumes, provider, create, single, running, databases, available, primitives, deploy

### Resumo baseado na transcript

[Applause] thank you thank you very much i'm really glad to be here uh this is actually my first kubecon done a little bit of workshop support in ancillary events in past but this is the first time actually attending a kubecon and i'm super excited so i'm not going to talk for five minutes about myself um just so you know where i'm coming from software engineer got into architecture after that and then um i've been worked in defense and in hospitality and for some reason i always

### Excerpt da transcript

[Applause] thank you thank you very much i'm really glad to be here uh this is actually my first kubecon done a little bit of workshop support in ancillary events in past but this is the first time actually attending a kubecon and i'm super excited so i'm not going to talk for five minutes about myself um just so you know where i'm coming from software engineer got into architecture after that and then um i've been worked in defense and in hospitality and for some reason i always try to get myself on whatever the project is that the company is betting the business on so that's where i seem to end up that has led me into some interesting spaces a lot of distributed systems so that got me into apache cassandra and kubernetes and then now putting them together so that's kind of the genesis of how i got involved in this kind of thing um so on the way over here i was grabbing a snack and i went outside to the coffee station and i'm walking past a table and i don't i don't recognize anybody here so maybe i'll be okay uh so i'm walking past the table and there's a group of folks and they're like hey did you see that um data stacks is going to be doing a talk about how to put a database in in kubernetes and one and one guy goes why would you do that that's what oh there is still skepticism out here around this now you know i'm in a world where um i'm used to this and i've already bought into it this is an article that i'm showing up here that a colleague of mine chris bradford wrote about his personal journey from being very anti you know running databases and containers just even that idea to how he kind of went through that progression of running databases on kubernetes so what i thought i would do is this is not the why you should run a database in kubernetes talk it's more of the assuming that you agree with the premise of doing it how do we actually go about doing it that's kind of where i'm coming from if you want to ask me questions about why at the end let's do it there's a whole community of people that are working on putting stateful workloads on to kubernetes it's the data on kubernetes community we had a great full day of sessions here on tuesday you can go and watch a lot of those sessions online i may even stole a couple of my points that you'll see later in the talk from things i heard on tuesday so i'm an active and avid learner in this space as well there's a whole community of innovators doing great things here one of the things that i learned re
