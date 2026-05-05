---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: ["Alex Greenbank", "Bartłomiej Płotka"]
source_url: https://promcon.io/2024-berlin/talks/unlocking-cost-savings--new-possibilities-your-guide-to-prometheus-remote-write-20/
youtube_url: https://www.youtube.com/watch?v=1sGmdQk22Ho
youtube_search_url: https://www.youtube.com/results?search_query=Unlocking+Cost+Savings+%26+New+Possibilities%3A+Your+Guide+to+Prometheus+Remote+Write+2.0+PromCon+2024
video_match_score: 1.057
status: video-found
---

# Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote Write 2.0

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: Alex Greenbank, Bartłomiej Płotka
- Página oficial: https://promcon.io/2024-berlin/talks/unlocking-cost-savings--new-possibilities-your-guide-to-prometheus-remote-write-20/
- YouTube: https://www.youtube.com/watch?v=1sGmdQk22Ho

## Resumo

Prometheus Remote Write is the protocol used to send Prometheus metrics from Prometheus or any other metric source to compatible remote storage endpoints such as Thanos and Cortex. Remote Write is generally used for metric long-term storage, centralization, and cloud services. It also enables users to run Prometheus in an agent mode, reducing local storage requirements.

## Abstract oficial

Prometheus Remote Write is the protocol used to send Prometheus metrics from Prometheus or any other metric source to compatible remote storage endpoints such as Thanos and Cortex. Remote Write is generally used for metric long-term storage, centralization, and cloud services. It also enables users to run Prometheus in an agent mode, reducing local storage requirements.

Welcome to Remote Write 2.0! In this talk, Bartek and Alex, Prometheus maintainers and RW2.0 spec. co-authors, will introduce you to the next iteration of the popular protocol which adds more functionality while cutting your egress costs up to 60%, and keeps the previous versions easy-to-implement stateless design!

The audience will learn what's changed in the second version of Remote Write, what it unlocks, and how easy it is to update or adopt. Finally, the speakers will share the latest benchmarks and differences with the common alternatives.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/unlocking-cost-savings--new-possibilities-your-guide-to-prometheus-remote-write-20/
- YouTube: https://www.youtube.com/watch?v=1sGmdQk22Ho
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1sGmdQk22Ho
- YouTube title: PromCon 2024 - Unlocking Cost Savings & New Possibilities: Your Guide to Prometheus Remote Write 2.0
- Match score: 1.057
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/unlocking-cost-savings-new-possibilities-your-guide-to-prometheus-remo/1sGmdQk22Ho.txt
- Transcript chars: 36350
- Keywords: remote, protocol, storage, actually, version, features, compression, histograms, prometheus, solutions, format, already, string, better, simple, samples, promit, metadata

### Resumo baseado na transcript

[Music] oh welcome everyone we are super EXC extremely excited actually to be here at promcon and talk about yeah the new version of remote right um and I have to admit um in the cont context of distributed systems um I have some kind of strange weakness or respect towards designing Network protocols and apis and I would love to learn if you share the sentiment but you know for me designing Network protocols especially for High um high volume data and open source and in open source um correctly and did you consider potential um challenges in in terms of how to implement that and how that could impact the performance and thinking in like uh languages I don't know like python or uh other client libraries that they not go I mean simple like so I wouldn't Envision like huge huge problems there and what more is that if you look on promus what we realize it like all our strings in for example labels like it would use interning string interning so we actually have strink interning for every you know labels in our PR storage so I think it allows actually more optimizations where maybe we use the same references or something we have like a global uh string inter turning across the storage uh the prit use kind of

### Excerpt da transcript

[Music] oh welcome everyone we are super EXC extremely excited actually to be here at promcon and talk about yeah the new version of remote right um and I have to admit um in the cont context of distributed systems um I have some kind of strange weakness or respect towards designing Network protocols and apis and I would love to learn if you share the sentiment but you know for me designing Network protocols especially for High um high volume data and open source and in open source um it poses a lot of interesting questions right for example like how to make this API you know both extensible but also stable how to make them flexible and Powerful but also like simple efficient and consistent and plus it takes years to adopt those protocols and really get feedback proper feedback on what you did so um so yeah it's challenging and then you have to think about usual Network you know problems or distributed system challenges like consistency and availability um so for those reasons I really like to sometimes study how other protocols work and how they were created and while I you know help a little bit with the design of the remote read streaming one and the streaming mode and we both help in the remote right protocol next version of it it is only when I preparing I Was preparing this talk I kind of like look on the big picture of the remote right protocol history and I found useful learnings um so I want to share that with you and might that might give us a little bit of perspective so let's begin um yeah so today is hard to imagine you know promes without those remote storage interfaces right literally from the beginning of the prome the developers like Julius like 11 years ago Issue Number 10 were thinking about how promus can integrate with other Storage Solutions um and back then I found mentions about influx DB and open DB in particular and such need of this remote storage inter integration shouldn't come as a surprise right pruse by Design uh it's it's a single node and it doesn't have any replication or clustering um so those comes handy this is why the younger Protocol remote read was introduced so any client can you know ask for some historical role metric samples in promit use format for example it was initially used to enable promql through promit use against metrics stored in different database I think it was open this DB uh as the first thing it wasn't long until the read API was also Exposed on prit use it itself right um allowing the long-term s
