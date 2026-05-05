---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Connectivity"
themes: ["SRE Reliability"]
speakers: ["Yannick Epstein", "Anya Hristova", "Spotify"]
sched_url: https://kccnceu2026.sched.com/event/2CVzg/smart-routing-at-scale-how-spotifys-xds-control-plane-cut-75-of-cross-zone-traffic-yannick-epstein-anya-hristova-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Smart+Routing+at+Scale%3A+How+Spotify%E2%80%99s+XDS+Control+Plane+Cut+75%25+of+Cross-Zone+Traffic+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Smart Routing at Scale: How Spotify’s XDS Control Plane Cut 75% of Cross-Zone Traffic - Yannick Epstein & Anya Hristova, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Connectivity]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yannick Epstein, Anya Hristova, Spotify
- Schedule: https://kccnceu2026.sched.com/event/2CVzg/smart-routing-at-scale-how-spotifys-xds-control-plane-cut-75-of-cross-zone-traffic-yannick-epstein-anya-hristova-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Smart+Routing+at+Scale%3A+How+Spotify%E2%80%99s+XDS+Control+Plane+Cut+75%25+of+Cross-Zone+Traffic+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Smart Routing at Scale: How Spotify’s XDS Control Plane Cut 75% of Cross-Zone Traffic.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzg/smart-routing-at-scale-how-spotifys-xds-control-plane-cut-75-of-cross-zone-traffic-yannick-epstein-anya-hristova-spotify
- YouTube search: https://www.youtube.com/results?search_query=Smart+Routing+at+Scale%3A+How+Spotify%E2%80%99s+XDS+Control+Plane+Cut+75%25+of+Cross-Zone+Traffic+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oFdW1yAoaHc
- YouTube title: Smart Routing at Scale: How Spotify’s XDS Control Plane Cut 75%... Yannick Epstein & Anya Hristova
- Match score: 0.824
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/smart-routing-at-scale-how-spotifys-xds-control-plane-cut-75-of-cross/oFdW1yAoaHc.txt
- Transcript chars: 26022
- Keywords: traffic, capacity, clients, client, routing, requests, distributed, actually, second, shameless, server, servers, reports, control, algorithm, distribution, request, called

### Resumo baseado na transcript

I assume if you're here today, you're probably running workloads in multiple availability zones. And you've maybe looked at your cloud bill and thought, what is Corzone? As it turns out, crozone traffic costs money and it might not be a lot per per request, but imagine at that scale, you have service A calling service B, calling service C and D. Intuitively, you might think, well, we could keep we could keep requests within the same zone, but that kills the purpose of zones because it compromises your reliability. How can we keep as much traffic as possible within the same zone without compromising our reliability and keeping high availability? We're going to start with the solution back in the day when we first saw the problem when we were using DNS's service discovery.

### Excerpt da transcript

Good afternoon, CubeCon. Oh, this is exciting. Hi. Um, thank you for coming. Hello. Thank you for joining us on a late afternoon. I assume if you're here today, you're probably running workloads in multiple availability zones. And you've maybe looked at your cloud bill and thought, what is Corzone? Why is it so expensive? My name is Ana Christoa. I'm Yanikai >> and today we're going to tell you how we cut our cross zone eress by 75% using our XDS control plane. We're going to go through the problem. We're going to go through uh one of the optimizations we made initially with DNS. We're then going to talk about the zoneware routing algorithm that we implemented, the heristics behind it with XDS. Um, we're going to go through the system architecture and some key optimizations that we implemented as well as stories from production. So, what maybe didn't go so well? Um, and how could we improve the algorithm. So, let's dig in. Um, I hope you've all heard of Spotify, but if you haven't, it's an audio streaming company, 180 markets.

I'm not going to go through each of those numbers, but I hope that what they convey is the scale at which we operate and that is a multi-reion multiszone infrastructure where routing decisions make a big difference. So to start with the fundamentals, what is a zone? A zone um an availability zone is an isolated physical location inside a region. And zones have purpose. Their purpose is to provide high availability and resiliency. So if one zone goes down, your service will keep serving through the other zones. To put things in perspective, one zone has multiple pots, one region has um multiple zones and then you get Spotify um multiple regions, multiple zones, all connected by more than two million nodes in a mesh. And at that point you might be thinking, we get it. Spotify is big. Um, but there is a point to it. As it turns out, crozone traffic costs money and it might not be a lot per per request, but imagine at that scale, you have service A calling service B, calling service C and D. And each of those could cross a zone.

Um, intuitively, and you know that accumulates, and the money quickly builds up. Intuitively, you might think, well, we could keep we could keep requests within the same zone, but that kills the purpose of zones because it compromises your reliability. And so, it quickly becomes an optimization challenge. How can we keep as much traffic as possible within the same zone without compromising our reliability and k
