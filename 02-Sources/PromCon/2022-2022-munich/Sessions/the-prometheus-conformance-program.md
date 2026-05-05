---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/the-prometheus-conformance/
youtube_url: https://www.youtube.com/watch?v=u_Mfa0OfSBo
youtube_search_url: https://www.youtube.com/results?search_query=The+Prometheus+Conformance+Program+PromCon+2022
video_match_score: 0.94
status: video-found
---

# The Prometheus Conformance Program

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/the-prometheus-conformance/
- YouTube: https://www.youtube.com/watch?v=u_Mfa0OfSBo

## Resumo

Speaker(s): Richard Hartmann Join us for an update on the Prometheus conformance program. What did we do, where are we at, and what are the next steps?

## Abstract oficial

Speaker(s): Richard Hartmann

Join us for an update on the Prometheus conformance program. What did we do, where are we at, and what are the next steps?

## Links

- Página oficial: https://promcon.io/2022-munich/talks/the-prometheus-conformance/
- YouTube: https://www.youtube.com/watch?v=u_Mfa0OfSBo
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=u_Mfa0OfSBo
- YouTube title: PromCon EU 2022: The Prometheus Conformance Program
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/the-prometheus-conformance-program/u_Mfa0OfSBo.txt
- Transcript chars: 8630
- Keywords: prometheus, compatible, actually, little, program, relatively, companies, conformance, trademark, numbers, initially, basically, against, foundation, company, grafana, market, figure

### Resumo baseado na transcript

[Music] foreign [Music] okay so this is going to be relatively short because it is initially like a few people cancel at the last minute blah blah blah long story short uh we didn't even plan to have this as a full talk uh thank you bartik for putting me on stage um so yeah this is an update on on the conformance program why do we want to have a conformance program well I don't have to convince this room that promises is The Defector standard in Cloud native

### Excerpt da transcript

[Music] foreign [Music] okay so this is going to be relatively short because it is initially like a few people cancel at the last minute blah blah blah long story short uh we didn't even plan to have this as a full talk uh thank you bartik for putting me on stage um so yeah this is an update on on the conformance program why do we want to have a conformance program well I don't have to convince this room that promises is The Defector standard in Cloud native metric based monitoring and and has set the scene for for basically the whole industry we have hundreds of thousands of installations millions of users the market segment which which Prometheus defines as per Gardner and all those others is literally billions and billions of Revenue per year which is quite a scary large number to think about and at the core it is really really easy to say you are compatible it's a lot harder to actually be compatible in particular when it comes down to the nitty-gritty details of how a specific function behaves or how that one value is returned and it's hard for people to um to figure this out on their own and it's hard for people to uh to do the same research again and again and then you have it through the gray point it's also simply unfair so there might be confusion sometimes deliberate sometimes not deliberate but in the end there is confusion that is why we felt forced to to go down this path how this works we have a repository where you have a set of tests which can be run against against your implementation against your cloud provider by the cloud provider internally we saw a little bit about this for the alert manager generator or alert generator compliance yesterday and this is only half of it because like for us the tech is interesting but that's actually not the not the thing which really bites so on the other side cncf or to be to be more precise the Linux Foundation because cncf is is not really its own legal thing it is the Linux Foundation which is actually standing behind all of this which also holds the trademarks like if you want to use the Prometheus trademarker so you always end up at the Linux foundation not at the cncf which most people don't know I just find it funny and amusing um or interesting to to be precise so the thing is by introducing a new trademark you can Define who is allowed to use that trademark for Prometheus It's relatively easy you can use it for descriptive use you cannot say blah blah blah Prometheus or the blah blah blah Pro
