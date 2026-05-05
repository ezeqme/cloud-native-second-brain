---
type: promcon-talk
conference: PromCon
edition: "PromCon 2016"
edition_id: 2016-berlin
year: 2016
city: "Berlin"
country: "Germany"
topics: ["Prometheus Core", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2016-berlin/talks/dynamic-monitoring-with-prometheus-and-rancher/
youtube_url: https://www.youtube.com/watch?v=fSJs-lvegtI
youtube_search_url: https://www.youtube.com/results?search_query=Dynamic+Monitoring+with+Prometheus+and+Rancher+PromCon+2016
video_match_score: 0.822
status: video-found
---

# Dynamic Monitoring with Prometheus and Rancher

## Identificação

- Edição: PromCon 2016
- País/cidade: Germany / Berlin
- Temas: [[Prometheus Core]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2016-berlin/talks/dynamic-monitoring-with-prometheus-and-rancher/
- YouTube: https://www.youtube.com/watch?v=fSJs-lvegtI

## Resumo

Speaker: Chris Urwin / Edward Marshall Both Prometheus and Rancher have extremely active communities and were born from the same requirement to support the newer dynamic infrastructures. This talk will focus on how Rancher and its community are leveraging the power of Prometheus for monitoring both hosts and applications, and how we are leveraging Prometheus's dynamic server discovery to minimise the amount of static configuration and maintenance.

## Abstract oficial

Speaker: Chris Urwin /
 Edward Marshall

Both Prometheus and Rancher have extremely active communities and were born
from the same requirement to support the newer dynamic infrastructures.

This talk will focus on how Rancher and its community are leveraging the power
of Prometheus for monitoring both hosts and applications, and how we are
leveraging Prometheus's dynamic server discovery to minimise the amount of
static configuration and maintenance.

## Links

- Página oficial: https://promcon.io/2016-berlin/talks/dynamic-monitoring-with-prometheus-and-rancher/
- YouTube: https://www.youtube.com/watch?v=fSJs-lvegtI
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=fSJs-lvegtI
- YouTube title: PromCon 2016: Dynamic Monitoring with Prometheus and Rancher - Chris Urwin, Edward Marshall
- Match score: 0.822
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2016/dynamic-monitoring-with-prometheus-and-rancher/fSJs-lvegtI.txt
- Transcript chars: 24494
- Keywords: prometheus, monitoring, rancher, basically, catalog, around, working, metrics, dynamic, source, together, across, docker, environment, running, companies, server, little

### Resumo baseado na transcript

alright please welcome to the stage at marshall in chris owen so chris has been the UK technical lead of Rancho labs and it has been consultant at infinity works and they've been working together to make dynamic monitoring with prometheus possible and that's what they're going to tell you about stolen our thunder for the first slide okay I'm Chris I mean I've been working for any lapse for about six months now and yet ed marshal so I work at infinity works I've worked with Chris in the run docker at scale so a few stats about us we've got em for over 4,000 get up stars got a million docker pulls that's not bad for a project that's only been around for just over 12 months and and we saw we've got enterprise features built in there so we've got authentication you can authenticate to an ad can authenticate to an LDAP directory and local database and stuff so this is sort of where we're coming to with the Prometheus stuff as part of the the rancher and server we have this thing called a catalog so the catalogs got three parts to it we've got a certified catalog which is basically things that we've written that we will support as part of any support contract we've got the private catalog where

### Excerpt da transcript

alright please welcome to the stage at marshall in chris owen so chris has been the UK technical lead of Rancho labs and it has been consultant at infinity works and they've been working together to make dynamic monitoring with prometheus possible and that's what they're going to tell you about stolen our thunder for the first slide okay I'm Chris I mean I've been working for any lapse for about six months now and yet ed marshal so I work at infinity works I've worked with Chris in the previous role and sort of came across rancher and prometheus at the same time so did some work with Chris and did some work with rancher and sort of snowball from there and we'll kind of go into that in the presentation so we're just going to give you sort of a bit of a background about companies that we work for and how we came across dynamic monetary and sort of link the two together with your own trim prometheus cool okay can I just ask who's heard of ranch elapsed excellent that's good that's good yeah yeah I'm so we've got yes it's always a surprise cuz you never know because when you go and speak at a docker conference it's like putting which every time he goes up when you breathe his confidence you know never quite sure what's gonna happen so em yeah so we've got two main products we've got a rancher server which is our container management platform and we've got round to OS so I'm going to go into the rancher serve a piece a little bit later on the presentation but rancho s just very quickly is basically a very lightweight cut down linux distribution that runs dr.

as pig one so it's basically a doc rised operating system it's about 30 meg when installed and it's sort of very very small footprint if you wanted to run a doctor environment on a bunch of hosts so this a.m eyes upon AWS and various other places you can get image and it's worth having a look at if you run in dr. encryption well I mean think it works so I work boy too much but infinity works were consultancy and we tend to sort of be a collection of people who've made various mistakes and then hopefully you've learned from them so you know what do you do we're helping companies solve problems with uk-based and we have an office out here and my role and that is using technologies in a blur to sort of resolve those issues for them so do not work a lot of good companies and that's how I first met Chris as well um alright so concept so dynamic monitoring so this change while starts making these slides and are
