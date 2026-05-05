---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Networking"
themes: ["Networking"]
speakers: ["Rob Scott", "Google", "Shane Utt", "Kong", "Inc."]
sched_url: https://kccncna2022.sched.com/event/182IG/exiting-ingress-with-the-gateway-api-rob-scott-google-shane-utt-kong-inc
youtube_search_url: https://www.youtube.com/results?search_query=Exiting+Ingress+With+the+Gateway+API+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Exiting Ingress With the Gateway API - Rob Scott, Google & Shane Utt, Kong, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Networking]]
- Temas: [[Networking]]
- País/cidade: United States / Detroit
- Speakers: Rob Scott, Google, Shane Utt, Kong, Inc.
- Schedule: https://kccncna2022.sched.com/event/182IG/exiting-ingress-with-the-gateway-api-rob-scott-google-shane-utt-kong-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Exiting+Ingress+With+the+Gateway+API+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Exiting Ingress With the Gateway API.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182IG/exiting-ingress-with-the-gateway-api-rob-scott-google-shane-utt-kong-inc
- YouTube search: https://www.youtube.com/results?search_query=Exiting+Ingress+With+the+Gateway+API+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sTQv4QOC-TI
- YouTube title: Exiting Ingress With the Gateway API - Rob Scott, Google & Shane Utt, Kong, Inc.
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/exiting-ingress-with-the-gateway-api/sTQv4QOC-TI.txt
- Transcript chars: 30808
- Keywords: gateway, ingress, traffic, cluster, implementation, namespace, implementations, little, routes, gateways, resource, another, splitting, actually, balancer, create, canary, reference

### Resumo baseado na transcript

I'm Shane utt from Kong and I am one of the Gateway API maintainers and I'm Rob Scott from Google and I'm also one of the Gateway API maintainers and today we're going to be covering everything about Gateway API why you might want to switch from Ingress to Gateway API and exactly how you can do that so let's do an overview of these apis real quick let's take a look at what we're talking about so the Ingress API which everybody's familiar with it's pretty simple you can I'm using an internal load balancer for this demo I actually have to get somewhere into the network the easiest way to do this is I'm just going to exec into a pod and I'm going to run a few curl requests and you can

### Excerpt da transcript

I'm Shane utt from Kong and I am one of the Gateway API maintainers and I'm Rob Scott from Google and I'm also one of the Gateway API maintainers and today we're going to be covering everything about Gateway API why you might want to switch from Ingress to Gateway API and exactly how you can do that so let's do an overview of these apis real quick let's take a look at what we're talking about so the Ingress API which everybody's familiar with it's pretty simple you can do host and path matching you can forward to a service you can do TLS configuration it's been around for a long time and there are lots of implementations like 22 plus implementations there are some limitations of the Ingress API um there's not enough features and this ended up leading to custom extensions everywhere so extensions that were they were and the biggest problem was extensions that weren't portable like the traffic splitting header matching and sticky sessions were some notable ones uh became this annotation Wild West also it had an insufficient permission model so Gateway API intends to be the next generation of kubernetes routing and load balancing apis it's designed to be expressive role oriented we have 15 plus implementations right now and we graduated to Beta in July so if you take a look at this diagram over on the left you're going to see that in Gateway API we have three main kinds of resources we have the Gateway class if you're familiar with the Ingress class resource before it Gateway class is nearly identical then we have HD HP route and a bunch of other route types at the bottom we'll focus on HTTP because it's the most similar to Ingress but we'll show you very soon that HTTP route and the Ingress resource are also very similar Gateway is kind of a New Concept in this API and we'll be talking about that just a little bit after now Gateway API has a ton of features I know that we've got lots of feature requests throughout kubernetes networking for many of these things whether it's request redirects rewrites header matching method matching there's a lot of things in here that we've had feature requests for a long time Gateway API finally allows you to do many of these things but some of you may say hold on you know I can do this with Ingress there are a few things you can do with the Ingress API today but everything in that blue box is entirely new with Gateway API so a lot of net new things in kubernetes because of Gateway API you may be wondering like how on Earth
