---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Giedrius Statkevičius", "Vinted"]
sched_url: https://kccnceu2026.sched.com/event/2EF4O/accelerating-thanos-at-scale-faster-and-cheaper-queries-with-parquet-giedrius-statkevicius-vinted
youtube_search_url: https://www.youtube.com/results?search_query=Accelerating+Thanos+at+Scale%3A+Faster+and+Cheaper+Queries+With+Parquet+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Accelerating Thanos at Scale: Faster and Cheaper Queries With Parquet - Giedrius Statkevičius, Vinted

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Giedrius Statkevičius, Vinted
- Schedule: https://kccnceu2026.sched.com/event/2EF4O/accelerating-thanos-at-scale-faster-and-cheaper-queries-with-parquet-giedrius-statkevicius-vinted
- Busca YouTube: https://www.youtube.com/results?search_query=Accelerating+Thanos+at+Scale%3A+Faster+and+Cheaper+Queries+With+Parquet+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Accelerating Thanos at Scale: Faster and Cheaper Queries With Parquet.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4O/accelerating-thanos-at-scale-faster-and-cheaper-queries-with-parquet-giedrius-statkevicius-vinted
- YouTube search: https://www.youtube.com/results?search_query=Accelerating+Thanos+at+Scale%3A+Faster+and+Cheaper+Queries+With+Parquet+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PySEmqtrvL8
- YouTube title: Accelerating Thanos at Scale: Faster and Cheaper Queries With Parquet - Giedrius Statkevičius
- Match score: 0.941
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/accelerating-thanos-at-scale-faster-and-cheaper-queries-with-parquet/PySEmqtrvL8.txt
- Transcript chars: 18326
- Keywords: parquet, format, labels, queries, another, columns, gateway, reality, faster, object, storage, column, needed, metadata, graphana, prometheus, compactor, multiple

### Resumo baseado na transcript

Uh I will be talking about accelerating tanos at scale faster and cheaper curies with with parquet. Uh uh so the current format is already quite fast but with parquet we can achieve even faster queries and we can use uh much less space to store the same exact amount of data. Uh so prehistory uh Tanos also I would say Tano spearheaded the current uh way mimmer and cortex work in in the sense in in the sense that they upload objects to object storage and read off from them. So Thomas also suffers from a lot of the same problems that are mentioned in other talks. So the first one is tano store is too slow for query and don't know where the time went. Uh, Tanos compactor employs some uh, tricks or you can call them hacks to work around this problem.

### Excerpt da transcript

Hello everyone, welcome. Uh thanks for coming to listen to me. Uh I will be talking about accelerating tanos at scale faster and cheaper curies with with parquet. Uh uh so the current format is already quite fast but with parquet we can achieve even faster queries and we can use uh much less space to store the same exact amount of data. invented. We are quite huge users of Tanos. I think in the biggest region we have over 700 terabytes of metrics data over one year. So we are very excited about this project. We contribute a lot to it and I hope that you will be hooked onto it as well after this presentation. Uh so uh this is kind of like a I would say maybe even a trilogy of Sirius. So there's this one presentation uh two years ago I think by Philillip uh co-maintainer of foss who uh inspired uh our upstream work. Uh so Philillip goes into detail uh about what are the current problems of this uh tsdb format and how perk helps of it. he goes much more in depth and uh there's another presentation from last year where people from Graphana AWS and Michael from the Tanos team presented this work also but uh from the upstream Prometheus point of view but uh today we will be only talking about the Tanos specifics.

So Tanos is another project in this space and I believe uh uh yeah that after this uh you will be able to take advantage of the park format as well. Uh I will add links to these videos in the documentation uh which and and the link to documentation you will find it uh in at the end of the slides or you can just go to tanos.io O and to the store page. Uh so prehistory uh Tanos also I would say Tano spearheaded the current uh way mimmer and cortex work in in the sense in in the sense that they upload objects to object storage and read off from them. So Thomas also suffers from a lot of the same problems that are mentioned in other talks. So I will just uh quickly go over some of the issues that we have on our tracker. So the first one is tano store is too slow for query and don't know where the time went. So depending on your luck factor uh you might your queries might be quite fast or quite slow. It all depends on the form of your queries and how the data is laid out. I will explain in a bit more detail shortly what that means.

Another issue, a very old one, offset table size exceeds four bytes, symbol table size exceeds four bytes. Uh, so it is possible to lift this requirement in the old format, but we still haven't done it. Uh, Tanos compactor emplo
