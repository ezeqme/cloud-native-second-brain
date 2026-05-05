---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/full-stack-metrics-with-tritons-native-prometheus-support/
youtube_url: https://www.youtube.com/watch?v=X8QV9HgPNbc
youtube_search_url: https://www.youtube.com/results?search_query=Full+Stack+Metrics+with+Triton%27s+Native+Prometheus+Support+PromCon+2016
video_match_score: 0.888
status: video-found
---

# Full Stack Metrics with Triton's Native Prometheus Support

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Metrics]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/full-stack-metrics-with-tritons-native-prometheus-support/
- YouTube: https://www.youtube.com/watch?v=X8QV9HgPNbc

## Resumo

Speaker: Richard Kiene / Tim Gross Triton is the open source data center automation solution that powers public cloud and private data centers world-wide. In early 2016, Joyent undertook a project to expose infrastructure and system for every instance — including infrastructure containers, Docker containers, and hardware virtual machines — using a Prometheus-compatible agent. The project, called Triton Container Monitor and described in our public request for discussion, https://github.com/joyent/rfd/blob/master/rfd/0027/README.md, takes advantage of container-native architecture, kstats, and other native introspection tools.

## Abstract oficial

Speaker: Richard Kiene /
 Tim Gross

Triton is the open source data center automation solution that powers public
cloud and private data centers world-wide. In early 2016, Joyent undertook a
project to expose infrastructure and system for every instance — including
infrastructure containers, Docker containers, and hardware virtual machines —
using a Prometheus-compatible agent. The project, called Triton Container
Monitor and described in our public request for discussion,
https://github.com/joyent/rfd/blob/master/rfd/0027/README.md, takes advantage
of container-native architecture, kstats, and other native introspection
tools.

Additionally, developers need tools to expose up-stack application metrics to
Prometheus. ContainerPilot, the open source, application-centric
micro-orchestrator that makes it easy to build and operate portable
application containers, now features a Prometheus-compatible telemetry
interface to monitor application performance with user-defined probes. This
interface brings monitoring directly to the container and eliminates the
dependence on complex host monitoring for application-specific details.

In this session, Container Monitor lead engineer Richard Kiene will discuss
the challenges and successes of implementing Prometheus as a native interface
in Triton, and ContainerPilot lead engineer Tim Gross will demonstrate
ContainerPilot telemetry and discuss the application-level decisions around
defining metrics to drive application scaling.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/full-stack-metrics-with-tritons-native-prometheus-support/
- YouTube: https://www.youtube.com/watch?v=X8QV9HgPNbc
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=X8QV9HgPNbc
- YouTube title: PromCon 2016: Full Stack Metrics with Triton's Native Prometheus Support - Richard Kiene, Tim Gross
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/full-stack-metrics-with-tritons-native-prometheus-support/X8QV9HgPNbc.txt
- Transcript chars: 21973
- Keywords: container, prometheus, actually, application, metric, metrics, running, containers, server, console, triton, little, talking, customers, discovery, important, production, public

### Resumo baseado na transcript

and we work for joyant uh which uh as we were just told uh we build infrastructure and data center software uh we've been container native since 2006 uh we we operate a public cloud with global data centers and the software that powers our cloud is open source so that you can run your private data center using the same software that we're running in our public cloud and that's important because uh and it's important for me to tell you that because of what we're going to be server wherever you put that um or if you're not using Prometheus and you want to push it somewhere else you can spin up a forwarder essentially some app that we or you have written which speaks to Prometheus server and then shuttles it on

### Excerpt da transcript

and we work for joyant uh which uh as we were just told uh we build infrastructure and data center software uh we've been container native since 2006 uh we we operate a public cloud with global data centers and the software that powers our cloud is open source so that you can run your private data center using the same software that we're running in our public cloud and that's important because uh and it's important for me to tell you that because of what we're going to be talking about today um I'm also going to take this opportunity to point out that we were just recently acquired by Samsung and we're going to be building uh new data centers and one of the largest Docker installations in the world so if that sort of thing is interesting to you we're hiring okay let's take a step back a little bit away from Prometheus per se and kind of get like one level up from that right so so with the rise of containers and this like model that we call microservices um suddenly we're finding that everybody is building distributed systems right the complexity of what we're trying to monitor has gone up a lot uh and these distributed system are harder to observe and to debug than anything that we built say just 10 years ago when joint CTO was saying things like this so and what's more a lot of the problems that we're facing are actually originating upstack from where we're monitoring right so like we get monitoring and alerts on like CPU percentage or which is not actually the Cause right it's the symptom that we're seeing and the cause is somewhere upstack it's it's it's in our um in this really large pile of abstractions that we have so our language run times our stand standard libraries the uh the application VM the application framework uh and of course our the crappy application code we all write so and because these problems are because these uh systems are distributed many of the most difficult problems to solve we're only ever going to see in production um which means we need to be able to debug our production environments not just what's happening on my laptop um and so to debug in production means debugging safely right so we can't if we if we uh if our systems crash when we debug them that doesn't work right that now we can't we we will be afraid to debug in production uh also if observing the system changes its behavior um which you know kind of in a hegelian sort of sense uh or caus it to crash uh then we can't use it to accurately solve performance problem
