---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Alerting", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: ["Ganesh Vernekar", "Arve Knudsen"]
source_url: https://promcon.io/2024-berlin/talks/the-future-of-metadata-in-prometheus-enhancing-storage-and-usability/
youtube_url: https://www.youtube.com/watch?v=Torm3M23Uyk
youtube_search_url: https://www.youtube.com/results?search_query=The+Future+of+Metadata+in+Prometheus%3A+Enhancing+Storage+and+Usability+PromCon+2024
video_match_score: 1.043
status: video-found
---

# The Future of Metadata in Prometheus: Enhancing Storage and Usability

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Alerting]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: Ganesh Vernekar, Arve Knudsen
- Página oficial: https://promcon.io/2024-berlin/talks/the-future-of-metadata-in-prometheus-enhancing-storage-and-usability/
- YouTube: https://www.youtube.com/watch?v=Torm3M23Uyk

## Resumo

Prometheus has revolutionized the way we handle monitoring and alerting, yet the management of metadata within the system remains a challenge. Currently, Prometheus stores series metadata per time-series only in memory, with no persistence on disk. As the use of Prometheus expands, the demand for more sophisticated metadata management has become evident.

## Abstract oficial

Prometheus has revolutionized the way we handle monitoring and alerting, yet the management of metadata within the system remains a challenge. Currently, Prometheus stores series metadata per time-series only in memory, with no persistence on disk. As the use of Prometheus expands, the demand for more sophisticated metadata management has become evident. Metadata use cases now extend beyond a single instance per time-series, encompassing metadata that holds independent significance or provides additional context to series or groups of series.

In this talk, we will explore the evolving landscape of metadata in Prometheus. We will discuss the emerging use cases that necessitate a more robust metadata management solution and our vision for addressing these needs. Our goal is to design a persistent metadata store that can efficiently handle diverse metadata requirements, enhancing the flexibility and functionality of Prometheus.

Join us as we delve into the challenges and opportunities of building a metadata storage layer. We will share our initial design considerations, anticipated benefits, and invite the community to contribute to shaping the future of metadata in Prometheus. This session is ideal for developers, system architects, and anyone interested in the inner workings of Prometheus and the future of observability.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/the-future-of-metadata-in-prometheus-enhancing-storage-and-usability/
- YouTube: https://www.youtube.com/watch?v=Torm3M23Uyk
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Torm3M23Uyk
- YouTube title: PromCon 2024 - The Future of Metadata in Prometheus: Enhancing Storage and Usability
- Match score: 1.043
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/the-future-of-metadata-in-prometheus-enhancing-storage-and-usability/Torm3M23Uyk.txt
- Transcript chars: 26395
- Keywords: metadata, series, labels, prometheus, attributes, resource, storage, design, metric, question, information, change, associated, changes, another, thought, basically, stored

### Resumo baseado na transcript

[Music] hello everyone we are going to talk about metadata and what's in the future of metadata for Prometheus I'm Ganesh marikar I'm a Prometheus maintainer and I have been contributing to Prometheus for over 6 years and currently I ALS I also working on the mem project so I try to give how much of time I can for Prometheus hello everyone I arvi nson I'm a senior software engineer with graphon Labs uh I work on graphon Mir but I'm also a maintainer mainly of the ult TLP

### Excerpt da transcript

[Music] hello everyone we are going to talk about metadata and what's in the future of metadata for Prometheus I'm Ganesh marikar I'm a Prometheus maintainer and I have been contributing to Prometheus for over 6 years and currently I ALS I also working on the mem project so I try to give how much of time I can for Prometheus hello everyone I arvi nson I'm a senior software engineer with graphon Labs uh I work on graphon Mir but I'm also a maintainer mainly of the ult TLP endpoint in prome so um as Ganesh said uh we are going to talk about uh our idea for uh persisted metad data in Prometheus so first of all what what do we mean by metadata uh so basically um is uh the idea is that we associate um each time series with a collection of key value pairs really and and this uh this collection per series of key value pairs can change over time because metad data four time series can uh can change and then there's a question why why is there a problem to solve uh for starters we have the existing concept of metric metad data in promethus where you can you can uh describe a metric's type its unit its help uh but the the the drawback is that it's or or the limitation I mean is that it's currently only stored in uh memory and and not persisted uh in uh in the long time longterm storage uh and in addition to just metric met metad data there are emerging use cases like uh open t like open Telemetry resource attributes so for those of you who are not familiar with open Telemetry uh every every metric in open Telemetry that um pritus receives is uh associated with a socaled resource and a resource basically represent represents the The Entity producing the the metric and every and then the the the resource has a collection of attributes describing it uh and the attributes are basically a collection of uh key value pairs um so they they they are now encoded uh via an infom metric in peritus but we think that uh if uh if if we had P natively persistent Med metad directly in peritus that would be um a better way of modeling and storing these attributes uh there's also the use case of attaching custom metadata to Series where people where where where now people will solve this by adding labels to series um and we would we and then there's use case of storing things like uh created time stamps for series their scrape interval the the series type like like is this a classical histogram or is it a native histogram um and and so on and so forth and we also need to track as alre
