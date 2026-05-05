---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Liqi Geng", "PingCAP"]
sched_url: https://kccncna2021.sched.com/event/lV9S/how-we-reduced-write-latency-in-tikv-liqi-geng-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=How+We+Reduced+Write+Latency+in+TiKV%3F+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How We Reduced Write Latency in TiKV? - Liqi Geng, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Liqi Geng, PingCAP
- Schedule: https://kccncna2021.sched.com/event/lV9S/how-we-reduced-write-latency-in-tikv-liqi-geng-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=How+We+Reduced+Write+Latency+in+TiKV%3F+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How We Reduced Write Latency in TiKV?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9S/how-we-reduced-write-latency-in-tikv-liqi-geng-pingcap
- YouTube search: https://www.youtube.com/results?search_query=How+We+Reduced+Write+Latency+in+TiKV%3F+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3BefLqw-4Go
- YouTube title: How We Reduced Write Latency in TiKV? - Liqi Geng, PingCAP
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-we-reduced-write-latency-in-tikv/3BefLqw-4Go.txt
- Transcript chars: 13183
- Keywords: duration, latency, series, message, weight, synchronous, asynchronous, response, request, proposal, version, source, percent, leader, process, figure, average, probability

### Resumo baseado na transcript

hi there thanks for being here today my name is lee chicken i'm very glad to be here to share with you how we reduce dry latency in thai kv let me introduce myself a little bit before we dig deep into our topic i'm an infrastructure engineer at pincap also a committer of taikv and the rafter eyes project i focus on making techyv more efficient scalable and reliable and i'm passionate about distributed systems and storage systems first let me introduce you to the techyv project we are

### Excerpt da transcript

hi there thanks for being here today my name is lee chicken i'm very glad to be here to share with you how we reduce dry latency in thai kv let me introduce myself a little bit before we dig deep into our topic i'm an infrastructure engineer at pincap also a committer of taikv and the rafter eyes project i focus on making techyv more efficient scalable and reliable and i'm passionate about distributed systems and storage systems first let me introduce you to the techyv project we are working with techyv is an open source distributed transactional keyword database also it is a cncf graduated project you might not be familiar with it but so far there are more than 9800 stars and more than 320 contributors in github furthermore it is adopted by more than 1500 adopters in production across multiple industries worldwide so you could see we have a good open source community and a healthy ecosystem back to today's topic to figure out how to reduce right latency in taikv i like to begin with the question why we need low average latency according to little's law concurrency is equal to circle times latency also super is equal to concurrency divided by latency please note that the latency here is average latency so if average latency is lower the throughput will be higher when the concurrency is the same next question i'd like you to think about is why we need low tail latency tail literacy is a tail end of a system's response time spectrum and is often expressed as 99 percentile response times techyv usually solves the customer facing applications the customers can only see the application slow and they don't care about whether they have encountered low probability events furthermore the slow events may not have a low probability because their latency may have amplification effects for parallel failed requests for instance in the transaction mode of the previous phase needs to wait for all parallel provides to be done so the latency of the right phase is the maximum latency of all playwrights if the provided phase involved in provides the probability that its latency is longer than x percentile latency or price request is one minus x percent to earn its power x percent represents the probability that the latency of the request is shorter than the x percentile latency and each request is an independent event so x percent to us power means the probability that earned requests latency are all shorter than the x percentile latency therefore the probability of its compl
