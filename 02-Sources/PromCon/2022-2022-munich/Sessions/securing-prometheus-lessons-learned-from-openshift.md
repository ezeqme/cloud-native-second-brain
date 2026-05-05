---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Kubernetes", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/securing-prometheus-lessons-lear/
youtube_url: https://www.youtube.com/watch?v=WtGOy5ob39M
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Prometheus%3A+Lessons+Learned+from+OpenShift+PromCon+2022
video_match_score: 0.992
status: video-found
---

# Securing Prometheus: Lessons Learned from OpenShift

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/securing-prometheus-lessons-lear/
- YouTube: https://www.youtube.com/watch?v=WtGOy5ob39M

## Resumo

Speaker(s): Manuel Hernandez Valero & Jesus Angel Samitier Nowadays, security is one of the most important things in an enterprise environment, and companies are investing a lot in secure software. When you deploy Prometheus in a Kubernetes cluster, there isn’t any built-in security feature, neither in Kubernetes nor in the Prometheus deployment. On the other hand, when you deploy an OpenShift cluster, you get a Prometheus monitoring stack fully secured with ServiceAccounts, RoleBindings, TLS, tokens, etc.

## Abstract oficial

Speaker(s): Manuel Hernandez Valero & Jesus Angel Samitier

Nowadays, security is one of the most important things in an enterprise environment, and companies are investing a lot in secure software.

When you deploy Prometheus in a Kubernetes cluster, there isn’t any built-in security feature, neither in Kubernetes nor in the Prometheus deployment.

On the other hand, when you deploy an OpenShift cluster, you get a Prometheus monitoring stack fully secured with ServiceAccounts, RoleBindings, TLS, tokens, etc. The question is, how does OpenShift integrate all these security features into Prometheus?

In this talk, Manuel and Jesus will go through all the security features that OpenShift implements, making Prometheus more secure. This way, the attendees will learn by example a toolbox of security best practices for Prometheus deployments in Kubernetes.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/securing-prometheus-lessons-lear/
- YouTube: https://www.youtube.com/watch?v=WtGOy5ob39M
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=WtGOy5ob39M
- YouTube title: PromCon EU 2022: Securing Prometheus: Lessons Learned from OpenShift
- Match score: 0.992
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/securing-prometheus-lessons-learned-from-openshift/WtGOy5ob39M.txt
- Transcript chars: 16545
- Keywords: prometheus, basically, access, exporters, server, account, exporter, airbag, cluster, openshift, information, metrics, default, secure, authorization, another, console, supporters

### Resumo baseado na transcript

[Music] foreign [Music] as I was saying uh we are really happy to be here my name is Jesus my name is Manuel Hernandez yeah we're both Integrations engineers at CSD and we are also the maintainers of franco.io which is an open source project it's an open source project that gives you a curated list of Prometheus exporters that are ready to go you go there so it's search for the application you want to Monitor and the configuration and the alerts and everything is there we are transitioning what's happening so it's really it's it's really handy when sorry when you are doing things uh and this is right how can you how you can configure the the job exactly the same as we were configuring the the kubernetes notes exporter uh later uh previously you need to Simply give the the token we'll see in a demo in a in a in a moment also you need to replace the port where parameters will uh will do the request because the the board from the of the

### Excerpt da transcript

[Music] foreign [Music] as I was saying uh we are really happy to be here my name is Jesus my name is Manuel Hernandez yeah we're both Integrations engineers at CSD and we are also the maintainers of franco.io which is an open source project it's an open source project that gives you a curated list of Prometheus exporters that are ready to go you go there so it's search for the application you want to Monitor and the configuration and the alerts and everything is there we are transitioning now to a full open source mode so uh it's not complete yet you might find some weird stuff but but we are okay we are working on it like uh full uh in this talk we we're gonna We want to show you guys uh how uh how easy or not so difficult to secure a Prometheus server and its exporters uh with some things we learned from openshift this year it's it's been a very exciting year we've we've worked with a lot of openshift clusters and at first we had we struggled of how to get information from the Prometheus exporters how to interact with it and it was quite quite an adventure at first uh so we are we're going to talk uh about it um first uh I mean from it is only contains metrics so it's not a account numbers or emails or passwords right so should we monitor it well yes we should we should yeah because there is a lot of public information out there if you filter with fabric on in Sudan or in fofa you can find a lot of open endpoints on the internet notes supporters apis consoles so just with a query you have there are a link where you can see there's a lot of hashes and you can see a lot of applications out there Prometheus is in there so you basically you can access to a primitive consoles and of course their metrics so what what information uh can you get from that at least do you guys know you have used the node exporter on the on the KSM and this those two supporters have a lot of information so they are they are given the attackers like at the perfect surface of attack it's like uh they don't need to it's a no-brainer for them they just go there and see namespaces secret names types of secret uh so for example this is a few metrics uh we found you can yes with the match the the time series you can get type secret types you can get load balancers open to the world you can find image versions uh Colonel versions ovens OS versions and even the the I O Zone where you are working in aiows so I mean they are gonna be attackers everywhere but at least we have to give them a
