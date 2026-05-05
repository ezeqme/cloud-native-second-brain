---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/promql-for-mere-mortals/
youtube_url: https://www.youtube.com/watch?v=hTjHuoWxsks
youtube_search_url: https://www.youtube.com/results?search_query=PromQL+for+Mere+Mortals+PromCon+2019
video_match_score: 0.872
status: video-found
---

# PromQL for Mere Mortals

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/promql-for-mere-mortals/
- YouTube: https://www.youtube.com/watch?v=hTjHuoWxsks

## Resumo

Speaker: Ian Billett PromQL can feel intimidating at first for those new to the Prometheus ecosystem, but it is an essential skill to learn when starting out monitoring and alerting in the Prometheus ecosystem. In this beginner-focused, demo-driven talk Ian Billett will walk through the thought processes, mental models and coping strategies he uses to tame PromQL and effectively query metrics data. We will demystify instant vector selectors from range vector selectors, understand how aggregate functions work, and, time-permitting, even touch on some PromQL engine internals.

## Abstract oficial

Speaker: Ian Billett

PromQL can feel intimidating at first for those new to the Prometheus ecosystem, but it is an essential skill to learn when starting out monitoring and alerting in the Prometheus ecosystem. In this beginner-focused, demo-driven talk Ian Billett will walk through the thought processes, mental models and coping strategies he uses to tame PromQL and effectively query metrics data. We will demystify instant vector selectors from range vector selectors, understand how aggregate functions work, and, time-permitting, even touch on some PromQL engine internals.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/promql-for-mere-mortals/
- YouTube: https://www.youtube.com/watch?v=hTjHuoWxsks
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hTjHuoWxsks
- YouTube title: PromCon EU 2019: PromQL for Mere Mortals
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/promql-for-mere-mortals/hTjHuoWxsks.txt
- Transcript chars: 22721
- Keywords: series, operators, vectors, prompt, function, instant, vector, metrics, counter, metric, aggregation, binary, documentation, prometheus, labels, operator, counters, values

### Resumo baseado na transcript

[Music] so my name is Ian billet I'm an engineer at improbable where I work on our internal platform observability team and the title of this talk is from ql for mere mortals and this talk is about the fundamentals a prompt you are it's about helping people out there to develop the right mental models and thought processes they're going to help them really get to grips with prompt QL and this talk is primarily aimed at kind of the more the new the new people in the ecosystem

### Excerpt da transcript

[Music] so my name is Ian billet I'm an engineer at improbable where I work on our internal platform observability team and the title of this talk is from ql for mere mortals and this talk is about the fundamentals a prompt you are it's about helping people out there to develop the right mental models and thought processes they're going to help them really get to grips with prompt QL and this talk is primarily aimed at kind of the more the new the new people in the ecosystem but I hope that even the more experienced among you can take something away and so this talk is gonna be full of mistakes that I've made which is good and if any of you go away from this talk and don't make one of the mistakes that I made then this talk has been a wrong success and so this was me maybe nine ten months ago when I started out with pom QL and I'm not sure how much has changed since then so a quick agenda we're gonna start with the very basics we're going to talk about time series instant vectors range vectors and we're going to use it as a foundation to build up to talking about gauges counters operators functions then we're going to tie it all together with a demo at the end so the first thing to say is that prompt QL is important of queries alerts dashboards any anywhere in the ecosystem that requires the retrieval of metrics data will necessarily involve prompt QL in some capacity but at the same time it's an intimidating technologies alone this spicy nugget was one of the first alerting rules I had to dig into and even now I couldn't easily tell you what is going on there and in the early days of using prompt QL my workflow was very much just fine some queries kind of mash them together add some square brackets and then to keep trying that until the console stopped complaining at me this wasn't a very sophisticated approach and definitely did not demonstrate an understanding of the fundamentals of this language but in all seriousness low prompt QL is essential but it also means it's a barrier to entry to the ecosystem and we must not lose sight of that so time-series first of all so a time series is a stream of time some value pairs like this and each time series is uniquely identified by the identifier and this identifier is a set of key value pairs that looks like this in the UI which is just syntactic sugar for a kind of a I think it is just like adjacent objects basically so when you set off on your adventure into the prompt QL documentation the first thing you bu
