---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/remote-write-storage-wars/
youtube_url: https://www.youtube.com/watch?v=OsH6gPdxR4s
youtube_search_url: https://www.youtube.com/results?search_query=Remote+Write+Storage+Wars+PromCon+2019
video_match_score: 0.888
status: video-found
---

# Remote Write Storage Wars

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/remote-write-storage-wars/
- YouTube: https://www.youtube.com/watch?v=OsH6gPdxR4s

## Resumo

Speaker: Alejandro Cespedes Remote write storage is a hot topic, several systems existed for a few years (Cortex, M3DB, InfluxDB) and some systems have been born in the past few months (Thanos receive, VictoriaMetrics). Each system has it's own architecture and different trade-offs. In this talk, Alejandro will present adidas findings on experiments to benchmark various remote write open source storage systems such as Cortex, M3DB, Thanos, VictoriaMetrics and others.

## Abstract oficial

Speaker: Alejandro Cespedes

Remote write storage is a hot topic, several systems existed for a few years (Cortex, M3DB, InfluxDB) and some systems have been born in the past few months (Thanos receive, VictoriaMetrics). Each system has it's own architecture and different trade-offs. In this talk, Alejandro will present adidas findings on experiments to benchmark various remote write open source storage systems such as Cortex, M3DB, Thanos, VictoriaMetrics and others. The experiments try to benchmark scalability and elasticity of each storage system.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/remote-write-storage-wars/
- YouTube: https://www.youtube.com/watch?v=OsH6gPdxR4s
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OsH6gPdxR4s
- YouTube title: PromCon EU 2019: Remote Write Storage Wars
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/remote-write-storage-wars/OsH6gPdxR4s.txt
- Transcript chars: 17186
- Keywords: wanted, question, matrix, cortex, metrics, cluster, memory, actually, storage, infrastructure, prometheus, solutions, single, results, everything, certain, tenant, running

### Resumo baseado na transcript

[Music] okay so today I'm going to talk about what we find at adidas when we wanted to use the remote volatile storage so let me introduce myself I'm Alejandra Vespers I work at the performed in anything I do anything that means everything metrics related but before starting I would like to ask you a question so what do you see here see my creativity see my creation we can't do what you picked on you see my creativity [Music] so you just saw a bunch of people doing

### Excerpt da transcript

[Music] okay so today I'm going to talk about what we find at adidas when we wanted to use the remote volatile storage so let me introduce myself I'm Alejandra Vespers I work at the performed in anything I do anything that means everything metrics related but before starting I would like to ask you a question so what do you see here see my creativity see my creation we can't do what you picked on you see my creativity [Music] so you just saw a bunch of people doing sports right so let me show you what we see [Music] see my creativity see my premium what is your pinch for me see my creativity so as you can see itís quite obsessed with data and we try to measure everything on different layers and not only on the technical side but also on our business processes and we try to apply all those metrics that we that we gather everywhere we can okay so first let me put you a little bit of in context of our landscape we run several quadratus clusters around the world and serving tens of apps in its cluster and that means you're soft I'm serious in its cluster and we have to meter the cluster itself on top of that and on top of that the growing usage of both the trainer stack and they could have this cluster itself is growing in inside our company and the way the infrastructure is provision means that we cannot grow big promises as much as we can so we have a limit and when we hit that limit the previous classes out of nori so good luck we have a professional football player giving us advice and yeah so if we run no Center to Matthews and nothing can complete because sometimes it's not just only the usage but mistakes are made and you know cards IDs our Reuters labels and cardinality institution means commissions explosion so so we decided to change ask teams to whom it's on Prometheus but there is an issue with that and one team's metrics are valuable for another team for example that they think that's managing promise you Kaka offers some metrics that are by the world for regularity meters that's using Kafka for example you want to be alerted if the certain topic is is getting drug or say pile up on things like that many so we found ourselves with lots of promises that of the to send matrix somewhere and central v1lat so we look for the in the open source for solutions to that problem that we have we found cortex we found in flux also free DB fellows and also recently picked area matrix but which one to use that was a question that nobody could tell us you ask the
