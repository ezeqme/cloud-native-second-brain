---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Visualization Dashboards"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/prometheus-as-a-internal-service/
youtube_url: https://www.youtube.com/watch?v=c61pNvU90yM
youtube_search_url: https://www.youtube.com/results?search_query=Prometheus+as+a+%28Internal%29+Service+PromCon+2017
video_match_score: 0.841
status: video-found
---

# Prometheus as a (Internal) Service

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Visualization Dashboards]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/prometheus-as-a-internal-service/
- YouTube: https://www.youtube.com/watch?v=c61pNvU90yM

## Resumo

Speaker: Paul Traylor LINE is a large company with many different development teams. Momentum can be a powerful force within a company so it can take some time, training (including unlearning the old) and evangelizing to get a new system adopted. This talk will give a brief summary of our development team’s monitoring environment (Prometheus, Grafana, Promgen) before going into educating developers on Prometheus adoption and some of the struggles and lessons learned from providing Prometheus as an internal service.

## Abstract oficial

Speaker: Paul Traylor

LINE is a large company with many different development teams. Momentum can be a powerful force within a company so it can take some time, training (including unlearning the old) and evangelizing to get a new system adopted. This talk will give a brief summary of our development team’s monitoring environment (Prometheus, Grafana, Promgen) before going into educating developers on Prometheus adoption and some of the struggles and lessons learned from providing Prometheus as an internal service.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/prometheus-as-a-internal-service/
- YouTube: https://www.youtube.com/watch?v=c61pNvU90yM
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c61pNvU90yM
- YouTube title: PromCon 2017: Prometheus as a (Internal) Service - Paul Traylor
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/prometheus-as-a-internal-service/c61pNvU90yM.txt
- Transcript chars: 20994
- Keywords: prometheus, metrics, configuration, wanted, little, probably, write, manager, better, server, trying, servers, targets, difficult, sometimes, cluster, developers, automatically

### Resumo baseado na transcript

[Music] so next up from line we have Paul Taylor he's came here all the way from Japan and people can start quieting down thank you and over to you thank you it's nice to be here so my name's Paul trailer I'm representing line from Lyon Fukuoka and I will be presenting on prometheus is an internal service I think whatever whatever as a service is a very popular title so that's what I went with so quick self introduction when I was in high school I wanted to

### Excerpt da transcript

[Music] so next up from line we have Paul Taylor he's came here all the way from Japan and people can start quieting down thank you and over to you thank you it's nice to be here so my name's Paul trailer I'm representing line from Lyon Fukuoka and I will be presenting on prometheus is an internal service I think whatever whatever as a service is a very popular title so that's what I went with so quick self introduction when I was in high school I wanted to make video games I thought that sounded fun ended up being a lot of work I decided to do something a little bit easier like web development internet stuff so probably like a lot of you went to university studied computer science after that I moved to San Francisco I thought that would be a fun challenge the first job there I primarily worked with web development so some PHP that kind of fun stuff my second job I transferred more into operations so building and packaging and deploying our software I've now been at Lyon Fukuoka for about a year now and my current focus is in improving our monitoring setup and improving monitoring so what is lying Fukuoka because line is very popular in Japan maybe not quite as popular elsewhere so line itself is a messaging application probably similar to a lot that you're familiar with and what Lyon Fukuoka does is we built a lot of other apps sort of along the line family brands so a recent one we've done is line creator studio so you can make stickers your pets is your family your friends we have something called lying fortune so you can get get your daily fortune told talk with different fortune tellers it's very popular we have some survey tools so tools that companies can easily survey their users part-time job searching and just many other services mostly targeted at Japan right now and so as I said my current responsibilities is monitoring so last year my colleague from Tokyo came and introduced tool called prompt gen a prom prometheus configuration tool so in the following year I rewrote that in Django because I wanted to have a little bit better RM I wanted the Django admin for free it's all there and github if you're interested but my main role is to to continue to develop that and to migrate a lot of our legacy monitoring to Prometheus so part of that is installing the various exporters making the play books to install them on various servers setting up the Prometheus targets what is prometheus gone is great and then configuring different alerting rules so whe
