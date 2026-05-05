---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/a-worked-example-of-monitoring-a-queue-based-application/
youtube_url: https://www.youtube.com/watch?v=EtxM48cWr4Y
youtube_search_url: https://www.youtube.com/results?search_query=A+Worked+Example+of+Monitoring+a+Queue+Based+Application+PromCon+2017
video_match_score: 0.892
status: video-found
---

# A Worked Example of Monitoring a Queue Based Application

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/a-worked-example-of-monitoring-a-queue-based-application/
- YouTube: https://www.youtube.com/watch?v=EtxM48cWr4Y

## Resumo

Speaker: Laurie Clark-Michalek There has been a lot of work around educating people about how to instrument their applications, and how to set up your Prometheus installation to do tons of interesting things. This talk aims to address questions around which metrics provide the most value, and why. We will go through an example of instrumenting a service in production at Qubit, and explain the rationale behind the metrics we use for alerting and dashboarding.

## Abstract oficial

Speaker: Laurie Clark-Michalek

There has been a lot of work around educating people about how to instrument their applications, and how to set up your Prometheus installation to do tons of interesting things. This talk aims to address questions around which metrics provide the most value, and why. We will go through an example of instrumenting a service in production at Qubit, and explain the rationale behind the metrics we use for alerting and dashboarding. The aim is to give viewers a concrete example of how to monitor something, and highlight the logic behind the decisions made, be they specific to this service, or generalisable to almost anything.

Viewers should come away with the ability to implement meaningful instrumentation on their services, and a basic understanding around the answer to the questions ‘what makes a good metric’, ‘what makes a good dashboard’ and ‘what makes a good alert’. My aim is that the services that viewers write will wake people up needlessly less often, and when they wake people up, the service’s dashboards will be a boon to the responder, and not a false friend.



Video link -
Slides (external
link)

## Links

- Página oficial: https://promcon.io/2017-munich/talks/a-worked-example-of-monitoring-a-queue-based-application/
- YouTube: https://www.youtube.com/watch?v=EtxM48cWr4Y
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EtxM48cWr4Y
- YouTube title: PromCon 2017: A Worked Example of Monitoring a Queue Based Application - Laurie Clark-Michalek
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/a-worked-example-of-monitoring-a-queue-based-application/EtxM48cWr4Y.txt
- Transcript chars: 23899
- Keywords: seconds, actually, component, message, dashboard, application, monitoring, prometheus, metric, buckets, little, thinking, without, delayed, graphs, kinesis, useful, writing

### Resumo baseado na transcript

[Music] so now and Laurie Keller is going to talk about monitoring queue based applications hey so I don't have to full screen this so be able to see my Firefox head up I'm so I'm gonna give Bree f11 okay so today it's okay to have a clicky thing as well this is going well okay so I'll hit space and that should be fine okay okay cool so yeah this is placed off work I did at my previous job at qubit since left there and work at

### Excerpt da transcript

[Music] so now and Laurie Keller is going to talk about monitoring queue based applications hey so I don't have to full screen this so be able to see my Firefox head up I'm so I'm gonna give Bree f11 okay so today it's okay to have a clicky thing as well this is going well okay so I'll hit space and that should be fine okay okay cool so yeah this is placed off work I did at my previous job at qubit since left there and work at another company not philia to Eve a company giving this talk so the basic idea of what I wanna tackle is we often with the people in the room are probably the monitoring enthusiasts are various employment places there are so a lot of people there who just they want monitoring because they are decent engineers and they see it as part of the engineering process but they're not actually you know enthused about monitoring or so and so forth so part of where the way I see that a lot is that people deploy previous or you say hey I've got problems q+ evesham on to your application and then the person wearing the application then says well cool I've read the tutorial I can understand the client library what do I actually monitor and part of the way I've been thinking about this is we can kind of find application archetypes we see on the prom documentation even it talks about here's how you Montes like request space here's how you monitor something that's kind of batch and one thing we saw a lot a cubit was Cubase applications thing that things that read and write to cues so my aim is to be kind of maybe a contrast the rest of the talks I don't want to be interesting here I want to explain how you can implement monitoring without thinking can take of a methodical approach that allows you to at the end of the day have something maybe not perfect but so you can build on and without really needing to think too much about what your application is actually doing beyond that that it seems to be doing something with keys so I'm gonna use that use an example I cube it we have this thing called stash the third and it tackled the complicated use case of I want to do something but in a bit so you would say hey can you send me I want to send you this message but here's a time standpoint I want to send it to you so kind of a big priority queue and so in from this in standard way we spun the big wheel of technologies and the mark I landed on BigTable so we had an API that wrote stuff into BigTable and then we spun the wheel again and then it landed on Kine
