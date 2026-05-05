---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/prometheus-as-a-customer-facing-monitoring-tool-for-spatialos-simulations/
youtube_url: https://www.youtube.com/watch?v=39xVoFW6eUw
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+as+a+Customer-Facing+Monitoring+Tool+for+SpatialOS+Simulations+PromCon+2016
video_match_score: 0.937
status: video-found
---

# Prometheus as a Customer-Facing Monitoring Tool for SpatialOS Simulations

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-as-a-customer-facing-monitoring-tool-for-spatialos-simulations/
- YouTube: https://www.youtube.com/watch?v=39xVoFW6eUw

## Resumo

Speaker: Dmytro Kislov At Improbable we provide a platform for spatially distributed simulations to our customers. We use Prometheus for monitoring our internal microservice stack, but also offer it as a first class customer-facing system on our platform. As far as we know, we are currently running one of the largest Prometheus set ups, with multiple clusters of federated Prometheus stacks.

## Abstract oficial

Speaker: Dmytro Kislov

At Improbable we provide a platform for spatially distributed simulations to
our customers. We use Prometheus for monitoring our internal microservice
stack, but also offer it as a first class customer-facing system on our
platform. As far as we know, we are currently running one of the largest
Prometheus set ups, with multiple clusters of federated Prometheus stacks.
Given the nature of the simulations built by our users, monitoring becomes
their go-to tool for debugging and troubleshooting. Since our customer facing
Prometheus stack is multitenant, we have also implemented monitoring data
isolation based on ACLs.

In this talk we will be discussing our federation set up and monitoring data
isolation.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/prometheus-as-a-customer-facing-monitoring-tool-for-spatialos-simulations/
- YouTube: https://www.youtube.com/watch?v=39xVoFW6eUw
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=39xVoFW6eUw
- YouTube title: PromCon 2016: Prometheus as a Customer-Facing Monitoring Tool for SpatialOS - Dmytro Kislov
- Match score: 0.937
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/prometheus-as-a-customer-facing-monitoring-tool-for-spatialos-simulati/39xVoFW6eUw.txt
- Transcript chars: 25377
- Keywords: metrics, prometheus, actually, request, monitoring, figure, server, deployment, metric, access, recording, simulation, cluster, leaves, federated, number, interesting, trying

### Resumo baseado na transcript

cool thank you all right so my name is dima i work at improbable I'm one of the infrastructure engineers there and today we'll be talking about how we use Prometheus Adam Pro Bowl the talk will cover three main parts one of them will be our general setup how we do the sharding how we do the Federation the other part will be using Prometheus as a user facing tool in a multi-tenant environment so we'll talk a little bit about that and the third part is going to you can use the prompt you from prometheus to figure out all the selectors so in our case the reason why it's possible is all the users are associated with a certain project and the permissions will have a project in that so you know that this user is allowed to see project as a secret project and also all the metrics that are coming from the simulation will have the project as a part of the label so looking at the metric we can say that this metric belongs

### Excerpt da transcript

cool thank you all right so my name is dima i work at improbable I'm one of the infrastructure engineers there and today we'll be talking about how we use Prometheus Adam Pro Bowl the talk will cover three main parts one of them will be our general setup how we do the sharding how we do the Federation the other part will be using Prometheus as a user facing tool in a multi-tenant environment so we'll talk a little bit about that and the third part is going to be bonus part I'll talk about a little bit of em for magic that we have to do for recording rules okay so before I get into that I quickly want to talk about what we do it will explain some of the design choices that we have made so speacial OS is a distributed operating system the distributed operating system is marketing talk I just lifted it from our promo slides but the idea is we basically are a platform that allows users to run large-scale online simulations that's what we do ok so how does it look from the above so we have put the purpose of this talk two main clusters that we are operating there is the platform cluster so that's where all our front ends and the user facing api's are so there we have the API server the authentication server the proxy server i'll talk about them in detail a little bit later and we have the platform on the train so this is what monitors this particular cluster our internal services in there we have about three of them up to production ones one stage in one the other part is the deployment cluster so the deployment cluster is the heart of kind of spatial OS this is where users simulations are running and normal deployment of simulation consists of a bunch of things the main ones are the wrong time that's what we provide this is our code and then the workers that users provide so the workers is what calculates the next simulation step a user worker can be a game engine or maybe some crazy simulation engine and for that we have two separate instance of Prometheus we have infrastructure monitoring they in from home and we have the simulation launched in the symbol so inform on as it says on the tin it's for our monitoring infrastructure services sim mom is what will later be kind of exposed to the user that's what monitors their simulations again the other thing that's kind of weird and that causes some issues for us is that deployments are kind of not standard long-running job they can be very different they can be super short lived in the order of minutes like when
