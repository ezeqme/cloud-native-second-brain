---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2024"
edition_id: 2024-berlin
year: 2024
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Community"]
speakers: ["Jan Fajerski"]
source_url: https://promcon.io/2024-berlin/talks/prometheus-30-overview/
youtube_url: https://www.youtube.com/watch?v=2pC38yWxanM
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+3.0+Overview+PromCon+2024
video_match_score: 0.91
status: video-found
---

# Prometheus 3.0 Overview

## Identificação

- Edição: PromCon EU 2024
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Community]]
- Speakers: Jan Fajerski
- Página oficial: https://promcon.io/2024-berlin/talks/prometheus-30-overview/
- YouTube: https://www.youtube.com/watch?v=2pC38yWxanM

## Resumo

This session will take a close look at what Prometheus 3 will be. I will outline what motivated a new major version, highlight major changes and features and we'll look at how this changes the community.

## Abstract oficial

This session will take a close look at what Prometheus 3 will be. I will outline what motivated a new major version, highlight major changes and features and we'll look at how this changes the community.

## Links

- Página oficial: https://promcon.io/2024-berlin/talks/prometheus-30-overview/
- YouTube: https://www.youtube.com/watch?v=2pC38yWxanM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2pC38yWxanM
- YouTube title: PromCon 2024 - Prometheus 3.0 Overview
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2024/prometheus-3-0-overview/2pC38yWxanM.txt
- Transcript chars: 21452
- Keywords: prometheus, couple, release, changes, course, little, otel, already, members, metrics, change, remote, commits, actually, around, usually, support, native

### Resumo baseado na transcript

[Music] okay um welcome to uh Prometheus 3 overview um first of all maybe thanks Matias thanks polar signals for organizing yet a fantastic promcon I'm already looking forward to all the sessions um that's no no easy job so uh be be sure to thanks thank them when you see them uh my name is Yan um I've been a longtime Prometheus user I've actually installed I think 1.7 or 1.8 first um and never uninstalled it uh and running and uh for the past couple of years um

### Excerpt da transcript

[Music] okay um welcome to uh Prometheus 3 overview um first of all maybe thanks Matias thanks polar signals for organizing yet a fantastic promcon I'm already looking forward to all the sessions um that's no no easy job so uh be be sure to thanks thank them when you see them uh my name is Yan um I've been a longtime Prometheus user I've actually installed I think 1.7 or 1.8 first um and never uninstalled it uh and running and uh for the past couple of years um I've Had The Good Fortune to actually work with and around Prometheus uh and uh Red Hat actually pays me for the privilege so that's very nice uh yeah and today I have the honor um to present the the good work of um a lot of people not me really but uh you know the Prometheus team um and yeah we'll have a look at um what Prometheus 3 is and what the team has been doing for Prometheus 3 all right so the plan um bonus points who knows what that subtitle means but only people who weren't there for that so uh let's see um so this is a picture uh from the de Summit September 23 this was uh just after promcon 23 if you don't know what a def Summit is um it's where the Prometheus Community comes together it's usually once a month um there's agenda items that can be proposed by anyone um the discussion can be um led by anyone so everybody's welcome to sort of add discussion topics there and usually these discussions are included um by a call for consensus um and that's then only for the team members where they decide on what to do with a particular topic so um on this U maybe fateful uh death Summit there were uh two uh two agreements um these two here so um one is that Prometheus should really become the default Choice uh to store open Telemetry metrics and the second one is kind of um a synthesis of several um I just added that here for for succinctness um and that's the intention to release Prometheus 3.0 this year um so this this sort of um plotline of open Telemetry compatibility um is going to follow us through this talk I do want to make sure um to mention that um most if not all of these features really um stand by themselves right um they they also support um oel compatibility but um they're by no means just motivated purely by that um just so that nobody gets the wrong impression here um a couple more words on on y 3.0 um there is you know we could have just gone with the 2.x releases um Prometheus is um a mature software right a grown-up software it's been around for 12 years almost it'll be end
