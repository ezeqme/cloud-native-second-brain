---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Adam Zwickey", "Liam White", "Tetrate"]
sched_url: https://kccnceu2021.sched.com/event/iE2W/turning-your-cloud-native-apps-inside-out-with-a-service-mesh-adam-zwickey-liam-white-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Turning+Your+Cloud+Native+Apps+Inside+Out+With+a+Service+Mesh+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Turning Your Cloud Native Apps Inside Out With a Service Mesh - Adam Zwickey & Liam White, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: Virtual / Virtual
- Speakers: Adam Zwickey, Liam White, Tetrate
- Schedule: https://kccnceu2021.sched.com/event/iE2W/turning-your-cloud-native-apps-inside-out-with-a-service-mesh-adam-zwickey-liam-white-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Turning+Your+Cloud+Native+Apps+Inside+Out+With+a+Service+Mesh+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Turning Your Cloud Native Apps Inside Out With a Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE2W/turning-your-cloud-native-apps-inside-out-with-a-service-mesh-adam-zwickey-liam-white-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Turning+Your+Cloud+Native+Apps+Inside+Out+With+a+Service+Mesh+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eLxx8WjmEdk
- YouTube title: Turning Your Cloud Native Apps Inside Out With a Service Mesh - Adam Zwickey & Liam White, Tetrate
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/turning-your-cloud-native-apps-inside-out-with-a-service-mesh/eLxx8WjmEdk.txt
- Transcript chars: 28893
- Keywords: application, envoy, applications, spring, traffic, mesh, across, network, architecture, within, actually, ingress, discovery, security, native, little, lastly, libraries

### Resumo baseado na transcript

okay good afternoon everyone great to meet you my name is adam i have with me liam we're from touchrate and we're super excited to be able to talk on this topic of how we can turn our cloud native applications inside out using a service mesh so as by way of introduction i'm part of our solution engineering organization at tetrad really a long time proponent and contributor to open source very active in the cloud foundry spring and kubernetes ecosystems and i have like i said liam with

### Excerpt da transcript

okay good afternoon everyone great to meet you my name is adam i have with me liam we're from touchrate and we're super excited to be able to talk on this topic of how we can turn our cloud native applications inside out using a service mesh so as by way of introduction i'm part of our solution engineering organization at tetrad really a long time proponent and contributor to open source very active in the cloud foundry spring and kubernetes ecosystems and i have like i said liam with me i'll let him introduce himself hi yes i'm liam uh i'm a software engineer at tetri um i lead the cloud team um so and i'm also an student maintainer so i'm a rare combination of seo maintainer and user so that provides some interesting insight great so what we're going to cover today is first a little bit of a history or what we kind of view as the common patterns and building blocks that are used for building cloud native applications specifically using the spring ecosystem and spring cloud and some of the iep that netflix contributed to the open source then we're going to cover how does service mesh fit in with this type of architecture and this type of approach with java applications then lastly we'll walk through a little bit of a migration example of how we go from potentially using some of these netflix libraries to introducing service mesh into the app now we're going to go through a couple of code examples architecture examples pretty quickly but you'll notice there is a link to a github repo that actually has the before and after code that you all can take a look at and maybe even try and run and use as an example as we start out i definitely want to preface this whole presentation with touch rate myself we all heart spring and spring cloud so the take away from this should not be abandoned spring cloud or abandoned spring and go a different route use service mesh as a completely new alternative the point is to show you how this can augment and support your spring and your spring boot applications potentially unlocking some new capabilities that maybe you don't have today and maybe making a few things a little bit easier for you your developers and your operators of your cloud platforms so how do we get to this point where looking at the end of the timeline where we are in 2020 or now 2021 um in what i see as most organizations looking at how do i build microservice or cloud native applications and then spread them across clusters and across multiple clouds well w
