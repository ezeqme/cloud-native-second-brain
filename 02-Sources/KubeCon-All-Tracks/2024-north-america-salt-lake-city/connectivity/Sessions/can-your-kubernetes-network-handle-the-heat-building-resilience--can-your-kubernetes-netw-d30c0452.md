---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["AI ML", "Networking", "Kubernetes Core", "SRE Reliability"]
speakers: ["Lior Lieberman", "Google", "Surya Seetharaman", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7kv/can-your-kubernetes-network-handle-the-heat-building-resilience-with-ai-chaos-lior-lieberman-google-surya-seetharaman-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Can+Your+Kubernetes+Network+Handle+the+Heat%3F+Building+Resilience+with+AI+Chaos+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Can Your Kubernetes Network Handle the Heat? Building Resilience with AI Chaos - Lior Lieberman, Google & Surya Seetharaman, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Networking]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Lior Lieberman, Google, Surya Seetharaman, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7kv/can-your-kubernetes-network-handle-the-heat-building-resilience-with-ai-chaos-lior-lieberman-google-surya-seetharaman-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Can+Your+Kubernetes+Network+Handle+the+Heat%3F+Building+Resilience+with+AI+Chaos+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Can Your Kubernetes Network Handle the Heat? Building Resilience with AI Chaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kv/can-your-kubernetes-network-handle-the-heat-building-resilience-with-ai-chaos-lior-lieberman-google-surya-seetharaman-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Can+Your+Kubernetes+Network+Handle+the+Heat%3F+Building+Resilience+with+AI+Chaos+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2oTtpRpv3M8
- YouTube title: Can Your Kubernetes Network Handle the Heat? Building Resilience wit... L. Lieberman, S. Seetharaman
- Match score: 0.927
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/can-your-kubernetes-network-handle-the-heat-building-resilience-with-a/2oTtpRpv3M8.txt
- Transcript chars: 33599
- Keywords: cluster, scenarios, basically, litmus, actually, networking, production, traffic, network, scenario, latency, probably, prompt, testing, clusters, inject, experiment, usually

### Resumo baseado na transcript

thank you everyone for coming to our session we'll be talking about how can you build resilient kubernetes networks using AI K experiments I'm sura sitaraman I'm an engineer working on the open shift networking team at Red Hat I'm also a Sig Network contributor yeah and I'm leor um liberman I'm a side relability engineer at Google and um I'm very active in the gway API Community I'm also maintaining a tool called in gway uh which helps uh moving configuration to get away from Ingress and as you

### Excerpt da transcript

thank you everyone for coming to our session we'll be talking about how can you build resilient kubernetes networks using AI K experiments I'm sura sitaraman I'm an engineer working on the open shift networking team at Red Hat I'm also a Sig Network contributor yeah and I'm leor um liberman I'm a side relability engineer at Google and um I'm very active in the gway API Community I'm also maintaining a tool called in gway uh which helps uh moving configuration to get away from Ingress and as you can hear uh my voice um had different plans so apologies for that and um yeah while we here to we here to talk about uh resiliency we're here to talk about networking and as we all know networking is hard it's uh kind of a big deal right and we have all this small Niche a lot of stuff we need to configure we need to remember but when we move to even talk about Cloud networking that's even harder right we have uh multiple Scopes we need to deal with regions zones um we have like complex environment setups we have VC peerings routing rules and those are just literally just a few things I had in mind to put on the slide we need to take care about tenant isolation encryption and then the smartest thing uh the smartest thing we could do after that is um moving to kubernetes right and kubernets networking is definitely the hardest um as you can see to my right like a lot of objects a lot of manifest kind of going on a screen and um in order to be able to remember to know to configure all that people need to deal with HP routes Network policies a lot of different objects that um are usually um basically a lot to remember right and how many people uh here are like sres platform Engineers um infrastructure Engineers yeah a lot well bless you um because traditionally it's uh your responsibility and that actually should be my next slide um but yeah what could possibly go wrong um policies with different labels right uh we can have broken pod networking we can have different implementation uh of the networking API working differently we can have issues with SSL TLS and uh as I said bless you all the SRE Engineers the infrastructure Engineers were uh most commonly uh responsible to develop obstructions for this comp complex configurations so the R&D team the the development team don't need to deal with everything um they also responsible for the five in conformance requirements so what is a service that actually uh can go to production how it should look like um and usually they
