---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking"]
speakers: ["Aleksandar Mitic", "Yannick Epstein", "Spotify"]
sched_url: https://kccnceu2024.sched.com/event/1YePw/reducing-cross-zone-egress-at-spotify-with-custom-grpc-load-balancing-aleksandar-mitic-yannick-epstein-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Reducing+Cross-Zone+Egress+at+Spotify+with+Custom+gRPC+Load+Balancing+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Reducing Cross-Zone Egress at Spotify with Custom gRPC Load Balancing - Aleksandar Mitic & Yannick Epstein, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]]
- País/cidade: France / Paris
- Speakers: Aleksandar Mitic, Yannick Epstein, Spotify
- Schedule: https://kccnceu2024.sched.com/event/1YePw/reducing-cross-zone-egress-at-spotify-with-custom-grpc-load-balancing-aleksandar-mitic-yannick-epstein-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Reducing+Cross-Zone+Egress+at+Spotify+with+Custom+gRPC+Load+Balancing+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Reducing Cross-Zone Egress at Spotify with Custom gRPC Load Balancing.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePw/reducing-cross-zone-egress-at-spotify-with-custom-grpc-load-balancing-aleksandar-mitic-yannick-epstein-spotify
- YouTube search: https://www.youtube.com/results?search_query=Reducing+Cross-Zone+Egress+at+Spotify+with+Custom+gRPC+Load+Balancing+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8E5zVdEfwi0
- YouTube title: Reducing Cross-Zone Egress at Spotify with Custom gRPC Load Balancing
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/reducing-cross-zone-egress-at-spotify-with-custom-grpc-load-balancing/8E5zVdEfwi0.txt
- Transcript chars: 25729
- Keywords: latency, balancing, traffic, server, spotify, expected, decision, client, servers, algorithm, question, actually, basically, response, across, probably, request, simple

### Resumo baseado na transcript

hello everyone hello nice to see you all Welcome to our talk this is reducing cross Zone eress at Spotify with custom grpc load balancing really long title my team is here they're trying to get me to say it in French I'm not even going to attempt it and make a fool out of myself here my name is Alex this is my colleague Yik we work at Spotify specifically the computer networking uh departments our team concerns itself with service Discovery um we manage the protocols in our

### Excerpt da transcript

hello everyone hello nice to see you all Welcome to our talk this is reducing cross Zone eress at Spotify with custom grpc load balancing really long title my team is here they're trying to get me to say it in French I'm not even going to attempt it and make a fool out of myself here my name is Alex this is my colleague Yik we work at Spotify specifically the computer networking uh departments our team concerns itself with service Discovery um we manage the protocols in our backend to backend communication and everything that comes with that specifically uh one big concern is load balancing everything around it and that's why we're here today so in our talk we'll start quite high level and talk about load balancing in general H why we do it what we care about and then we'll dive deeper into exactly how we do load balancing at Spotify what tradeoffs we take and just how it works in general so without further Ado the problem in a microservice architecture the choice of load balancing greatly impacts the performance of the product what does this mean so if we look at an illustration here um a common load balancing decision might look like this there is a client it needs to speak to some API to to get a response and build the the package it wants to that API is served by several servers uh so in this case we have three instances uh and we have to pick one right that's the choice of flood balancing as humans we look at this and we see that the first one is fast the second one is slow the third one's on Fire doesn't even work so naturally we pick the first one so implicitly we are optimizing for latency error rates utilization various others attributes that affect the product so in the case of Spotify High latency means slow playback error rates means you can't see your playlist and Etc now on a slightly higher level as a business we're always optimizing for cost right we need to spend less money than we make in order to be profitable and how we do load balancing affects this cost uh in many ways and we're here specifically to talk about the cost of Crossing networking boundaries so again what does that mean and I want to apologize to all data center experts in advance this is going to be very handwavy how a cloud works but I think it will get the point across your favorite cloud provider probably has a room that looks like this a data center with a bunch of servers uh hooked on to each other to serve the needs of you know the global apps we have and everything
