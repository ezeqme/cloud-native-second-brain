---
type: promcon-talk
conference: PromCon
edition: "PromCon 2018"
edition_id: 2018-munich
year: 2018
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2018-munich/talks/introducing-our-reliability-toolkit/
youtube_url: https://www.youtube.com/watch?v=btnXuFLcpS8
youtube_search_url: https://www.youtube.com/results?search_query=Improving+Reliability+Through+Engineering+an+Easy-to-use+Prometheus-Based+Monitoring+and+Alerting+Stack%3A+Introducing+Our+Reliability+Toolkit+PromCon+2018
video_match_score: 0.594
status: video-found
---

# Improving Reliability Through Engineering an Easy-to-use Prometheus-Based Monitoring and Alerting Stack: Introducing Our Reliability Toolkit

## Identificação

- Edição: PromCon 2018
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2018-munich/talks/introducing-our-reliability-toolkit/
- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8

## Resumo

Speakers: Robin van Zijll By definition, SREs are responsible for the reliability of sites, but what if they don't own any sites themselves? Within ING, the largest bank of the Netherlands, BizDevOps teams are autonomous and responsible for building and running their services. In theory, that could make the existence of SRE obsolete, right?

## Abstract oficial

Speakers:


Robin van Zijll


By definition, SREs are responsible for the reliability of sites, but what if they don't own any sites themselves? Within ING, the largest bank of the Netherlands, BizDevOps teams are autonomous and responsible for building and running their services. In theory, that could make the existence of SRE obsolete, right? How can you improve availability for end customers in an environment of engineers with full service ownership? How to convince without the power of intervention? How to improve without being blameful?

We'll explain how we, a team of 8 SREs among 1700 DevOps engineers, try to improve stability by focussing on software engineering. We created the Reliability Toolkit to help BizDevOps teams with their reliability challenges in the fields of white box monitoring and alerting while minimizing toil.

This talk will explain:


Our SRE team purpose and why we think our approach with heavy focus on software engineering works for our organization
The concept of the Reliability Toolkit and introduction of its components and their setup (Prometheus, Alertmanager, Grafana, NGINX Log Aggregator, SMS and ChatOps functionalities)
How we provision Reliability Toolkit
How we convince, onboard and educate BizDevOps teams to use the Reliability Toolkit


During this talk we will demo:


A Kafka to Prometheus consumer (and why this is not what we want)
Prometheus Model Builder, generate expectation models out of any Prometheus metric
A collection of templated Grafana dashboards to give every team a kickstart




Video link -
Slides

## Links

- Página oficial: https://promcon.io/2018-munich/talks/introducing-our-reliability-toolkit/
- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8
- YouTube title: PromCon 2017: Play with Prometheus - Journey to Make “testing in Production” More Reliable
- Match score: 0.594
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2018/improving-reliability-through-engineering-an-easy-to-use-prometheus-ba/btnXuFLcpS8.txt
- Transcript chars: 27904
- Keywords: parameters, instance, production, prometheus, actually, couple, started, working, solution, template, wanted, quickly, simple, instances, metrics, instrumentation, github, release

### Resumo baseado na transcript

[Music] and now welcome Giovanni I got judo - oh good one yes who is going to talk about play with for me theus and yeah yeah all right cool hi everyone I'm happy to be here very excited and my name is Johanna guru and before starting I'm software engineer and before starting I'd like to I'm sure that in the crowd there are lots of products guys as well a system engineer is there any developers that I shall use Prometheus app to monitor service in production okay

### Excerpt da transcript

[Music] and now welcome Giovanni I got judo - oh good one yes who is going to talk about play with for me theus and yeah yeah all right cool hi everyone I'm happy to be here very excited and my name is Johanna guru and before starting I'm software engineer and before starting I'd like to I'm sure that in the crowd there are lots of products guys as well a system engineer is there any developers that I shall use Prometheus app to monitor service in production okay so there are a few of them yeah any one of you running in AWS Amazon Web Services alright cool so they're gonna be like a couple of takeaways for you and so today I'm gonna speak about the little journey that we started last year in in guilt into adopting from me to Sangha vana as a monitoring system so very very brief introduction about myself I'm a software engineer I've been working on jvm languages for the past 12 years the last two on Scala I am part since 2015 of the gift personalization and Tim and here there are a couple of details for not reach me on github and Twitter and very quick story about gift and gif design fashion online retailer so we sell very expensive clothes on on internet at the discounted price the the business model is called flash sales and every day afternoon and there would be like a very high spike in usage of the website because we would release the new products at very low cost high discount it was initially launched in November of 2007 was a monolithic Ruby on Rails up in 2010 when the website started to get very popular we very quickly hit and a problem in scalability and this is the reason why we started to break the the monolith down and it took quite a few years to get there we eventually managed to split the Ruby on Rails up into pretty much the 350 mostly Scala micro-services and last year in 2016 the give to join the HPC family that is awesome a company to which a more online retailer shops are part of there are a few names here Lauren Taylor it itself sucks of 5th and 6th 5th Avenue so the development processing guilt is very very simple this is that this has evolved over the years but we eventually managed to get the point whereby we do shortly directions so we deliver to production very quickly we make use of continuous deployment and continual continuous integration Jenkins is your friend and in our team we do not have QA people we do not have test results oft where engineers they follow the whole lifecycle of the app from development to testing we do th
