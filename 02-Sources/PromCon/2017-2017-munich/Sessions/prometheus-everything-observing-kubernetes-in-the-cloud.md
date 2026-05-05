---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Kubernetes", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/prometheus-everything-observing-kubernetes-in-the-cloud/
youtube_url: https://www.youtube.com/watch?v=5P_A7KN7F6I
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+Everything%2C+Observing+Kubernetes+in+the+Cloud+PromCon+2017
video_match_score: 0.939
status: video-found
---

# Prometheus Everything, Observing Kubernetes in the Cloud

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/prometheus-everything-observing-kubernetes-in-the-cloud/
- YouTube: https://www.youtube.com/watch?v=5P_A7KN7F6I

## Resumo

Speaker: Sneha Inguva As the industry moves towards a microservices architecture, many companies are embracing container orchestration solutions. DigitalOcean is no different. Over the course of the last year, DigitalOcean’s move towards a container orchestration solution based on Kubernetes has empowered service owners to quickly and efficiently deploy and update their applications.

## Abstract oficial

Speaker: Sneha Inguva

As the industry moves towards a microservices architecture, many companies are embracing container orchestration solutions. DigitalOcean is no different. Over the course of the last year, DigitalOcean’s move towards a container orchestration solution based on Kubernetes has empowered service owners to quickly and efficiently deploy and update their applications. A vital component of this, however, is a white box monitoring and alerting solution based upon Prometheus and Alertmanager.

In this talk, you will hear of DigitalOcean’s in-cluster setup of Prometheus and Alertmanager that allows service owners to instrument their their own metrics and alerts. Listeners will hear about the architecture from both the service owner’s point of view as well as the internals that allow for the dynamic addition of alerts. I will highlight the successes of this approach - ease of use and avoiding alerting fatigue - as well as potential pitfalls and gotchas. And lastly, I will end with a discussion of future modifications.

Individuals looking to similarly leverage Prometheus and Alertmanager to monitor their own container orchestration platforms will be able to learn from our experiences at DigitalOcean and subsequently apply key lessons learned to their own alerting use cases.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/prometheus-everything-observing-kubernetes-in-the-cloud/
- YouTube: https://www.youtube.com/watch?v=5P_A7KN7F6I
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5P_A7KN7F6I
- YouTube title: PromCon 2017: Prometheus Everything, Observing Kubernetes in the Cloud - Sneha Inguva
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/prometheus-everything-observing-kubernetes-in-the-cloud/5P_A7KN7F6I.txt
- Transcript chars: 24002
- Keywords: cluster, actually, monitoring, prometheus, manager, basically, metrics, alerts, server, manifest, definitely, application, deploy, information, leveraged, actual, deployed, communicate

### Resumo baseado na transcript

[Music] so now as Nina from digitalocean is going to talk about how they're monitoring your Cooper daddy said yes hello you guys hear me awesome so hi my name is Sneha and kuva I'm from digitalocean if it wasn't a parent before we use Prometheus at digitalocean you guys are probably said good seeing us here however today I'm going to be talking about something slightly different I'll be talking about how we leverage Prometheus and alert manager for both cluster monitoring and alerting so it's name of my

### Excerpt da transcript

[Music] so now as Nina from digitalocean is going to talk about how they're monitoring your Cooper daddy said yes hello you guys hear me awesome so hi my name is Sneha and kuva I'm from digitalocean if it wasn't a parent before we use Prometheus at digitalocean you guys are probably said good seeing us here however today I'm going to be talking about something slightly different I'll be talking about how we leverage Prometheus and alert manager for both cluster monitoring and alerting so it's name of my talk oh yeah about me again I am a software engineer at digitalocean I was formerly on the team that used Prometheus alert manager for monitoring Hera kubernetes clusters still working with Prometheus an alert manager but now for I guess our data center wide monitoring so before I delve into exactly what we've done I just wanted to share some stats with you so we currently have 15 kubernetes clusters in 12 data centers which are located all around the world we have more than 300 production applications in them generally have two Promethea I know there's a lot of contention about the plural of that but I want with from API this time there's two from a piano and an alert manager player cluster with a million a half time series on the aggregate and then we're scraping about a hundred thousand samples the second also an aggregate step so the plan today is I'm going to first talk about the pre kubernetes days at digitalocean and how those felt um then I'll talk about when we started using kubernetes at digitalocean and this is something we like to call GOCC i'm going to talk about how we've leveraged prometheus and alert manager for monitoring up finally gonna go into some like actual examples of what we're monitoring and how we've set up learning and of course no change you know happens without some friction so I'm gonna talk about potential pitfalls that we've run into and how we address them and only end with my absolute favorite part of the talk which is like my pie-in-the-sky ideas so so in the pre kubernetes world typically what would happen is that a service owner would write an application you know either and go or rails or whatnot they would provision a server using chef or ansible they would then use like a CI pipeline maybe they would use bash scripts or something else and then they would deploy and or update their application as needed in terms of monitoring we had you know Nagios you still use it but for host monitoring which didn't provide too much
