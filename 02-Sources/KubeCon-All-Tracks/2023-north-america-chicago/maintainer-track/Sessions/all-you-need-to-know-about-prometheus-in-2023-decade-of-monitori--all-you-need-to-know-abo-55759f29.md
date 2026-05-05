---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Julien Pivotto", "O11y", "Ben Kochie", "Reddit"]
sched_url: https://kccncna2023.sched.com/event/1R2mK/all-you-need-to-know-about-prometheus-in-2023-decade-of-monitoring-julien-pivotto-o11y-ben-kochie-reddit
youtube_search_url: https://www.youtube.com/results?search_query=All+You+Need+to+Know+About+Prometheus+in+2023%3A+Decade+of+Monitoring+CNCF+KubeCon+2023
slides: []
status: parsed
---

# All You Need to Know About Prometheus in 2023: Decade of Monitoring - Julien Pivotto, O11y & Ben Kochie, Reddit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Julien Pivotto, O11y, Ben Kochie, Reddit
- Schedule: https://kccncna2023.sched.com/event/1R2mK/all-you-need-to-know-about-prometheus-in-2023-decade-of-monitoring-julien-pivotto-o11y-ben-kochie-reddit
- Busca YouTube: https://www.youtube.com/results?search_query=All+You+Need+to+Know+About+Prometheus+in+2023%3A+Decade+of+Monitoring+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre All You Need to Know About Prometheus in 2023: Decade of Monitoring.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2mK/all-you-need-to-know-about-prometheus-in-2023-decade-of-monitoring-julien-pivotto-o11y-ben-kochie-reddit
- YouTube search: https://www.youtube.com/results?search_query=All+You+Need+to+Know+About+Prometheus+in+2023%3A+Decade+of+Monitoring+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xoaQ9RIDqfs
- YouTube title: All You Need to Know About Prometheus in 2023: Decade of Monitoring - Julien Pivotto & Ben Kochie
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/all-you-need-to-know-about-prometheus-in-2023-decade-of-monitoring/xoaQ9RIDqfs.txt
- Transcript chars: 30363
- Keywords: prometheus, client, actually, working, metric, series, metrics, native, performance, monitoring, basically, libraries, labels, exporter, memory, config, support, server

### Resumo baseado na transcript

all right welcome this is the Prometheus 2023 ecosystem update uh my name is Ben coochi I'm a principal engineer at Reddit and I'm also a member of the Prometheus developer team with me is Julian you want to give yourself a quick intro yes so I am maintaining the prome server and uh my work is supporting Prometheus customer all day long so cool so uh who's used Prometheus 1.0 oh wow a lot of 1.0 users that's pretty cool um uh who's not using Prometheus yet cool nice

### Excerpt da transcript

all right welcome this is the Prometheus 2023 ecosystem update uh my name is Ben coochi I'm a principal engineer at Reddit and I'm also a member of the Prometheus developer team with me is Julian you want to give yourself a quick intro yes so I am maintaining the prome server and uh my work is supporting Prometheus customer all day long so cool so uh who's used Prometheus 1.0 oh wow a lot of 1.0 users that's pretty cool um uh who's not using Prometheus yet cool nice well welcome uh what is Prometheus Prometheus is a metric based monitoring system um and uh it's designed to pull data from all of your servers and all of your software uh infrastructure uh applications uh pretty much anything uh it provides a basic uh built-in web server uh data storage and allows you to do uh uh extremely powerful data queries with prom qo um and it can scale from anywhere from uh sitting on a Raspberry Pi to uh Global uh hyperscaling so uh Prometheus started in 201 uh2 back at SoundCloud where we had uh already started experimenting with container platforms uh before kubernetes even existed and we had the problem of we've got all these containers but we we can get data out of them with stany but stany doesn't actually let us know that the containers are running so we needed a an active polling based monitoring platform and there really wasn't a good polling uh polling system at the time so Prometheus was created to actively monitor the containers running in the container cluster um and uh it's been fully open source the entire time um uh I don't know why it says 2015 but Prometheus was created as as open source since the beginning in 2012 uh and we joined the cncf and released uh 1.0 in 2016 uh Prometheus 20 uh 2.0 came out with a completely new tsdb in 2017 and uh we created we were a graduated project of the cncf in 2018 um uh we've got a cool documentary if you want to if you can scan that bar code oh that's a little off the screen um uh but yeah there's a Prometheus documentary up on YouTube it's pretty great um we have lots and lots of maintainers lots of contributors uh and it's a a big and growing community of people uh so we've been you want to talk about the community yeah so first of all uh one month ago prome crossed 50k GitHub star so that's was a really nice achievement for all the community and basically uh in the last year we have expanded the promotive team so we have added a lot of new members across the different uh client libraries that we have so like uh
