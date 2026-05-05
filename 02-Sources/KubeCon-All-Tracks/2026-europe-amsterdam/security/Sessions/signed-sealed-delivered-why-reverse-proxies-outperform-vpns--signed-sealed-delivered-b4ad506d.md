---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Security"
themes: ["Security"]
speakers: ["Peter ONeill", "Teleport", "Boris Kurktchiev", "Independent"]
sched_url: https://kccnceu2026.sched.com/event/2CW56/signed-sealed-delivered-why-reverse-proxies-outperform-vpns-peter-oneill-teleport-boris-kurktchiev-independent
youtube_search_url: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered%3A+Why+Reverse+Proxies+Outperform+VPNs+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs - Peter ONeill, Teleport & Boris Kurktchiev, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Peter ONeill, Teleport, Boris Kurktchiev, Independent
- Schedule: https://kccnceu2026.sched.com/event/2CW56/signed-sealed-delivered-why-reverse-proxies-outperform-vpns-peter-oneill-teleport-boris-kurktchiev-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered%3A+Why+Reverse+Proxies+Outperform+VPNs+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW56/signed-sealed-delivered-why-reverse-proxies-outperform-vpns-peter-oneill-teleport-boris-kurktchiev-independent
- YouTube search: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered%3A+Why+Reverse+Proxies+Outperform+VPNs+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=0tq06AAdKWQ
- YouTube title: Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs - Peter O'Neill & Boris Kurktchiev
- Match score: 0.877
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/signed-sealed-delivered-why-reverse-proxies-outperform-vpns/0tq06AAdKWQ.txt
- Transcript chars: 25939
- Keywords: identity, access, network, envoy, information, endpoints, reverse, trying, authorization, endpoint, inside, little, keycloak, actually, talking, single, authentication, controls

### Resumo baseado na transcript

I'm very surprised that so many of you are skipping beer hour and are hanging out with us today this late into the conference. Before we start Peter and I would like to take a quick selfie with all of you to prove to our company that we're not on a boondoggle. What we'll be talking about today are two open source projects, Keycloak and Envoy, and we'll be using those in order to build out the architecture that we're talking about. I've spent a lot of times a lot of time in the IT industry and I love logging into Splunk and then I hate writing a 7-mile long query in order to try and prove out that an attack happened or that to figure out how an attack happened. So now you're able to scale the idea of a VPN instead of to a singular front gate to your entire network, you can now put it in front of just about anything. And with that I'm going to hand it off to Peter to walk you through the actual demo.

### Excerpt da transcript

All right. Hi everybody. I'm very surprised that so many of you are skipping beer hour and are hanging out with us today this late into the conference. Before we start Peter and I would like to take a quick selfie with all of you to prove to our company that we're not on a boondoggle. All right. Appreciate it. Everybody I saw the people making funny faces in the back. So yeah, thank you for being here. What we're going to be talking about is sign sealed and delivered. How do we do identity based control with reverse proxies and why that's important and why that's something that you would want to implement and do in your companies and day-to-day lives. First and foremost, why you should you know trust us or why you should listen to us. Hi, I am Boris. My last name is very complicated. I am the field CTO for Teleport. I'm also one of the leads for the CNCF AI TCG. Shout out. We just published some agentic based um cloud native framework if you will. You should go read about that. And then Peter. Hi. So my name is Peter O'Neal.

I'm a sales engineering manager at Teleport. Uh and yeah, this is this is something like zero trust security something I've been working on for for many years now. So definitely definitely excited to share with you guys. All right. So let's get going. Why are we here? I think AI has done one thing and I have to talk about AI cuz we are here and AI is everywhere, right? It has made it very clear that our identity story is broken. And more specifically we have been using things like VPNs. We have been using singular points of control in order to enable access to private resources. And the issue with something like VPN is that it's a single front gate and once you're inside you do not have the you know the tools necessary to reduce lateral control lateral access to reduce the ability to crawl the network to discover and maybe that is just enough when we're dealing with just humans, but now we have automations that can come in and without the right authorizations, without the right authentication, without the right controls can just wreak havoc.

I think we've all been reading the news. All it takes is a single identity to be consumed as Trivy discovered unfortunately yesterday and cause a lot of issues. So why or what are we proposing? Right? The idea behind our entire talk is that you need to do the lift to add authentication, authorization to every endpoint in your stack. And that is that means absolutely everything that your end users
