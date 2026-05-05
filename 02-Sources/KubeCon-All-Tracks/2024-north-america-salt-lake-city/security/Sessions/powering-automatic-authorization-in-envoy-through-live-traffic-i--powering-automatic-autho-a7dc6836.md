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
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Dom Del Nano", "Pixie core maintainer"]
sched_url: https://kccncna2024.sched.com/event/1i7pm/powering-automatic-authorization-in-envoy-through-live-traffic-inspection-dom-del-nano-pixie-core-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Powering+Automatic+Authorization+in+Envoy+Through+Live+Traffic+Inspection+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Powering Automatic Authorization in Envoy Through Live Traffic Inspection - Dom Del Nano, Pixie core maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Dom Del Nano, Pixie core maintainer
- Schedule: https://kccncna2024.sched.com/event/1i7pm/powering-automatic-authorization-in-envoy-through-live-traffic-inspection-dom-del-nano-pixie-core-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Powering+Automatic+Authorization+in+Envoy+Through+Live+Traffic+Inspection+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Powering Automatic Authorization in Envoy Through Live Traffic Inspection.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pm/powering-automatic-authorization-in-envoy-through-live-traffic-inspection-dom-del-nano-pixie-core-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Powering+Automatic+Authorization+in+Envoy+Through+Live+Traffic+Inspection+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_d5ff8QTmX4
- YouTube title: Powering Automatic Authorization in Envoy Through Live Traffic Inspection - Dom Del Nano
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/powering-automatic-authorization-in-envoy-through-live-traffic-inspect/_d5ff8QTmX4.txt
- Transcript chars: 22915
- Keywords: authorization, policy, traffic, policies, authentication, envoy, details, actually, export, request, header, security, access, components, architecture, processing, ultimately, basically

### Resumo baseado na transcript

hello cucon my name is Dom Dono and I'm CEO and founder of cosmic and pixie core maintainer and today I'm excited to tell you more about how powering automatic authorization in Envoy through live traffic inspection Works before we jump into things a little bit more about myself I've been working in the ebpf and observability space for the last few years I first got introduced to the pixie project when I was at Twitter as an end user and since then I've uh moved over to the maintainer authorization so let's just do a brief recap of everything here so at this bottom part here we have our authentication layer we're using mtls between the front ends Envoy and the back ends Envoy for this demo we're actually going to have a front

### Excerpt da transcript

hello cucon my name is Dom Dono and I'm CEO and founder of cosmic and pixie core maintainer and today I'm excited to tell you more about how powering automatic authorization in Envoy through live traffic inspection Works before we jump into things a little bit more about myself I've been working in the ebpf and observability space for the last few years I first got introduced to the pixie project when I was at Twitter as an end user and since then I've uh moved over to the maintainer side and been working on the project the last few years before we get into the details here's a disclaimer I'm not a security expert despite working for a security company you've probably heard of um security is not a one-size fits-all solution and always consult your Security Experts um I see this as a beginning of a conversation about how we can use tools like pixie and other observ things to scope authorization policies so why do we care about automatic authorization the oasp top 10 has security misconfiguration listed at number five the authorization policies that people use last week last month last year eventually suffer from security and configuration drift products are sunsetted teams change the organizational boundaries are drawn differently and people forget to fix and write make the boundaries of your authorization to match the world today and so I'd like to see a place where authorization policies actually change in response to microservice environment changes and I think modern observability is to the rescue we've had a rise of zero instrumentation observability tools things like pixie and Hubble that provide real-time service map and layer visibility through the power of ebpf they instrument all Network traffic providing full visibility of an environment this means there's no blind spots nothing gets missed nothing needs to be manually instrumented and because their ability to Peak in at the layer 7even level this allows us to analyze access patterns and scope access rules accordingly on the Le hand side here this is a picture of what the pixie UI looks like we have a you know Network flow graph that shows kind of how all the microservices are connected on the right hand side is Hubble which shows a similar view and also is able to point out that these htdp services are talking to kofka zookeeper and elastic search downstreams so the goal of this talk is that we are going to close Au Z policy gaps as traffic evolves we're going to leverage these powerful ebpf too
