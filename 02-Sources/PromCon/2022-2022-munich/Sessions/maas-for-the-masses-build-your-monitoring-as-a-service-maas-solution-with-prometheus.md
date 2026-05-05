---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/maas-for-the-masses-build-your-m/
youtube_url: https://www.youtube.com/watch?v=EFPPic9dBS4
youtube_search_url: https://www.youtube.com/results?search_query=MaaS+for+the+Masses%3A+Build+Your+Monitoring-as-a-Service+%28MaaS%29+Solution+With+Prometheus+PromCon+2022
video_match_score: 1.013
status: video-found
---

# MaaS for the Masses: Build Your Monitoring-as-a-Service (MaaS) Solution With Prometheus

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/maas-for-the-masses-build-your-m/
- YouTube: https://www.youtube.com/watch?v=EFPPic9dBS4

## Resumo

Speaker(s): Moad Zardab & Matej Gera Patterns of operating Prometheus-based monitoring solutions are changing steadily. More and more organizations want to leverage the Prometheus data model with all its capabilities and offer it to their users without an operational burden in a centralized manner. This is often motivated by the need to deal with issues such as abstracting away complexities, managing costs, resiliency, and security.

## Abstract oficial

Speaker(s): Moad Zardab & Matej Gera

Patterns of operating Prometheus-based monitoring solutions are changing steadily. More and more organizations want to leverage the Prometheus data model with all its capabilities and offer it to their users without an operational burden in a centralized manner. This is often motivated by the need to deal with issues such as abstracting away complexities, managing costs, resiliency, and security. Having to implement the same best practices and know-how, learned from running Prometheus, while dealing with multiple teams, products, and environments can quickly become a daunting task.

Prometheus provides us with well-grounded and stable foundation to expand its functionality to monitoring-as-a-service (MaaS). However, achieving this on the TSDB data model, with remote client-controlled environments, poses some unique challenges. With this paradigm shift, we now need to consider aspects such as authentication, authorization, rate limiting, allow-listing, and tenancy. 

In this talk, you will learn how to leverage Prometheus and its ecosystem to implement functional MaaS for your needs. Matej and Moad will discuss several state-of-the-art open source solutions, ranging from using a simple proxy to deploying a fully-fledged multi-tenancy system like Prometheus in receive mode, Thanos, Cortex, and Mimir. They will also talk about the challenges faced and the future work ahead.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/maas-for-the-masses-build-your-m/
- YouTube: https://www.youtube.com/watch?v=EFPPic9dBS4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EFPPic9dBS4
- YouTube title: PromCon EU 2022: MaaS for the Masses: Build Your Monitoring-as-a-Service  Solution With Prometheus
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/maas-for-the-masses-build-your-monitoring-as-a-service-maas-solution-w/EFPPic9dBS4.txt
- Transcript chars: 25199
- Keywords: metrics, prometheus, monitoring, tenants, tenant, series, thanos, projects, active, cost, clusters, yourself, write, particular, oftentimes, everyone, running, source

### Resumo baseado na transcript

okay [Music] you have to set up the microphones cool hello everyone uh thanks for coming to our talk today we're going to be talking about mass for the masses so building your own monitoring as a service why you would do it how you would go back doing it so hey everyone my name is mache I'm working as a software engineer at red hat at the openshift monitoring team I'm also tunnels maintainer observator and maintainer that's about it cool my name is MOA that's my face that's

### Excerpt da transcript

okay [Music] you have to set up the microphones cool hello everyone uh thanks for coming to our talk today we're going to be talking about mass for the masses so building your own monitoring as a service why you would do it how you would go back doing it so hey everyone my name is mache I'm working as a software engineer at red hat at the openshift monitoring team I'm also tunnels maintainer observator and maintainer that's about it cool my name is MOA that's my face that's my face I've been I work at red hat with mate as well and I focus primarily on What's called the red hat observability service which is How We Gather a lot of telemetry for openshift from tens of thousands of clusters that are running we also wanted to give a shout out to our colleagues as what I was supposed to be with us he was supposed to talk with me he was also helping us with the presentation and giving us feedback so if you're watching saswata hi yeah he's alive he just came back to Germany cool so um context uh so what is monitoring as a service um it's pretty straightforward it means you have a third party service you might own it you might not that you send metrics to um why would you need that uh kind of the challenges around multi-tenancy if you're having multiple people use this um and then how to migrate to using mass what are some projects in open source that you could use what are some commercial products you can use and how much will it cost you I think that's an important question for a lot of people observability kind of exists in the space where everybody wants a lot of it but nobody wants to pay for it so that's always a sensitive topic when it comes to metrics before we start though I want to kind of get an impression of where everyone is in this kind of Journey if they are using monitoring service or not how many people use Prometheus in production just the show of hands so most people that's good at prom con most people use Prometheus that's great how many of those people use a third-party monitoring as a service so a handful of smothering that's much less than I expected and how many of those people who put their hands up use a commercial one so a third party okay so about half of the people that put their hands up there that's quite interesting so before we go into why you might need monitoring as a service let's just look at a typical use case uh you have a kubernetes cluster running somewhere you have some pods in a namespace this is a simplified diagram and
