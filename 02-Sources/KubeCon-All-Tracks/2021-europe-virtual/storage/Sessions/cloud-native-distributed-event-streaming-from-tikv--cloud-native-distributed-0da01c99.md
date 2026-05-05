---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Storage"
themes: ["Storage Data"]
speakers: ["Zixiong Liu", "PingCAP"]
sched_url: https://kccnceu2021.sched.com/event/iE5r/cloud-native-distributed-event-streaming-from-tikv-zixiong-liu-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Distributed+Event+Streaming+from+TiKV+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Native Distributed Event Streaming from TiKV - Zixiong Liu, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]]
- País/cidade: Virtual / Virtual
- Speakers: Zixiong Liu, PingCAP
- Schedule: https://kccnceu2021.sched.com/event/iE5r/cloud-native-distributed-event-streaming-from-tikv-zixiong-liu-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Distributed+Event+Streaming+from+TiKV+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Native Distributed Event Streaming from TiKV.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5r/cloud-native-distributed-event-streaming-from-tikv-zixiong-liu-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Distributed+Event+Streaming+from+TiKV+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=i1oAGJGAFUo
- YouTube title: [KubeCon EU 2021]Cloud Native Distributed Event Streaming from TiKV
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-native-distributed-event-streaming-from-tikv/i1oAGJGAFUo.txt
- Transcript chars: 13390
- Keywords: regions, transaction, region, capture, transactions, distributed, stream, streaming, design, replicated, second, watermark, events, needed, protocol, component, important, wanted

### Resumo baseado na transcript

hello everyone i'm an engineer from teamcat the company that made kv and i'm here to share with you our experience with implementing distributed event streaming from ipv before we get to business here's some background about myself i'm jishin liu a software engineer at pincap and i'm part of the data migration team i'm a contributor to taikv and one of the maintainers of thai cdc but in the field of computer science my interests are databases operating systems distributed systems and for education i'm an alumnus of the

### Excerpt da transcript

hello everyone i'm an engineer from teamcat the company that made kv and i'm here to share with you our experience with implementing distributed event streaming from ipv before we get to business here's some background about myself i'm jishin liu a software engineer at pincap and i'm part of the data migration team i'm a contributor to taikv and one of the maintainers of thai cdc but in the field of computer science my interests are databases operating systems distributed systems and for education i'm an alumnus of the university of chicago and that was part of the class of 2018. now let's go over today's agenda first i'll give a brief introduction to techyv and then i'll talk about the high level design of our distributed event streaming project then i'll talk mainly two aspects of the detailed design and then i'll also talk about our use of edcp and the higher bit high availability we implemented with it okay now let me talk a little bit about tech tv to give you some background for the main topic of this talk kv is a distributed transactional key value database and it is a graduated project of the cncf this diagram shows the overall architecture of thai kv so this is a tech heavy cluster with four machines we use shared nothing architecture so that techiev can run on commodity hardware with no special equipment needed each machine can host multiple regions the number of regions on each machine can be quite high like more than 10 000 these regions are replicated by draft protocol and are regulated by placement driver which is a component that runs out outside of the tachyv processes and communicates with type av by grpc here i summarize four points that are helpful to understand before we proceed first take av is a transactional key value storage where you can manipulate multiple keys within the transaction second the keys are sharded into multiple regions well you can regard the region as a replicated key value store third the regions are replicated by using raft protocol which provides strong consistency among the replicas and the fourth point is that regions can merge and split while being regulated by the placement driver in order to demonstrate the rationale behind the design choices we made when implementing data streaming it's important to go over the abstraction layers of ipv first on top of everything is the transaction layer the transaction layer is where our concurrency control protocol is implemented we use a percolator like protocol but i'll
