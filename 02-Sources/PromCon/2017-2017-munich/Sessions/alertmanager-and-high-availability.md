---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/alertmanager-and-high-availability/
youtube_url: https://www.youtube.com/watch?v=i6Hmc0bKHAY
youtube_search_url: https://www.youtube.com/results?search_query=Alertmanager+and+High+Availability+PromCon+2017
video_match_score: 0.817
status: video-found
---

# Alertmanager and High Availability

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/alertmanager-and-high-availability/
- YouTube: https://www.youtube.com/watch?v=i6Hmc0bKHAY

## Resumo

Speaker: Frederic Branczyk The Alertmanager is a highly critical component in the monitoring pipeline. Operators must trust it to be a reliable component. Thus in the 0.5 release of the Alertmanager a high availability mode has been implemented.

## Abstract oficial

Speaker: Frederic Branczyk

The Alertmanager is a highly critical component in the monitoring pipeline. Operators must trust it to be a reliable component. Thus in the 0.5 release of the Alertmanager a high availability mode has been implemented. This talk will go over some implementation details of the high availability mode as well as highlight what this means for operators using and running the Alertmanager.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/alertmanager-and-high-availability/
- YouTube: https://www.youtube.com/watch?v=i6Hmc0bKHAY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=i6Hmc0bKHAY
- YouTube title: PromCon 2017: Alertmanager and High Availability - Frederic Branczyk
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/alertmanager-and-high-availability/i6Hmc0bKHAY.txt
- Transcript chars: 20216
- Keywords: manager, actually, prometheus, notification, alerts, instances, availability, already, database, notifications, gossip, basically, silence, question, simple, received, notified, seconds

### Resumo baseado na transcript

[Music] my name is ben kochi I'm gonna MC this afternoon and our first speaker is Frederick Brent chick from core OS and he's going to talk about alert manager and high availability he's got a background in distributed systems and rely really has some experience and reliability so it should be a great great talk about the alert manager thanks Ben for the introduction so yeah I'll be talking about alert manager and high availability we've actually already heard about the feature itself a couple times today and today

### Excerpt da transcript

[Music] my name is ben kochi I'm gonna MC this afternoon and our first speaker is Frederick Brent chick from core OS and he's going to talk about alert manager and high availability he's got a background in distributed systems and rely really has some experience and reliability so it should be a great great talk about the alert manager thanks Ben for the introduction so yeah I'll be talking about alert manager and high availability we've actually already heard about the feature itself a couple times today and today I want to bring some light into the darkness of this dark magic how it actually works and what that means for us running alert manager and veil abilities yeah I'm an engineer at chorus and I work on upstream prometheus alert manager and kubernetes and like everything that connects the two worlds so yeah which is which brings me to something that I want to bring up front why does Korres invest in Prometheus and the community that's myth because of our enterprise coronaries offering tech tonic which basically has Prometheus monitoring fully automated so that you can focus on building your product rather than monitoring infrastructure so what will I be talking about today in terms of high availability so I want to talk about how Prometheus how we get from Prometheus generating alerts to alert manager receiving those then the high availability contract between those two applications then how that how that actually works and what that means in terms of implications for us running the alert manager and high availability so we've already heard this somewhat and there's also a non-exhaustive list but the main features of alert manager is that it receives and groups alerts into a meaningful message or notification it deduplicate those so that we don't get notified every 30 seconds or however often Prometheus sends those alerts to alert monitor but in a reasonable time span so that we can actually fix these problems that are occur rather than just get alert fatigue and then it has routing so that we can say for this particular service we want this team to receive for the notification on slack or be a pager duty or all the other integrations that alert manager has built in and beyond that the alert manager also has silencing so when if we know that there is a maintenance window where we know our application is going to behave in a different way or there are all kinds of situations where you might want to mute an alert firing then that's where you want to u
