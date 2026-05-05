---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Denis Magda", "Yugabyte"]
sched_url: https://kccncna2024.sched.com/event/1i7rt/goodbye-etcd-running-kubernetes-on-distributed-postgresql-denis-magda-yugabyte
youtube_search_url: https://www.youtube.com/results?search_query=Goodbye+etcd%21+Running+Kubernetes+on+Distributed+PostgreSQL+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Goodbye etcd! Running Kubernetes on Distributed PostgreSQL - Denis Magda, Yugabyte

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Denis Magda, Yugabyte
- Schedule: https://kccncna2024.sched.com/event/1i7rt/goodbye-etcd-running-kubernetes-on-distributed-postgresql-denis-magda-yugabyte
- Busca YouTube: https://www.youtube.com/results?search_query=Goodbye+etcd%21+Running+Kubernetes+on+Distributed+PostgreSQL+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Goodbye etcd! Running Kubernetes on Distributed PostgreSQL.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rt/goodbye-etcd-running-kubernetes-on-distributed-postgresql-denis-magda-yugabyte
- YouTube search: https://www.youtube.com/results?search_query=Goodbye+etcd%21+Running+Kubernetes+on+Distributed+PostgreSQL+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VdF1tKfDnQ0
- YouTube title: Goodbye etcd! Running Kubernetes on Distributed PostgreSQL - Denis Magda, Yugabyte
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/goodbye-etcd-running-kubernetes-on-distributed-postgresql/VdF1tKfDnQ0.txt
- Transcript chars: 28682
- Keywords: database, pogress, cluster, distributed, running, generally, across, databases, server, yugabyte, information, storage, deployments, another, question, several, machine, reason

### Resumo baseado na transcript

hello everyone welcome to one of the last sessions of the conference congratulations you made it uh my name is Dennis Magda I've been working with distributed systems applications and databases for the last I think eight nine years and today I'd like to share my experience on how to run kubernetes cluster on a distributed database in particular on a distributed pogress SQL as you can see I don't have any slides it's not because I'm lazy to put them together but generally my goal is to show you

### Excerpt da transcript

hello everyone welcome to one of the last sessions of the conference congratulations you made it uh my name is Dennis Magda I've been working with distributed systems applications and databases for the last I think eight nine years and today I'd like to share my experience on how to run kubernetes cluster on a distributed database in particular on a distributed pogress SQL as you can see I don't have any slides it's not because I'm lazy to put them together but generally my goal is to show you how everything works in action it's going to be a Hands-On session for me and then if you find this session useful then you will be able to Google or go to CH GPT and you will be able to learn from resources prepared by people who are much smarter than me in this area all right so that's the reason so let's talk about let's take a look at the plan first we need to figure out what is a tcd then we will talk the reasons why we even have this session and why some of the folks within the kubernetes community decided that we need to have some replacement an alternate option uh for this distributed storage then uh you'll see we'll talk about a project kind because kind is a special component that makes it possible to use pogress my equal Oracle or pretty much I think bunch of other relational databases instead of atcd for kubernetes deployments and then I will show you real world examples So speaking about the demos what exactly we are going to do we are going to run kubernetes on vanilla pogress and vanilla I mean it's pogress open source single note cluster single note instance and after that once we make this happen we will will do the same kubernetes but on distributed POS okay that's the plan by the way question how many of you came to this session because of pogress in the title anyone I knew that all right so what's tcd a tcd is a distributed scalable and highly available key value store or key value database it's quite simple but the part is in the Simplicity because what it does really well it works across several nodes across several machines or VMS that you have in your cluster it uses the raft consensus protocol to replicate all of the changes and then if any of the itcd noes goes down then guess what their database itself remains available the data is stored in a consistent State and that was one of the reasons why kubernetes selected etcd as a component so let's write this down tcd is distributed and highly available data store it's just you can think about i
