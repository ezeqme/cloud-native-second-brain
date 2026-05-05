---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["Security", "Kubernetes Core"]
speakers: ["Jimmy Zelinskie", "authzed", "Lucas Käldström", "Upbound"]
sched_url: https://kccncna2024.sched.com/event/1i7m9/expanding-the-capabilities-of-kubernetes-access-control-jimmy-zelinskie-authzed-lucas-kaldstrom-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Expanding+the+Capabilities+of+Kubernetes+Access+Control+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Expanding the Capabilities of Kubernetes Access Control - Jimmy Zelinskie, authzed & Lucas Käldström, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Jimmy Zelinskie, authzed, Lucas Käldström, Upbound
- Schedule: https://kccncna2024.sched.com/event/1i7m9/expanding-the-capabilities-of-kubernetes-access-control-jimmy-zelinskie-authzed-lucas-kaldstrom-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Expanding+the+Capabilities+of+Kubernetes+Access+Control+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Expanding the Capabilities of Kubernetes Access Control.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7m9/expanding-the-capabilities-of-kubernetes-access-control-jimmy-zelinskie-authzed-lucas-kaldstrom-upbound
- YouTube search: https://www.youtube.com/results?search_query=Expanding+the+Capabilities+of+Kubernetes+Access+Control+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IXHCSSQeXBg
- YouTube title: Expanding the Capabilities of Kubernetes Access Control - Jimmy Zelinskie & Lucas Käldström
- Match score: 0.855
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/expanding-the-capabilities-of-kubernetes-access-control/IXHCSSQeXBg.txt
- Transcript chars: 35239
- Keywords: actually, authorization, access, cluster, problems, domains, question, language, talking, particular, resource, global, create, deployment, resources, called, everyone, probably

### Resumo baseado na transcript

this is the session on expanding the capabilities of kubernetes Access Control if that's not why you're here door is right back there um all right so as we get started I think it makes sense to understand who's up here and who's telling you and why you should listen um I myself I'm the co-founder of a company called ozed um as explicitly an authorization company so that ties straight into this talk um formerly I worked at a company called coros uh coros got acquired by Red Hat

### Excerpt da transcript

this is the session on expanding the capabilities of kubernetes Access Control if that's not why you're here door is right back there um all right so as we get started I think it makes sense to understand who's up here and who's telling you and why you should listen um I myself I'm the co-founder of a company called ozed um as explicitly an authorization company so that ties straight into this talk um formerly I worked at a company called coros uh coros got acquired by Red Hat Red Hat got acquired by IBM and I decided to start my own company um I'm an oci maintainer so that's the specification that defines what containers are uh so I also do that and then I've been around in this space since kind of the beginning since before kubernetes existed in the container ecosystem I've created a bunch of different projects in that time spice DB which is my current company does but also things like operator framework um Lucas yeah hi hi everyone um yeah I've also been here for for some nine years or something um I kind of uh represent the kubernetes side and like um have been thinking about how can we evolve kubernetes in these directions um been doing some Cube stuff like Cube admin and and similar things in the past um also doing the Cloud meetups for example in Finland and you should definitely come to the kubernetes Community Days that we're organizing in Helsinki in May next year cool all right so this talk has an agenda because authorization is a pretty de topic we don't want to get caught in Weeds um so we're going to give a very quick overview through the foundations of authorization so everyone's on the same page going into this then we're going to take stock of what kubernetes does for authorization these are things that probably yall are familiar with um but then we're going to talk about the challenges that exist with those Primitives um and kind of the problems that they are not addressing and then we're going to kind of dive into future looking and uh technologies that are going to help us kind of evolve with kubernetes um so I think it's by obligation that you always have this slide when you're talking about authorization um there's this terminology o and it's really ambiguous whether someone is talking about authentication or authorization um for this uh this talk the focus is entirely on authorization so not authentication and I prefer these completely alternative terms uh terms because I think they're far less ambiguous um that's identity for authen
