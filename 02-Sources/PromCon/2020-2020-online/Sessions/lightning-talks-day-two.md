---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus"]
speakers: []
source_url: https://promcon.io/2020-online/talks/lightning-talks-day2/
youtube_url: https://www.youtube.com/watch?v=UTODrbR9yxE
youtube_search_url: https://www.youtube.com/results?search_query=Lightning+Talks+Day+Two+PromCon+2020
video_match_score: 0.872
status: video-found
---

# Lightning Talks Day Two

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/lightning-talks-day2/
- YouTube: https://www.youtube.com/watch?v=UTODrbR9yxE

## Resumo

Talk da PromCon sobre Lightning Talks Day Two.

## Abstract oficial

_Abstract não encontrado._

## Links

- Página oficial: https://promcon.io/2020-online/talks/lightning-talks-day2/
- YouTube: https://www.youtube.com/watch?v=UTODrbR9yxE
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UTODrbR9yxE
- YouTube title: PromCon EU 2019: Lightning Talks Day Two
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/lightning-talks-day-two/UTODrbR9yxE.txt
- Transcript chars: 65137
- Keywords: actually, metrics, prometheus, basically, running, storage, pretty, version, silence, capacity, another, security, manager, everything, systems, alerts, numbers, probably

### Resumo baseado na transcript

[Music] okay hey hello I'm talking about metric storage for capacity management of openshift clusters we've heard something about capacity management so the part is capacity management needs highly aggregated metrics for not a capacity quota and resource usages probably you want to keep this over several months and years unfortunately Pro meters has only one retention policies for also we have a conflict here in our meter system for once we want to have detailed metrics for post-mortem analysis which we only want to need days or up to

### Excerpt da transcript

[Music] okay hey hello I'm talking about metric storage for capacity management of openshift clusters we've heard something about capacity management so the part is capacity management needs highly aggregated metrics for not a capacity quota and resource usages probably you want to keep this over several months and years unfortunately Pro meters has only one retention policies for also we have a conflict here in our meter system for once we want to have detailed metrics for post-mortem analysis which we only want to need days or up to months and on the other hand we need these highly aggregated metrics for a long term so we heard also before the one solution to this is to have long-term storage why are the which was first why are they provide us with preemie size remote right feature and with this we can we can keep the capacity management metrics in storage and we can essentially use the same dashboards directly on premiere OS and on the long term storage so next thing is a small architecture for this so for Cuban ages up shift clusters we have the classical set up here have the promised OS within within the cluster set up and for the optional part another component is added shift state metrics which provides us additionally with object specific metric and of course so the remote side we put outside our clusters to be monitored because we want to keep the capacity management data or for several clusters in one place so we looked for a central storage system so this can be set up on a virtual machine or in another class than you would like so forth uh no solution we need a couple of containers to to run them so the first is the itano's receiver which receives the metrics by a remote write and then stores it in a compatible bucket in our case we used the Menuhin Mineo container to do this and we need regularly running from us compactor and to get the storage efficient for creaming we wanted to use a fauna as visualization pack and therefore we need a saunas query which can which provides the query interferometers from qf query interface and this tunnel store container to talk to the s3 bucket so what's the result of this is this capacity management overview where we keep an overview of the whole cluster for memory CPU and ports which are the typical resources and yeah what we distinguished what we see on the on the right hand side here is that we distinguish between application and infrastructure containers so we can keep an eye on both of them the tricky p
