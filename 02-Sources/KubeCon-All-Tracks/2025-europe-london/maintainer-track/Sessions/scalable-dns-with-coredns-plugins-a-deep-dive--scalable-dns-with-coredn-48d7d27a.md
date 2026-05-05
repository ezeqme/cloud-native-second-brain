---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Yong Tang", "Ivanti", "John Belamaric", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1tcxt/scalable-dns-with-coredns-plugins-a-deep-dive-yong-tang-ivanti-john-belamaric-google
youtube_search_url: https://www.youtube.com/results?search_query=Scalable+DNS+With+CoreDNS+Plugins%3A+A+Deep+Dive+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Scalable DNS With CoreDNS Plugins: A Deep Dive - Yong Tang, Ivanti & John Belamaric, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yong Tang, Ivanti, John Belamaric, Google
- Schedule: https://kccnceu2025.sched.com/event/1tcxt/scalable-dns-with-coredns-plugins-a-deep-dive-yong-tang-ivanti-john-belamaric-google
- Busca YouTube: https://www.youtube.com/results?search_query=Scalable+DNS+With+CoreDNS+Plugins%3A+A+Deep+Dive+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Scalable DNS With CoreDNS Plugins: A Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxt/scalable-dns-with-coredns-plugins-a-deep-dive-yong-tang-ivanti-john-belamaric-google
- YouTube search: https://www.youtube.com/results?search_query=Scalable+DNS+With+CoreDNS+Plugins%3A+A+Deep+Dive+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=W3f5Ks0j2Q8
- YouTube title: Scalable DNS With CoreDNS Plugins: A Deep Dive - Yong Tang, Ivanti & John Belamaric, Google
- Match score: 0.778
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/scalable-dns-with-coredns-plugins-a-deep-dive/W3f5Ks0j2Q8.txt
- Transcript chars: 23178
- Keywords: little, plugin, plug-in, function, plugins, server, external, internal, configuration, actually, probably, pretty, exactly, network, request, basically, sockets, requests

### Resumo baseado na transcript

Um, we're gonna talk about core DNS today, so I hope you're in the right place. Um, so you're probably a little bit familiar with cordns at least because most of you are here for Kubernetes and uh, core DNS is the default DNS server in uh, in Kubernetes. different backends um with as I said file being the biggest one zone files and then kubernetes actually probably kubernetes is more widely used than file um which means we back using the kubernetes api um And uh but you can also do back directly If uh your network is going to receive a DNS query of the same name and if it's the traffic is coming from the internal you're going to return 1.1.1.1 this is a faked IP anyway right just give you example and if it's external you're going to return 8.8.8.8 eight fairly straightforward. This is nothing just a stop function to say this is uh demo plugin with a server type of DNS and the second function that's a setup. setup is going to pass the core file but because this is a demo plug-in we don't have lot of configurations we just say let's just pass the simple standard core file without anything okay so that's several lines of code again uh now we

### Excerpt da transcript

All right. Hello everybody. Um, welcome. Um, we're gonna talk about core DNS today, so I hope you're in the right place. Um, my name is John Belame. I'm with Google and uh, uh, my name is Yang. Uh, I'm working for Cord DNS. Yeah. Um, so you're probably a little bit familiar with cordns at least because most of you are here for Kubernetes and uh, core DNS is the default DNS server in uh, in Kubernetes. Um, but it is it is more than that. It is um, a general purpose DNS server pretty much everything but a recursive DNS server, although there's ways to make it that too. Um, so it's an authoritative DNS server primarily, but it's um, you know, it it's a little different than than your traditional uh, bind type of thing because we are written in Go, which is a memory safe language. Uh, a lot of people had a lot of CVES in bind and uh, so one of the reasons that cordiness exists is for that. But more interestingly, it exists because of the level of flexibility it offers. So it's really really easy to build integrations of cordns with other backends.

So sure we support zone files. Sure we support Kubernetes as a backend. Um but it's super easy to build other support and uh in a few minutes Yang is going to show you how to do that. Um but uh uh essentially you know it's just a few you know obviously it depends on how complicated your back end is but it's just a few lines of code in general uh today because of it so easy we support a bunch of different backends um with as I said file being the biggest one zone files and then kubernetes actually probably kubernetes is more widely used than file um which means we back using the kubernetes api um And uh but you can also do back directly um be backed directly by like your cloud provers uh DNS service. So essentially we can provide a caching layer um for those um reading from their APIs rather than from their upstream DNS. Um as a community we're pretty I mean there's 387 contributors but actively there's just a handful of people. It's pretty small friendly place. So, if you are interested in this um and I'll I'll I'll go through in detail some recent um things that contributors added that are are pretty cool.

But, um the you know, we're we're very welcoming as a as a project. Um and uh it's pretty easy to get to get involved. Um and uh I think now I'll hand it off to Yang who's going to talk a little bit about how you might extend it. uh and then I'll talk about like I said some new things that are in there and we'll
