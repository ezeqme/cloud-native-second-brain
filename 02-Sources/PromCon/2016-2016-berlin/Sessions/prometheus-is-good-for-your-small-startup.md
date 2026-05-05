---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/prometheus-is-good-for-your-small-startup/
youtube_url: https://www.youtube.com/watch?v=gMHa4Yh8avk
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Is+Good+for+Your+Small+Startup+PromCon+2016
video_match_score: 0.843
status: video-found
---

# Prometheus Is Good for Your Small Startup

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-is-good-for-your-small-startup/
- YouTube: https://www.youtube.com/watch?v=gMHa4Yh8avk

## Resumo

Speaker: Ignacio P. Carretero ShuttleCloud is a small startup specialized in email and contacts migrations. We are proud of having Gmail, Gcontacts and Comcast among our clients.

## Abstract oficial

Speaker: Ignacio P. Carretero

ShuttleCloud is a small startup specialized in email and contacts migrations.
We are proud of having Gmail, Gcontacts and Comcast among our clients.

You don't need to have a big fleet to embrace Prometheus. In this talk we'll
explain our journey from having near-zero monitoring to having a comfortable
cost-effective in-house monitoring stack based on Prometheus.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-is-good-for-your-small-startup/
- YouTube: https://www.youtube.com/watch?v=gMHa4Yh8avk

## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gMHa4Yh8avk
- YouTube title: PromCon 2016: Prometheus Is Good for Your Small Startup - Ignacio P. Carretero
- Match score: 0.843
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/prometheus-is-good-for-your-small-startup/gMHa4Yh8avk.txt
- Transcript chars: 23000
- Keywords: prometheus, metrics, everything, monitoring, actually, already, publisher, operation, explain, pretty, exporter, instance, another, beginning, definitely, projects, decided, wanted

### Resumo baseado na transcript

uh we've talked about a lot of user cases and a lot of big companies that use prometheus and we are not so i'm gonna explain i'm definitely not an expert i'm not even an expert on prometheus not even on monitoring but i'm gonna tell you how we started to use it and how we are using it which is not perfect and i'm here to learn a lot from you guys but i think it's interesting to well i will explain later so this is me i'm a

### Excerpt da transcript

uh we've talked about a lot of user cases and a lot of big companies that use prometheus and we are not so i'm gonna explain i'm definitely not an expert i'm not even an expert on prometheus not even on monitoring but i'm gonna tell you how we started to use it and how we are using it which is not perfect and i'm here to learn a lot from you guys but i think it's interesting to well i will explain later so this is me i'm a software developer at shadow cloud uh i'm not really active on twitter but you should definitely follow shuttle tab on shell cloud engineering and we post a lot of some technical discussions because we do some learnings and it's interesting give it a try who we are we are sharecloud we are america a startup founded in in dexter's it's an incubator in new york city you might know it and we were part of it on 2011 we have offices in chicago and madrid and it sounds big but we are actually 15 people and six engineers so that's it we basically uh offer an api for our customers to import email and contacts that's the main idea and our customers usually are isps email address book providers those are some examples before we migrate a lot of edus like harvard and stanford university we have some isps customers like time warner cable or chromecast and even google is a customer of us which we're really proud of it and some facts it's always good to share some facts gmail has already imported three million users using our api we have slas of 99.5 availability so uh we have to be really available and we fulfill them so good for us we move around six terabytes per hour and more than 12 000 migrations per day 12 million emails per day 2.5 million contacts per day well those are number and we support 247 providers so source and destination we move email and contacts from certain destinations from 247 different providers those are the numbers that's it and but as i mentioned we are only six engineers and we're not really we only have someone that's more technical in devops and but yeah we do all of us we do a little bit of everything so what you expect from this presentation i will do first some disclaimers and i'll let you know what we had on the very beginning before we had even the monitoring system so prometheus and what we did we first with prometheus and how it what everything we did wrong and why we did it and how we revamped everything what we have right now and the things we have on our backlog or that we are still working in and things we wan
