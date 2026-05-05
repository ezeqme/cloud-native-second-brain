---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Marek Siarkowicz", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2vl/secrets-of-running-etcd-marek-siarkowicz-google
youtube_search_url: https://www.youtube.com/results?search_query=Secrets+of+Running+Etcd+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Secrets of Running Etcd - Marek Siarkowicz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Marek Siarkowicz, Google
- Schedule: https://kccncna2023.sched.com/event/1R2vl/secrets-of-running-etcd-marek-siarkowicz-google
- Busca YouTube: https://www.youtube.com/results?search_query=Secrets+of+Running+Etcd+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Secrets of Running Etcd.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vl/secrets-of-running-etcd-marek-siarkowicz-google
- YouTube search: https://www.youtube.com/results?search_query=Secrets+of+Running+Etcd+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aJVMWcVZOPQ
- YouTube title: Secrets of Running Etcd - Marek Siarkowicz, Google
- Match score: 0.737
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/secrets-of-running-etcd/aJVMWcVZOPQ.txt
- Transcript chars: 26164
- Keywords: cluster, events, running, cannot, failures, issues, changes, defrag, experience, server, easily, pretty, change, algorithm, number, request, leader, solution

### Resumo baseado na transcript

okay hello everyone um thank you for taking your time and staying for one of the last sessions in the cucon hope everyone had a great time and maybe and I'm hopeful to see you maybe on the next one and we can discuss more but today we have one of the last sessions uh let's finish it with some secrets of running CD uh I'm Mar shovi I'm uh I've been maintainer of etcd for last two years uh with recent creation of Sig ET CDs the special interest

### Excerpt da transcript

okay hello everyone um thank you for taking your time and staying for one of the last sessions in the cucon hope everyone had a great time and maybe and I'm hopeful to see you maybe on the next one and we can discuss more but today we have one of the last sessions uh let's finish it with some secrets of running CD uh I'm Mar shovi I'm uh I've been maintainer of etcd for last two years uh with recent creation of Sig ET CDs the special interest group in kubernetes I'm the TL of the uh of the Sig and I'm also the person uh working at gke and making sure that if you run in in in Google your class your kubernetes classers are running and the atcd that we are running is the best that we can bring you so today I wanted to share some of the experiences and my view on reliability of etcd that I have seen personally in production um so uh agenda for today is look at some simple cases of failures in distributed system uh I would want to focus on especially on cluster scope failures which is in my EXP experience biggest reason of failures that I have seen uh I will propose couple of mitigations how you can avoid those problems and we'll finish maybe the secret maybe some people already know it uh and yeah uh so failures in distribut systems uh kuber or etcd is really great at uh handling failures of single members uh this is because it uses uh rough consensus algorithm and it allows it to survive failures or of single maybe two nodes depending of your cluster size so it as long as the Quorum so the majority of the members are alive we can we can the cluster can proceed and this is great for like failures of this Network some disconnections so short temporary uh issues that you don't want to like think like about uh but uh so this works because of raft uh raft is an algorithm that can take a um any number of concurrent request and provide us a singular organized and ordered stream of uh of requests and properly distributed along all members this allows us to be sure that every member has the same data and every member uh can end up uh in the same state but unfortunately it also means that uh every time there is a developer mistake application issue or just a corrupt even a corruption in the data it's as easily to replicate correct Behavior it's as or it's as easily to inject failure to all the members so today I would want to give you a couple of examples of Errors like this where the whole cluster can suffer because of some issue that was either U hard to predict in e
