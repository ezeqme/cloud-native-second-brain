---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/two-households-both-alike-in-dignity-cortex-and-thanos/
youtube_url: https://www.youtube.com/watch?v=KmJnmd3K3Ws
youtube_search_url: https://www.youtube.com/results?search_query=Two+Households%2C+Both+Alike+in+Dignity%3A+Cortex+and+Thanos+PromCon+2019
video_match_score: 1.001
status: video-found
---

# Two Households, Both Alike in Dignity: Cortex and Thanos

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/two-households-both-alike-in-dignity-cortex-and-thanos/
- YouTube: https://www.youtube.com/watch?v=KmJnmd3K3Ws

## Resumo

Speakers: Bartlomiej Plotka and Tom Wilkie Perhaps some of the success of the original Prometheus project can be attributed to the desire to keep it simple: no dependencies, no trendy distributed systems, a single binary with a simple mission. This approach left some problems unsolved - how do you scale your Prometheus installation across multiple sites? How do you ensure your metrics are durably stored for long term analysis?

## Abstract oficial

Speakers: Bartlomiej Plotka and Tom Wilkie

Perhaps some of the success of the original Prometheus project can be attributed to the desire to keep it simple: no dependencies, no trendy distributed systems, a single binary with a simple mission. This approach left some problems unsolved - how do you scale your Prometheus installation across multiple sites? How do you ensure your metrics are durably stored for long term analysis? And how do you build a monitoring system that can transparently tolerate machine failure? In this talk, we introduce two of the most popular solutions to these problems: Cortex and Thanos. Both CNCF projects, Cortex and Thanos share many components with Prometheus, but they take a fundamentally different approach to how these pieces are joined together. This talk will help you understand the different tradeoffs these two projects have taken, give you an understanding of where each project’s strengths lie and help you decide which of these projects is best for you.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/two-households-both-alike-in-dignity-cortex-and-thanos/
- YouTube: https://www.youtube.com/watch?v=KmJnmd3K3Ws
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KmJnmd3K3Ws
- YouTube title: PromCon EU 2019: Two Households, Both Alike in Dignity: Cortex and Thanos
- Match score: 1.001
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/two-households-both-alike-in-dignity-cortex-and-thanos/KmJnmd3K3Ws.txt
- Transcript chars: 29224
- Keywords: cortex, actually, prometheus, storage, pretty, queries, cluster, object, question, questions, global, blocks, long-term, however, basically, certain, wouldn, systems

### Resumo baseado na transcript

[Music] Bartek Arctic before our to our taxes okay Julius close we didn't even do that one in school start my name is Bart vodka I'm here with Tom honky-tonk is VP product of the Gulf Anna and one of the initial authors of the cortex project and I'm a software engineer at Red Hat and one of the quadrants project so today we won't you want to walk you through those two projects thymus and cortex which I would say extends from Hughes in some way and maybe talk

### Excerpt da transcript

[Music] Bartek Arctic before our to our taxes okay Julius close we didn't even do that one in school start my name is Bart vodka I'm here with Tom honky-tonk is VP product of the Gulf Anna and one of the initial authors of the cortex project and I'm a software engineer at Red Hat and one of the quadrants project so today we won't you want to walk you through those two projects thymus and cortex which I would say extends from Hughes in some way and maybe talk when we go through you know kind of trade-offs and strengths each product project has from the very high-level overview and hopefully those will help you to choose what project to use if you are looking for the next long-term storage for example system and at the end we are planning to tell some exciting plans for the future so it's pretty cool so as the title states two households maybe two systems may be different but alike in the same way absolutely so just quick catch-up tano's was started almost two years ago by five in Reiner's who is somewhere here maybe in this venue for sure so if you keep meet him like say hello to him and and me it was almost two years ago and then yeah this year we also joined the CN CF sandbox stage on the other hand cortex was started year before tonneaus a three and a half years ago and by Tom and Judy's walls and yet they joined CNC of sandbox stage as well year before towers so okay before we move on some questions to the audience who is using tano's Wow I'm surprised okay so I hope we have nice discussion today on the party about current you know issue progress and discussions and plans for improvement so that's pretty cool who is using cortex yeah yeah and how many of them work for the farm labs anyway even even though like you you're running a huge scale so if you have any questions around that like crap tone or anyone from Ravana because that's exciting as well okay who is using Prometheus for Direction all good come to use Federation yeah that's good is first so that's pretty exciting as well okay some asking because going to share what are the girls who want to solve what we're actually the goals we wanted to solve where we designing the those post systems and what did we yeah what do you want to solve the session so probably everyone is familiar with those you know three dreams every prom to use user have any of your ability system actually have one to that right so first of all global view right so you know ability to do queries and aggravations over the data f
