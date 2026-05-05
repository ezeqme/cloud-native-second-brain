---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Nick Cameron", "Andy Lok", "PingCAP"]
sched_url: https://kccnceu2021.sched.com/event/iE7D/using-a-distributed-key-value-store-nick-cameron-andy-lok-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Using+a+Distributed+Key-Value+Store+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Using a Distributed Key-Value Store - Nick Cameron & Andy Lok, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Nick Cameron, Andy Lok, PingCAP
- Schedule: https://kccnceu2021.sched.com/event/iE7D/using-a-distributed-key-value-store-nick-cameron-andy-lok-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Using+a+Distributed+Key-Value+Store+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Using a Distributed Key-Value Store.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7D/using-a-distributed-key-value-store-nick-cameron-andy-lok-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Using+a+Distributed+Key-Value+Store+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=i5Hrx2atx9w
- YouTube title: [KubeCon EU 2021]Using a Distributed KeyValue Store
- Match score: 0.86
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/using-a-distributed-key-value-store/i5Hrx2atx9w.txt
- Transcript chars: 17508
- Keywords: transaction, client, distributed, mongodb, stores, protocol, actually, cluster, regions, commit, application, dictionary, python, source, database, interface, single, usually

### Resumo baseado na transcript

using a distributed key value store and the word i really want to emphasize in that title is using because our talk today is about how you would actually use a distributed key value store in your application we're nick and andy we're engineers at pincap where we both work on tai kv which is an example of a key value store as well we'll tell you a bit later in the talk the talk is going to be in three parts so first of all we're going to talk

### Excerpt da transcript

using a distributed key value store and the word i really want to emphasize in that title is using because our talk today is about how you would actually use a distributed key value store in your application we're nick and andy we're engineers at pincap where we both work on tai kv which is an example of a key value store as well we'll tell you a bit later in the talk the talk is going to be in three parts so first of all we're going to talk very quickly about what a key value store actually is and some example kv stores and about their features and how you would choose one of them for your application after that well we have to pick one of those to actually talk about the rest of the the talk and we're going to pick taikevi now that is obviously a biased choice but um hopefully it will be an appropriate choice for some of you and the more general principles will apply to other kb stores too then the the bulk of the talk is about how your application communicates with a distributed kv store in this case thai kv so to start off i'm going to hand over to andy who is going to talk about how to choose a kv store so amanda thanks for the introduction i'm here to talk to you in this section about what is a kiwi store and what are the key stores available further i will talk about their pros and cons so in the beginning what is the clearview store he might have already been using game stores in your programming language for example the dictionary in python or the map in other programming languages are qb scores this example in python is a dictionary that maps the key k1 to value v1 and tk2 to value v2 kv source often allows you to look up the value by the corresponding key for instance curing this dictionary with gk1 the returns is value v1 this operation now import get except get the k restore also have method put and delete for modified data in the real world a kv store often refers to a database that receives gigabytes to terabytes of data in the form of key value instead of this more dictionary impulses but once you search for qr stores in google and then you will be drawn by too many cube stores which may all have subtle differences and you must struggle to figure out which one best fits your needs so i'll pick some of the most common ones and talk about their pros and cons and different kinds of scenarios they are best for you may have heard of roxby it is built by facebook and it is a high performance embedded kp store what embed means is that it's a libra
