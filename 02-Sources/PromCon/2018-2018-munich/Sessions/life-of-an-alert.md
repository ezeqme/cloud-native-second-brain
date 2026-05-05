---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/life-of-an-alert/
youtube_url: https://www.youtube.com/watch?v=PUdjca23Qa4
youtube_search_url: https://www.youtube.com/results?search_query=Life+of+an+Alert+PromCon+2018
video_match_score: 0.841
status: video-found
---

# Life of an Alert

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/life-of-an-alert/
- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4

## Resumo

Speaker: Stuart Nelson Alerting is a key concept to remediating issues that arise in the systems we monitor. In order to alert effectively, it's helpful to understand the concepts available in Alertmanager and how they are actually executed within the code. In this talk, I'll give a brief, high-level description of the wondrous journey an alert takes, from its triggering in Prometheus to the email in your mailbox.

## Abstract oficial

Speaker: Stuart Nelson

Alerting is a key concept to remediating issues that arise in the systems we monitor. In order to alert effectively, it's helpful to understand the concepts available in Alertmanager and how they are actually executed within the code. In this talk, I'll give a brief, high-level description of the wondrous journey an alert takes, from its triggering in Prometheus to the email in your mailbox. Then, I'll break down in-depth how alerts are ingested, grouped, and processed, including high availability mode. At the end of this exciting trip you'll understand how your configuration affects Alertmanager, what an alerting pipeline is, and why you sometimes get two emails for the same alert.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/life-of-an-alert/
- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PUdjca23Qa4
- YouTube title: PromCon 2018: Life of an Alert
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/life-of-an-alert/PUdjca23Qa4.txt
- Transcript chars: 23611
- Keywords: alerts, manager, actually, prometheus, notification, interval, sending, happens, question, firing, notifications, managers, mentioned, deduplication, inhibition, pipeline, message, labels

### Resumo baseado na transcript

hey everybody yeah as mentioned I'm Stewart Nelson I work at SoundCloud on the production engineering team where most of the time we focus on uptime availability and we also operate a lot of the infrastructure there so very briefly why does the alert manager exist so we have prometheus Prometheus is sending the alerts why can't Prometheus just integrate against all these notifiers or all these people at like pager duty that want to accept our alerts the reason is actually pretty simple if you run a Prometheus in

### Excerpt da transcript

hey everybody yeah as mentioned I'm Stewart Nelson I work at SoundCloud on the production engineering team where most of the time we focus on uptime availability and we also operate a lot of the infrastructure there so very briefly why does the alert manager exist so we have prometheus Prometheus is sending the alerts why can't Prometheus just integrate against all these notifiers or all these people at like pager duty that want to accept our alerts the reason is actually pretty simple if you run a Prometheus in H a mode which you should be doing how do you handle deduplication they would have to somehow coordinate with each other and then that would all get very very messy additionally there are a lot of core features which we'll talk about an alert manager like silencing or inhibition so between different unrelated Prometheus servers how would they handle inhibition so it's really convenient to have this alert manager thing be separate that manages all that for you all right so moving into it this is an overview of what happens to an alert so at a high level we start with the alert generator in this case it's going to be Prometheus the alert gets ingested into the alert manager from there it hops along through the alert provider it gets grouped and this grouping then moves to the notification pipeline at the end of the notification pipeline you receive your your page your slack message however it's configured but let's take a deeper dive into the alert manager and let's see what actually happens in the life of an alert so stage one so we have this alert generator prometheus multiple Prometheus servers all sending their alerts all the time to the alert manager why is it doing this basically the alert manager exists for deduplication if you have as mentioned all of these h.a servers sending all of their alerts each a Prometheus servers sending all of their alerts all the time you if you send them directly to some sort of integration such as page or duty that's gonna be a lot of alerts that's going to be a pager storm so the detector to do you what's happening here is they go into the alert manager the alert manager takes all of these potentially duplicate alerts and it merges them together so that you have just one example of by its labels and alert from there it moves into our alert moves into the alert provider which is what kind of keeps track of all this for you and moves your alert throughout the rest of the system moving on to grouping you can think
