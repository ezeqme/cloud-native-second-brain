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
themes: ["Networking", "Kubernetes Core"]
speakers: ["Flynn", "Buoyant"]
sched_url: https://kccncna2024.sched.com/event/1i7pQ/one-gateway-api-to-rule-them-all-and-in-the-cluster-configure-them-flynn-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=One+Gateway+API+to+Rule+Them+All+%28and+in+the+Cluster+Configure+Them%29+CNCF+KubeCon+2024
slides: []
status: parsed
---

# One Gateway API to Rule Them All (and in the Cluster Configure Them) - Flynn, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Flynn, Buoyant
- Schedule: https://kccncna2024.sched.com/event/1i7pQ/one-gateway-api-to-rule-them-all-and-in-the-cluster-configure-them-flynn-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=One+Gateway+API+to+Rule+Them+All+%28and+in+the+Cluster+Configure+Them%29+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre One Gateway API to Rule Them All (and in the Cluster Configure Them).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pQ/one-gateway-api-to-rule-them-all-and-in-the-cluster-configure-them-flynn-buoyant
- YouTube search: https://www.youtube.com/results?search_query=One+Gateway+API+to+Rule+Them+All+%28and+in+the+Cluster+Configure+Them%29+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sRHjg6bGfug
- YouTube title: One Gateway API to Rule Them All (and in the Cluster Configure Them) - Flynn, Buoyant
- Match score: 0.984
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/one-gateway-api-to-rule-them-all-and-in-the-cluster-configure-them/sRHjg6bGfug.txt
- Transcript chars: 30923
- Keywords: traffic, gateway, cluster, egress, linker, smiley, ingress, controller, actually, running, network, mesh, parent, application, networks, talking, everything, routes

### Resumo baseado na transcript

so yeah this is the one Gateway API to rule them all and in the darkness I mean sorry in the cluster configure them um I am Flynn I'm a tech evangelist for Linker at buyant you can find me on basically all of the slacks that have anything to do with the cncf as Flynn if email is your thing you can send email to Flyn boo. Ingress problem is about providing access but the egress problem is about providing control so we talk about them kind of as opposites or of two sides of the same coin that's not quite accurate they really do have different goals so that brings us example.com please route that to the kubernetes service named Smiley use it Port 80 and since I have not said anything about name spaces in that back end ref that will be using or in the parent ref that requires a Gateway in the faces this service and uh this is the problem with using your phone as your keynote remote and then accidentally having it flip over to the camera not that that ever happens um we can get more complex about this right so we can do things route and TLS route actually although we're not going to show that today um and uh that brings us to to a brief discussion of what the demo is going to look like before we see if the demo works I mean before we look

### Excerpt da transcript

so yeah this is the one Gateway API to rule them all and in the darkness I mean sorry in the cluster configure them um I am Flynn I'm a tech evangelist for Linker at buyant you can find me on basically all of the slacks that have anything to do with the cncf as Flynn if email is your thing you can send email to Flyn boo. that works as well the point here is that it would be really nice to have one way to talk about all the different kind of traffic that can happen in cetes whether that's traffic from outside the cluster going inside angress traffic or traffic between workloads in the cluster or traffic leaving the cluster for outside it would be nice to be able to talk about these things in pretty much the same way so we're going to talk a little bit about these kinds of traffic and then if the demo goddesses smile upon us we will have a demo now is an appropriate time to start praying to the demo goddesses um it worked great in rehearsal but uh all right so we are going to start with Ingress specifically this is the Engish problem not the Engish resource or Engish controller so this is the Engish problem the problem is pretty simple if you have a cluster and you have workloads in the cluster you will have users outside the cluster who want to use things inside the cluster but One does not simply send packets into a cluster clusters do not let you do this this is a critical thing about security within kubernetes you can't just randomly talk to things inside a cluster so instead we need something to sit right there at the edge to mediate this path from outside to inside to do this safely that thing historically is called an Engish controller I should also point out that yes there is a thing called an inous resource we're not really going to talk about that it's sort of back from the bad old days so the egress problem is kind of the opposite of the Ingress problem where sometimes also you have workloads in your cluster that need to talk to things outside your cluster and generally one does simply send packets outside the cluster this is allowed for the most part and in fact that is the egis problem because yeah okay for the most part your workloads will be talking to things that they should be talking to maybe they're talking to your payment processor or they're talking to your bank or they're doing good things like that if they decide to not do good things we would like to be able to do something about that right where doing something might mean several thi
