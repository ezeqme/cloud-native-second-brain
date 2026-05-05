---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Kubernetes", "Scalability Reliability"]
speakers: ["Mihail Mihaylov"]
source_url: https://promcon.io/2025-munich/talks/from-manual-to-managed-prometheus-agent-deployment-at-scale/
youtube_url: https://www.youtube.com/watch?v=RY5JG7mvSd4
youtube_search_url: https://www.youtube.com/results?search_query=From+Manual+to+Managed%3A+Prometheus+Agent+Deployment+at+Scale+PromCon+2025
video_match_score: 1.031
status: video-found
---

# From Manual to Managed: Prometheus Agent Deployment at Scale

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Mihail Mihaylov
- Página oficial: https://promcon.io/2025-munich/talks/from-manual-to-managed-prometheus-agent-deployment-at-scale/
- YouTube: https://www.youtube.com/watch?v=RY5JG7mvSd4

## Resumo

The journey to comprehensive monitoring is paved with significant challenges, including navigating restrictive security policies, adapting to complex network topologies, and shifting developer mindsets. Therefore, automating the deployment and maintenance of the Prometheus Agents is as critical as the stability of the monitoring system itself. This presentation continues the narrative from last year's discussion on the trials of building and promoting our core Prometheus/Thanos monitoring service.

## Abstract oficial

The journey to comprehensive monitoring is paved with significant challenges, including navigating restrictive security policies, adapting to complex network topologies, and shifting developer mindsets. Therefore, automating the deployment and maintenance of the Prometheus Agents is as critical as the stability of the monitoring system itself.

This presentation continues the narrative from last year's discussion on the trials of building and promoting our core Prometheus/Thanos monitoring service. Now, we turn our focus to the crucial task of data ingestion: deploying and managing the Prometheus Agents that feed our observability platform. This session will provide a case study of four distinct ways we have successfully implemented to address the challenge of Prometheus adoption in an automated way at scale.

Furthermore, we will address the complex networking hurdles of secure data transmission, including authentication and authorization strategies.

The presentation will conclude with a live, hands-on demonstration. We will use our simple Go templating tool to install a Prometheus Agent on a Raspberry Pi cluster and witness how easy the UTF8 metric appears in our central monitoring platform, showcasing the power and simplicity of our approach.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/from-manual-to-managed-prometheus-agent-deployment-at-scale/
- YouTube: https://www.youtube.com/watch?v=RY5JG7mvSd4
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RY5JG7mvSd4
- YouTube title: Promcon 2025 - From Manual to Managed: Prometheus Agent Deployment at Scale
- Match score: 1.031
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/from-manual-to-managed-prometheus-agent-deployment-at-scale/RY5JG7mvSd4.txt
- Transcript chars: 20189
- Keywords: cluster, environment, prometheus, install, actually, basically, customer, customers, approach, exporter, control, metrics, installed, package, everything, another, course, simply

### Resumo baseado na transcript

I work at MARB and today I will be presenting from manual to managed our story of how we deploy Prometheus agents at scale. It was about the challenges that we faced when we were um trying to introduced our core monitoring system and also the challenges that we uh also faced when we were building it and maintaining it. So now comes the story of uh how we help people install Prometheus agents so that they can send us the data. And as easy as that sounds uh meaning installing Prometheus and configuring Prometheus of course it the challenges came at scale and uh from simple mindset of people to uh restrictions due to topology or some uh simple differences in in the stack. And first of all when we started designing this we had to face the biggest issue of all of them all how to send the data uh basically the networking. So the networking not always if ever the uh Prometheus agent is part of the core cluster or is in the network of the core cluster or in fact is paired with the core customer core cluster.

### Excerpt da transcript

[music] Hello everybody. My name is Mik Mihov. I work at MARB and today I will be presenting from manual to managed our story of how we deploy Prometheus agents at scale. Uh last year at PromCom I presented another story of ours. It was about the challenges that we faced when we were um trying to introduced our core monitoring system and also the challenges that we uh also faced when we were building it and maintaining it. And just a quick reminder of our system, it is a tunnels based monitoring system that is multicloud, multi-environment. uh we scale on different clouds. We scale on different regions, different tanos receivers. So the data is spread evenly and we have one centralized cluster that can access all the data. It has the tanos global view also we have the graphana dashboards there. We have also uh all the alerts there and basically that's the core environment and the uh the good news after one year is that it started gaining traction. People started asking how they can join teams started u integrating with the system and the good design always wins.

So uh this actually came presented us with another challenge how to enable people to feed us with metrics. So now comes the story of uh how we help people install Prometheus agents so that they can send us the data. And as easy as that sounds uh meaning installing Prometheus and configuring Prometheus of course it the challenges came at scale and uh from simple mindset of people to uh restrictions due to topology or some uh simple differences in in the stack. We had to face a lot of issues. So actually automating, propagating and maintaining the agents became as important as actually maintaining the core system. So we came up with four different ways to um bridge the gap between the agents in the system. And first of all when we started designing this we had to face the biggest issue of all of them all how to send the data uh basically the networking. So the networking not always if ever the uh Prometheus agent is part of the core cluster or is in the network of the core cluster or in fact is paired with the core customer core cluster.

So we h we had to make some uh very easy to use cheap and secure way to send the data over the internet. So what we have what we did is we used Cloudflare. We have a huge Cloudflare infrastructure. We have a geo load balancer there. We have um we issue per customer tokens for every customer to send their data with. Also we have integrated it with our IDP the MARB I
