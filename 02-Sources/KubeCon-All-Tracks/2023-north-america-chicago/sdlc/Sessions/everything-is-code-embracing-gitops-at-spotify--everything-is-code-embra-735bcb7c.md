---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "SDLC"
themes: ["GitOps Delivery"]
speakers: ["Tim Hansen", "Spotify"]
sched_url: https://kccncna2023.sched.com/event/1R2qU/everything-is-code-embracing-gitops-at-spotify-tim-hansen-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Everything+Is+Code%3A+Embracing+GitOps+at+Spotify+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Everything Is Code: Embracing GitOps at Spotify - Tim Hansen, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[SDLC]]
- Temas: [[GitOps Delivery]]
- País/cidade: United States / Chicago
- Speakers: Tim Hansen, Spotify
- Schedule: https://kccncna2023.sched.com/event/1R2qU/everything-is-code-embracing-gitops-at-spotify-tim-hansen-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Everything+Is+Code%3A+Embracing+GitOps+at+Spotify+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Everything Is Code: Embracing GitOps at Spotify.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2qU/everything-is-code-embracing-gitops-at-spotify-tim-hansen-spotify
- YouTube search: https://www.youtube.com/results?search_query=Everything+Is+Code%3A+Embracing+GitOps+at+Spotify+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wdUiSbYsDiU
- YouTube title: Everything Is Code: Embracing GitOps at Spotify - Tim Hansen, Spotify
- Match score: 0.909
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/everything-is-code-embracing-gitops-at-spotify/wdUiSbYsDiU.txt
- Transcript chars: 21153
- Keywords: changes, software, little, infrastructure, spotify, builds, deployments, gitops, declarative, declarations, source, automatically, release, templates, process, database, resources, automated

### Resumo baseado na transcript

it's wonderful to see this many people in the room I'm Tim Hansen I'm here to talk to you a little bit about gitops and how we use it at Spotify and I'm so excited that there's so many people eager to learn about this could I get a quick show of hands who feels like they know kind of what get Ops is all right that's a pretty good percentage that's really good well if bear with me for the people that didn't raise their hands I'm going to

### Excerpt da transcript

it's wonderful to see this many people in the room I'm Tim Hansen I'm here to talk to you a little bit about gitops and how we use it at Spotify and I'm so excited that there's so many people eager to learn about this could I get a quick show of hands who feels like they know kind of what get Ops is all right that's a pretty good percentage that's really good well if bear with me for the people that didn't raise their hands I'm going to go over some Basics but I promise it's just a few minutes then we'll get to the good stuff about Spotify so what is gitops this is my simple definition if you haven't heard this term before giops is an approach to infrastructure automation using files stored in Source control git is obviously the preferred source control system here if you're using SVN you might be too old for this [Music] talk I'm just kidding I've been there too man all right so you might be thinking this sounds familiar isn't that just infostructure as code we already have a term for that you can't just make up new terms well first of all I didn't make up the term uh we Works did so you can blame them but infrastructure as code is a little bit loose I can apply changes from my local machine still be doing infrastructure as code I can push code straight to the main branch without reviews and still be doing infrastructure as code I can set things up with code and then go go into the cloud console and muck around and still be doing infrastructure as code so gitops applies infrastructure as code but it's a bit more prescriptive in the workflow so in addition to the prescriptive workflow there's a few basic principles um that must be followed for giops these are almost self-evident from the name but worth going over so first we must be able to express the desired state declaratively that means I can describe the infrastructure I want in a file so that I can store it and get second these de ations must be versioned and immutable this makes the third bullet much easier and third these changes to these declarations must be applied automatically so that means something's paying attention to get and tries to make reality match my declarations so the git part of giops already handles the first two since we're using G as the source of Truth the Declarations are clearly stored in files and get commits or also show versioned and immutable so that leaves the last bullet which is like way harder than the first two I could imagine someone proposing these like I'll handle
