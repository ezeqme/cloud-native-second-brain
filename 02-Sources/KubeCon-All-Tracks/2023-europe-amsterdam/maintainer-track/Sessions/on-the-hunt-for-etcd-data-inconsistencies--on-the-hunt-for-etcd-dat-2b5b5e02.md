---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Storage Data", "Community Governance"]
speakers: ["Marek Siarkowicz", "Google"]
sched_url: https://kccnceu2023.sched.com/event/1HyTX/on-the-hunt-for-etcd-data-inconsistencies-marek-siarkowicz-google
youtube_search_url: https://www.youtube.com/results?search_query=On+the+Hunt+for+Etcd+Data+Inconsistencies+CNCF+KubeCon+2023
slides: []
status: parsed
---

# On the Hunt for Etcd Data Inconsistencies - Marek Siarkowicz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Storage Data]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Marek Siarkowicz, Google
- Schedule: https://kccnceu2023.sched.com/event/1HyTX/on-the-hunt-for-etcd-data-inconsistencies-marek-siarkowicz-google
- Busca YouTube: https://www.youtube.com/results?search_query=On+the+Hunt+for+Etcd+Data+Inconsistencies+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre On the Hunt for Etcd Data Inconsistencies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyTX/on-the-hunt-for-etcd-data-inconsistencies-marek-siarkowicz-google
- YouTube search: https://www.youtube.com/results?search_query=On+the+Hunt+for+Etcd+Data+Inconsistencies+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IIMs0EjQZHg
- YouTube title: On the Hunt for Etcd Data Inconsistencies - Marek Siarkowicz, Google
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/on-the-hunt-for-etcd-data-inconsistencies/IIMs0EjQZHg.txt
- Transcript chars: 26846
- Keywords: testing, validate, history, correct, changes, traffic, multiple, correctness, cannot, revision, process, inconsistencies, operations, pretty, requests, failures, basically, happening

### Resumo baseado na transcript

welcome to the talk on the hunt of for hcd data inconsistencies and data inconsistencies are pretty it's Unique animal so finding them is more than an art than strict science at least yet so hopefully after the talk you will have a better understanding of the topic and be able to find inconsistencies in your own system I'm Mark sarkovich I work at Google and I'm one of the HD maintainers so topic for the day is I would like to Define what are data inconsistencies what tools we

### Excerpt da transcript

welcome to the talk on the hunt of for hcd data inconsistencies and data inconsistencies are pretty it's Unique animal so finding them is more than an art than strict science at least yet so hopefully after the talk you will have a better understanding of the topic and be able to find inconsistencies in your own system I'm Mark sarkovich I work at Google and I'm one of the HD maintainers so topic for the day is I would like to Define what are data inconsistencies what tools we use to hand them and how hcd has adapted to to to find the problems that we had with inconsistencies so at the end I will do a short demo showing you how how it works in practice uh so hcd implements uh so-called distributed consensus it means that multiple units processes work as a or multiple processes of hcd server run as a single unit a cluster that can cause consistently respond to user requests so any user can observe the same data any write by a user can be observed by all the users so what is the inconsistency inconsistency is when one of the one of the instances breaks loose and starts spilling nonsense no matter how cool your free head dragon is it doesn't it's stopped working when one of the one of the heads goes berserk to give you more concrete example here is a real production case that I noticed and tried to document a where hcd inconsistency caused problems with HD cluster kubernetes cluster using it [Music] in this case at CD or kubernetes nodes were flapping from status ready and not ready there were random failures random timeouts authorization didn't work sometimes sometimes it worked so how do you know what is happening atoms were crashing um yeah basically because of like architecture one of the API servers were structurally misbehaving and what was the root cause it was just missing one exactly one right so as you see on the graph missing one right can cause the the revision of hcd to totally diverge this is because how kubernetes uses at CD and its revision is pretty crucial for kubernetes correctness um to to explain revision is like Global counter for each change that happened is happening in the cluster and revision is used by kubernetes for optimistic concurrency control so um the example above was unrelated but why I'm talking to you today is about the state of HCG 3.5.0 the release was done after a long time with a lot of changes in the project including total change of maintainers and loss of a lot of knowledge that was Unwritten between maintainers and
