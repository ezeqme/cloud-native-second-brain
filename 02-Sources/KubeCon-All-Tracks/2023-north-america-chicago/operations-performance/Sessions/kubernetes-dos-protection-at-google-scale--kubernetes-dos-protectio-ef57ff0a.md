---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Andrew Sy Kim", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2vN/kubernetes-dos-protection-at-google-scale-andrew-sy-kim-google
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+DoS+Protection+at+Google+Scale+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Kubernetes DoS Protection at Google Scale - Andrew Sy Kim, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Chicago
- Speakers: Andrew Sy Kim, Google
- Schedule: https://kccncna2023.sched.com/event/1R2vN/kubernetes-dos-protection-at-google-scale-andrew-sy-kim-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+DoS+Protection+at+Google+Scale+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Kubernetes DoS Protection at Google Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2vN/kubernetes-dos-protection-at-google-scale-andrew-sy-kim-google
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+DoS+Protection+at+Google+Scale+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9TRzfJrU35M
- YouTube title: Kubernetes DoS Protection at Google Scale - Andrew Sy Kim, Google
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/kubernetes-dos-protection-at-google-scale/9TRzfJrU35M.txt
- Transcript chars: 32075
- Keywords: actually, basically, priority, request, requests, cluster, clients, capacity, control, levels, cost, server, flight, amount, events, objects, resource, google

### Resumo baseado na transcript

so hello everyone uh welcome to my talk where I'll be covering uh some recent developments uh in kubernetes and and within GK for um overload protection and and prevention of um um various uh denal service um scenarios that we've been working on uh so firstly just a little bit about myself um obviously I work on gke and I joined Google about uh two years ago um prior to working at Google I've been I've been working on uh kubernetes uh for about uh five to six years varies like significantly um so it was important for us to have some kind of uh way to associate like a more accurate cost to these requests and then apply it to the amount of seats that were picking up in these in these cues

### Excerpt da transcript

so hello everyone uh welcome to my talk where I'll be covering uh some recent developments uh in kubernetes and and within GK for um overload protection and and prevention of um um various uh denal service um scenarios that we've been working on uh so firstly just a little bit about myself um obviously I work on gke and I joined Google about uh two years ago um prior to working at Google I've been I've been working on uh kubernetes uh for about uh five to six years at this point uh so over the years I've worked on um many areas of of the codebase uh but more recently I've been uh uh working U on some areas uh in Cube API server specifically around uh API priority and fairness and kind of trying to operationalize this uh subsystem within gke um and so that that'll be uh the focus for most of the talk um but before we go there it's worth just kind of mentioning kind of the different types of uh denal service that a kubernetes cluster can experience and I'm sure there's been like tons of talks about how you can brick your cluster and and and whatnot um and so many times when we think about like denial surfice attacks we think about you know uh uh Bots flooding your network with millions of packets per second or we think about you know security vulnerabilities being exploited at scale and uh you know don't get me wrong like these types of attacks do happen but luckily for um myself and the the the other Engineers that work on gke WE leverage uh many of Google's um common infrastructure and services and so out of the box we get pretty good protection for for those types of um attacks like really large scale um and yeah it turns out you know Google Google infrastructure is fairly good at this kind of thing so uh many of these uh denal service attacks um not like don't end up really being my problem right they're kind of like handled at a more like common infrastructure layer and there's really smart teams of Engineers that kind of work on on these kind of things for for our networks and our servers at Google and yeah there's like tons of uh recent block posts around these kind of topics the most recent one around um the http2 rapid reset that was pretty cool blog post which I I recommend um you check it out if you haven't um so From gk's perspective the types of denial of service that we need to mainly be concerned with is uh denial of service at the application layer or in this case the application being like kubernetes or specifically the the QB API server um
