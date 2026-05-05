---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2019"
edition_id: 2019-munich
year: 2019
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2019-munich/talks/migrating-from-nagios-to-prometheus-at-runtastic/
youtube_url: https://www.youtube.com/watch?v=xSPNYXbAhQE
youtube_search_url: https://www.youtube.com/results?search_query=Migrating+from+Nagios+to+Prometheus+at+Runtastic+PromCon+2019
video_match_score: 0.987
status: video-found
---

# Migrating from Nagios to Prometheus at Runtastic

## Identificação

- Edição: PromCon EU 2019
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2019-munich/talks/migrating-from-nagios-to-prometheus-at-runtastic/
- YouTube: https://www.youtube.com/watch?v=xSPNYXbAhQE

## Resumo

Speaker: Niko Dominkowitsch Thinking of replacing your existing monitoring solution with Prometheus? In this talk we will show you how Runtastic moved its monitoring and alerting stack from Nagios to Prometheus. We'll show you how we managed to do this, how monitoring and alerting works with Prometheus and what challenges we were facing.

## Abstract oficial

Speaker: Niko Dominkowitsch

Thinking of replacing your existing monitoring solution with Prometheus? In this talk we will show you how Runtastic moved its monitoring and alerting stack from Nagios to Prometheus. We'll show you how we managed to do this, how monitoring and alerting works with Prometheus and what challenges we were facing. 

We will cover these topics: 


How our journey started 
Using Consul for Service Discovery 
Using Terraform for managing health checks and silences for new micro services
Building a pipeline to test and deploy alerting and recording rules automatically
Using OpsGenie for Alert management
Examples of common checks in Nagios and how we implemented them with Prometheus
Examples of custom written Exporters
Lessons Learned




Video link -
Slides

## Links

- Página oficial: https://promcon.io/2019-munich/talks/migrating-from-nagios-to-prometheus-at-runtastic/
- YouTube: https://www.youtube.com/watch?v=xSPNYXbAhQE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xSPNYXbAhQE
- YouTube title: PromCon EU 2019: Migrating from Nagios to Prometheus at Runtastic
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2019/migrating-from-nagios-to-prometheus-at-runtastic/xSPNYXbAhQE.txt
- Transcript chars: 28086
- Keywords: basically, actually, alerts, prometheus, running, checks, exporter, console, production, alerting, infrastructure, important, export, server, define, health, priority, mongodb

### Resumo baseado na transcript

[Music] so hello good morning everyone after all not to present you the first talkie at the prom come well my name is Nikhil I'm from Mont a stick and together with my colleagues and managing maintaining automating our production infrastructure at runtastic and I want to show tell you some story about us how we managed to make it on monitoring to Prometheus from mag wheels just as a quick overview of what their own testing infrastructure looks like so basically we are mostly open source to research a

### Excerpt da transcript

[Music] so hello good morning everyone after all not to present you the first talkie at the prom come well my name is Nikhil I'm from Mont a stick and together with my colleagues and managing maintaining automating our production infrastructure at runtastic and I want to show tell you some story about us how we managed to make it on monitoring to Prometheus from mag wheels just as a quick overview of what their own testing infrastructure looks like so basically we are mostly open source to research a lot of open source technology in our production infrastructure most of Linux based and they have a lot of virtualization at the moment KVM based at the moment we have around 40 thousand CPU cores so for thousands because I'm sorry 20 terabytes of memory in total and 100 terabytes of storage provided by our self cluster so all of them is managed broke neighbor on and we have also some kind of databases here MongoDB my sequel Cassandra also RabbitMQ so we have to take care of a lot of stuff and therefore else I have to automate a lot of things we have Cisco is a 40% the networking which were also responsible of and we will share for bootstrapping on machines and setting up all the servers and use terraform for infrastructure as code in the past at fantastic we grew a lot so we had a lot of micro services we have 70 microservices life and yeah we had a lot of virtual machines to spawn up and so also a monitoring had to scale a bit but back in 2017 we started actually when realistic started we used a girls in the past to maintain our infrastructure to check all services to check out services with basic checks we had basic checks by CPU for Lords disk space as you can imagine there's a 75% warning state and 90% critical states super familiar with Nagios then this might be common for you we also use and still use new relic for instrumentation of our applications so also the crash rates error rates response times and to be able to alert on that when somebody opposes on phone call we use Pingdom for that which is an external service for doing external HTTP checks and we also use ping them to force it to check specific national service pages and with string matching so if service tracking our girls is being an honorable critical state it would be 7 SMS to that person that is being on it was horrible so we use check for preparing all Magna set up and you can see screenshot of our chef data pack for adding new Nagios checks basically this is a configuration file we would
