---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Alerting"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/life-of-a-label/
youtube_url: https://www.youtube.com/watch?v=PUdjca23Qa4
youtube_search_url: https://www.youtube.com/results?search_query=Life+of+a+Label+PromCon+2016
video_match_score: 0.675
status: video-found
---

# Life of a Label

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Alerting]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/life-of-a-label/
- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4

## Resumo

Speaker: Brian Brazil Labels are at the core of Prometheus's dimensional data model. The Prometheus server and its surrounding ecosystem components all either attach, modify, or act on labels in various ways. In this talk, Brian explains the entire life cycle of labels, including their generation in the client libraries, their transformation in relabeling, as well as their use in service discovery and alerting.

## Abstract oficial

Speaker: Brian Brazil

Labels are at the core of Prometheus's dimensional data model. The Prometheus
server and its surrounding ecosystem components all either attach, modify, or
act on labels in various ways. In this talk, Brian explains the entire life
cycle of labels, including their generation in the client libraries, their
transformation in relabeling, as well as their use in service discovery and
alerting.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/life-of-a-label/
- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4
- YouTube title: PromCon 2018: Life of an Alert
- Match score: 0.675
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/life-of-a-label/PUdjca23Qa4.txt
- Transcript chars: 23611
- Keywords: alerts, manager, actually, prometheus, notification, interval, sending, happens, question, firing, notifications, managers, mentioned, deduplication, inhibition, pipeline, message, labels

### Resumo baseado na transcript

hey everybody yeah as mentioned I'm Stewart Nelson I work at SoundCloud on the production engineering team where most of the time we focus on uptime availability and we also operate a lot of the infrastructure there so very briefly why does the alert manager exist so we have prometheus Prometheus is sending the alerts why can't Prometheus just integrate against all these notifiers or all these people at like pager duty that want to accept our alerts the reason is actually pretty simple if you run a Prometheus in

### Excerpt da transcript

hey everybody yeah as mentioned I'm Stewart Nelson I work at SoundCloud on the production engineering team where most of the time we focus on uptime availability and we also operate a lot of the infrastructure there so very briefly why does the alert manager exist so we have prometheus Prometheus is sending the alerts why can't Prometheus just integrate against all these notifiers or all these people at like pager duty that want to accept our alerts the reason is actually pretty simple if you run a Prometheus in H a mode which you should be doing how do you handle deduplication they would have to somehow coordinate with each other and then that would all get very very messy additionally there are a lot of core features which we'll talk about an alert manager like silencing or inhibition so between different unrelated Prometheus servers how would they handle inhibition so it's really convenient to have this alert manager thing be separate that manages all that for you all right so moving into it this is an overview of what happens to an alert so at a high level we start with the alert generator in this case it's going to be Prometheus the alert gets ingested into the alert manager from there it hops along through the alert provider it gets grouped and this grouping then moves to the notification pipeline at the end of the notification pipeline you receive your your page your slack message however it's configured but let's take a deeper dive into the alert manager and let's see what actually happens in the life of an alert so stage one so we have this alert generator prometheus multiple Prometheus servers all sending their alerts all the time to the alert manager why is it doing this basically the alert manager exists for deduplication if you have as mentioned all of these h.a servers sending all of their alerts each a Prometheus servers sending all of their alerts all the time you if you send them directly to some sort of integration such as page or duty that's gonna be a lot of alerts that's going to be a pager storm so the detector to do you what's happening here is they go into the alert manager the alert manager takes all of these potentially duplicate alerts and it merges them together so that you have just one example of by its labels and alert from there it moves into our alert moves into the alert provider which is what kind of keeps track of all this for you and moves your alert throughout the rest of the system moving on to grouping you can think
