---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Emerging + Advanced"
themes: ["AI ML"]
speakers: ["Stefan Schimanski", "Upbound", "Mangirdas Judeikis", "Cast AI"]
sched_url: https://kccncna2024.sched.com/event/1i7lu/deep-dive-into-generic-control-planes-and-kcp-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai
youtube_search_url: https://www.youtube.com/results?search_query=Deep+Dive+Into+Generic+Control+Planes+and+Kcp+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Deep Dive Into Generic Control Planes and Kcp - Stefan Schimanski, Upbound & Mangirdas Judeikis, Cast AI

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Stefan Schimanski, Upbound, Mangirdas Judeikis, Cast AI
- Schedule: https://kccncna2024.sched.com/event/1i7lu/deep-dive-into-generic-control-planes-and-kcp-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai
- Busca YouTube: https://www.youtube.com/results?search_query=Deep+Dive+Into+Generic+Control+Planes+and+Kcp+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Deep Dive Into Generic Control Planes and Kcp.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7lu/deep-dive-into-generic-control-planes-and-kcp-stefan-schimanski-upbound-mangirdas-judeikis-cast-ai
- YouTube search: https://www.youtube.com/results?search_query=Deep+Dive+Into+Generic+Control+Planes+and+Kcp+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=R9YUOo0MwqY
- YouTube title: Deep Dive Into Generic Control Planes and Kcp - Stefan Schimanski & Mangirdas Judeikis
- Match score: 0.789
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/deep-dive-into-generic-control-planes-and-kcp/R9YUOo0MwqY.txt
- Transcript chars: 32372
- Keywords: cluster, basically, control, server, generic, clusters, logical, controller, workspace, object, another, second, binding, everything, pattern, export, config, create

### Resumo baseado na transcript

so welcome to our talk can I be heard yeah I think so I hear it Echo um so welcome to our talk about generic control plans and uh kcp um my name is Stefan shimansky I'm working at upbound on control plans so on kubernetes API Machinery API server stuff so hey I'm MJ I work at CTI we we're trying to look into control planes so to so before we jump in question how many of you heard about kcp right hand how many of you used kcp

### Excerpt da transcript

so welcome to our talk can I be heard yeah I think so I hear it Echo um so welcome to our talk about generic control plans and uh kcp um my name is Stefan shimansky I'm working at upbound on control plans so on kubernetes API Machinery API server stuff so hey I'm MJ I work at CTI we we're trying to look into control planes so to so before we jump in question how many of you heard about kcp right hand how many of you used kcp okay we need to change the second part so this is why we're here cool all right so we we uh I tweeted recently that this is a deep dive and we mean it so don't be afraid um you will learn something either way so we have basically two topics generic control plane and kcp they are highly related basically generic control plane is a foundational work to enable kcp eventually but you don't need to to do the Second Step you can use generic control plane also on its own so we start with generic control plane and um there was a cap 4080 um one a half years ago and it was about allowing this um yeah the construction easy construction of API servers which are Cube like and they should inherit certain apis from kubernetes for example airb permissions roles and role binding similar things config Maps so they are like coup API server but without all the compute stuff so a partial API server C API server basically and the cap is still not closed uh but um since 131 so the previous release We have basically done the heavy lifting and I guess even if you followed uh the pr flow in the API server you might not have noticed that this actually happened the reason is that um the heavy lifting has been done but we didn't do any renaming any package movement so there are those um packages here if you look into the code basically the first one is the essential one for for the work of generic control plans this is a generic API server which is able to use apis from kubernetes like conf map Secrets similar things the second one if you read the code package control plane um don't be confused it sounds like generic control plane it's not this is Cube API server so the renaming um the cleanup all of that will happen but the heavy lifting has been done like the split has been done um there's a second part in in the cap about a staging repository hasn't been done either so um this is basically the movement so every everything you see in the first line the control pain API server will likely move into such a staging repository eventually it's working progress there
