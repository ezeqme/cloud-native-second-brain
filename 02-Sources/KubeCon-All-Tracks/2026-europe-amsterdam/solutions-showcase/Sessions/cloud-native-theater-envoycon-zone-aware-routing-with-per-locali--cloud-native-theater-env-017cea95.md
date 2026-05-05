---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking"]
speakers: []
sched_url: https://kccnceu2026.sched.com/event/2EFzg/cloud-native-theater-envoycon-zone-aware-routing-with-per-locality-load-awareness-isaac-wilson-the-trade-desk
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Zone+Aware+Routing+With+Per-Locality+Load+Awareness-+Isaac+Wilson%2C+The+Trade+Desk+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | EnvoyCon: Zone Aware Routing With Per-Locality Load Awareness- Isaac Wilson, The Trade Desk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: N/A
- Schedule: https://kccnceu2026.sched.com/event/2EFzg/cloud-native-theater-envoycon-zone-aware-routing-with-per-locality-load-awareness-isaac-wilson-the-trade-desk
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Zone+Aware+Routing+With+Per-Locality+Load+Awareness-+Isaac+Wilson%2C+The+Trade+Desk+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | EnvoyCon: Zone Aware Routing With Per-Locality Load Awareness- Isaac Wilson, The Trade Desk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFzg/cloud-native-theater-envoycon-zone-aware-routing-with-per-locality-load-awareness-isaac-wilson-the-trade-desk
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+EnvoyCon%3A+Zone+Aware+Routing+With+Per-Locality+Load+Awareness-+Isaac+Wilson%2C+The+Trade+Desk+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZTacKbmGfMI
- YouTube title: Cloud Native Theater | EnvoyCon: Zone Aware Routing With Per-Locality Load Awareness- Isaac Wilson
- Match score: 1.006
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-envoycon-zone-aware-routing-with-per-locality-loa/ZTacKbmGfMI.txt
- Transcript chars: 14987
- Keywords: envoy, routing, traffic, dynamic, distribution, question, modules, policy, whatever, within, trying, experience, issues, request, actually, getting, client, module

### Resumo baseado na transcript

I work at a company called The Trade Desk and yeah, today I'm going to talk to you about a little bit about zone aware routing within Envoy and some issues that we How do I mute this? Some issues that we had with trying to run that with our environment and some changes that I'm trying to get into Envoy more recently to hopefully solve it for everybody. And for for most of the time this works amazing, but if you maybe have unequal amounts of incoming traffic or maybe different clients sending different amounts of traffic per zone this could create challenges. If any of you went to the Spotify talk yesterday that was actually an amazing talk and kind of solves a very similar challenge to this one. So we'd prefer to route traffic to the local zone as much as possible because we get reduced network cost, we get faster latency and it's just more efficient whether you're running in cloud or in on premise data centers. this and hopefully the demo gods will be with me to to show you some of that now, but yeah, this is one way that works and then the other thing that I've been working on is trying to add something in tree.

### Excerpt da transcript

Yes, thanks for the intro, Erica. Yeah, so I'm Isaac. I work at a company called The Trade Desk and yeah, today I'm going to talk to you about a little bit about zone aware routing within Envoy and some issues that we How do I mute this? Some issues that we had with trying to run that with our environment and some changes that I'm trying to get into Envoy more recently to hopefully solve it for everybody. Um Yeah, so to just quickly maybe go over our architecture. At the the last KubeCon I did a talk about our migration story from HAProxy to Envoy, but this is a basic overview of what one of our data centers look like. We run a lot of our infrastructure on premise and within one of these data centers we might have say like I don't know 100 to 200 racks within it and then with with in each rack we have a number of nodes and then on top of that we we run Kubernetes. Uh that's a a bit quick but hopefully this graph is starting to make sense and we use Envoy Gateway as the service to facilitate traffic routing.

I'm also an Envoy Gateway maintainer and what we do currently is on every single rack we we we use a least request routing algorithm and then we enable zone aware routing and we try to schedule our workloads roughly equal per rack. So if you look at the diagram here you can see that we have about three back end pods per rack and what that ends up meaning is that Envoy is going to route 100% of the traffic locally. If you're familiar with zone aware routing it effectively takes account of how many Envoy pods there are per zone as well as the number of upstream hosts there are per zone and then will route traffic accordingly. And for for most of the time this works amazing, but if you maybe have unequal amounts of incoming traffic or maybe different clients sending different amounts of traffic per zone this could create challenges. If any of you went to the Spotify talk yesterday that was actually an amazing talk and kind of solves a very similar challenge to this one. Um Yeah, that's a quick overview.

Hopefully that makes sense. And so jumping into maybe like what what are some of the the issues with zone aware routing that that we experience. So the way that we uh facilitate like different Envoy pods within the the data center getting traffic is we use what's called BGP anycast. What that just means is every single node that's running Envoy is advertising a certain IP. They're all advertising the same IP and you can mostly get a a roughly equal amount
