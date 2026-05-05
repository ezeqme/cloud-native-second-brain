---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/prometheus-histograms-past-present-and-future/
youtube_url: https://www.youtube.com/watch?v=7sQFkaMCyEI
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Histograms+%E2%80%93+Past%2C+Present%2C+and+Future+PromCon+2019
video_match_score: 0.979
status: video-found
---

# Prometheus Histograms – Past, Present, and Future

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/prometheus-histograms-past-present-and-future/
- YouTube: https://www.youtube.com/watch?v=7sQFkaMCyEI

## Resumo

Speaker: Björn Rabenstein Representing distributions in a metrics-based monitoring system is both important and hard. Doing it right unlocks many powerful use cases. What does Prometheus offer in this regard?

## Abstract oficial

Speaker: Björn Rabenstein

Representing distributions in a metrics-based monitoring system is both important and hard. Doing it right unlocks many powerful use cases. What does Prometheus offer in this regard? And what are the pitfalls with the current state of the art? To help understand the present, this talk will also shed light on the past. How have the Histogram and Summary metric types become what they are today with all their weal and woe? Finally, let's have a look at the rich body of research happening in the area, and how it might benefit future versions of Prometheus.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/prometheus-histograms-past-present-and-future/
- YouTube: https://www.youtube.com/watch?v=7sQFkaMCyEI
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7sQFkaMCyEI
- YouTube title: PromCon EU 2019: Prometheus Histograms – Past, Present, and Future
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/prometheus-histograms-past-present-and-future/7sQFkaMCyEI.txt
- Transcript chars: 27442
- Keywords: bucket, histogram, pockets, histograms, metrics, prometheus, layout, format, latency, questions, whatever, already, pocket, essentially, actually, change, series, future

### Resumo baseado na transcript

[Music] yeah I would like to talk about one of my top three most favorite topics infirmities languages histograms past personal future first of all this is not a how-to there are gazillions of talks and blog posts and how to's and everything on the internet about how to use Prometheus histograms there's a lot to say about it if you haven't used them or you use them in the wrong way there's a link does that work no so there's the link to the very old but still very

### Excerpt da transcript

[Music] yeah I would like to talk about one of my top three most favorite topics infirmities languages histograms past personal future first of all this is not a how-to there are gazillions of talks and blog posts and how to's and everything on the internet about how to use Prometheus histograms there's a lot to say about it if you haven't used them or you use them in the wrong way there's a link does that work no so there's the link to the very old but still very valid best practice document on our web page and you can just take it from there I guess so the idea of this talk was to first obviously parse of histograms not so much to explain you how they work but more like why they work the way they do and I kind of was tempted to have a subtitle like secret history of Prometheus systems unfortunately that was all when I thought this talk will be 40 minutes so we have to skip the past because we have only 20 minutes there there will be I hope at some point I can give the director's cut of this talk and then I can put all the secret history in it so we have to jump to the present mostly looking at what really works well our histograms and what doesn't work that well and then of course later we look at the future what we might improve okay part one of the present what works really well I summarized it all on one slide so these questions that I have put here these are questions you might have asked what percentage of requests in the last hour got a response in 100 milliseconds or less I think this is one of the most relevant questions in observability or whatever they call it these days also like stuff like like between certain time frames this is what Prometheus histograms can do perfectly almost perfectly accurate optics if you have never heard about it you can look it up it was mentioned in one of the talks that's very similar to this same thing so these are kind of the relevant questions there are two things that are perhaps not that well-known the one thing is really important you for granted I guess as happy formative uses we can mathematically correct aggregate histograms or sometimes called they emerge about and this is what many people still get wrong like the shortest version is you cannot aggregate pre-calculated contents there are still talks and ah like like flame wars on the internet about it it's really quite amusing the other thing and this is what you might probably have missed high-frequency sampling is feasible like you could totally tell yo
