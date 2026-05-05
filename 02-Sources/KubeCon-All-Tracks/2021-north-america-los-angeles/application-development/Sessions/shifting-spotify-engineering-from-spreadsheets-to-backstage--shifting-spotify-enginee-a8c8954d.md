---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Application + Development"
themes: ["Platform Engineering"]
speakers: ["Johan Haals", "Patrik Oldsberg", "Spotify"]
sched_url: https://kccncna2021.sched.com/event/lV1c/shifting-spotify-engineering-from-spreadsheets-to-backstage-johan-haals-patrik-oldsberg-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Shifting+Spotify+Engineering+from+Spreadsheets+to+Backstage+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Shifting Spotify Engineering from Spreadsheets to Backstage - Johan Haals & Patrik Oldsberg, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Application + Development]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Los Angeles
- Speakers: Johan Haals, Patrik Oldsberg, Spotify
- Schedule: https://kccncna2021.sched.com/event/lV1c/shifting-spotify-engineering-from-spreadsheets-to-backstage-johan-haals-patrik-oldsberg-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Shifting+Spotify+Engineering+from+Spreadsheets+to+Backstage+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Shifting Spotify Engineering from Spreadsheets to Backstage.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1c/shifting-spotify-engineering-from-spreadsheets-to-backstage-johan-haals-patrik-oldsberg-spotify
- YouTube search: https://www.youtube.com/results?search_query=Shifting+Spotify+Engineering+from+Spreadsheets+to+Backstage+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lCgDiusuixM
- YouTube title: Shifting Spotify Engineering from Spreadsheets to Backstage - Johan Haals & Patrik Oldsberg, Spotify
- Match score: 0.846
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/shifting-spotify-engineering-from-spreadsheets-to-backstage/lCgDiusuixM.txt
- Transcript chars: 23732
- Keywords: backstage, catalog, information, software, engineers, spotify, entities, plugins, source, organization, tooling, component, documentation, engineering, started, available, plugin, templates

### Resumo baseado na transcript

welcome to this talk describing spotify's journey from spreadsheets to backstage we'll start by walking through the struggles we had over the years and how we gradually evolved the way we track software at spotify and once we progress through the dark days we'll arrive at present day with an introduction to backstage we'll talk about how it's more than just an inventory of your services and give you a demo what it's look like lastly we'll share our learnings and help you get started with backstage but before we

### Excerpt da transcript

welcome to this talk describing spotify's journey from spreadsheets to backstage we'll start by walking through the struggles we had over the years and how we gradually evolved the way we track software at spotify and once we progress through the dark days we'll arrive at present day with an introduction to backstage we'll talk about how it's more than just an inventory of your services and give you a demo what it's look like lastly we'll share our learnings and help you get started with backstage but before we start here is a brief introduction to us my name is johan and i'll be co-presenting this session together with patrick we're both engineers at spotify and have spent many years building infrastructure platforms we currently work as open source maintainers of the backstage project and let's begin our journey in the beginning of 2010 and let's call it a stone age spotify was still fairly small at this time with an operations team of just six people these were the days where servers had names and feelings the only thing that matters were servers they ran big monoliths tasked with solving all the world's problems and we had yet to figure out how to shrink them down into a microscopic scale provisioning of new hardware was a completely manual process that was coordinated through the spreadsheets we did find an opportunity to sprinkle some automation on top so we built a software called or a system called serverdb when purchasing hardware we received spreadsheets from our vendors which contain basic information such as mac addresses and serial numbers we then imported that data into server db which in turn gave it human names and a purpose these were then re-exported into yet another spreadsheet that got sent over to remote hands in the data center which did racking and installation it's worth pointing out that there were no fancy user interfaces at this time and all changes were done using a cli and as years passed we ventured into this century where microservices were invented our engineering team had grown into the size of a small village and we've even convinced some of our platform engineers to learn html the stone age monoliths were starting to break down into microservices but with this shift or engineers starting having trouble to keep track of all the pebbles and since server db only knew about hardware we had no place to keep track of all the new services so we built service db which in true microservice fashion was completely separate from serv
