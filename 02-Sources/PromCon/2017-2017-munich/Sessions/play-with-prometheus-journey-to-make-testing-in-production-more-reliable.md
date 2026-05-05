---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Scalability Reliability", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/play-with-prometheus/
youtube_url: https://www.youtube.com/watch?v=btnXuFLcpS8
youtube_search_url: https://www.youtube.com/results?search_query=Play+with+Prometheus+-+Journey+to+Make+%E2%80%9Ctesting+in+Production%E2%80%9D+More+Reliable+PromCon+2017
video_match_score: 1.047
status: video-found
---

# Play with Prometheus - Journey to Make “testing in Production” More Reliable

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Scalability Reliability]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/play-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8

## Resumo

Speaker: Giovanni Gargiulo Gilt is a high end fashion e-commerce that in the recent years has moved from a monolithic architecture to 150+ distributed microservices running on AWS. In Gilt we have to make sure our website runs smoothly and our customers are getting the best experience we can deliver. For this reason we have to keep an eye on our microservices and make sure they behave as expected.

## Abstract oficial

Speaker: Giovanni Gargiulo

Gilt is a high end fashion e-commerce that in the recent years has moved from a monolithic architecture to 150+ distributed microservices running on AWS.

In Gilt we have to make sure our website runs smoothly and our customers are getting the best experience we can deliver. For this reason we have to keep an eye on our microservices and make sure they behave as expected.

We’ve been looking for a long time to way to keep long lasting time series, we could aggregate, query, visualize and use for alerting. After a lot of trial and error, we ended up finding the right pieces of the puzzle: Prometheus, Alertmanager, Push Gateway, and Grafana.

Our success story went viral in Gilt, and very recently Prometheus and Grafana have been added to the Gilt (and HBC!) techradar. A few teams have already lined up to adopt our Prometheus Stack in production and eventually we will implement a hierarchical Prometheus federation alongside meta-monitoring.

I would like to share with you our journey, what worked well, the problems we faced, and how we fixed them.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/play-with-prometheus/
- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=btnXuFLcpS8
- YouTube title: PromCon 2017: Play with Prometheus - Journey to Make “testing in Production” More Reliable
- Match score: 1.047
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/play-with-prometheus-journey-to-make-testing-in-production-more-reliab/btnXuFLcpS8.txt
- Transcript chars: 27904
- Keywords: parameters, instance, production, prometheus, actually, couple, started, working, solution, template, wanted, quickly, simple, instances, metrics, instrumentation, github, release

### Resumo baseado na transcript

[Music] and now welcome Giovanni I got judo - oh good one yes who is going to talk about play with for me theus and yeah yeah all right cool hi everyone I'm happy to be here very excited and my name is Johanna guru and before starting I'm software engineer and before starting I'd like to I'm sure that in the crowd there are lots of products guys as well a system engineer is there any developers that I shall use Prometheus app to monitor service in production okay

### Excerpt da transcript

[Music] and now welcome Giovanni I got judo - oh good one yes who is going to talk about play with for me theus and yeah yeah all right cool hi everyone I'm happy to be here very excited and my name is Johanna guru and before starting I'm software engineer and before starting I'd like to I'm sure that in the crowd there are lots of products guys as well a system engineer is there any developers that I shall use Prometheus app to monitor service in production okay so there are a few of them yeah any one of you running in AWS Amazon Web Services alright cool so they're gonna be like a couple of takeaways for you and so today I'm gonna speak about the little journey that we started last year in in guilt into adopting from me to Sangha vana as a monitoring system so very very brief introduction about myself I'm a software engineer I've been working on jvm languages for the past 12 years the last two on Scala I am part since 2015 of the gift personalization and Tim and here there are a couple of details for not reach me on github and Twitter and very quick story about gift and gif design fashion online retailer so we sell very expensive clothes on on internet at the discounted price the the business model is called flash sales and every day afternoon and there would be like a very high spike in usage of the website because we would release the new products at very low cost high discount it was initially launched in November of 2007 was a monolithic Ruby on Rails up in 2010 when the website started to get very popular we very quickly hit and a problem in scalability and this is the reason why we started to break the the monolith down and it took quite a few years to get there we eventually managed to split the Ruby on Rails up into pretty much the 350 mostly Scala micro-services and last year in 2016 the give to join the HPC family that is awesome a company to which a more online retailer shops are part of there are a few names here Lauren Taylor it itself sucks of 5th and 6th 5th Avenue so the development processing guilt is very very simple this is that this has evolved over the years but we eventually managed to get the point whereby we do shortly directions so we deliver to production very quickly we make use of continuous deployment and continual continuous integration Jenkins is your friend and in our team we do not have QA people we do not have test results oft where engineers they follow the whole lifecycle of the app from development to testing we do th
