---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["Networking"]
speakers: ["Adam Sayah", "Jim Barton", "Solo.io"]
sched_url: https://kccnceu2022.sched.com/event/yto7/cloud-native-building-blocks-an-interactive-envoy-proxy-workshop-adam-sayah-jim-barton-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Cloud-Native+Building+Blocks%3A+An+Interactive+Envoy+Proxy+Workshop+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Cloud-Native Building Blocks: An Interactive Envoy Proxy Workshop - Adam Sayah & Jim Barton, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[Networking]]
- País/cidade: Spain / Valencia
- Speakers: Adam Sayah, Jim Barton, Solo.io
- Schedule: https://kccnceu2022.sched.com/event/yto7/cloud-native-building-blocks-an-interactive-envoy-proxy-workshop-adam-sayah-jim-barton-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud-Native+Building+Blocks%3A+An+Interactive+Envoy+Proxy+Workshop+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Cloud-Native Building Blocks: An Interactive Envoy Proxy Workshop.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yto7/cloud-native-building-blocks-an-interactive-envoy-proxy-workshop-adam-sayah-jim-barton-soloio
- YouTube search: https://www.youtube.com/results?search_query=Cloud-Native+Building+Blocks%3A+An+Interactive+Envoy+Proxy+Workshop+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SNM-wnyRR8U
- YouTube title: Cloud-Native Building Blocks: An Interactive Envoy Proxy Workshop - Adam Sayah & Jim Barton, Solo.io
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/cloud-native-building-blocks-an-interactive-envoy-proxy-workshop/SNM-wnyRR8U.txt
- Transcript chars: 72383
- Keywords: envoy, configuration, filter, upstream, request, important, cluster, connection, workshop, actually, metrics, listener, couple, interface, logs, basically, everything, response

### Resumo baseado na transcript

all right good morning everyone uh buenos dias um i i don't know about you but adam and i talk about envoy and technologies built on top of envoy to people all the time and for the past two years most of that talking has been to you know two-dimensional people on the other side of the zoom uh meeting and so to see this many people here in three-dimensional form is is pretty exciting for us so so we're really glad you're here we hope you're going to get with those protocols it's really built from the ground up to work in a dynamic services environment so an environment like kubernetes where services can be ephemeral they're going up they're going down new things are being added it's not a single static environment with a collection of you know 10 or 12 software monoliths behind it it's actually designed for a dynamic environment it's also built from the ground up to be dynamically configurable so one of the things that adam will talk about a bit later as we appstream again is a reminder just a demo application we installed with our docker compose stack okay so here we have a backend service now that we have this name and this cluster called app stream defined let's define the routing to that and i way back to the back end and if you see we're just referencing the cluster upstream that we defined which is our demo application so let's now that we had the we have the...

### Excerpt da transcript

all right good morning everyone uh buenos dias um i i don't know about you but adam and i talk about envoy and technologies built on top of envoy to people all the time and for the past two years most of that talking has been to you know two-dimensional people on the other side of the zoom uh meeting and so to see this many people here in three-dimensional form is is pretty exciting for us so so we're really glad you're here we hope you're going to get some really useful information perhaps a spark of inspiration out of this workshop we are going to be talking about envoy proxy and specifically we're going to be talking about it in the context of a hands-on workshop that's going to give you the opportunity to uh to get your hands dirty just a bit to get a taste of what using raw envoy proxy is uh is like so if you're interested in following along with the hands-on exercise you know get your laptop out if you have uh if you have chrome installed on your laptop we've had we've had great results from chrome with this with this particular workshop uh occasionally there can be issues with with other browsers so yeah so absolutely get that fired up and we'll give you we'll give you some instructions for uh for for getting connected to that in just uh in just a bit uh before we start into the actual uh hands-on workshop part what we want to do is uh is just lay a little bit of groundwork for uh for for who we are and what is envoy so so my name is jim barton i am a field engineer with solo.io i've been here for a couple of years now adam uh adam sayah i'm a field engineer working with jim and the team a couple of years too can you take any questions here yep so um if you if you have questions over the course of the uh of this session what we'd encourage you to do given the size of the audience and the fact that a large percentage of it is remote what we'd like to do is encourage you to get onto the the session chat you can do that by following this bitly link up here bit.ly slash envoy dash chat and we have one of our solo colleagues here somewhere alex over here stage right heading in the corner yep in the corner we keep him back there in the corner um and uh he will be he will be happy to answer your questions just go to the q a tab and i think that can work as kind of a quasi-chat mechanism um if you have issues we we hope that you won't but but just in case alex will be there to answer your questions we also there's a lot of content in the next 90 minutes and
