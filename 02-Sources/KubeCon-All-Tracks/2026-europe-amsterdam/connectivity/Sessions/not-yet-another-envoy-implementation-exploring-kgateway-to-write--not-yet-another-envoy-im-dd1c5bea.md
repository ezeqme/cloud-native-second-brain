---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Ricardo Katz", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CVyZ/not-yet-another-envoy-implementation-exploring-kgateway-to-write-your-own-gatewayapi-backend-ricardo-katz-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Not+Yet+Another+Envoy+Implementation+-+Exploring+Kgateway+To+Write+Your+Own+GatewayAPI+Backend+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Not Yet Another Envoy Implementation - Exploring Kgateway To Write Your Own GatewayAPI Backend - Ricardo Katz, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ricardo Katz, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CVyZ/not-yet-another-envoy-implementation-exploring-kgateway-to-write-your-own-gatewayapi-backend-ricardo-katz-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Not+Yet+Another+Envoy+Implementation+-+Exploring+Kgateway+To+Write+Your+Own+GatewayAPI+Backend+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Not Yet Another Envoy Implementation - Exploring Kgateway To Write Your Own GatewayAPI Backend.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVyZ/not-yet-another-envoy-implementation-exploring-kgateway-to-write-your-own-gatewayapi-backend-ricardo-katz-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Not+Yet+Another+Envoy+Implementation+-+Exploring+Kgateway+To+Write+Your+Own+GatewayAPI+Backend+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9VqzQgin6vk
- YouTube title: Not Yet Another Envoy Implementation - Exploring Kgateway To Write Your Own GatewayA... Ricardo Katz
- Match score: 0.989
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/not-yet-another-envoy-implementation-exploring-kgateway-to-write-your/9VqzQgin6vk.txt
- Transcript chars: 20151
- Keywords: gateway, actually, configuration, envoy, control, server, basically, implementation, client, resource, messages, write, wanted, address, message, workload, saying, apache

### Resumo baseado na transcript

Probably uh you are seeing like this crossed K gateway stuff and a lot of people they are asking me like why you cross it. So apparently uh K gateway maintainers they decided to make my life harder and they decided to split the control plane uh two days before my talk. uh I do not want my data plane accessing kubernetes API so that's a trauma that I get from ingress in ginex right so uh one of the things it's like uh when you are developing a gateway implementation or something that deals with the if it's good or not sorry but uh uh I I I already put that on if you want to download the PDF as well uh so you apply a configuration in your Kubernetes API then K gateway will do the whole reconciliation loop for So logs and agent gateway system uh in GX gateway I can see the message here on in GX log message sending all all of those things right so basically what I want actually to to to pass to you it's like uh if you

### Excerpt da transcript

Welcome everyone. Uh my talk today is about exploring agent gateway. Probably uh you are seeing like this crossed K gateway stuff and a lot of people they are asking me like why you cross it. So apparently uh K gateway maintainers they decided to make my life harder and they decided to split the control plane uh two days before my talk. So now it's like it's part in agent gateway to write your own gateway API back end. Uh I am Ricardo. I am a software engineer at Red Hat doing all gate API stuff. I was doing previously a long time ago in resin genex stuff before James decided to deprecate and archive that. Thank you James. Woohoo. I'm maintainer of gate API at Kubernetes. Uh I like Lego are playing traveling and making jokes at the wrong moments. Usually that's what get me in trouble. And uh my soccer team Vorons. Thank you. Uh okay come on guys. So uh you want to write you want your own gateway API implementation right? So um I've been hearing that a lot like people saying yeah uh I don't like envoy I want to do Apache web server whatever.

So I wanted to have I tried that like I wanted to have an Apache HTTP as a back end uh with FreeBSD. It's very bad idea. Uh I did that with Injet because it was my comfort zone but uh you know you can do whatever you want. It's your time your Gemini license. uh I do not want my data plane accessing kubernetes API so that's a trauma that I get from ingress in ginex right so uh one of the things it's like uh when you are developing a gateway implementation or something that deals with the traffic coming to your cluster you don't want the same pod that access your API server to be exposed to your users otherwise you're going to get cve uh and I want to make it easy and reusable for other backends uh that's something that we tried with in gape uh I'm Not sure how many of you know about or have heard about ingate the other project that we kind of archive it but we tried to do something like that which was like some generic control plane for gateway API. Uh so creating your own gateway API implementation is actually easy you know like if you just seriously you just ask you know some AI after all like we are just doing AI uh to implement that and you ask like okay I need a gate API controller and um I just need to reconcile gateway classes listeners HTTP route put on the data plane and done right so that's easy and actually uh let me put this thing here because I wanted to make it easier so So you can see uh I asked Gemini to
