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
themes: ["Connectivity"]
speakers: ["Rob Scott", "Google"]
sched_url: https://kccncna2024.sched.com/event/1i7rZ/topology-aware-routing-understanding-the-tradeoffs-rob-scott-google
youtube_search_url: https://www.youtube.com/results?search_query=Topology+Aware+Routing%3A+Understanding+the+Tradeoffs+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Topology Aware Routing: Understanding the Tradeoffs - Rob Scott, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Connectivity]]
- País/cidade: United States / Salt Lake City
- Speakers: Rob Scott, Google
- Schedule: https://kccncna2024.sched.com/event/1i7rZ/topology-aware-routing-understanding-the-tradeoffs-rob-scott-google
- Busca YouTube: https://www.youtube.com/results?search_query=Topology+Aware+Routing%3A+Understanding+the+Tradeoffs+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Topology Aware Routing: Understanding the Tradeoffs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rZ/topology-aware-routing-understanding-the-tradeoffs-rob-scott-google
- YouTube search: https://www.youtube.com/results?search_query=Topology+Aware+Routing%3A+Understanding+the+Tradeoffs+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=taR63hFeuAQ
- YouTube title: Topology Aware Routing: Understanding the Tradeoffs - Rob Scott, Google
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/topology-aware-routing-understanding-the-tradeoffs/taR63hFeuAQ.txt
- Transcript chars: 25006
- Keywords: traffic, points, routing, topology, endpoint, actually, completely, trying, number, distribution, basically, everywhere, support, little, probably, planes, better, working

### Resumo baseado na transcript

session uh and also just because this isn't quite the last session of cukon there is at least one more after this and I want to highlight the person in the very front row gar who's going to be giving that session uh and he really could or should be giving this session right now because he did a lot of the work for routing so all credit to G here so he can come up and give the same thought no pressure no pressure no pressure so I don't

### Excerpt da transcript

session uh and also just because this isn't quite the last session of cukon there is at least one more after this and I want to highlight the person in the very front row gar who's going to be giving that session uh and he really could or should be giving this session right now because he did a lot of the work for routing so all credit to G here so he can come up and give the same thought no pressure no pressure no pressure so I don't know I don't know we'll see I'll try and live up to it but uh let's talk about to routing and the many trade-offs that exist within apolog routing uh my name is Rob Scott I work at Google on GK networking I've worked there for five years or thereabouts and uh before then I was an end user of kubernetes so I have some experience with actually dealing with some of the frustrations and magic of kubernetes along the way but these days I mostly work on things like gway API and other kubernetes networking things now it might help to provide just a little bit of context about what we're talking about with apolog routing and the components involved here so first off uh there are Services pods probably mostly familiar with them and then there's this really fun endpoint slice controller well I'm probably the only person who considers it fun this was my first project welcome to Google uh and so endpoint slice controller is this thing that basically creates shards of end points uh and for each service finds all the pods finds the IPS and ports drops them into endpoint slice and then you have a data plane usually C proxy on each node that reads those and does some cool IP tables magic to do the routing for you and what we're going to be talking about is different forms of logic in C proxy or your kubernetes data planes of choice so by default everything just goes everywhere incling this well maybe not everywhere but there's no concept of preferring traffic stay close to where it originated from if it's an endpoint behind a service it's equally likely to go there as opposed to one in a completely different Zone we don't really care now the pros of that is it's least likely to overload traffic to a single end point and Autos scaling is straightforward well I'm not going to say Auto scaling is ever completely straightforward but it's less complicated than when you start to add some preference about we traffic goes on the con side if you happen to use a cloud provider or something where traffic going across zones is expensive this approach ca
