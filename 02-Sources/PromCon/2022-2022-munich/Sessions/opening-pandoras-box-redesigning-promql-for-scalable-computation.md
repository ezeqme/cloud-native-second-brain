---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Cost Optimization", "Community"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/opening-pandoras-box-redesigning/
youtube_url: https://www.youtube.com/watch?v=kmXUupTj4Y0
youtube_search_url: https://www.youtube.com/results?search_query=Opening+Pandora%E2%80%99s+Box%3A+Redesigning+PromQL+for+Scalable+Computation+PromCon+2022
video_match_score: 1.02
status: video-found
---

# Opening Pandora’s Box: Redesigning PromQL for Scalable Computation

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Cost Optimization]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/opening-pandoras-box-redesigning/
- YouTube: https://www.youtube.com/watch?v=kmXUupTj4Y0

## Resumo

Speaker(s): Bartłomiej Płotka & Filip Petkovski Thanks to projects like Thanos, Mimir and Cortex, the ecosystem can ingest large amounts of Prometheus metrics and retain them for long periods of time. Although storing large amounts of data is feasible today at a fairly low cost, querying such volumes of data efficiently and within reasonable time is still quite challenging. A central piece to this problem is that most of the metrics systems in the Prometheus ecosystem import the PromQL engine from Prometheus itself.

## Abstract oficial

Speaker(s): Bartłomiej Płotka & Filip Petkovski

Thanks to projects like Thanos, Mimir and Cortex, the ecosystem can ingest large amounts of Prometheus metrics and retain them for long periods of time. Although storing large amounts of data is feasible today at a fairly low cost, querying such volumes of data efficiently and within reasonable time is still quite challenging.

A central piece to this problem is that most of the metrics systems in the Prometheus ecosystem import the PromQL engine from Prometheus itself. While this engine has had many optimizations over the past years, it is primarily designed to be executed in a single-threaded, single-node environment. This design decision puts a hard scalability limit on how quickly and efficiently a single query can be executed.

In this talk, Filip and Bartek will show the open-source PromQL query engine that the Thanos Community has been developing over the past several months. They will demonstrate how we achieved extreme latency and efficiency improvements by utilizing multiple cores on multiple machines. The audience will learn about the architecture of the new engine, how they can start using it in production in all projects (not only Thanos!), how to contribute and what we might see in the future.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/opening-pandoras-box-redesigning/
- YouTube: https://www.youtube.com/watch?v=kmXUupTj4Y0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kmXUupTj4Y0
- YouTube title: PromCon EU 2022: Opening Pandora’s Box: Redesigning PromQL for Scalable Computation
- Match score: 1.02
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/opening-pandoras-box-redesigning-promql-for-scalable-computation/kmXUupTj4Y0.txt
- Transcript chars: 30724
- Keywords: engine, prometheus, operator, memory, basically, series, essentially, storage, actually, thanos, selector, already, execution, simply, design, second, expression, binary

### Resumo baseado na transcript

[Music] foreign [Music] can you hear me well now okay sorry hi welcome everyone um we are super excited to be here um I think what is like first in-person program after covered lockdown so it's super amazing um and and to see you know all those familiar faces and new faces in the community um today we would like to discuss um uh you know like a new open source initiative that we uh that we are kind of doing in premature ecosystem so our new open source experimental

### Excerpt da transcript

[Music] foreign [Music] can you hear me well now okay sorry hi welcome everyone um we are super excited to be here um I think what is like first in-person program after covered lockdown so it's super amazing um and and to see you know all those familiar faces and new faces in the community um today we would like to discuss um uh you know like a new open source initiative that we uh that we are kind of doing in premature ecosystem so our new open source experimental promptual engine what's funny is that I don't think we we thought that we'll be working on this two months ago so it's very fresh idea but we are working on it and and we are super excited about the initial results so this is why we are here we would love to share with you um you know a couple of a couple of details first of all why are we even developing this was the design how you can contribute and generally we'll yeah we'll try to finish with some live demo if if time will allow before short introduction I have Philip with me today no we don't have Philip now we have Philip hi yes hi everyone my name is Philip I'm based here in Munich actually so it's a bit strange not to travel for a conference but it is what it is I currently work as a production engineer at Shopify I'm a Thanos team member and also help maintain The Primitives operator and keep State metrics thanks my name is you can call me bartek I work with red hat I maintain couple of things including Primitives Thanos and lots of golang projects I am active in the cncf and I recently wrote a book it's going to be printed like literally this week so it's done it's efficient go about go like and writing efficient go code but it's kind of like language agnostic lots of lots of chapters are just about optimization observability and so on so yeah if you're interested uh link is there but we are here to talk about prom ql so I'm kind of grateful that we are in a prom con where I don't need to introduce this but generally this is a Prometheus query language and it's everywhere right it's beautiful it's powerful it's flexible Martin mentioned that some people like it some people hate it I don't think I remember anyone hate it so um if you if you hate it let me know but it's it's generally likable um and many vendors supports that right and this is kind of the proof of the of the you know wide adoption you know every cloud provider almost all of them supports some kind of like language integration right including Google logs IO Amazon IBM eve
