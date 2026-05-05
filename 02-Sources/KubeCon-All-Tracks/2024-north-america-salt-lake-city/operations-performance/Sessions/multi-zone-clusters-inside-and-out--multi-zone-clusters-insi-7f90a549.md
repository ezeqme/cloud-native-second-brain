---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Tom Dean", "Phil Henderson", "Buoyant"]
sched_url: https://kccncna2024.sched.com/event/1i7ne/multi-zone-clusters-inside-and-out-tom-dean-phil-henderson-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Zone+Clusters+Inside+and+Out+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Multi-Zone Clusters Inside and Out - Tom Dean & Phil Henderson, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Tom Dean, Phil Henderson, Buoyant
- Schedule: https://kccncna2024.sched.com/event/1i7ne/multi-zone-clusters-inside-and-out-tom-dean-phil-henderson-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Zone+Clusters+Inside+and+Out+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Multi-Zone Clusters Inside and Out.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ne/multi-zone-clusters-inside-and-out-tom-dean-phil-henderson-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Multi-Zone+Clusters+Inside+and+Out+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WhFsYVHmg6E
- YouTube title: Multi-Zone Clusters Inside and Out - Tom Dean & Phil Henderson, Buoyant
- Match score: 0.76
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/multi-zone-clusters-inside-and-out/WhFsYVHmg6E.txt
- Transcript chars: 33998
- Keywords: routing, topology, traffic, points, latency, everything, little, success, important, observability, metrics, failure, endpoints, pretty, spread, connection, annotation, enough

### Resumo baseado na transcript

hi I'm Tom Dean I'm a field engineer with buyant and we are the creators of linker D service mesh and Phil Henderson is here with me this is our first time presenting please be gentle with us and uh you know right now we're scared out of our wits but we'll be okay uh show of hands uh how many people here in the audience are service mesh users cool linkerd users few cool how many people run in a multi-az setup right now and with their clusters how and metrics kind of the same thing but they are but they're not there's a lot of overlap and the reason that's important and it's important in this talk is that we want to know what's going on with topology aware routing and with our traffic in general so that if we witness a condition that's strange or maybe we don't witness it at all we need something to tell us hey something's hanky here we really need to kind of look and see what's going on performance is another and it's a lot more powerful too it's much better this one was a little barbaric demo yeah and that was our goal was be able to lift this stuff right out of our readme and whatnot it's just you know the the the timeline for getting it working and and fixing python took a back seat right demos are hard but we wanted to do it live a and there's a lot of commands I can't remember all those oh yeah yeah yeah check it out yeah it's it

### Excerpt da transcript

hi I'm Tom Dean I'm a field engineer with buyant and we are the creators of linker D service mesh and Phil Henderson is here with me this is our first time presenting please be gentle with us and uh you know right now we're scared out of our wits but we'll be okay uh show of hands uh how many people here in the audience are service mesh users cool linkerd users few cool how many people run in a multi-az setup right now and with their clusters how many people are paying a lot of money for cross- ay traffic that's what I expected right so today we're here to talk a little bit about cross ay traffic and really focus on kind of you know what what the impact of that is and and uh how you can leverage topology aware routing to avoid that and you know how you can use a service mesh to kind of keep an eye on what topology aware routing does and understanding understand what's happening in your cluster and you know address certain scenarios this is based on a blog post that I worked on with William our CEO if you'd like to go ahead and uh dig down and read that you can scan this QR code or you can go up to buy.

and look for the blog section and it's in there it's pretty recent a couple of months back it shouldn't be hard to find so it digs in we did a little bit of research wrote this up and uh talked about you know some ways to to mitigate it so before we start reliability is the first Duty right and this is why we're using service meshes generally it's going to give us security that's with us you know our experience has been mtls is the gateway drug for most people when it's we're talking service meshes they want to mesh they want to get encryption in Flight you know they want to make sure that their traffic is is secure but the another big thing for customers is observability you can consider observability and metrics kind of the same thing but they are but they're not there's a lot of overlap and the reason that's important and it's important in this talk is that we want to know what's going on with topology aware routing and with our traffic in general so that if we witness a condition that's strange or maybe we don't witness it at all we need something to tell us hey something's hanky here we really need to kind of look and see what's going on performance is another Advantage you know topology we routing is great but when you put Linker D in the mix we're going to get this power of two choices load balancing and I'm not going to go deep into it but we look a
