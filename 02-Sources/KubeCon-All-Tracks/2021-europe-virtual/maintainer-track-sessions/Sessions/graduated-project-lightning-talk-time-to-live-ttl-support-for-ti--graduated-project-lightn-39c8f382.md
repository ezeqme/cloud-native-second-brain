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
speakers: ["Bokang Zhang"]
sched_url: https://kccnceu2021.sched.com/event/iaAv/graduated-project-lightning-talk-time-to-live-ttl-support-for-tikv-bokang-zhang
youtube_search_url: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Time+to+Live+%28TTL%29+Support+for+TiKV+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Graduated Project Lightning Talk: Time to Live (TTL) Support for TiKV - Bokang Zhang

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Bokang Zhang
- Schedule: https://kccnceu2021.sched.com/event/iaAv/graduated-project-lightning-talk-time-to-live-ttl-support-for-tikv-bokang-zhang
- Busca YouTube: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Time+to+Live+%28TTL%29+Support+for+TiKV+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Graduated Project Lightning Talk: Time to Live (TTL) Support for TiKV.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iaAv/graduated-project-lightning-talk-time-to-live-ttl-support-for-tikv-bokang-zhang
- YouTube search: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+Time+to+Live+%28TTL%29+Support+for+TiKV+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6Nojm3xnKl0
- YouTube title: Graduated Project Lightning Talk: Time to Live (TTL) Support for TiKV - Bokang Zhang
- Match score: 0.99
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/graduated-project-lightning-talk-time-to-live-ttl-support-for-tikv/6Nojm3xnKl0.txt
- Transcript chars: 5233
- Keywords: timestamp, compaction, distributed, support, without, besides, region, information, provides, transaction, current, checks, exceeds, filter, graduated, techyv, database, github

### Resumo baseado na transcript

hello everyone it's very honored to have you here during this lighting talk today this is spoken from the technv community i'm an infrastructure engineer at pincap also a core contributor to the type tv project besides i'm a maintainer of titan which is roxdb plugin for key value separation inspired by whiskey i'm going to give a presentation of how we support gtl in thai tv first what is thai tv techyv is an open source distributed transactional key value database it became a graduated since that project last

### Excerpt da transcript

hello everyone it's very honored to have you here during this lighting talk today this is spoken from the technv community i'm an infrastructure engineer at pincap also a core contributor to the type tv project besides i'm a maintainer of titan which is roxdb plugin for key value separation inspired by whiskey i'm going to give a presentation of how we support gtl in thai tv first what is thai tv techyv is an open source distributed transactional key value database it became a graduated since that project last year so far we have over 9 000 stars and 300 contributors on github and there are over 1 500 adopters in production across multiple industries worldwide techyv is based on the design of google spanner and each base but simpler to manage and without the dependency on any distributed file systems here is a picture showing the overall architecture of tel tv the full data range is split into small areas called region and there are three replicas in a region by default the replicas are scattered around in two different types of nodes and keep confident by route the placement driver stores the metadata of regions to provide clients with region routine information and it is also responsible for auto charging and low balance type tv use roxdb as the underlying storage energy on top of that it provides horizontal stability and high availability based on raft and unlike other traditional nosql systems tech tv not only provides classic cookie value apis here we call it later roki way but also both optimistic and pessimistic distributed transaction namely transaction kb besides it impulse the kubernetes api which is similar to each base to support the distributed computing and it also provides the ability of elastic scheduling and the geo replication for detail we talked about is mainly supported in the local way okay what is ttl ttl stands for time to live which means data will be deleted automatically without a flight time in minor user cases the value of the data is highly temporal correlation as time goes by the value of the data declines user may need to delete data manual manually periodically which caused extra overhead with tdl the data can be dropped in the database automatically without any mental burden as mentioned before taikv is built on top of roxdb rock db supports tdl natively but with the limitation that all keys should be of the same tdr whereas zero's demand to cite different ttl for each k and the song keys are of non-ttl that is to say the
