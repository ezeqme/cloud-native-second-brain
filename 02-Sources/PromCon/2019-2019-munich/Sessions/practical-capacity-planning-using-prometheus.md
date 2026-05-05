---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/practical-capacity-planning-using-prometheus/
youtube_url: https://www.youtube.com/watch?v=swnj6KTRg08
youtube_search_url: https://www.youtube.com/results?search_query=Practical+Capacity+Planning+Using+Prometheus+PromCon+2019
video_match_score: 0.976
status: video-found
---

# Practical Capacity Planning Using Prometheus

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/practical-capacity-planning-using-prometheus/
- YouTube: https://www.youtube.com/watch?v=swnj6KTRg08

## Resumo

Speaker: Andrew Newdigate GitLab.com’s monolithic Rails application experiences high week-on-week traffic growth. To ensure availability, GitLab’s Infrastructure team track and plan ahead in order to avoid hitting capacity limits in the application, whether these limits be CPU, database connection pools, memory, storage or any number of other finite resources. Hitting these limits could result in hours, or days, of degraded service while workarounds are put in place.

## Abstract oficial

Speaker: Andrew Newdigate

GitLab.com’s monolithic Rails application experiences high week-on-week traffic growth. To ensure availability, GitLab’s Infrastructure team track and plan ahead in order to avoid hitting capacity limits in the application, whether these limits be CPU, database connection pools, memory, storage or any number of other finite resources. Hitting these limits could result in hours, or days, of degraded service while workarounds are put in place. With this in mind, the team set about building a set of tools on top of Prometheus recording rules and alerts to provide them with the information they need to be sufficiently forewarned, up to a month in advance, of potential resource saturation issues. If you’ve ever felt that you’re reactively responding to resource saturation issues, this session will provide practical examples of how we’re building a framework for resource planning into our SRE team workflow. We’ll be presenting our open-source solution and explaining how it works for us.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/practical-capacity-planning-using-prometheus/
- YouTube: https://www.youtube.com/watch?v=swnj6KTRg08
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=swnj6KTRg08
- YouTube title: PromCon EU 2019: Practical Capacity Planning Using Prometheus
- Match score: 0.976
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/practical-capacity-planning-using-prometheus/swnj6KTRg08.txt
- Transcript chars: 25717
- Keywords: saturation, resource, application, metrics, started, actually, always, capacity, getting, second, wanted, prometheus, metric, instance, linear, question, everything, another

### Resumo baseado na transcript

[Music] my name's and you need agates I am in the infrastructure group at gitlab and most of what I do there is focus will get live calm and try to keep it up and running so this talk is about capacity planning and the reason we started thinking about capacity planning was to avoid resource a aeration so I guess the question is what is resource a ation and probably the best way to illustrate this is by walking through an incident that we experienced on gitlab comm which system and it's designed to alert us to potential issues and it ranked those by severity so the most severe come up at the top and then we can look from there and this is a it's helps us to prioritize work in our system and it's early days but this method is actually giving us a lot of insight into it what we need to work on and where we have resource saturation problems are coming so of course get lab is open so if you're interested in finding

### Excerpt da transcript

[Music] my name's and you need agates I am in the infrastructure group at gitlab and most of what I do there is focus will get live calm and try to keep it up and running so this talk is about capacity planning and the reason we started thinking about capacity planning was to avoid resource a aeration so I guess the question is what is resource a ation and probably the best way to illustrate this is by walking through an incident that we experienced on gitlab comm which was caused by resource saturation and an actual factor was one of several incidents that we saw that happened within a short period of time and they were all related to saturation problems and this led us to thought to start thinking about this problem in a little bit more detail so it all started with this graph just by the way I think it'd be really useful if we could get animated gifs ingre fauna I don't have Thompson but it would be a super useful type of annotation so this is the optics core of our web service so it measures the percentage of requests that complete within a satisfactory amount of time so with app tech schools hires better and the red line like right near the top is is our SLO for that metric and so when the when the metric goes below the red line we start getting alerted and so what you can see is that our licensees like rapidly shut up and our app decks tumbled and we started getting alerted a lot and what we're sort of seeing was major slowdowns on our web endpoint we started seeing similar slow dance on our API fleet a background processing started getting really bad and we were getting a lot of notifications and pages so we know if the problem down to our Redis caching fleet now some of you may know Redis is a single single threaded server and this means that it can only scale vertically on a single rate on a single call on a single machine and that's as much capacity as you can get from from a single Redis instance and so our Redis cash runs on Google card instances on n1 standard four machines and these are the four cores but Redis can only use one of those cause so the average CPU on the machine was actually pretty low but somewhere around 30% but Redis was pinned at 100% basically on one of those cores so we needed to figure out why this Redis instance had slowly started acting up and causing us so many problems and so we went through the checklist of of all the usual suspects that caused these kind of problems and obviously the the first one that we always loo
