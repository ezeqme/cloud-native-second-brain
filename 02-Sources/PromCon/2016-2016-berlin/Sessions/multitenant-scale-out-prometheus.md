---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Alerting", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/multitenant-scale-out-prometheus/
youtube_url: https://www.youtube.com/watch?v=3Tb4Wc0kfCM
youtube_search_url: https://www.youtube.com/results?search_query=Multitenant%2C+Scale-Out+Prometheus+PromCon+2016
video_match_score: 0.857
status: video-found
---

# Multitenant, Scale-Out Prometheus

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Alerting]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/multitenant-scale-out-prometheus/
- YouTube: https://www.youtube.com/watch?v=3Tb4Wc0kfCM

## Resumo

Speaker: Tom Wilkie In this talk we'll present a prototype solution for multitenant, scale-out Prometheus. Our solution turns a lot of the Prometheus architectural assumptions on its head, by marrying a scale-out PromQL query engine with a storage layer based on DynamoDB. We have disaggregated the Prometheus binary into a microservices-style architecture, with separate services for query, ingest, alerting rules and storage.

## Abstract oficial

Speaker: Tom Wilkie

In this talk we'll present a prototype solution for multitenant, scale-out
Prometheus.

Our solution turns a lot of the Prometheus architectural assumptions on its
head, by marrying a scale-out PromQL query engine with a storage layer based
on DynamoDB. We have disaggregated the Prometheus binary into a
microservices-style architecture, with separate services for query, ingest,
alerting rules and storage. By designing all these services as fungible
replicas, this solution can be scaled out with ease and failure of any
individual replica can be dealt with gracefully.

This multitenant, scale-out Prometheus service forms a core component of the
Weave Service, a hosted management, monitoring and visualisation platform for
microservice & containerised applications. This platform is built from 100%
open source components, and we're working with the Prometheus community to
contribute all the changes we've made back to Prometheus.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/multitenant-scale-out-prometheus/
- YouTube: https://www.youtube.com/watch?v=3Tb4Wc0kfCM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3Tb4Wc0kfCM
- YouTube title: PromCon 2016: Multitenant, Scale-Out Prometheus - Tom Wilkie
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/multitenant-scale-out-prometheus/3Tb4Wc0kfCM.txt
- Transcript chars: 31816
- Keywords: prometheus, actually, queries, running, source, distributor, dynamodb, pretty, probably, started, retriever, memory, julius, everything, wanted, scheme, months, hopefully

### Resumo baseado na transcript

thank you brian um yes well as brian my name is tom wilkie i work for weworks as a software engineer and we have bunch of stuff a lot of irons in the fire but today i'm really talking about this project frankenstein um julius's name is up here because julius has actually been working with me on it for about two months um so you know this is really what's made it possible first off i'd like to start with questions right now put your hands down if you're what are we going to do next well i we very much intend to continue working on this we currently don't support recording rules and we don't do alerting so that's very much the next thing i'm going to do and that's i think once we've got recording rules and alerting then we're going to start using this as our main monitoring system and really dog fooding it then reliability you know there's a long list of things we need to do we need to implement replication we need to

### Excerpt da transcript

thank you brian um yes well as brian my name is tom wilkie i work for weworks as a software engineer and we have bunch of stuff a lot of irons in the fire but today i'm really talking about this project frankenstein um julius's name is up here because julius has actually been working with me on it for about two months um so you know this is really what's made it possible first off i'd like to start with questions right now put your hands down if you're not using containers and okay how about using you know i mean docker containers now your hands down and in production if you're not using introduction put your hands down oh wow so a lot of a lot of containers that's good okay so now keep your hands up good now if you're using kubernetes put your hands down if you're not rather sorry okay how about introduction hands down if you're not using kubernetes in production so some of us actually use too much to keep my hand up okay all right now keep your hands up who's heard of weave other than obviously plastic classical over this event again who's actually used it okay great well that's that's audience participation over you can go absolutely the other question i get about this project is where does the name come from um so one evening i went home to my girlfriend and said i'm working on this new exciting project uh it's called prometheus and we're gonna be doing some really cool stuff yeah i need a name and she's been a literary buff and she came up with frankenstein because apparently the subtitle is a modern prometheus i think that's awfully like you know setting expectations really hard so that's why the name um and about one one sentence about the company this is kind of our thing about being the best way to visualize manage monitor your clarinet applications so um that kind of is a way we try and unify everything we do to do some different things anyway so we started off the journey started off with this thing called weak scope um this is a uh visualization tool for cloud native applications for resource docker blah blah blah and as you can see we started gathering some metrics in scope um it's really really basic don't really do anything special and i thought you know we'll leave this for the experts at some point then next we've built a hosted version of scope called wii cloud um it's pretty cool we're gonna try it out and you know finally we got this launched dockercon two months ago and finally it's now time to focus on the metrics bit that we said we'
