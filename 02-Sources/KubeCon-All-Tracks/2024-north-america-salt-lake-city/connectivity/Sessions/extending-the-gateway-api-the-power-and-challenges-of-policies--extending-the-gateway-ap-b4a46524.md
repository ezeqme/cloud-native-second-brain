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
themes: ["Networking"]
speakers: ["Kate Osborn", "NGINX"]
sched_url: https://kccncna2024.sched.com/event/1i7ln/extending-the-gateway-api-the-power-and-challenges-of-policies-kate-osborn-nginx
youtube_search_url: https://www.youtube.com/results?search_query=Extending+the+Gateway+API%3A+The+Power+and+Challenges+of+Policies+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Extending the Gateway API: The Power and Challenges of Policies - Kate Osborn, NGINX

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Kate Osborn, NGINX
- Schedule: https://kccncna2024.sched.com/event/1i7ln/extending-the-gateway-api-the-power-and-challenges-of-policies-kate-osborn-nginx
- Busca YouTube: https://www.youtube.com/results?search_query=Extending+the+Gateway+API%3A+The+Power+and+Challenges+of+Policies+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Extending the Gateway API: The Power and Challenges of Policies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7ln/extending-the-gateway-api-the-power-and-challenges-of-policies-kate-osborn-nginx
- YouTube search: https://www.youtube.com/results?search_query=Extending+the+Gateway+API%3A+The+Power+and+Challenges+of+Policies+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=haeVAmhihT4
- YouTube title: Extending the Gateway API: The Power and Challenges of Policies - Kate Osborn, NGINX
- Match score: 0.953
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/extending-the-gateway-api-the-power-and-challenges-of-policies/haeVAmhihT4.txt
- Transcript chars: 32395
- Keywords: policy, gateway, policies, ingress, resource, defaults, client, attachment, annotations, application, settings, direct, inherited, resources, target, implementations, controller, cluster

### Resumo baseado na transcript

so thank you so much for coming today um I'm really excited to be here my name is Kate Osborne I work at enginex I'm a software engineer there on the enginex Gateway fabric team which is a free and open- Source implementation of the Gateway API so today I'm going to talk about extending the Gateway Pi in particular one type of extension mechanism called policy attachment I'm going to go uh explain what it is the two different types and then finish with some of the challenges okay

### Excerpt da transcript

so thank you so much for coming today um I'm really excited to be here my name is Kate Osborne I work at enginex I'm a software engineer there on the enginex Gateway fabric team which is a free and open- Source implementation of the Gateway API so today I'm going to talk about extending the Gateway Pi in particular one type of extension mechanism called policy attachment I'm going to go uh explain what it is the two different types and then finish with some of the challenges okay okay so to start what is the Gateway API well straight from the docs it's the next generation of communities Ingress load balancing and service mes apis what I want to focus on today though is that next generation of communities Ingress piece so why do we need a new generation of Ingress what problems in the Ingress API is the Gateway API trying to solve and there are several answers to that question but today we're talking about extensibility so how do you extend Ingress today well Ingress API like the Gateway API is a universal specification it boasts numerous implementations so it has to be portable but the Ingress API has a pretty basic feature set it doesn't support common routing capabilities like traffic waiting header manipulation rewrites redirects out of the box so when users want those features or they want to enable some proprietary configuration for their implementation of Ingress what do they do well they add an annotations to their Ingress resources and more annotations and more annotations so you might ask I hope not but you might ask what's wrong with annotations well first of all they're not portable right these implementations up on the screen here these are enginex Ingress controller annotations and if I wanted to switch from enginex Ingress controller to another Ingress controller let's say that even uses engine X under the hood all of those annotations would be different so you'd be mapping one to one all these annotations and both in controllers might not support the same thing right so it's definitely not portable what else well these are strings to Strings so they're unstructured they're harder to validate you can't apply a schema to them like you can the spec of a crd um they're also a little bit harder to use when you're dealing with more advanced features for example let's look at how you configure rewrites with inex angress controller that's pretty challenging right I mean that's almost like learning a domain specific language just to configure rewrite
